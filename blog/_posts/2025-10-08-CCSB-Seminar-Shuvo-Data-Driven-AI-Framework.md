---
layout: ccsbtalk
title: "[CCSB Seminar Series] Data-Driven AI Frameworks toward Computational Drug Discovery"
speaker: Md Hossain Shuvo
speakerurl: https://mdhossainshuvo.github.io/
photo: /images/talks/speakers/md-hossain-shuvo.jpg
date: 2025-10-08
time: 12:00pm
venue: Zoom
venue-inperson: CCSB Conference Room ELEN 231
venue-ece: ECE Conference Room ELEN 315D or Zoom
past-webinar: https://pvpanther.zoom.us/j/98705850635?pwd=lYb4oSwu6obv6wjdfmPiPFg6DX9v47.1
recording: 
talkslide: 2025-10-09-CCSB-Seminar-Shuvo-Data-Driven-AI-Framework.pdf
categories: [blog, talks]
tags: [ccsb-seminar]
event: CCSB-Seminar
---


## Abstract

Chain-of-Thought (CoT) prompting has been shown to improve Large Language Model (LLM) performance on various tasks. With this approach, LLMs appear to produce human-like reasoning steps before providing answers (a.k.a., CoT reasoning), which often leads to the perception that they engage in deliberate inferential processes. However, some initial findings suggest that CoT reasoning may be more superficial than it appears, motivating us to explore further. In this paper, we study CoT reasoning via a data distribution lens and investigate if CoT reasoning reflects a structured inductive bias learned from in-distribution data, allowing the model to conditionally generate reasoning paths that approximate those seen during training. Thus, its effectiveness is fundamentally bounded by the degree of distribution discrepancy between the training data and the test queries. With this lens, we dissect CoT reasoning via three dimensions: task, length, and format. To investigate each dimension, we design DataAlchemy, an isolated and controlled environment to train LLMs from scratch and systematically probe them under various distribution conditions. Our results reveal that CoT reasoning is a brittle mirage that vanishes when it is pushed beyond training distributions. This work offers a deeper understanding of why and when CoT reasoning fails, emphasizing the ongoing challenge of achieving genuine and generalizable reasoning.


## Speaker Bio

Chengshuai Zhao (he/him) is a second-year Ph.D. student in Computer Science at Arizona State University (ASU). He is also a Graduate Research Associate in the Data Mining and Machine Learning Lab (DMML), advised by Prof. Huan Liu. His research spans data mining, AI for science, representation learning, and large language models, with the goal of building systems that are more generalizable, transparent, and capable of uncovering knowledge at the frontiers of human understanding. He also serves as a program committee member and reviewer for leading conferences, including NeurIPS, SIGKDD, ACL, and AAAI.

