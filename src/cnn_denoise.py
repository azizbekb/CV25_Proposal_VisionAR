import os, time
import cv2
import numpy as np
import torch
import torch.nn as nn

VIDEO_IN = "data/sample_videos/example.mp4"
OUT_DIR = "results"
OUT_VIDEO = os.path.join(OUT_DIR, "cnn_demo.mp4")
METRICS = os.path.join(OUT_DIR, "metrics.txt")
os.makedirs(OUT_DIR, exist_ok=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

class SmallDenoiser(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(32, 32, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(32, 3, 3, padding=1)
        )
    def forward(self, x):
        return x + 0.1 * self.net(x)

model = SmallDenoiser().to(device)
model.eval()

cap = cv2.VideoCapture(VIDEO_IN)
if not cap.isOpened():
    print(f"ERROR: cannot open video {VIDEO_IN}")
    exit(1)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = cap.get(cv2.CAP_PROP_FPS) or 30
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(OUT_VIDEO, fourcc, fps, (w, h))

frame_count = 0
total_infer = 0.0
print("Running CNN denoiser inference (file input)...")

with torch.no_grad():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        tensor = torch.from_numpy(img).float().permute(2,0,1).unsqueeze(0).to(device) / 255.0

        t0 = time.time()
        out_t = model(tensor)
        infer_time = time.time() - t0
        total_infer += infer_time

        out_img = (out_t.squeeze(0).permute(1,2,0).cpu().numpy() * 255.0).clip(0,255).astype("uint8")
        bgr = cv2.cvtColor(out_img, cv2.COLOR_RGB2BGR)
        out.write(bgr)

        frame_count += 1

cap.release()
out.release()

avg_infer_ms = (total_infer / frame_count) * 1000 if frame_count else 0.0
fps_proc = 1000.0 / avg_infer_ms if avg_infer_ms>0 else 0.0

print(f"CNN done: frames={frame_count}, avg_infer_ms={avg_infer_ms:.2f}ms, fps_est={fps_proc:.2f}")

with open(METRICS, "a") as f:
    f.write(f"[cnn] frames:{frame_count} avg_infer_ms:{avg_infer_ms:.2f} fps_est:{fps_proc:.2f}\n")

print(f"Saved: {OUT_VIDEO}")
