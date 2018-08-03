---
layout: paper
title: "Closed loop control of blood glucose level with neural network predictor for diabetic patients"
image: /images/papers/2017-10-12-bamgbose-close-loop.png
authors: Bamgbose S, Li X, Qian L.
year: 2017
ref: Bamgbose et al. 2017. IEEE HealthCom; Oct. 12-15, 2017; Dalian, China.
journal: "IEEE HealthCom 2017"
doi: 10.1109/HealthCom.2017.8210817
github:
pdf: /pdfs/papers/2017-10-12-bamgbose-close-loop.pdf
keywords: Diabetes, Blood Glucose Prediction, Insulin Pump, Neural Network, Glycemic Control
PMID: 
PMCID: 
---

# Abstract

Despite the recent advancements in glycemic control for diabetic patients, the realization of an automated closed-loop artificial pancreas is still a challenge. The purpose of this research is to develop an integrated control system for in silico closed loop administration of insulin for Type 1 diabetic patients based on patients' medical record and real-time control-relevant data. The proposed system consists of a virtual patient model from the online AIDA diabetes simulator, a neural network predictor trained on patients' data for feedback purposes, and a Proportional-Integral Controller and data logging nodes. The virtual patient takes into account the delayed and time-varying insulin and carbohydrate absorption rate associated with the existing subcutaneous insulin delivery and complex glucose metabolism, respectively. The neural network predictor was trained using 23 features including semi-static and dynamic data, with built-in knowledge of all available past blood glucose levels. Then the controller calculates the infusion bolus to be delivered by the insulin pump. Extensive simulations are performed and it is shown that the neural network predictor has less Root-Mean-Square error than the currently used continuous glucose monitors, which takes measurement from the interstitial fluid. Simulation results also demonstrate that our proposed data-driven closed loop system for glycemic control can effectively regulate the blood glucose level of Type 1 diabetic patients without hypoglycemic excursions, and with no preset instruction on meal ingestion.