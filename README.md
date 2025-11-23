# Image2Image + Text2Image Video Generation for FAU Engineering

**Course:** CAP6415 – Computer Vision (Fall 2025)  
**Team:** Akhileshwar Reddy Bommineni, Manaswini Pasupuleti, Pathri Jaydeep  
**Instructor:** Prof. Velibor Adzic (vadzic@fau.edu)
**University:** Florida Atlantic University – College of Engineering and Computer Science  

---

## 🎯 Abstract
AI-generated visualizations play an increasingly large role in engineering research, simulations, and educational demonstrations.
This project covers a **hybrid AI video generation pipeline** based on **Text-to-Image (T2I)** and **Image-to-Image (I2I)** transformation concepts.

The system conceptually follows three major stages:

1. **Text-to-Image Generation:**
A frame is generated from a descriptive engineering-themed prompt; examples include "*FAU engineering drone lab with multiple sensors and LED lighting*".

Currently, this step is simulated using a lightweight **mock diffusion pipeline** to ensure **full reproducibility across all devices** without requiring GPUs or large model downloads.
2. **Image-to-Image Refinement:**

The initial frame can be refined or changed so as to simulate small variations including those resulting from lighting, motion, and angle changes.

A lightweight placeholder version is implemented to demonstrate the pipeline architecture. 
3. **Video Assembly:** These generated or refined frames are combined to form a short engineering-themed video clip using some simple frame-to-video utility. 

The whole repository is meant to be **portable**, **lightweight**, and **fully reproducible** on any system, Windows, macOS, Linux, without specific hardware or authentication requirements.
---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/akhileshwarreddy1706/Image2Image-Text2Image-video-generation-for-FAU-Engineering.git
cd Image2Image-Text2Image-video-generation-for-FAU-Engineering
```
### 2️⃣ (Recommended) Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate     # (on macOS/Linux)
# OR
.venv\Scripts\activate        # (on Windows)
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ (Optional) Create the environment via Conda
```bash
conda env create -f environment.yml
conda activate cap6415-img2vid
```
## Repository Structure

```bash
├── src/
│   ├── generate_frames.py        # Mock Text-to-Image frame generator (Week 3)
│   ├── refine_frames.py          # Image-to-Image refinement placeholder
│   └── frames_to_video.py        # Combine frames into a video (FFMPEG/ImageIO)
│
├── results/
│   ├── week2_frames/             # Frames generated during Week 2
│   ├── week3_frames/             # Mock ONNX frames (Week 3 output)
│   └── frame_000.png             # Example starting frame
│
├── models/
│   └── onnx/                     # Contains config files only (no large ONNX binaries)
│
├── week1log.txt                  # Weekly progress log
├── week2log.txt
├── week3log.txt
│
├── requirements.txt              # Python dependencies
├── environment.yml               # Conda environment file
│
├── demo_video_script.md          # Outline for final project presentation video
├── LICENSE                       # MIT License
└── README.md                     #Projectdocumentation (this file)
```


## Running the Project

### Generate frames (mock Text-to-Image)
```bash 
python src/generate_frames.py
```
### Convert frames to video
```bash
python src/frames_to_video.py
```
