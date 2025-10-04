🐍 SVG to PNG Image Generator (Python Automation)



📘 Overview

This project is a Python-based automation script that converts an SVG file into 1000 unique PNG images.
During each conversion, the script automatically updates a number inside the SVG, creating sequentially numbered PNG outputs — perfect for templates, badges, certificates, or digital collectibles.

⚙️ Features

🔄 Converts SVG → PNG automatically
🔢 Dynamically modifies numbers in each image
⚡ Generates 1000+ images efficiently
🧩 Clean and modular Python code

🧾 Easy to customize for any SVG template

🛠️ Tech Stack
Python 3.10+
CairoSVG / svglib / reportlab
os / re / shutil for file management

📦 Installation
Clone the repository:

git clone https://github.com/yourusername/svg-to-png-generator.git
cd svg-to-png-generator


Install dependencies:
pip install cairosvg


Place your SVG file in the project folder (e.g., template.svg).

🚀 Usage
Run the script:
python generate_images.py


Output:

All PNGs will be saved in the output/ directory

Each file will be named as image_1.png, image_2.png, ..., image_1000.png

🖼️ Example

Input SVG:
Contains a placeholder number like {{number}}

Output PNGs:

image_001.png → number = 1

image_002.png → number = 2

...

image_1000.png → number = 1000

💼 Use Cases

Certificate generation

NFT and digital art creation

Dynamic badge or label generation

Automated graphic design workflows
