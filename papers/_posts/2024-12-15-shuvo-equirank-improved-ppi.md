---
layout: paper
title: "EquiRank: Improved protein-protein interface quality estimation using protein language-model-informed equivariant graph neural networks"
image: /images/papers/2024-12-15-shuvo-equirank-improved-ppi.jpg
authors: Shuvo MH, Bhattacharya D
year: 2024
ref: Shuvo, Compu. and Struct. Biotech, Dec 2024, vol. 27, 160-170
doi: 10.1016/j.csbj.2024.12.015
github: https://github.com/mhshuvo1/EquiRank
pdf: https://www.csbj.org/action/showPdf?pii=S2001-0370%2824%2900438-0
keywords: Protein-protein interaction, Protein complex quality estimation, Protein language models, Graph neural networks, Deep learning
PMID: 39850657
PMCID: PMC11755013
---

# Abstract

Quality estimation of the predicted interaction interface of protein complex structural models is not only important for complex model evaluation and selection but also useful for protein-protein docking. Despite recent progress fueled by symmetry-aware deep learning architectures and pretrained protein language models (pLMs), existing methods for estimating protein complex quality have yet to fully exploit the collective potentials of these advances for accurate estimation of protein-protein interface. Here we present EquiRank, an improved protein-protein interface quality estimation method by leveraging the strength of a symmetry-aware E(3) equivariant deep graph neural network (EGNN) and integrating pLM embeddings from the pretrained ESM-2 model. Our method estimates the quality of the protein-protein interface through an effective graph-based representation of interacting residue pairs, incorporating a diverse set of features, including ESM-2 embeddings, and then by learning the representation using symmetry-aware EGNNs. Our experimental results demonstrate improved ranking performance on diverse datasets over existing latest protein complex quality estimation methods including the top-performing CASP15 protein complex quality estimation method VoroIF_GNN and the self-assessment module of AlphaFold-Multimer repurposed for protein complex scoring and across different performance evaluation metrics. Additionally, our ablation studies demonstrate the contributions of both pLMs and the equivariant nature of EGNN for improved protein-protein interface quality estimation performance. EquiRank is freely available at https://github.com/mhshuvo1/EquiRank.


