---
layout: post
title: "Thanmayee Yeluri to Present Short Talk at DTMBIO 2026"
author: Seungchan Kim
image: /images/team/thanmayee-yeluri.jpg
categories: [blog]
tags: [conference, news]
published: true
---

Congratulations to **[Thanmayee Yeluri](/team/thanmayee-yeluri/)**, a Ph.D. student in the Department of Electrical and Computer Engineering and Graduate Research Assistant at the [Center for Computational Systems Biology (CCSB)](https://ccsb.pvamu.edu), whose recent research submission has been accepted for a **Short Talk** presentation at the **[20th International Conference on Data and Text Mining in Biomedical Informatics (DTMBIO 2026)](https://dtmbio.net/)**!

Thanmayee will travel to Osaka, Japan, to present her research, co-authored with her advisor **[Dr. Seungchan Kim](/team/seungchan-kim/)**. The conference will be held at the Osaka University Nakanoshima Center from October 6 to October 10, 2026.

<br/>

**Title:** Multimodal Machine Learning with Cell-Specific Regulatory Features for Single-Cell DNA Methylation Prediction

**Authors:** Thanmayee Yeluri and Seungchan Kim

<br/>

**Abstract**

Single-cell DNA methylation measurements are often sparse, making it difficult to characterize methylation patterns across cells and genomic regions. Multi-omic measurements from the same cells provide complementary information that may help predict methylation at unobserved cell–gene pairs. Here, we developed a multimodal machine-learning framework for cell–gene DNA methylation prediction using genomic sequence, RNA expression, chromatin accessibility, transcription factor (TF) features, CpG context, and regulatory annotations.

We compared XGBoost, CatBoost, a multi-layer perceptron (MLP), and a knowledge-guided neural network using a within-cell gene-split evaluation. Using the gene-associated feature representation, $x_{\cdot,g}$, the MLP and Knowledge-Guided models performed similarly, with Pearson correlations of 0.6066 and 0.6072, respectively. We then incorporated cell-specific RNA, accessibility, and TF-related features, $x_{c,\cdot}$, to construct the full multimodal feature representation, $x_{c,g}$. With this representation, the MLP reached a Pearson correlation of 0.6222, whereas the Knowledge-Guided model achieved 0.6523, with $\text{RMSE} = 1.2655$ and $R^2 = 0.4249$. The Knowledge-Guided model also improved cell-level correlation for 79.4% of evaluable cells and reduced prediction bias across the methylation range.

Ablation experiments showed that cell-specific TF expression contributed most strongly to the improvement associated with the cell-specific regulatory information, whereas ablating TF motif, TF-expression–motif interaction, or learned gating components did not reduce performance. These results show that cell-specific molecular information can improve within-cell methylation prediction and identify TF expression as the most informative cell-specific regulatory component in the current framework.
