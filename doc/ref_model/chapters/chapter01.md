[<< Back](../../ref_model)
# 1. Introduction
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [1.1 Overview.](#overview)
* [1.2 Problem Statement.](#problemstatement)
* [1.3 Scope.](#scope)
* [1.4 Relations to other industry projects.](#relation)
* [1.5 How this document works.](#docu)
* [1.6 What this document is not covering.](#notcovering)
* [1.7 Bogo-Meter.](#bogometer)
* [1.8 Roadmap.](#roadmap)

<a name="overview"></a>
## 1.1 Overview
The main concept of NFV (Network Function Virtualization) is the ability to use general purpose computer hardware and platforms that run multiple VNFs (Virtualised Network Functions) and hence achieving the desired CapEx and OpEx savings. However, one of big challenges NFV is facing with VNF vendors is that vendors, while building or designing their virtualized services (whether it's VoLTE, EPC, or enterprise services like SD-WAN (Software Defined Wide Area Network)), must bring their own set of infrastructure requirements and custom design parameters. This attitude from vendors triggered the creation of various vendor/function specific silos which are incompatible with each other and have different operating models. In addition, this makes the onboarding and certification processes of VNFs (coming from different vendors) hard to automate and standardise.
 
Therefore, for a true cloud type deployment, a model, which relies on engagement with specific vendors and unique infrastructure, needs to be reversed in a way that there is a lot more consistency on infrastructure. Vendors need to bring their software to run into pre-defined environment with common capabilities. That common infrastructure, whether it is optimized for IT (Information Technology) workloads, NFV workloads, or even for AI (Artificial Intelligence) workloads, needs to be fully abstracted to VNFs so that it can be a standard offer.
 
Additionally, to bring the most value to telco operators as well as vendors, agreeing on a standard set of infrastructure profiles for vendors to use for their VNFs is needed within the industry.

The benefits of this approach are:

- Configuration over customisation
  - By abstracting the infrastructure capabilities, operators are able to have common infrastructure platforms across all VNF vendors.
  - Maintaining a consistent infrastructure allows for higher levels of automation as there is less customisation.
  - Overall, this will reduce the total cost of ownership for operators.

- Onboarding and certification
  - By defining abstracted infrastructure capabilities, and the metrics by which they are measured, the onboarding and certification process for both NFVI and VNFs can be standardised.
  - Supply chain, procurement and assurance teams can also then use these metrics to more accurately assess the most efficient / best value vendor for each scenario.
- Better utilization
  - Mapping VNFs to flavours which are properly mapped to IaaS will bring better utilization, than current VNFs expressing variety of instance types as their needs on IaaS.

<a name="problemstatement"></a>
## 1.2	Problem Statement
Analysis of On-Boarding and On-Going Support of ‘i’ in relation to the VNF Challenges - Identified Long-Poles

<a name="scope"></a>
## 1.3	Scope
The scope of this document is illustrated in **Figure 1** below

<p align="center"><img src="../figures/scope.PNG" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 1:</b> Scope of Wrok</p>

This document specifies:
- NFVI Infrastructure abstraction
  - **NFVI metrics & capabilities**: A set of carrier grade metrics and capabilities of NFVI which VNFs require to perform telco grade network functions.
  - **Infrastructure profiles catalogue**: A catalogue of standard profiles needed in order to completely abstract the infrastructure from VNFs. With a limited and well defined profiles and well understood characteristics, VNF compatibility and performance predictability can be achieved. The current focus is for VMs but the intention is to expand the definition to include Container profiles too.
- Reference software and hardware Infrastructure profiling
  - **Reference NFVI software profiles and configurations**: These reference software profiles and configurations should map efficiently to the infrastructure exposed profiles catalogue. The expectation is for Open Source communities (such as OPNFV) to maintain those reference profiles as the software technology evolves.
  - **Reference NFVI hardware profiles and configurations**: These reference hardware profiles and configurations should be suitable for the defined NFVI software profiles & configurations. The expectation is for Open Source communities (such as OPNFV) to maintain those reference profiles as the hardware technology evolves.
- Compliance and verification
  - **Certification programs**: Define the requirement for certification programs for both VNFs and NFVI.
  - **Test framework**:  Provide test suites to allow compliance, certification, and verification of VNFs and NFVI against the defined set of profiles. Part of the framework is also developing a reference implementation of the defined profiles (with the defined configurations0 to be used as a reference for compliance, certification, and verification of NFVI and VNFs.

<a name="relation"></a>
## 1.4	Relations to other industry projects 
(clarify ETSI discussion re: what part of ETSI NFVi arch)
Software Stack Model (Abstracted)

<a name="docu"></a>
## 1.5	How this document works
How to engage with it 
How the model links to reference

<a name="notcovering"></a>
## 1.6	What this document is not covering 
Separate document w/labels/artifacts
Not part of model but will be applicable to architecture 

<a name="bogometer"></a>
## 1.7	Bogo-Meter
A carefully chosen “Bogo-Meter” rating at the beginning of each chapter indicates the completeness and maturity each chapter’s content, at a glance.

<a name="roadmap"></a>
## 1.8	Roadmap
What’s next in further releases/what’s the backlog and priority roadmap


