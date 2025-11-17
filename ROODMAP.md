# 🗺️ VisionAR — Project Roadmap  
**Course:** Computer Vision (CV25)  
**Team:** VisionAR (Azizbek, Azim, Ikromjon)  

---

## 📌 Overview  
This roadmap tracks development progress for the VisionAR real-time artifact removal system.  
It includes milestones, responsibilities, deliverables, and progress logs.

---

# 🧱 Milestones

### **M1 — Project Setup**
- Team formation  
- Topic selection (#23 Real-Time Artifact Removal for AR Passthrough)  
- GitHub repo created  
- Proposal submitted (`docs/CV25_Proposal_VisionAR.pdf`)

**Status:** ✔ Completed  

---

### **M2 — Baseline Pipeline**
- Load sample video (`data/sample_videos/example.mp4`)  
- Implement Gaussian + Bilateral denoise  
- Generate baseline demo video  
- Measure FPS + Latency  

**Files:**  
`src/baseline_denoise.py`  
`src/measure_latency.py`

**Status:** ✔ Completed

---

### **M3 — CNN Denoising Module**
- Implement lightweight CNN (PyTorch)  
- Apply per-frame inference  
- Save CNN demo video  
- Compare with baseline  

**Files:**  
`src/cnn_denoise.py`

**Status:** ✔ Completed

---

### **M4 — Evaluation**
- Compute PSNR / SSIM  
- Compare Original vs CNN Output  
- Append results to metrics file  

**Files:**  
`src/eval_metrics.py`  
`results/metrics.txt`

**Status:** ✔ Completed

---

### **M5 — Final Deliverables**
- Final combined comparison video  
- README polished  
- Repo finalized  
- In-class demo prepared  

**Status:** ⏳ In Progress

---

# 📅 Weekly Progress Log (Required for class)

