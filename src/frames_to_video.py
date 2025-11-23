# Week 3 – Assemble frames into a video (FFmpeg + GIF fallback)

import os
import subprocess
import imageio.v2 as imageio


def frames_to_video(
    frame_dir="results/week3_frames",
    output_file="results/week3_demo.mp4",
    fps=2,
):
    """
    Week 3 task:
    - Convert generated PNG frames into a video.
    - Primary path: use ffmpeg CLI (works reliably across systems).
    - Fallback: if ffmpeg is missing, write an animated GIF instead.
    """

    print("[Week 3] Assembling frames into video...")

    # Collect frames in sorted order
    frames = sorted(
        os.path.join(frame_dir, f)
        for f in os.listdir(frame_dir)
        if f.endswith(".png")
    )

    if not frames:
        print(f"[Week 3] No PNG frames found in {frame_dir}")
        return

    # -------- Option A: Use ffmpeg to create MP4 --------
    try:
        print("[Week 3] Trying ffmpeg path (MP4 output)...")

        # Example: frame_0.png, frame_1.png, ...
        frame_pattern = os.path.join(frame_dir, "frame_%d.png")

        cmd = [
            "ffmpeg",
            "-y",                     # overwrite if exists
            "-framerate",
            str(fps),
            "-i",
            frame_pattern,
            "-pix_fmt",
            "yuv420p",
            output_file,
        ]

        subprocess.run(cmd, check=True)
        print(f"[Week 3] MP4 video saved at: {output_file}")
        return

    except FileNotFoundError:
        print("[Week 3] ffmpeg not found on this system. Falling back to GIF...")
    except subprocess.CalledProcessError as e:
        print("[Week 3] ffmpeg failed, falling back to GIF...")
        print("        ffmpeg error:", e)

    # -------- Option B: Fallback – animated GIF --------
    gif_path = "results/week3_demo.gif"
    print(f"[Week 3] Creating GIF instead at: {gif_path}")

    images = [imageio.imread(f) for f in frames]
    # duration is seconds per frame
    imageio.mimsave(gif_path, images, duration=1.0 / fps)
    print(f"[Week 3] GIF saved at: {gif_path}")


if __name__ == "__main__":
    frames_to_video()