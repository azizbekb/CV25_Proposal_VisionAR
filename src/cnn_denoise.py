import cv2, torch, torch.nn as nn, numpy as np, os, time
from tqdm import tqdm

# Simple lightweight CNN model
class SmallDenoiser(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.ReLU(),
            nn.Conv2d(32, 32, 3, padding=1), nn.ReLU(),
            nn.Conv2d(32, 3, 3, padding=1)
        )
    def forward(self, x):
        return self.net(x)

# Initialize model
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = SmallDenoiser().to(device)
model.eval()

# Open sample video
os.makedirs("../results", exist_ok=True)
input_video = "../data/sample_videos/example.mp4"
cap = cv2.VideoCapture(input_video)
if not cap.isOpened():
    print("Error: no video")
    exit()

# Video writer for output
out_path = "../results/cnn_demo.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
w, h = int(cap.get(3)), int(cap.get(4))
out = cv2.VideoWriter(out_path, fourcc, fps, (w, h))

frame_count, total_t = 0, 0
print("Running lightweight CNN denoiser...")

with torch.no_grad():
    for _ in tqdm(range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))):
        ret, frame = cap.read()
        if not ret:
            break
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        tensor = torch.from_numpy(img).float().permute(2,0,1).unsqueeze(0).to(device)/255.
        t0 = time.time()
        denoised = model(tensor)
        t1 = time.time()
        total_t += (t1 - t0)
        frame_count += 1
        out_img = (denoised.squeeze(0).permute(1,2,0).cpu().numpy()*255).astype(np.uint8)
        out_bgr = cv2.cvtColor(out_img, cv2.COLOR_RGB2BGR)
        out.write(out_bgr)

cap.release()
out.release()

avg_latency = (total_t/frame_count)*1000
fps_out = 1000 / avg_latency
print(f"Average latency: {avg_latency:.2f} ms | FPS: {fps_out:.2f}")

with open("../results/metrics.txt", "a") as f:
    f.write(f"CNN avg_latency_ms:{avg_latency:.2f} fps:{fps_out:.2f}\n")
