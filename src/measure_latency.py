import cv2, time, numpy as np, os

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: no camera")
    exit()

times = []
for i in range(100):
    t0 = time.time()
    ret, frame = cap.read()
    if not ret: break
    _ = cv2.bilateralFilter(frame, 9, 75, 75)
    t1 = time.time()
    times.append((t1 - t0)*1000)

avg_ms = sum(times)/len(times)
cap.release()
print(f"Average latency: {avg_ms:.2f} ms")

os.makedirs("../results", exist_ok=True)
with open("../results/metrics.txt", "a") as f:
    f.write(f"Average latency (ms): {avg_ms:.2f}\n")
