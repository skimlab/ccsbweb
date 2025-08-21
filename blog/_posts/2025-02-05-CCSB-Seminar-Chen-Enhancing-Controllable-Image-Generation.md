---
layout: ccsbtalk
title: "[CCSB Seminar Series] Enhancing Controllable Image Generation with Efficient Consistency Feedback" 
speaker: Chen Chen, Ph.D.
speakerurl: https://www.crcv.ucf.edu/chenchen/
photo: /images/talks/speakers/chen-chen.jpeg
date: 2025-02-05
time: 12:00pm
venue: Zoom
venue-inperson: CCSB Conference Room ELEN 231
venue-ece: ECE Conference Room ELEN 315D or Zoom
past-webinar: https://pvpanther.zoom.us/j/98038578074?pwd=ABHJ2XmoJwFCPw2rta24dpVySbmieK.1&from=addon
recording:  
categories: [blog, talks]
tags: [ccsb-seminar]
event: CCSB-Seminar
---

[Talk slides](/pdfs/talks/2025-02-05-CCSB-Seminar-Chen-Enhancing-Controllable-Image-Generation.pdf)

## Abstract

Controllable text-to-image generation is a crucial advancement in AI-driven content creation, enabling users to specify structured constraints such as segmentation masks, edge maps, and depth cues. While existing methods like ControlNet attempt to integrate such controls into diffusion models, they often struggle with precise alignment between input conditions and generated outputs. In this talk, I will introduce ControlNet++, a novel approach that explicitly optimizes pixel-level cycle consistency between generated images and their conditional controls. Unlike prior methods that implicitly integrate conditions into the denoising process, ControlNet++ leverages a pre-trained discriminative reward model to enforce consistency, significantly enhancing controllability. Furthermore, we propose an efficient reward fine-tuning strategy that eliminates the need for costly multi-step sampling, enabling scalable training with reduced memory overhead. Extensive experiments demonstrate that ControlNet++ outperforms existing techniques across various control modalities.


## Speaker Bio

[Dr. Chen Chen](https://www.crcv.ucf.edu/chenchen/) is an Associate Professor at the [Center for Research in Computer Vision](https://www.crcv.ucf.edu), [Department of Computer Science](https://www.cs.ucf.edu) at the [University of Central Florida (UCF)](https://www.ucf.edu). He earned his Ph.D. in Electrical Engineering from the University of Texas at Dallas in 2016, where he was honored with the David Daniel Fellowship for the Best Doctoral Dissertation. His research interests span computer vision, efficient deep learning, multimodal learning, and federated learning. Actively involved in NSF and industry-sponsored research projects, Dr. Chen focuses on developing efficient, resource-aware machine vision algorithms and systems for extensive camera networks. His work is also supported by notable agencies including IARPA and NIFA. Dr. Chen serves as an Associate Editor for the IEEE Transactions on Circuits and Systems for Video Technology (T-CSVT), the Journal of Real-Time Image Processing, and the IEEE Journal on Miniaturization for Air and Space Systems. He has also taken on the role of area chair for several conferences, such as ECCV 2022, CVPR 2022, and ACM Multimedia from 2019 to 2024. His scholarly contributions are highlighted by his Google Scholar metrics, with more than 22,800 citations and an h-index of 72. For more information, please visit [https://www.crcv.ucf.edu/chenchen/](https://www.crcv.ucf.edu/chenchen/).


