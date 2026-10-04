---
layout: paper
title: "Text Generator and Text Discriminator for NIST GenAI T2T Challenge"
image: /images/papers/2025-05-07-sarker-text-generator-discriminator-nist-genai.jpg
authors: Sarker S, Qian L, Dong X
year: 2025
ref: Sarker et al., 2025 6th International Conference on Artificial Intelligence, Robotics and Control (AIRC), pp. 222-228, 2025 | | https://doi.org/10.1109/AIRC64931.2025.11077532.
doi: 10.1109/AIRC64931.2025.11077532
github: 
pdf: 
keywords: Generative AI, Large Language Models, text generation, text discrimination, Reinforcement Learning, GPT-4o, BERT, RoBERTa
PMID: 
PMCID: 
---

# Abstract

Recent advances in large language models pre-trained on a large scale of text corpora have significantly enhanced the capabilities of LLMs in both text generation and discrimination. To further drive the development of text generation and discrimination, the NIST GenAI Text-to-Text Challenge provided a structured evaluation framework for the participants to advance research in generative AI's capabilities. This paper proposes two generator pipelines including a reinforcement learning-based approach using GPT-2 and a GPT-4o pipeline with advanced psycholinguistic adjustments as well as two discriminator methods: one that integrates human-guided self-training with pretrained models (BERT and RoBERTa) and another based on a fine-tuned RoBERTa-base model. We leverage the capabilities of GPT model families to generate summaries based on a specific given topic and a set of articles. The process begins with data preparation and pairing each article with its corresponding topic. The first set of initial summaries was generated using Bidirectional AutoRegressive Transformers (BART) through semantic compression. The summaries were then refined by the Advantage ActorCritic algorithm (A2C) to ensure the summaries adhere to the constraints such as writing style, length, factual accuracy, and ethical compliance. We also generate another set of summaries using the advanced GPT-4o model paired with psycholinguistic adjustments and post-processing. For text discrimination, we propose a novel method based on integrating human-guided self-training with a pre-trained BERT and RoBERTa model. This approach involves three key steps: sample selection, human review, and model fine-tuning and retraining. The evaluation results indicate that our submissions demonstrate competitive performance in text summarization, even when the results are compared to the top three participants in this task. However, in text discrimination, our submissions require improvement to match the performance of the top three teams.
