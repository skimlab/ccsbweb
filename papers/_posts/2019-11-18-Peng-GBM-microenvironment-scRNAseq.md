---
layout: paper
title: " Probing glioblastoma and its microenvironment using single-nucleus and single-cell sequencing"
image: /images/papers/2019-11-18-Peng-GBM-microenvironment-scRNAseq.png
authors: Peng S, Rath S, Vuong C, Bollam S, Eschbacher J, Dong X, Mehta S, Sanai N, Berens M, Kim S, Dhruv H
year: 2019
ref: Peng et al. Nov 2019. BIBM'19 Single Cell-omics - Challenges and Opportunities 
journal: "IEEE BIBM 2019"
doi: 10.1101/775197
github:
pdf: /pdfs/papers/2019-11-18-Peng-GBM-microenvironment-scRNAseq.pdf
keywords: glioblastoma; microenvironment; single cell sequencing; single nucleus sequencing 
PMID: 
PMCID: 
---

# Abstract

Single-cell (scSeq) and single-nucleus sequencing (snSeq) are powerful tools to investigate cancer genomics at single cell resolution. Multiple studies have recently illuminated intratumoral heterogeneity in glioblastoma, however, the majority focused on molecular complexity of tumor cells, without considering unexplored host cell types that contribute to the microenvironment around tumor. To address the glioblastoma microenvironment composition and potential tumor-host interactions, we performed deep coverage sequencing of freshly resected primary GBM patient tissue without implementing any tumor enrichment strategies. The sequencing resulted in 902 cells and 1186 nuclei, respectively, passing quality control and with low mitochondrial gene percentage. We customized reference transcriptome by listing gene transcript loci as exons to take into account immature RNA, which greatly improved the alignment rate for single-nucleus data. We applied Cell Ranger pipelines (Version 3.0.2) and Seurat package (Version 2.3.1) and discovered 10 clusters in both scSeq and snSeq. Pathway analysis of each cluster signature in scSeq data along with known GBM microenvironment cell signatures revealed glioma tumor population along with surrounding microglia/macrophages, astrocytes, pericytes, oligodendrocytes, T cells and endothelial cells. The analysis of snSeq was able to capture the majority of cell types from patient tissues (tumor and microenvironment cells), but interestingly presented different cell type composition in microenvironment cell types such as microglia/macrophages. Integrating single-cell and single-nucleus transcriptomic data using canonical correlation analysis facilitated a comparison of snSeq and scSeq, contrasting depiction for certain cell types (e.g. NKX6-2 gene in Oligodendrocytes).  Differential analysis of pathways between tumor and microenvironment cells unveiled potentially rewired pathways such as double strand break repair pathway. Our results demonstrate the cellular diversity of brain tumor microenvironment and lay a foundation to further investigate the individual tumor and host cell transcriptomes that are influenced not only by their cell identity but also by their interaction with surrounding microenvironment.