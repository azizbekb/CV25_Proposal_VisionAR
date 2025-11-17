import cv2, numpy as np, os
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

ORIG = "../data/sample_videos/example.mp4"
CNN_OUT = "../results/cnn_demo.mp4"
METRICS = "../results/metrics.txt"
os.makedirs(os.path.dirname(METRICS), exist_ok=True)

cap_o = cv2.VideoCapture(ORIG)
cap_c = cv2.VideoCapture(CNN_OUT)
if not cap_o.isOpened() or not cap_c.isOpened():
    print("ERROR: cannot open original or cnn output video.")
    exit(1)

psnr_list = []
ssim_list = []
count = 0

while True:
    ret_o, fo = cap_o.read()
    ret_c, fc = cap_c.read()
    if not ret_o or not ret_c:
        break
    if fo.shape != fc.shape:
        fc = cv2.resize(fc, (fo.shape[1], fo.shape[0]))
    fo_rgb = cv2.cvtColor(fo, cv2.COLOR_BGR2RGB)
    fc_rgb = cv2.cvtColor(fc, cv2.COLOR_BGR2RGB)

    try:
        ps = psnr(fo_rgb, fc_rgb, data_range=255)
        ss = ssim(fo_rgb, fc_rgb, multichannel=True, data_range=255)
    except Exception:
        ps = psnr(fo_rgb, fc_rgb, data_range=255)
        ss = ssim(cv2.cvtColor(fo, cv2.COLOR_BGR2GRAY),
                  cv2.cvtColor(fc, cv2.COLOR_BGR2GRAY), data_range=255)

    psnr_list.append(ps)
    ssim_list.append(ss)
    count += 1

cap_o.release()
cap_c.release()

if count == 0:
    print("No frames compared.")
    exit(1)

avg_psnr = float(sum(psnr_list) / len(psnr_list))
avg_ssim = float(sum(ssim_list) / len(ssim_list))

print(f"Eval: PSNR={avg_psnr:.2f}, SSIM={avg_ssim:.3f} over {count} frames")

with open(METRICS, "a") as f:
    f.write(f"[eval] PSNR:{avg_psnr:.2f} SSIM:{avg_ssim:.3f} frames:{count}\n")
