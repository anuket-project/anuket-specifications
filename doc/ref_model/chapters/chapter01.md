[<< Back](../../ref_model)
# 1. Introduction

## Table of Contents
* [1.1 Overview](#1.1)
* [1.2 Scope](#1.2)
* [1.3 Principles](#1.3)
* [1.4 Definitions/Terminology](#1.4)
* [1.5 Abbreviations](#1.5)
* [1.6 References](#1.6)
* [1.7 Conventions](#1.7)

<a name="1.1"></a>
## 1.1 Overview
The Reference Model (RM) specifies a virtualisation technology agnostic (VM-based and container-based) cloud infrastructure abstraction and acts as a "catalogue" of the exposed infrastructure capabilities, resources, and interfaces required by the workloads. 

The document starts from the abstract and as it progresses it increasingly gets into more details.  It follows the traditional design process where you start from core principles, progress to abstract concepts and models, then finish with operational considerations, such as security and lifecycle management.

- **Chapter 01 - Introduction**: Overall scope of the Reference Model document including the goals and objectives of the project.  
  >	**Audience**: This chapter is written for a general technical audience with interest in this topic.
- **Chapter 02 - Workload requirements & Analysis**: High level requirements and core principles needed to understand how the model was developed.  Addresses the thinking behind the decisions that were made.
  >	**Audience**: This chapter is written for architects and others with an interest in how the decisions were made.
- **Chapter 03 - Modelling**:  The high-level cloud infrastructure model itself.  
  >	**Audience**: This chapter is written for architects and others who wants to gain a quick high-level understanding of the model.
- **Chapter 04 - Infrastructure Capabilities, Metrics, and Catalogue**:  Details about the capabilities needed to support the various types of workloads and how the capabilities are applied to the model. The details regarding T-shirt sizes and other considerations are found in this section.
  >	**Audience**: This chapter is written for architects, developers and others who need to deploy infrastructure or develop applications.
- **Chapter 05 - Featureset and Requirements from Infrastructure**: This chapter goes into more details on what needs to be part of the cloud infrastructure.  It describes the software and hardware capabilities and configurations recommended for the different types of cloud infrastructure profiles.
  > **Audience**: This chapter is written for architects, developers and others who need to deploy infrastructure or develop applications.
- **Chapter 06 - External Interfaces**:  This chapter covers APIs and any actual interfaces needed to communicate with the workloads and any other external components.
  >	**Audience**: This chapter is written for architects, developers and others who need to develop APIs or develop applications that use the APIs.
- **Chapter 07 - Security Guidelines**:  This chapter identifies the security components that need to be taken into consideration when designing and implementing a cloud infrastructure environment.  It does not cover details related to company specific requirements to meet regulatory requirements.
  > **Audience**: This chapter is written for security professional, architects, developers and others who need to understand the role of security in the cloud infrastructure environment.
- **Chapter 08 - Conformance, Verification, and Certification**: This chapter details the requirements for developing test suites for a verification and validation program for developers and vendors to validate that their software and applications meet the requirements for the cloud infrastructure architectures.
  >	**Audience**: This chapter is written for QA testers, developers and others who need to deploy infrastructure or develop applications.
- **Chapter 09 - Life Cycle Management**: This chapter focuses on the operational aspects of the cloud infrastructure.  Discussions include deployment considerations, on-going management, upgrades and other lifecycle concerns and requirements.  It does not cover details related to company specific operational requirements, nor does it go into how the cloud infrastructure will interface with existing BSS/OSS systems.
  > **Audience**: This chapter is written for lifecycle managers, operational support teams and others who need to support the infrastructure or the applications.
- **Chapter 10 - Challenges and Gaps**: Opportunities for future developments as technology changes over time.
  > **Audience**: This chapter is written for a general technical audience with interest in this topic.
- **Appendix A - Guidelines For Application Vendors**: More details related to how the applications will interface with the cloud infrastructure through APIs (including Cloud Infrastructure Manager and CaaS).
  > **Audience**: This chapter is written for architects, developers and others who need to deploy infrastructure or develop applications.

<a name="1.2"></a>
## 1.2 Scope
This **Reference Model** document focuses on identifying the abstractions, and associated concepts, that are needed to represent the cloud infrastructure. **Figure 1-1** below highlights its scope in more details.

<p align="center"><img src="../figures/ch01_scope.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 1-1:</b> Scope of Reference Model</p>

This document specifies:
- **Cloud Infrastructure abstraction**: in context with how it interacts with the other components required to build a complete cloud system that supports workloads deployed in Virtual Machines (VM) or containers. Network function workloads that are deployed on virtual machines and containers are referred to as virtual network functions (VNF) and containerised network functions (CNF), respectively; please note that it is now more common to refer CNFs as cloud native network functions. 
  - **Cloud Infrastructure capabilities & metrics**: A set of cloud infrastructure capabilities and metrics required to perform telco scale network functions and satisfy their performance criterion.
  - **Infrastructure profiles catalogue**: A catalogue of standard infrastructure software and hardware configurations, referred to as profiles; these profiles abstract the infrastructure for the workloads. Only a few profiles, with well-defined characteristics, can meet the operational and performance requirements of all workloads.

- Cloud Infrastructure Software and Hardware profiles:
  - **Cloud Infrastructure software profiles**: These software profiles are components of the corresponding infrastructure profiles within the infrastructure profiles catalogue, and specify the host infrastructure software configurations.
  - **Cloud Infrastructure hardware profiles**: These hardware profiles are components of the corresponding infrastructure profiles within the infrastructure profiles catalogue, and specify the host infrastructure hardware configurations.

- Conformance and verification
  - **Conformance programs**: These define the requirements for verification and validation programs for both the cloud infrastructure and workloads.
  - **Test framework**: Provides test suites to allow conformance of cloud infrastructure and workloads.

<a name="1.3"></a>
## 1.3 Principles
The Reference Model specifications conform with the overall principles defined in the preface chapter [Cloud iNfrastructure Telco Taskforce](../../tech#2.0).

<a name="1.4"></a>
## 1.4 Definitions/Terminology
To help guide the reader, a [CNTT Terminology](../../tech/glossary.md) section in [Cloud iNfrastructure Telco Taskforce] provides an introduction to the main terms used within this document and throughout the project in general. These definitions are, with a few exceptions, based on the [ETSI GR NFV 003 V1.5.1 (2020-01)](https://www.etsi.org/deliver/etsi_gr/NFV/001_099/003/01.05.01_60/gr_NFV003v010501p.pdf) definitions.  In a few cases, they have been modified to avoid deployment technology dependencies only when it seems necessary to avoid confusion.

<a name="1.5"></a>
## 1.5	Abbreviations
| Term           | Description                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| CNTT           | Cloud iNfrastructure Telco Taskforce  |  
| PRD            | Permanent Reference Document |
| RM             | Reference Model |


<a name="1.6"></a>
## 1.6	References 
|Ref	   | Doc Number	            |Title                                                                                                             |
|--------|------------------------|------------------------------------------------------------------------------------------------------------------|
| [1]    | ETSI GR NFV 003 V1.5.1 | "Network Functions Virtualisation (NFV); Terminology for Main Concepts in NFV", January 2020. Available at https://www.etsi.org/deliver/etsi_gr/NFV/001_099/003/01.05.01_60/gr_NFV003v010501p.pdf |
| [2]    |  RFC 2119              | “Key words for use in RFCs to Indicate Requirement Levels”, S. Bradner, March 1997. Available at http://www.ietf.org/rfc/rfc2119.txt |


<a name="1.7"></a>  
## 1.7	Conventions
 “The key words “must”, “must not”, “required”, “shall”, “shall not”, “should”, “should not”, “recommended”, “may”, and “optional” in this document are to be interpreted as described in RFC2119 [2].”

<!--Separate document w/labels/artefacts
Not part of model but will be applicable to architecture -->
