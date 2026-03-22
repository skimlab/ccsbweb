---
layout: ccsbtalk
title: "[CCSB Seminar Series] Computational Methods for Molecular Cancer Classification: From Traditional Machine Learning to Prior-Fitted Networks in Multi-Omics Analysis"
speaker: Seungchan Kim
speakerurl: https://ccsb.pvamu.edu/teams/seungchan-kim/
photo: /images/team/seungchan-kim.png
date: 2025-09-10
time: 12:00pm
venue: Zoom
venue-inperson: CCSB Conference Room ELEN 231
venue-ece: ECE Conference Room ELEN 315D or Zoom
past-webinar: https://pvpanther.zoom.us/j/98705850635?pwd=lYb4oSwu6obv6wjdfmPiPFg6DX9v47.1
recording: 
categories: [blog, talks]
tags: [ccsb-seminar]
event: CCSB-Seminar
---


## Abstract

Molecular classification of cancer using multi-omics data is central to precision oncology, enabling identification of distinct subtypes based on gene expression, mutations, and methylation—beyond traditional histology. While machine learning methods like Support Vector Machines and Random Forests have shown success, they struggle with high-dimensionality, multi-omics integration, and limited generalizability. Deep learning offers promise but faces challenges such as overfitting on small datasets, lack of interpretability, and poor cross-cohort performance.

We present TabPFN, a Prior-data Fitted Network designed for tabular data, as a new foundation model for cancer classification. Unlike traditional models requiring dataset-specific training, TabPFN uses in-context learning via pretraining on synthetic data. This eliminates hyperparameter tuning, allows fast inference, performs well on small datasets, and includes built-in uncertainty estimation—making it ideal for clinical use.

Applied to multiple cohorts of gene expression data of bladder cancer, including The Cancer Genome Atlas (TCGA) RNA-seq data, TabPFN achieves competitive or superior performance with significantly reduced computational time. Our results show robust classification of tumor subtypes using gene expression alone.

Foundation models like TabPFN represent a paradigm shift in computational oncology, addressing long-standing barriers to clinical translation. We conclude by outlining future directions, including multi-omics integration, automated feature selection, and cancer-specific foundation models.


## Speaker Bio

Dr. Seungchan Kim is a Chief Scientist and Executive Professor at the [Department of Electrical and Computer Engineering](http://www.pvamu.edu/ece/) and the Director of the [CRI Center for Computational Systems Biology](https://ccsb.pvamu.edu/) at the [Prairie View A&M University (PVAMU)](https://www.pvamu.edu). Prior to this appointment, he was the Head of Biocomputing Unit and an Associate Professor at Integrated Cancer Genomics Division of [Translational Genomics Research Institute (TGen)](https://www.tgen.org). He was one of the founding faculty members of TGen, founded in 2002, by Dr. Trent, then-Scientific Director of the [National Human Genome Research Institute](https://www.genome.gov/) at the [National Institutes of Health](https://www.nih.gov), leading computational systems biology research at the institute. He was also an Assistant Professor in the [School of Computing, Informatics, Decision Systems Engineering (CIDSE)](https://cidse.engineering.asu.edu/) at the [Arizona State University](https://www.asu.edu) from 2004 till 2011. Dr. Kim received B.S. and M.S. degrees in [Agriculture Engineering](http://bse.snu.ac.kr/) from the [Seoul National University](http://www.snu.ac.kr/), and Ph.D. in [Electrical Engineering](https://engineering.tamu.edu/electrical/) from the [Texas A&M University](http://www.tamu.edu/). He also got his post-doctoral training at the Cancer Genetics Branch of [National Human Genome Research Institute](https://www.genome.gov/).

Dr. Kim’s research interests include: 1) mathematical modeling of genetic regulatory networks, 2) development of computational methods to analyze multitude of high throughput multi-omics data to identify disease biomarkers, and 3) computational models to diagnose patients or predict patient outcomes, for example, disease subtypes or drug response. His studies have had a large influence on the development of computational tools to study underlying mechanisms for cancer development and better understand the molecular mechanisms behind cancer biology and biological systems.

