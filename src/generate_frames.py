# Week 3 – Mock ONNX Stable Diffusion Pipeline
# NO INTERNET, NO HUGGINGFACE, NO MODELS NEEDED
# Runs on ANY device (Mac, Windows, Linux, Python 3.10–3.12)

import os
from PIL import Image, ImageDraw

def generate_frames(prompt="FAU Engineering building, futuristic lighting",
                    num_frames=3,
                    output_dir="results/week3_frames"):

    os.makedirs(output_dir, exist_ok=True)

    print("[Week 3] Simulating ONNX Stable Diffusion Pipeline (mock)...")
    print("[Week 3] Prompt:", prompt)

    for i in range(num_frames):
        img = Image.new("RGB", (512, 512), (40 * i, 50, 180))
        draw = ImageDraw.Draw(img)
        draw.text((20, 20), f"FAU Mock Frame {i}", fill="white")
        img.save(f"{output_dir}/frame_{i}.png")
        print(f"[Week 3] Saved: frame_{i}.png")

    print("[Week 3] Completed mock pipeline.")

if __name__ == "__main__":
    generate_frames()