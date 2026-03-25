#!/usr/bin/env python3
"""Generate static font instances from variable TTF fonts using fonttools instancer."""

import os
import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

FONTS_DIR = Path(__file__).parent.parent / "assets" / "fonts"

# Variable font filename -> list of (weight_value, output_suffix)
FONT_CONFIGS = {
    "Caveat": {
        "variable_file": None,  # will detect
        "weights": [
            (400, "Regular"),
            (500, "Medium"),
            (600, "SemiBold"),
            (700, "Bold"),
        ],
    },
    "Quicksand": {
        "variable_file": None,
        "weights": [
            (300, "Light"),
            (400, "Regular"),
            (500, "Medium"),
            (600, "SemiBold"),
            (700, "Bold"),
        ],
    },
}


def find_variable_font(family_name: str) -> Path:
    """Find the variable font file (the -Variable.ttf we downloaded)."""
    candidate = FONTS_DIR / f"{family_name}-Variable.ttf"
    if candidate.exists():
        return candidate
    raise FileNotFoundError(f"No variable font found at {candidate}")


def main():
    for family_name, config in FONT_CONFIGS.items():
        source = find_variable_font(family_name)
        print(f"\n--- {family_name} ---")
        print(f"Source: {source} ({source.stat().st_size:,} bytes)")

        # Verify it's actually a variable font
        test_font = TTFont(str(source))
        if "fvar" not in test_font:
            print(f"  WARNING: {source.name} is NOT a variable font. Skipping.")
            continue

        fvar = test_font["fvar"]
        axes = {a.axisTag: (a.minValue, a.defaultValue, a.maxValue) for a in fvar.axes}
        print(f"  Axes: {axes}")
        test_font.close()

        for weight, suffix in config["weights"]:
            output_path = FONTS_DIR / f"{family_name}-{suffix}.ttf"
            print(f"  Generating {output_path.name} (wght={weight})...", end=" ")

            font = TTFont(str(source))
            instantiateVariableFont(font, {"wght": weight}, inplace=True, static=True)
            font.save(str(output_path))
            font.close()

            size = output_path.stat().st_size
            print(f"{size:,} bytes")

    # Summary: verify files are different sizes
    print("\n=== Verification ===")
    for family_name, config in FONT_CONFIGS.items():
        sizes = {}
        for _, suffix in config["weights"]:
            p = FONTS_DIR / f"{family_name}-{suffix}.ttf"
            sizes[suffix] = p.stat().st_size
        print(f"\n{family_name}:")
        for suffix, size in sizes.items():
            print(f"  {suffix}: {size:,} bytes")

        unique_sizes = len(set(sizes.values()))
        total = len(sizes)
        if unique_sizes == total:
            print(f"  OK: All {total} weights have different file sizes.")
        elif unique_sizes > 1:
            print(f"  PARTIAL: {unique_sizes}/{total} unique sizes.")
        else:
            print(f"  FAIL: All weights are identical!")


if __name__ == "__main__":
    main()
