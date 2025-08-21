---
layout: ccsbtalk
title: "[CCSB Seminar Series] Toward reliability evaluation of computational models of protein molecules and their interactions"
speaker: Md Hossain Shuvo, Ph.D.
speakerurl: https://mdhossainshuvo.github.io/
photo: /images/talks/speakers/md-hossain-shuvo.jpg
date: 2025-02-19
time: 12:00pm
venue: Zoom
venue-inperson: CCSB Conference Room ELEN 231
venue-ece: ECE Conference Room ELEN 315D or Zoom
past-webinar: https://pvpanther.zoom.us/j/98038578074?pwd=ABHJ2XmoJwFCPw2rta24dpVySbmieK.1&from=addon
recording: https://pvpanther.zoom.us/rec/share/MJ97oDsfTElu2Jd3ywqqsBx5I9DxHLMn-Q1HkUR9iYRvMBEbldEtedczLrnpzgJF.Bc5ee_amxutl4sBT
categories: [blog, talks]
tags: [ccsb-seminar]
event: CCSB-Seminar
---

[Seminar slide](/pdfs/talks/2025-02-19-CCSB-Seminar-Shuvo-EquiRank-toward-reliability-evaluation.pdf) - thanks to the speark, Dr. Shuvo.

## Abstract

Protein three-dimensional (3D) structures regulate various biological processes within cells. Recent breakthroughs in computational prediction have significantly improved the accuracy of protein 3D structure modeling, making notable progress in bridging the gap between available sequence data and the corresponding 3D protein structures. However, the accuracy of computationally predicted protein models varies depending on the availability of experimentally solved homologous structures, prompting uncertainty about their reliability. Therefore, estimating the accuracy of computationally predicted protein models is crucial to understanding their reliability when the experimental structures are unavailable. Subsequently, it helps identify unreliable regions for further improvement of their structural reliability for practical application in biomedical and life science research.

In this talk, I will present my research on developing data-driven computational methods for estimating the accuracy of predicted protein models. First, I will introduce the problem of protein model quality estimation for evaluating their reliability and discuss recent advancements in applying deep learning to this challenge. Then, I will introduce EquiRank, our method for estimating the quality of protein-protein interaction interfaces in multimeric protein models. EquiRank leverages a symmetry-aware E(3) equivariant deep graph neural network (EGNN) and integrates embeddings from the pretrained ESM-2 protein language model to improve prediction accuracy. By representing interacting residue pairs as a graph and incorporating diverse structural and sequence-derived features, EquiRank demonstrates improved ranking performance over existing protein complex quality estimation methods. 


## Speaker Bio

Md Hossain Shuvo is an Assistant Professor in the Department of Computer Science at Prairie View A&M University. His research lies at the intersection of computational biology, bioinformatics, machine learning, and data science. He is particularly interested in developing data-driven computational approaches for evaluating and improving the reliability of computational models of protein molecules by combining machine learning and optimization algorithms. He has published in flagship conferences and high-impact journals, such as ISMB and Nucleic Acid Research, respectively. He is a recipient of the Pratt Fellowship by Virginia Tech and the Young Scientist Excellence Award. For more information, please visit [https://mdhossainshuvo.github.io/](https://mdhossainshuvo.github.io/).

