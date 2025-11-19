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

### [W1] Baseline Pipeline Completed
- Sample video selected and added to `data/sample_videos/example.mp4`
- Implemented baseline Gaussian + Bilateral denoising
- Generated `baseline_demo.mp4`
- Logged baseline FPS and latency to `results/metrics.txt`
**Status:** ✔ Completed

---

### [W2] CNN Denoising Module Completed
- Implemented lightweight 3-layer CNN in `cnn_denoise.py`
- Ran per-frame inference on sample video
- Generated `cnn_demo.mp4`
- Logged CNN FPS and latency to `results/metrics.txt`
**Status:** ✔ Completed

---

### [W3] Evaluation Metrics Implemented
- Wrote `eval_metrics.py`
- Calculated PSNR and SSIM between original vs CNN
- Added evaluation results to `results/metrics.txt`
**Status:** ✔ Completed

---

### [W4] Optimization + Final Comparison (In Progress)
- Side-by-side final comparison video in progress
- Code refactoring and performance tuning
- Preparing final demo video
**Status:** 🔄 In Progress

---

### [W5] Final Report + Presentation (Upcoming)
- Write final 5–6 page report
- Prepare final slide deck
- Prepare live in-class demo
- Finalize GitHub repo
**Status:** ⏳ Not Started



