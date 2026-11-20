import subprocess
import os

def create_clip(video_file, start_time, duration, output_file):
    os.makedirs("clips", exist_ok=True)

    command = [
        "ffmpeg",
        "-ss", str(start_time),
        "-i", video_file,
        "-t", str(duration),
        "-c:v", "libx264",
        "-c:a", "aac",
        "-y", output_file
    ]

    subprocess.run(command, check=True)
    print("Clip created:", output_file)


if __name__ == "__main__":
    print("VICE CITY CLIPPER READY")
