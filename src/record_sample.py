"""
record_sample.py
----------------
Simple webcam recorder for VisionAR dataset.
Press 'q' to stop recording.
"""

import cv2
import os

# Make sure output folder exists
os.makedirs("../data/sample_videos", exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Error: Cannot access webcam.")
    exit()

# Set video output path
out_path = "../data/sample_videos/example.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

print("🎥 Recording started... (press 'q' to stop)")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow("Recording — VisionAR", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"✅ Recording saved to {out_path}")
