---
layout: paper
title: "GPU-accelerated differential dependency network analysis"
image: /images/papers/2018-03-21-speyer-GPU-accelerated.png
authors: Speyer G, Rodriguez JJ, Bencomo T, Kim S.
year: 2018
ref: Speyer et al. 2018. Euromicro International Conference on Parallel, Distributed and Network-based Processing (PDP 2018), Mar 21-23, 2018.
journal: "PDP 2018"
doi: 10.1109/PDP2018.2018.00072
github: https://github.com/dolchan/eddy-gpu
pdf: /pdfs/papers/2018-03-21-speyer-GPU-accelerated.pdf
keywords: EDDY, differential dependency analysis, gene regulatory networks, biochemical pathways, graphics processing units
PMID: 
PMCID: 
---

# Abstract

EDDY (Evaluation of Differential DependencY) interrogates transcriptomic data to identify differential genetic dependencies within a biological pathway. Through its probabilistic framework with resampling and permutation, aided by the incorporation of annotated gene sets, EDDY demonstrated superior sensitivity to other methods. However, this statistical rigor incurs considerable computational cost, limiting its application to larger datasets. The ample and independent computation coupled with manageable memory footprint positioned EDDY as a strong candidate for graphical processing unit (GPU) implementation. Custom kernels decompose the independence test loop, network construction, network enumeration, and Bayesian network scoring to accelerate the computation. GPU-accelerated EDDY consistently exhibits two orders of magnitude in performance enhancement, allowing the statistical rigor of the EDDY algorithm to be applied to larger datasets.
