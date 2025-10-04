import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

output_dir = "generated_images"
os.makedirs(output_dir, exist_ok=True)


def convert_svgs_to_png():
    svg_files = [f for f in os.listdir('.') if f.lower().endswith('.svg')]

    if not svg_files:
        print("No SVG files found in current directory!")
        return

    print(f"Found {len(svg_files)} SVG files to convert...")

    for svg_file in svg_files:
        try:
            drawing = svg2rlg(svg_file)
            png_file = os.path.splitext(svg_file)[0] + ".png"
            renderPM.drawToFile(drawing, os.path.join(output_dir, png_file), fmt="PNG")
            print(f"✓ Converted: {svg_file} → {png_file}")
        except Exception as e:
            print(f"✗ Error converting {svg_file}: {e}")

    print(f"\nConversion complete! Converted {len(svg_files)} files.")


if __name__ == "__main__":
    convert_svgs_to_png()
