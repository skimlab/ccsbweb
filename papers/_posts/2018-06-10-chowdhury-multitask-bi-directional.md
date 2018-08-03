---
layout: paper
title: "A multitask bi-directional RNN model for named entity recognition on electronic medical records"
image: /images/papers/2018-06-10-chowdhury-multitask-bi-directional.png
authors: Chowdhury S, Dong X, Qian L, Li X, Guan Y, Yang J, Yu Q.
year: 2018
ref: Chowdhury et al. 2018. International Conference on Intelligent Biology and Medicine (ICIBM 2018); June 10-12, 2018; Los Angeles, CA.
journal: "ICIBM 2018"
doi: 
github:
pdf: /pdfs/papers/2018-06-10-chowdhury-multitask-bi-directional.pdf
keywords: recurrent neural network, multitask learning, word embedding, parts-of-speech tagging, named entity recognition, electronic medical records
PMID: 
PMCID: 
---

# Abstract

**Background**: Electronic Medical Record (EMR) comprises patients’ medical
 Entity Recognition (NER) is a sub-field of information extraction aimed at identifying specific entity terms such as disease, test, symptom, genes etc. NER can be a relief for healthcare providers and medical specialists to extract useful information automatically and avoid unnecessary and unrelated information in EMR. However, limited resources of available EMR pose a great challenge for mining entity terms. Therefore, a multitask bi-directional RNN model is proposed here as a potential solution of data augmentation to enhance NER performance with limited data.

**Methods**: A multitask bi-directional RNN model is proposed for extracting entity terms from Chinese EMR. The proposed model can be divided into a shared layer and a task specific layer. Firstly, vector representation of each word is obtained as a concatenation of word embedding and character embedding. Then Bi-directional RNN is used to extract context information from sentence. After that, all these layers are shared by two different task layers, namely the parts-of-speech tagging task layer and the named entity recognition task layer. These two tasks layers are trained alternatively so that the knowledge learned from named entity recognition task can be enhanced by the knowledge gained from parts-of-speech tagging task.

**Results**: The performance of our proposed model has been evaluated in terms of micro average F-score, macro average F-score and accuracy. It is observed that the proposed model outperforms the baseline model in all cases. For instance, the micro average F-score and the macro average F-score are improved by 2.41% and 4.16%, respectively, and the overall accuracy is improved by 5.66%.

**Conclusions**: In this paper, a novel multitask bi-directional RNN model is proposed for improving the performance of named entity recognition in EMR. Evaluation results using real datasets demonstrate the effectiveness of the proposed model.
