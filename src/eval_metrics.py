import cv2, numpy as np, os
from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim

orig = cv2.VideoCapture("../data/sample_videos/example.mp4")
cnn = cv2.VideoCapture("../results/cnn_demo.mp4")

psnr_list, ssim_list = [], []
while True:
    ret1, f1 = orig.read()
    ret2, f2 = cnn.read()
    if not ret1 or not ret2:
        break
    f1 = cv2.resize(f1, (f2.shape[1], f2.shape[0]))
    psnr_list.append(psnr(f1, f2))
    ssim_list.append(ssim(cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY),
                          cv2.cvtColor(f2, cv2.COLOR_BGR2GRAY)))

avg_psnr = np.mean(psnr_list)
avg_ssim = np.mean(ssim_list)
print(f"PSNR: {avg_psnr:.2f}, SSIM: {avg_ssim:.3f}")

with open("../results/metrics.txt", "a") as f:
    f.write(f"PSNR:{avg_psnr:.2f} SSIM:{avg_ssim:.3f}\n")
