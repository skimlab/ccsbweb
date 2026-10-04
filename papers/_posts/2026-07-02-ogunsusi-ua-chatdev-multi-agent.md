---
layout: paper
title: "UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development"
image: /images/papers/2026-07-02-ogunsusi-ua-chatdev-multi-agent.jpg
authors: Temitayo Olamilekan Ogunsusi, Lijun Qian, Xishuang Dong
year: 2026
ref: Ogunsusi et al., arXiv:2607.02186, 2026
doi: 
github: 
pdf: https://arxiv.org/pdf/2607.02186
keywords: Multi-agent collaboration, Large Language Models, Software Development, Uncertainty Quantification, Hallucination Mitigation
PMID: 
PMCID: 
---

# Abstract

Software development is a complex task that demands cooperation among agents with diverse roles. Large language models (LLMs) have enabled autonomous multi-agent software development frameworks that leverage role-based collaboration to automate requirements analysis, coding, testing, and refinement. However, existing approaches typically assume that intermediate agent outputs are equally reliable, leaving them vulnerable to hallucination propagation, where incorrect decisions generated in early development phases are transferred to downstream agents and negatively impact final software quality. To address this challenge, we propose UA-ChatDev, an uncertainty-aware multi-agent software development framework that integrates uncertainty quantification into agent interactions. It introduces a lightweight uncertainty estimation mechanism based on token-level log probabilities to assess the confidence of agent responses and employs phase-aware threshold calibration to selectively trigger retrieval-based verification when uncertainty exceeds acceptable levels. Extensive experiments on the SRDD benchmark demonstrate that UA-ChatDev consistently outperforms existing single-agent and multi-agent software development frameworks across completeness, executability, consistency, and overall quality metrics. Further ablation studies and communication analyses verify that uncertainty-aware interactions enhance code execution reliability.
