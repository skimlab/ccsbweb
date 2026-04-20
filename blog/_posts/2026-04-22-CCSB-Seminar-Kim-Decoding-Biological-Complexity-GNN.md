---
layout: ccsbtalk
title: "[CCSB Seminar Series] Decoding Biological Complexity: Graph Neural Networks in Single-Cell and Spatial Transcriptomics"
speaker: Seungchan Kim
speakerurl: https://ccsb.pvamu.edu/team/seungchan-kim/
photo: /images/talks/speakers/seungchan-kim.png
date: 2026-04-22
time: 12:00pm
venue: Zoom
venue-inperson: CCSB Conference Room ELEN 231
venue-ece: ECE Conference Room ELEN 315D or Zoom
webinar: https://pvpanther.zoom.us/j/99830638545?pwd=rmE3MoIErFQW9Zz36fBp8ns1cDGQp2.1&from=addon
recording: 
talkslide:
categories: [blog, talks]
tags: [ccsb-seminar]
event: CCSB-Seminar
---


## Abstract

The rapid evolution of high-throughput sequencing has transformed our ability to profile biological systems, yet the inherent relational complexity of these data necessitates advanced computational frameworks. This seminar explores the paradigm shift from traditional deep learning to Graph Neural Networks (GNNs), a class of models uniquely equipped to handle non-Euclidean data. We begin by establishing the mathematical foundations of GNNs, focusing on the message-passing framework and the role of graph convolutional operators in aggregating neighborhood information. We will contrast standard architectures—such as Graph Convolutional Networks (GCNs) and Graph Attention Networks (GATs)—while highlighting their utility in both general domains (social networks, recommendation engines) and specialized biomedical research.

The core of the presentation delves into the integration of GNNs with single-cell RNA sequencing (scRNA-seq) and spatial transcriptomics. We will discuss how cell-cell similarity graphs and physical spatial coordinates can be modeled to perform critical tasks such as cell-type annotation, data imputation, and spatial domain detection. Furthermore, we will examine the application of GNNs in reconstructing Gene Regulatory Networks (GRNs). By treating genes as nodes and regulatory interactions as edges, GNNs provide a robust mechanism for inferring causal relationships and identifying spatially varying regulatory patterns that are often obscured in traditional, non-graph-based analyses.

The seminar will also review the current ecosystem of tools, including PyTorch Geometric (PyG) and specialized packages like SpaGCN and DeepSEM. We conclude by discussing future directions for GNNs in modeling multi-modal biomedical data. 


## Speaker Bio

Dr. Seungchan Kim is a Chief Scientist and Executive Professor at the [Department of Electrical and Computer Engineering](http://www.pvamu.edu/ece/) and the Director of the CRI [Center for Computational Systems Biology]({{site.baseurl}}{{"/"}}) at the [Prairie View A&M University (PVAMU)](http://www.pvamu.edu).  Prior to this appointment, he was the Head of Biocomputing Unit and an Associate Professor at Integrated Cancer Genomics Division of [Translational Genomics Research Institute (TGen)](http://www.tgen.org).  He was one of the founding faculty members of TGen, founded in 2002, by Dr. Trent, then-Scientific Director of the [National Human Genome Research Institute](https://www.genome.gov) at the [National Institutes of Health](https://www.nih.gov), leading computational systems biology research at the institute.  He was also an Assistant Professor in the [School of Computing, Informatics, Decision Systems Engineering (CIDSE)](https://cidse.engineering.asu.edu) at the [Arizona State University](http://www.asu.edu) from 2004 till 2011.  Dr. Kim received B.S. and M.S. degrees in [Agriculture Engineering](http://bse.snu.ac.kr/) from the [Seoul National University](http://www.snu.ac.kr), and Ph.D. in [Electrical Engineering](https://engineering.tamu.edu/electrical/) from the [Texas A&M University](http://www.tamu.edu). He also got his post-doctoral training at the Cancer Genetics Branch of [National Human Genome Research Institute](https://www.genome.gov).

Dr. Kim's research interests include: 1) mathematical modeling of genetic regulatory networks, 2) development of computational methods to analyze multitude of high throughput multi-omics data to identify disease biomarkers, and 3) computational models to diagnose patients or predict patient outcomes, for example, disease subtypes or drug response. His studies have had a large influence on the development of computational tools to study underlying mechanisms for cancer development and better understand the molecular mechanisms behind cancer biology and biological systems.
