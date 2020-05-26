---
layout: ccsbtalk
title: "[CCSB Seminar Series] Cell Type Identification from Single-Cell Transcriptomic Data via Deep Learning"
speaker: Xishuang Dong, Ph.D.
speakerurl: https://ccsb.pvamu.edu/team/xishuang-dong/
photo: /images/talks/speakers/xdong.jpg
date: 2020-04-08
time: 12:00pm
venue: ELEN231
webinar: https://pvamu.webex.com/pvamu/j.php?MTID=mec801df2a0fe9967c7f20b31a1ca51a8
categories: [blog, talks]
tags: [ccsb-seminar]
venue: Webinar
event: CCSB-Seminar
speaker: Xishuang Dong, Ph.D.
---

### [Watch the talk](https://ccsb.pvamu.edu/media/video/ccsb-seminar-dong-2020-04-08.mp4) - New!

## Abstract

Cell type identification from single-cell transcriptomic data is a common goal of single-cell RNA sequencing (scRNAseq) data analysis. Neural networks have been employed to identify cell types from scRNAseq data with high performance. However, it requires a large mount of individual cells with accurate and unbiased annotated types to build the identification models. Unfortunately, labeling the scRNAseq data is cumbersome and time-consuming as it involves manual inspection of marker genes. To overcome this challenge, we propose a semi-supervised learning model to use unlabeled scRNAseq cells and limited amount of labeled scRNAseq cells to implement cell identification. Firstly, we transform the scRNAseq cells to gene sentences?, which is inspired by similarities between natural language system and gene system. Then genes in these sentences are represented as gene embeddings to reduce data sparsity. With these embeddings, we implement a semi-supervised learning model based on recurrent convolutional neural networks (RCNN), which includes a shared network, a supervised network and an unsupervised network. The proposed model is evaluated on macosko2015, a large-scale single-cell transcriptomic dataset with ground truth of individual cell types. It is observed that the proposed model is able to achieve encouraging performance by learning on very limited amount of labeled scRNAseq cells together with a large number of unlabeled scRNAseq cells.


## Speaker Bio
Dr. Xishuang Dong is an Assistant Professor of CRI Center for Computational Systems Biology at Department of Electrical and Computer Engineering at Prairie View A&M University (PVAMU). Dr. Dong received B.S. degree in computer science and technique (sub-field of computer engineering) at Harbin University of Science and Technology, M.S. degree in computer software and theory (sub-field of computer engineering) at Harbin Engineering University, and Ph.D. in computer application (sub-field of computer engineering) at Harbin Institute of Technology.

His research interests include: 1) machine learning based computational systems biology; (2) biomedical information processing; (3) deep learning for big data analysis; (4) natural language processing.
