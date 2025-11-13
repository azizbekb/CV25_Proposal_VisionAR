import cv2
import numpy as np
import time, os

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

frame_count = 0
start = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply simple baseline filters
    gaussian = cv2.GaussianBlur(frame, (5,5), 0)
    bilateral = cv2.bilateralFilter(gaussian, 9, 75, 75)

    combined = np.hstack((frame, bilateral))
    cv2.putText(combined, "Original | Denoised", (40, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("VisionAR Baseline", combined)
    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

end = time.time()
fps = frame_count / (end - start)
print(f"FPS: {fps:.2f}")

os.makedirs("../results", exist_ok=True)
with open("../results/metrics.txt", "a") as f:
    f.write(f"Baseline FPS: {fps:.2f}\n")

cap.release()
cv2.destroyAllWindows()
