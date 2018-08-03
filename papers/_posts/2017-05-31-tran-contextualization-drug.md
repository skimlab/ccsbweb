---
layout: paper
title: "Contextualization of drug-mediator relations using evidence networks"
image: /images/papers/2017-05-31-tran-contextualization-drug.jpg
authors: Tran HJ, Speyer G, Kiefer J, Kim S.
year: 2017
ref: Tran et al. 2017. BMC Bioinformatics. 2017; 18(Suppl 7):252.
journal: "BMC Bioinformatics"
doi: 10.1186/s12859-017-1642-8
github:
pdf: /pdfs/papers/2017-05-31-tran-contextualization-drug.pdf
keywords: Precision medicine, EDDY, CTRP, Gene regulatory networks, Drug development, Biochemical pathways
PMID: 28617226
PMCID: PMC5471944
---

# Abstract

**BACKGROUND**: 
Genomic analysis of drug response can provide unique insights into therapies that can be used to match the "right drug to the right patient." However, the process of discovering such therapeutic insights using genomic data is not straightforward and represents an area of active investigation. EDDY (Evaluation of Differential DependencY), a statistical test to detect differential statistical dependencies, is one method that leverages genomic data to identify differential genetic dependencies. EDDY has been used in conjunction with the Cancer Therapeutics Response Portal (CTRP), a dataset with drug-response measurements for more than 400 small molecules, and RNAseq data of cell lines in the Cancer Cell Line Encyclopedia (CCLE) to find potential drug-mediator pairs. Mediators were identified as genes that showed significant change in genetic statistical dependencies within annotated pathways between drug sensitive and drug non-sensitive cell lines, and the results are presented as a public web-portal (EDDY-CTRP). However, the interpretability of drug-mediator pairs currently hinders further exploration of these potentially valuable results.

**METHODS**: 
In this study, we address this challenge by constructing evidence networks built with protein and drug interactions from the STITCH and STRING interaction databases. STITCH and STRING are sister databases that catalog known and predicted drug-protein interactions and protein-protein interactions, respectively. Using these two databases, we have developed a method to construct evidence networks to "explain" the relation between a drug and a mediator.  RESULTS: We applied this approach to drug-mediator relations discovered in EDDY-CTRP analysis and identified evidence networks for ~70% of drug-mediator pairs where most mediators were not known direct targets for the drug. Constructed evidence networks enable researchers to contextualize the drug-mediator pair with current research and knowledge. Using evidence networks, we were able to improve the interpretability of the EDDY-CTRP results by linking the drugs and mediators with genes associated with both the drug and the mediator.

**CONCLUSION**:
We anticipate that these evidence networks will help inform EDDY-CTRP results and enhance the generation of important insights to drug sensitivity that will lead to improved precision medicine applications.
