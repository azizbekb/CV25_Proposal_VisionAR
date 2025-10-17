# 🗺️ VisionAR — Project Roadmap
**Project:** Real-Time Artifact Removal for Passthrough AR (Temporal + Spatial Denoising)  
**Team:** VisionAR  
- 🧩 **Azizbek — Project Lead**  
- ⚙️ **Azim — Model & Evaluation Lead**  
- 🧪 **Ikromjon — Data & Integration Lead**  
**Semester:** Fall 2025  
**Course:** Computer Vision (CV25)  
**Repo:** https://github.com/azizbekb/CV25_Proposal_VisionAR

---

## 📆 Weekly Milestones

### **Week 1 (Oct 17–Oct 21) — Team & Proposal**
- ✅ Finalize topic (#23) and submit proposal PDF.  
- ✅ Create repo and add README + ROADMAP.md.  
- 🔧 Set up Python environment and verify OpenCV + PyTorch installations.  
- **Owner:** Azizbek  

---

### **Week 2 (Oct 22–Oct 28) — Research & Dataset Setup**
- Collect AR passthrough or webcam video samples (OpenAR dataset or custom recordings).  
- Review denoising models: DnCNN, FastDVDnet, Real-ESRGAN.  
- Prepare small dataset for initial testing.  
- **Owner:** Ikromjon  

---

### **Week 3 (Oct 29–Nov 4) — Baseline Implementation**
- Implement baseline denoising using OpenCV filters (Gaussian, Bilateral, Median).  
- Measure baseline metrics (PSNR, SSIM, FPS, latency).  
- Log results in `/results/baseline/` folder.  
- **Owner:** Azim  

---

### **Week 4 (Nov 5–Nov 11) — Model Integration**
- Integrate lightweight CNN (DnCNN or FastDVDnet).  
- Add temporal consistency module for smoother video denoising.  
- Test real-time FPS and latency performance.  
- **Owner:** Azim  

---

### **Week 5 (Nov 12–Nov 18) — Optimization & Evaluation**
- Optimize inference (frame resizing, batch tuning, GPU vs CPU).  
- Evaluate latency (<30ms), PSNR, SSIM, and perceptual stability.  
- Record short before/after sample video.  
- **Owner:** Azizbek  

---

### **Week 6 (Nov 19–Nov 25) — Final Report & Demo**
- Write final report and prepare presentation/demo video.  
- Conduct internal review and finalize deliverables.  
- Submit report + repo link via LMS.  
- **Owner:** Whole Team  

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

## ✅ Weekly Progress Log
- **[W1]** Team & topic finalized, repo created, environment verified.  
- **[W2]** Dataset collected, reviewed existing denoising models.  
- **[W3]** Baseline filters implemented, metrics tested.  
- **[W4]** Lightweight CNN integrated, real-time FPS verified.  
- **[W5]** Optimization done, evaluation results collected.  
- **[W6]** Final report and demo video submitted.  

---

## 🏁 Final Deliverables
- 📄 **Final Report (PDF)**  
- 💻 **GitHub Repository** (code, README, ROADMAP.md)  
- 🎥 **Demo Video** showing before/after denoising  
- 📊 **Evaluation Results:** Latency, PSNR, SSIM, perceptual stability  

---

### 🧠 Notes
> This roadmap will be updated weekly as part of the project’s continuous progress tracking.  
> Each week’s commit will reference its corresponding milestone (e.g., `[W3] Baseline model results logged`).
