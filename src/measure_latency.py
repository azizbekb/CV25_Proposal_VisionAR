import cv2, time, os

VIDEO_IN = "data/sample_videos/example.mp4"
OUT_DIR = "results"
METRICS = os.path.join(OUT_DIR, "metrics.txt")
os.makedirs(OUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_IN)
if not cap.isOpened():
    print(f"ERROR: cannot open video {VIDEO_IN}")
    exit(1)

times = []
count = 0
max_frames = 200

while count < max_frames:
    ret, frame = cap.read()
    if not ret:
        break
    t0 = time.time()

    _ = cv2.GaussianBlur(frame, (5, 5), 0)
    _ = cv2.bilateralFilter(frame, 9, 75, 75)

    t1 = time.time()
    times.append((t1 - t0) * 1000)
    count += 1

cap.release()
if not times:
    print("No frames measured.")
    exit(1)

avg_ms = sum(times) / len(times)
min_ms = min(times)
max_ms = max(times)
print(f"Latency (ms) avg:{avg_ms:.2f} min:{min_ms:.2f} max:{max_ms:.2f} over {len(times)} frames")

with open(METRICS, "a") as f:
    f.write(f"[latency] avg_ms:{avg_ms:.2f} min_ms:{min_ms:.2f} max_ms:{max_ms:.2f}\n")
