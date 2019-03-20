---
layout: paper
title: "Leveraging Spatial Variation in Tumor Purity for Improved Somatic Variant Calling of Archival Tumor Only Samples"
image: /images/papers/2019-03-18-halperin-tumor-only-somatic-variant-calling.jpg
authors: Halperin RF, Liang WS, Kulkarni S, Tassone EE, Adkins J, Enriquez D, Tran NL, Hank NC, Newell J, Kodira C, Korn R, Berens ME, Kim S, Byron SA
year: 2019
ref: Halperin et al. 20 March 2019. Front. Oncol. 9:119.
journal: "Frontiers in Oncology"
doi: 10.3389/fonc.2019.00119
github:
pdf: /pdfs/papers/2019-03-18-halperin-tumor-only-somatic-variant-calling.pdf
keywords: Somatic Variant Calling; Tumor; Bioinformatics
PMID: 
PMCID: 
---

# Abstract

Archival tumor samples represent a rich resource of annotated specimens for translational genomics research.  However, standard variant calling approaches require a matched normal sample from the same individual, which is often not available in the retrospective setting, making it difficult to distinguish between true somatic variants and individual-specific germline variants.  Archival sections often contain adjacent normal tissue, but this tissue can include infiltrating tumor cells.  As existing comparative somatic variant callers are designed to exclude variants present in the normal sample, a novel approach is required to leverage adjacent normal tissue with infiltrating tumor cells for somatic variant calling.  Here we present lumosVar 2.0, a software package designed to jointly analyze multiple samples from the same patient, built upon our previous single sample tumor only variant caller lumosVar 1.0.  The approach assumes that the allelic fraction of somatic variants and germline variants follow different patterns as tumor content and copy number state change.  LumosVar 2.0 estimates allele specific copy number and tumor sample fractions from the data, and uses a model to determine expected allelic fractions for somatic and germline variants and classify variants accordingly. To evaluate lumosVar 2.0 to jointly call somatic variants with tumor and adjacent normal samples, we used a glioblastoma dataset with matched high and low tumor content and germline whole exome sequencing data (for true somatic variants) available for each patient.   Both sensitivity and positive predictive value were improved when analyzing the high tumor and low tumor samples jointly compared to analyzing the samples individually or in-silico pooling of the two samples. Finally, we applied this approach to a set of breast and prostate archival tumor samples for which tumor blocks containing adjacent normal tissue were available for sequencing.  Joint analysis using lumosVar 2.0 detected several variants, including known cancer hotspot mutations that were not detected by standard somatic variant calling tools using the adjacent normal as a reference. Together, these results demonstrate the potential utility of leveraging paired tissue samples to improve somatic variant calling when a constitutional sample is not available.