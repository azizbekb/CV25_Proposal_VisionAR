import cv2
import numpy as np
import time
import os

VIDEO_IN = "../data/sample_videos/example.mp4"
OUT_DIR = "../results"
OUT_VIDEO = os.path.join(OUT_DIR, "baseline_demo.mp4")
METRICS = os.path.join(OUT_DIR, "metrics.txt")

os.makedirs(OUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_IN)
if not cap.isOpened():
    print(f"ERROR: cannot open video {VIDEO_IN}")
    exit(1)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = cap.get(cv2.CAP_PROP_FPS) or 30
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(OUT_VIDEO, fourcc, fps, (w * 2, h))

frame_count = 0
start_time = time.time()

print("Processing baseline denoise... (file input)")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gaussian = cv2.GaussianBlur(frame, (5, 5), 0)
    bilateral = cv2.bilateralFilter(gaussian, 9, 75, 75)

    combined = np.hstack((frame, bilateral))
    out.write(combined)

    frame_count += 1

cap.release()
out.release()
elapsed = time.time() - start_time
fps_proc = frame_count / elapsed if elapsed > 0 else 0.0

print(f"Baseline done: frames={frame_count}, elapsed={elapsed:.2f}s, fps={fps_proc:.2f}")

with open(METRICS, "a") as f:
    f.write(f"[baseline] frames:{frame_count} elapsed:{elapsed:.2f} fps:{fps_proc:.2f}\n")

print(f"Saved: {OUT_VIDEO}")
