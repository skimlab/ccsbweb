---
layout: paper
title: "A Generalizable Low-Precision Softmax Approximation for Small-FPGA Deployment of Vision Transformers"
image: /images/papers/2026-04-22-aboagye-generalizable-low-precision-softmax-approximation.jpg
authors: Samuel Aboagye, Lujun Zhai, Suxia Cui
year: 2026
ref: Samuel Aboagye et al., Electronics, 2026 | | https://doi.org/10.3390/electronics15091774
doi: 10.3390/electronics15091774
github: 
pdf: https://doi.org/10.3390/electronics15091774
keywords: 
PMID: 
PMCID: 
---

# Abstract

The growing prominence of transformer-based architectures in computer vision tasks has created a need for their efficient hardware deployment, especially on resource-constrained platforms such as small Field-Programmable Gate Arrays (FPGAs). However, the complex mathematical operations in transformers, such as the Softmax activation function, pose a significant challenge for efficient hardware implementation due to the substantial computational resources required. Previous works have largely focused on large FPGA platforms, leaving a gap in solutions tailored for small FPGAs with limited resources. This paper proposes a generalizable low-precision Softmax approximation tailored for deploying Vision Transformers on small FPGA platforms while significantly improving their hardware efficiency. The approach is first validated in software using SwinIR super resolution to ensure reconstruction fidelity and is then analyzed for FPGA deployment. Experimental results demonstrate that the proposed fourth-order clamped approximation achieves near-reference performance, incurring only 0.15 dB PSNR and 0.0059 SSIM degradation on SwinIR-M, while significantly reducing precision and memory requirements. A Horner-form reformulation further improves hardware efficiency by limiting intermediate precision growth. Overall, this work presents a reconstruction-aware and hardware-friendly Softmax reformulation that enables practical deployment of vision transformers on small FPGA platforms.
