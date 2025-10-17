# 🗺️ VisionAR — Project Roadmap
**Project:** Real-Time Artifact Removal for Passthrough AR  
**Team:** Azizbek (Lead), Azim (Model & Evaluation), Ikromjon (Data & Integration)  
**Semester:** Fall 2025  
**Repo:** https://github.com/VisionAR/CV25_VisionAR

---

## 📆 Weekly Milestones

### **Week 1 (Oct 17–Oct 21) — Team & Proposal**
- ✅ Finalize topic (#23) and submit proposal PDF.
- ✅ Create repo and add README + ROADMAP.md.
- 🔧 Set up Python environment and verify OpenCV + PyTorch versions.
- **Owner:** Azizbek  

### **Week 2 (Oct 22–Oct 28) — Research & Dataset Setup**
- Collect AR passthrough or webcam video samples (e.g., OpenAR dataset or custom recordings).
- Study existing denoising models (DnCNN, FastDVDnet).
- Prepare small test dataset for experiments.
- **Owner:** Ikromjon  

### **Week 3 (Oct 29–Nov 4) — Baseline Implementation**
- Implement baseline denoising with OpenCV filters (Gaussian, Bilateral).
- Measure PSNR/SSIM and latency for baseline.
- **Owner:** Azim  

### **Week 4 (Nov 5–Nov 11) — Model Integration**
- Integrate lightweight CNN (DnCNN or FastDVDnet).
- Add temporal consistency module for smoother video output.
- Test real-time FPS performance.
- **Owner:** Azim  

### **Week 5 (Nov 12–Nov 18) — Optimization & Evaluation**
- Optimize inference speed (batch size, frame resizing, GPU/CPU switch).
- Evaluate latency (<30ms), PSNR, SSIM, and perceptual stability.
- Record sample output video for report/demo.
- **Owner:** Azizbek  

### **Week 6 (Nov 19–Nov 25) — Final Report & Demo**
- Write final report + prepare slides/video demo.
- Conduct internal team review.
- Submit code, report, and video.
- **Owner:** Whole team  

---

## 🧭 Roles (RACI Summary)
| Task | Responsible | Accountable | Consulted | Informed |
|------|-------------|--------------|------------|-----------|
| Project Management | Azizbek | Azizbek | Team | Instructor |
| Dataset & Preprocessing | Ikromjon | Azizbek | Azim | Team |
| Model Implementation | Azim | Azizbek | Ikromjon | Team |
| Evaluation & Metrics | Azim | Azizbek | Team | Instructor |
| Documentation & Report | Azizbek | Whole Team | Team | Instructor |

---

## ✅ Progress Updates
- **[W1]** Team + topic finalized, repo created, environment verified.  
- **[W2]** Dataset collected, baseline filters tested.  
- **[W3]** Baseline model running, evaluation metrics defined.  
- **[W4–W6]** Advanced model integrated, optimized, and final demo produced.

---

## 🏁 Final Deliverables
- 📄 **Final Report (PDF)**  
- 💻 **GitHub Repository** (code, README, ROADMAP.md)  
- 🎥 **Demo Video** showing before/after denoising  
- 🧮 **Evaluation Results:** latency, PSNR, SSIM, perceptual stability
