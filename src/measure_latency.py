"""
measure_latency.py
------------------
Measures average per-frame latency (ms) for VisionAR baseline filter.
"""

import cv2, time, numpy as np, os

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

times = []
frames_to_test = 100

for i in range(frames_to_test):
    t0 = time.time()
    ret, frame = cap.read()
    if not ret:
        break
    # Apply baseline filter
    _ = cv2.bilateralFilter(frame, 9, 75, 75)
    t1 = time.time()
    times.append((t1 - t0) * 1000)

cap.release()

avg_ms = sum(times) / len(times)
print(f"Average Latency: {avg_ms:.2f} ms per frame")

os.makedirs("../results", exist_ok=True)
with open("../results/metrics.txt", "a") as f:
    f.write(f"[W3] latency_avg_ms:{avg_ms:.2f}\n")
