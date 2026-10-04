---
layout: paper
title: "Enhancing Learning Path Recommendation via Multi-task Learning"
image: /images/papers/2025-10-01-nasrin-learning-path-recommendation-multitask.jpg
authors: Nasrin A, Qian L, Obiomon P, Dong X
year: 2025
ref: Nasrin et al., 2025 Artificial Intelligence x Humanities, Education, and Art (AIxHEART), pp. 85-91, 2025 | | https://doi.org/10.1109/AIxHEART65685.2025.00021.
doi: 10.1109/AIxHEART65685.2025.00021
github: 
pdf: https://arxiv.org/pdf/2507.05295
keywords: personalized learning, learning path recommendation, multi-task learning, LSTM, sequence-to-sequence, Deep Knowledge Tracing
PMID: 
PMCID: 
---

# Abstract

Personalized learning is a student-centered educational approach that adapts content, pace, and assessment to meet each learner's unique needs. As the key technique to implement the personalized learning, learning path recommendation sequentially recommends personalized learning items such as lectures and exercises. Advances in deep learning, particularly deep reinforcement learning, have made modeling such recommendations more practical and effective. This paper proposes a multi-task LSTM model that enhances learning path recommendation by leveraging shared information across tasks. The approach reframes learning path recommendation as a sequence-to-sequence (Seq2Seq) prediction problem, generating personalized learning paths from a learner's historical interactions. The model uses a shared LSTM layer to capture common features for both learning path recommendation and deep knowledge tracing, along with task-specific LSTM layers for each objective. To avoid redundant recommendations, a nonrepeat loss penalizes repeated items within the recommended learning path. Experiments on the ASSIST09 dataset show that the proposed model significantly outperforms baseline methods for the learning path recommendation.
