"""
baseline_denoise.py
-------------------
Simple baseline for VisionAR project.
Applies OpenCV denoising filters (Gaussian + Bilateral)
to a live webcam feed. Press 'q' to quit.
"""

import cv2
import numpy as np
import time
import os

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access webcam.")
    exit()

frame_count = 0
start_time = time.time()

print("Running VisionAR baseline... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply basic denoising
    gaussian = cv2.GaussianBlur(frame, (5, 5), 0)
    bilateral = cv2.bilateralFilter(gaussian, 9, 75, 75)

    combined = np.hstack((frame, bilateral))
    cv2.putText(combined, "Original | Denoised", (40, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("VisionAR Baseline", combined)
    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

end_time = time.time()
elapsed = end_time - start_time
fps = frame_count / elapsed

print(f"Processed {frame_count} frames in {elapsed:.2f}s — FPS: {fps:.2f}")

# Save metrics
os.makedirs("../results", exist_ok=True)
with open("../results/metrics.txt", "a") as f:
    f.write(f"[W3] baseline - frames:{frame_count} elapsed:{elapsed:.2f}s fps:{fps:.2f}\n")

cap.release()
cv2.destroyAllWindows()
