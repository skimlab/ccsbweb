---
layout: paper
title: "Semi-supervised Deep Learning for Cell Type Identification from Single-Cell Transcriptomic Data"
image: /images/papers/2022-05-10-dong-semi-supervised-deep-learning.png
authors: Dong X, Chowdhury S, Victor U, Li X, Qian L
year: 2022
ref: Dong et al., IEEE/ACM Trans Comput Biol Bioinform. 2022 May 10
journal: "IEEE/ACM Trans Comput Biol Bioinform."
doi: 10.1109/TCBB.2022.3173587
github:
pdf: /pdfs/papers/2022-05-10-dong-semi-supervised-deep-learning.pdf
keywords:  Single-Cell Sequencing, Semi-supervised Learning, Recurrent Convolutional Neural Networks, Joint Optimization
PMID: 35536811
PMCID: 
---

# Abstract

Cell type identification from single-cell transcriptomic data is a common goal of single-cell RNA sequencing (scRNAseq) data analysis. Deep neural networks have been employed to identify cell types from scRNAseq data with high performance. However, it requires a large mount of individual cells with accurate and unbiased annotated types to train the identification models. Unfortunately, labeling the scRNAseq data is cumbersome and time-consuming as it involves manual inspection of marker genes. To overcome this challenge, we propose a semi-supervised learning model "SemiRNet" to use unlabeled scRNAseq cells and a limited amount of labeled scRNAseq cells to implement cell identification. The proposed model is based on recurrent convolutional neural networks (RCNN), which includes a shared network, a supervised network and an unsupervised network. The proposed model is evaluated on two large scale single-cell transcriptomic datasets. It is observed that the proposed model is able to achieve encouraging performance by learning on the very limited amount of labeled scRNAseq cells together with a large number of unlabeled scRNAseq cells.
