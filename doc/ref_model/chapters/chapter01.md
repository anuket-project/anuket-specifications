[<< Back](../../ref_model)
# 1. Introduction
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [1.1 Overview](#1.1)
* [1.2 Terminology](#1.2)
* [1.3 Principles](#1.3)
* [1.4 Scope](#1.4)
* [1.5 Audience](#1.5)

<a name="1.1"></a>
## 1.1 Overview
The Reference Model (RM) specifies complete infrastructure abstraction and the exposure of a set of capabilities, resources, and interfaces to workloads. The aim of the Reference Model is to be virtualisation technology agnostic (VM-based and container-based) and act as a "catalogue" of the exposed infrastructure capabilities, resources, and interfaces needed to develop the workloads.

<a name="1.2"></a>
## 1.2 Terminology
To help guide the reader, a glossary [Reference Model Terminology](../../tech/glossary.md) provides an introduction to the main terms used within this document and throughout the project in general. These definitions are, with a few exceptions, based on the [ETSI GR NFV 003 V1.5.1 (2020-01)](https://www.etsi.org/deliver/etsi_gr/NFV/001_099/003/01.05.01_60/gr_NFV003v010501p.pdf) definitions.  In a few cases, they have been modified to avoid deployment technology dependencies only when it seems necessary to avoid confusion.

<a name="1.3"></a>
## 1.3 Principles
The Reference Model specification conform with the principles defined in [here](../../tech#2.0).

<a name="1.4"></a>
## 1.4 Scope
This document focuses on the documenting the higher level concepts that are needed to identify **Reference Model**. **Figure 1-1** below highlights its scope in more details.

<p align="center"><img src="../figures/ch01_scope.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 1-1:</b> Scope of Reference Model</p>

This document specifies:
- **Cloud Infrastructure abstraction**: in context with how it interacts with the other components required to build a complete system that supports workloads deployed in Virtual Machines (VNF) or containers (CNF).
  - **Cloud Infrastructure metrics & capabilities**: A set of metrics and capabilities for the cloud infrastructure which workloads require to perform telco scale network functions.
  - **Infrastructure profiles catalogue**: A catalogue of standard profiles needed in order to completely abstract the infrastructure from workloads. With a limited and well-defined set of profiles with well understood characteristics, workload compatibility and performance predictability can be achieved.

- Cloud Infrastructure Software and Hardware profiling
  - **Cloud Infrastructure software profiles and configurations**: These are software profiles and configurations that map directly to the infrastructure profiles within the infrastructure profiles catalogue.
  - **Cloud Infrastructure hardware profiles and configurations**: These are hardware profiles and configurations which are suitable for the defined cloud infrastructure software profiles & configurations.

- Conformance and verification
  - **Conformance programs**: This defines the requirements for certification and validation programs for both workloads and cloud infrastructure.
  - **Test framework**: Provide test suites to allow conformance, certification, and verification of workloads and cloud infrastructure against the defined set of profiles.

<a name="1.5"></a>
## 1.5 Audience
The document starts from the abstract and as it progresses it increasingly gets into more details.  It follows the traditional design process where you start from core principles, progress to abstract concepts and models, then finish with operational considerations, such as security and lifecycle management.

- **Chapter 01 - Introduction**: Overall scope of the Reference Model document including the goals and objectives of the project.  
  >	**Audience**: This chapter is written for a general technical audience with interest in this topic.
- **Chapter 02 - Workload requirements & Analysis**: High level requirements and core principles needed to understand how the model was developed.  Addresses the thinking behind the decisions that were made.
  >	**Audience**: This chapter is written for architects and others with an interest in how the decisions were made.
- **Chapter 03 - Modelling**:  The high-level cloud infrastructure model itself.  
  >	**Audience**: This chapter is written for architects and others who wants to gain a quick high-level understanding of the model.
- **Chapter 04 - Infrastructure Capabilities, Metrics, and Catalogue**:  Details about the capabilities needed to support the various types of workloads and how the capabilities are applied to the model. The details regarding T-shirt sizes and other considerations are found in this section.
  >	**Audience**: This chapter is written for architects, developers and others who need to develop infrastructure or write applications.
- **Chapter 05 - Featureset and Requirements from Infrastructure**: This chapter goes into more details on what needs to be part of the cloud infrastructure.  It describes the software and hardware capabilities and configurations recommended for the different types of cloud infrastructure profiles.
  > **Audience**: This chapter is written for architects, developers and others who need to develop infrastructure or write workload applications.
- **Chapter 06 - External Interfaces**:  This chapter covers APIs and any actual interfaces needed to communication with the workloads themselves and any other external components.
  >	**Audience**: This chapter is written for architects, developers and others who need to develop APIs or write workload applications that use the APIs.
- **Chapter 07 - Security Guidelines**:  This chapter identifies the security components that need to be taken into consideration when designing and implementing a cloud infrastructure environment.  It does not cover details related to company specific requirements to meet regulatory requirements.
  > **Audience**: This chapter is written for security professional, architects, developers and others who need to understand the role of security in the cloud infrastructure environment.
- **Chapter 08 - Conformance, Verification, and Certification**: This chapter details the requirements for developing test suites for a verification and validation program for developers and vendors to validate that their software and applications meet the requirements for the cloud infrastructure architectures.
  >	**Audience**: This chapter is written for QA testers, developers and others who need to develop infrastructure or write workload applications.
- **Chapter 09 - Life Cycle Management**: This chapter focuses on the operational aspects of the cloud infrastructure.  Discussions include deployment considerations, on-going management, upgrades and other lifecycle concerns and requirements.  It does not cover details related to company specific operational requirements, nor does it go into how the cloud infrastructure will interface with existing BSS/OSS systems.
  > **Audience**: This chapter is written for lifecycle managers, operational support teams and others who need to support the infrastructure or the workload applications.
- **Chapter 10 - Challenges and Gaps**: Opportunities for future developments as technology changes over time.
  > **Audience**: This chapter is written for a general technical audience with interest in this topic.
- **Appendix A - Guidelines For VNF Vendors**: More details related to how the workload applications will interface with the cloud infrastructure through APIs (including Cloud Infrastructure Manager and CaaS).
  > **Audience**: This chapter is written for architects, developers and others who need to develop infrastructure or write workload applications.

<!--Separate document w/labels/artefacts
Not part of model but will be applicable to architecture -->
