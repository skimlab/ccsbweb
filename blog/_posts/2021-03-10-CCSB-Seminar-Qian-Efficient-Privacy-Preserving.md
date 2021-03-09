---
layout: ccsbtalk
title: "[CCSB Seminar Series] Efficient Privacy Preserving Edge Computing Framework for Image Classification in IoT"
speaker: Lijun Qian, Ph.D.
speakerurl: http://credit.pvamu.edu/qian_lijun/
photo: /images/talks/speakers/lijun-qian.png
date: 2021-03-10
time: 12:00pm
venue: webinar/Zoom
webinar: https://pvpanther.zoom.us/j/97412787782?pwd=WkRYNEM0eTFBNXFURk95ZEswQXFPUT09
recording: 
categories: [blog, talks]
tags: [ccsb-seminar]
event: CCSB-Seminar
---


## Abstract

In this talk, an overview of the research works in the CREDIT center will be introduced briefly. Then a detailed discussion on edge computing for image classification will be given. In order to extract knowledge from the large data collected by edge devices, traditional cloud based approach that requires raw data upload may not be feasible due to communication bandwidth limitation as well as privacy and security concerns of end users. To address these challenges, a novel privacy preserving edge computing framework is proposed in this study for image classification. Specifically, autoencoder will be trained unsupervised at each edge device individually, then the obtained latent vectors will be transmitted to the edge server for the training of a classifier. This framework would reduce the communications overhead and protect the data of the end users. Comparing to federated learning, the training of the classifier in the proposed framework does not subject to the constraints of the edge devices, and the autoencoder can be trained independently at each edge device without any server involvement. Furthermore,  the privacy of the end users' data is protected by transmitting latent vectors without additional cost of encryption. Experimental results provide insights on the image classification performance vs. various design parameters such as the data compression ratio of the autoencoder and the model complexity.


## Speaker Bio

Dr. Qian is currently Regents Professor and holds the AT&T Endowment with the Department of Electrical and Computer Engineering at Prairie View A&M University, where he is also the Director of the Center of Excellence in Research and Education for Big Military Data Intelligence (CREDIT Center). He received B.E. degree from Tsinghua University, Beijing, China, M.S. degree from the Technion-Israel Institute of Technology, Haifa, Israel, and Ph.D. degree from Rutgers University, NJ, USA. He was a Technical Staff Member of Bell-Labs Research, Murray Hill, NJ, USA, and a Visiting Professor to Aalto University, Espoo, Finland. His research interests are in the area of big data processing, artificial intelligence, wireless communications and mobile networks, network security and intrusion detection, and computational systems biology.


