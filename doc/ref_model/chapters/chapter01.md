[<< Back](../../ref_model)
# 1. Introduction
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [1.1 Overview](#1.1)
* [1.2 Terminology](#1.2)
* [1.3 Principles](#1.3)
* [1.4 Scope](#1.4)
* [1.5 Audience](#1.5)
* [1.6 Relationship to other industry projects](#1.6)
* [1.7 Out of Scope Components](#1.7)

<a name="1.1"></a>
## 1.1 Overview
The Reference Model (RM) specification is written on the basis of complete infrastructure abstraction and exposing set of capabilities, resources, and interfaces to workloads which they will be written against. The aim of Reference Model is to be agnostic across VM-based and container-based workloads and this document should act as a "catalogue" for VNF/CNF application designers to understand everything they need to know from the underlying infrastructure they are writing their application to run on.

<a name="1.2"></a>
## 1.2 Terminology
To help guide the reader, a glossary [Reference Model Terminology](../../tech/glossary.md) provides an introduction to the main terms used within this document and throughout the project in general. These definitions are, with a few exceptions, based on the [ETSI GR NFV 003 V1.5.1 (2020-01)](https://www.etsi.org/deliver/etsi_gr/NFV/001_099/003/01.05.01_60/gr_NFV003v010501p.pdf) definitions.  In a few cases, they have been modified to avoid deployment technology dependencies only when it seems necessary to avoid confusion.

<a name="1.3"></a>
## 1.3 Principles
This section introduces the high-level principles of infrastructure abstraction and profiling that will be used in context of this document.

1. A top-level objective of the CNTT is to build a single, overarching Reference Model with the smallest number of Reference Architectures tied to it as is practical. Two principles are introduced in support of these objectives:
    - **Minimize Architecture proliferation by stipulating compatible features be contained within a single Architecture as much as possible:**
      - Features which are compatible, meaning they are not mutually exclusive and can coexist in the same cloud infrastructure instance, shall be incorporated into the same Reference Architecture. For example, IPv4 and IPv6 should be captured in the same Architecture, because they don't interfere with each other
      - Focus on the commonalities of the features over the perceived differences. Seek an approach that allows small differences to be handled at either the low-level design or implementation stage. For example, assume the use of existing common APIs over new ones.

    - **Create an additional Architecture only when incompatible elements are unavoidable:**
      - Creating additional Architectures is limited to when incompatible elements are desired by Taskforce members. For example, if one member desires KVM be used as the hypervisor, and another desires ESXi be used as the hypervisor, and no compromise or mitigation* can be negotiated, the Architecture could be forked, subject to review and vote to approve by the CNTT technical Working Group, such that one Architecture would be KVM-based and the other would be ESXi-based.

        >*Depending on the relationships and substitutability of the component(s) in question, it may be possible to mitigate component incompatibility by creating annexes to a single Architecture, rather than creating an additional Architecture. With this approach, the infrastructure architecture designers might implement the Architecture as described in the reference document, however when there is a potential for incompatibility for  particular component, they would select their preferred option from one of the relevant annexes. For example, if one member wanted to use Software-Defined storage (SDS) as CEPH , and another member wanted to use Storage attached network(SAN) , assuming the components are equally compatible with the rest of the Architecture, there could be one annex for the Ceph implementation and one annex for the SAN implementation.
1. Cloud infrastructure provides abstract and physical resources corresponding to:
   - Compute resources.
   - Storage resources.
   - Memory resources.
   - Networking resources. (Limited to connectivity services only).
   - Acceleration resources.
1. Cloud infrastructure exposed resources should be supplier independent.
1. All cloud infrastructure Application Programming Interfaces (API) must ensure Interoperability (multi-vendor, components substitution), drive Simplification, and open source implementations that have an open governance model (e.g. come from Open Communities or Standards Development Organizations). Through such APIs will cloud infrastructure resources be discovered/monitored by management entities, configured on behalf of VNFs and consumed by VNFs.
1. VNFs should be modular and be designed to utilise the minimum resources required for the service.
1. Cloud infrastructure shall support pre-defined and parameterized sizes.
   - These pre-defined sizes will evolve over time.
1. Cloud infrastructure provides certain resources, capabilities and features and virtual applications (VA) should only consume these resources, capabilities and features.
1. VNFs that are designed to take advantage of cloud infrastructure accelerations shall still be able to run without these accelerations, however with the understanding that there will be potential performance impacts.
1. Workloads shall not require hardware-dependent software
   - This is in support of VNF abstraction, enabling portability across the Infra and simplification of VNF design
   - This pertains to features that expose hardware directly to workloads, such as PCIe PassThrough (PCI-PT) and capabilities that use these features, for example, SR-IOV
   - Use of critical features in this category are governed by policies in the RM Appendix and referenced in RM Chapter 4
1. Specific internal hardware details shall not be exposed above the Infra+VIM layers
   - This is in support of VNF abstraction, enabling portability across the Infra and simplification of VNF design
   - This pertains to features that operate at detailed levels of hardware granularity, such as EPA


<a name="1.4"></a>
## 1.4 Scope
This document focuses on the documenting the higher level concepts that are needed to identify **Reference Model**. **Figure 1-1** below highlights its scope in more details.

<p align="center"><img src="../figures/ch01_scope.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 1-1:</b> Scope of Reference Model</p>

This document specifies:
- **Cloud Infrastructure abstraction**: in context with how it interacts with the other components required to build a complete system that supports **VNF**s.
  - **Cloud Infrastructure metrics & capabilities**: A set of metrics and capabilities for the cloud infrastructure which VNFs require to perform telco scale network functions.
  - **Infrastructure profiles catalogue**: A catalogue of standard profiles needed in order to completely abstract the infrastructure from VNFs. With a limited and well-defined set of profiles with well understood characteristics, VNF compatibility and performance predictability can be achieved.

- Cloud Infrastructure Software and Hardware profiling
  - **Cloud Infrastructure software profiles and configurations**: These are software profiles and configurations that map directly to the infrastructure profiles within the infrastructure profiles catalogue.
  - **Cloud Infrastructure hardware profiles and configurations**: These are hardware profiles and configurations which are suitable for the defined cloud infrastructure software profiles & configurations.

- Conformance and verification
  - **Conformance programs**: This defines the requirements for certification and validation programs for both VNFs and cloud infrastructure.
  - **Test framework**: Provide test suites to allow conformance, certification, and verification of VNFs and cloud infrastructure against the defined set of profiles.

<a name="1.5"></a>
## 1.5 Audience
The document starts from the abstract and as it progresses it increasingly gets into more details.  It follows the traditional design process where you start from core principles, progress to abstract concepts and models, then finish with operational considerations, such as security and lifecycle management.

- **Chapter 01 - Introduction**: Overall scope of the Reference Model document including the goals and objectives of the project.  
  >	**Audience**: This chapter is written for a general technical audience with interest in this topic.
- **Chapter 02 - VNF requirements & Analysis**: High level requirements and core principles needed to understand how the model was developed.  Addresses the thinking behind the decisions that were made.
  >	**Audience**: This chapter is written for architects and others with an interest in how the decisions were made.
- **Chapter 03 - Modelling**:  The high-level cloud infrastructure model itself.  
  >	**Audience**: This chapter is written for architects and others who wants to gain a quick high-level understanding of the model.
- **Chapter 04 - Infrastructure Capabilities, Metrics, and Catalogue**:  Details about the capabilities needed to support the various types of VNFs and how the capabilities are applied to the model. The details regarding T-shirt sizes and other considerations are found in this section.
  >	**Audience**: This chapter is written for architects, developers and others who need to develop infrastructure or write VNF applications.
- **Chapter 05 - Featureset and Requirements from Infrastructure**: This chapter goes into more details on what needs to be part of the cloud infrastructure.  It describes the software and hardware capabilities and configurations recommended for the different types of cloud infrastructure profiles.
  > **Audience**: This chapter is written for architects, developers and others who need to develop infrastructure or write VNF applications.
- **Chapter 06 - External Interfaces**:  This chapter covers APIs and any actual interfaces needed to communication with the NFVs themselves and any other external components.
  >	**Audience**: This chapter is written for architects, developers and others who need to develop APIs or write VNF applications that use the APIs.
- **Chapter 07 - Security Guidelines**:  This chapter identifies the security components that need to be taken into consideration when designing and implementing a cloud infrastructure environment.  It does not cover details related to company specific requirements to meet regulatory requirements.
  > **Audience**: This chapter is written for security professional, architects, developers and others who need to understand the role of security in the cloud infrastructure environment.
- **Chapter 08 - Conformance, Verification, and Certification**: This chapter details the requirements for developing test suites for a verification and validation program for developers and vendors to validate that their software and applications meet the requirements for the cloud infrastructure architectures.
  >	**Audience**: This chapter is written for QA testers, developers and others who need to develop infrastructure or write VNF applications.
- **Chapter 09 - Life Cycle Management**: This chapter focuses on the operational aspects of the cloud infrastructure.  Discussions include deployment considerations, on-going management, upgrades and other lifecycle concerns and requirements.  It does not cover details related to company specific operational requirements, nor does it go into how the cloud infrastructure will interface with existing BSS/OSS systems.
  > **Audience**: This chapter is written for lifecycle managers, operational support teams and others who need to support the infrastructure or the VNF applications.
- **Chapter 10 - Challenges and Gaps**: Opportunities for future developments as technology changes over time.
  > **Audience**: This chapter is written for a general technical audience with interest in this topic.
- **Appendix A - Guidelines For VNF Vendors**: More details related to how the VNF applications will interface with the NFVI through APIs and the VIM.
  > **Audience**: This chapter is written for architects, developers and others who need to develop infrastructure or write VNF applications.

<a name="1.6"></a>
## 1.6 Relationship to other industry projects
The CNTT work is not done in a vacuum.  The intention from the beginning was to utilize the work from other Open Source and standards bodies within the industry. Some of the projects, but by no means all, that are related in some way to the CNTT efforts include:

 -	ETSI NFV ISG
 -	OpenStack
 -	OPNFV
 -	ONAP
 -	CNCF
 -	MEF
 -	TM Forum
 - OSM (ETSi Open Source MANO project)
 - VMWare (While not an Open Source project, VMWare is a commonly used platform used for VNF deployments in the telecom industry)

The ETSI NFV ISG is very closely related to the CNTT, in that it is a group that is working on supporting technologies for NFV applications. To facilitate more collaboration as the project matures, the CNTT Reference Model's scope has been purposely aligned to the ETSI NFV ISG Infrastructure plus the VIM (Virtualised Infrastructure Manager), inclusive of their external reference points, as specified by [ETSI GS NFV 002](https://www.etsi.org/deliver/etsi_gs/NFV/001_099/002/01.02.01_60/gs_NFV002v010201p.pdf). **Figure 1-2** illustrates which functional blocks of the ETSI NFV Architecture are in scope for CNTT.

<p align="center"><img src="../figures/ch01_etsi_archi_mapping_v2.PNG" alt="mapping" title="Mapping to ETSI NFV architecture" width="100%"/></p>
<p align="center"><b>Figure 1-2:</b> Mapping to ETSI NFV architecture</p>

Following the ETSI model, **Figure 1-2** also depicts the VIM, which controls and manages the cloud infrastructure, and while technically not part of the cloud infrastructure, the VIM is included in the CNTT scope, due to its role as a manager serving as a bridge between the underlying NVFI and the VNF applications. The interactions between cloud infrastructure and VIM will be part of this document as infrastructure resources management and orchestration have a strong impact on the cloud infrastructure.  These interactions and interfaces will be detailed in  **Chapter 7 API & Interfaces**.

The CNTT is also closely aligned with OVP, an open source, community-led compliance and verification program that demonstrates the readiness and availability of commercial NFV products and services, including cloud infrastructure and VNFs, using OPNFV. OVP combines open source-based automated compliance and verification testing for multiple parts of the NFV stack specifications established by ONAP, multiple SDOs such as ETSI and GSMA, and the LF Networking End User Advisory Group (EUAG).

Once the CNTT Reference Models and Architectures are implemented and tested via OPNFV (Reference Implementations), commercial products adhering to these specifications can undergo an enhanced OVP’s VNF and cloud infrastructure compliance testing for establishing baseline conformance and offering interoperability.  More details about the testing and verification requirements are found in **Chapter 08 - Conformance, Verification, and Certification**.

<!--
There will be dedicated OVP hacking tracks to facilitate VNF vendor onboarding and testing. More information on the work and how to get involved can be found at the following links.  
- https://www.lfnetworking.org/ovp.
- Information on the existing 11 OPNFV Verified products to date is available here: https://nfvi-verified.lfnetworking.org/#/
-->

The CNTT will collaborate with the respective API workgroups of SDOs (ETSI, MEF, TM Forum) as much as possible.  However, to collate on the relevant APIs from these SDOs in some cases requires special permission since information might not be available to the public.  For example. MEF LSO APIs & TM Forum OpenAPIs are accessible by members only.

<a name="1.7"></a>
## 1.7 Out of Scope Components
While the nature of the reference model might seem quite broad, the following areas are not at this time part of the scope of this effort.  
- Hardware specifications: beyond the abstracted high-level CPU, memory, network interface and storage elements.  The intention is to write the document so that it is general enough that any vendor hardware can be used in the implementation without making significant changes to the model.
- VNF and application specifications: Other than the API interfaces when they directly need to touch the VNFs themselves, the intention is to assume the VNF application is a blackbox that the cloud infrastructure is providing resources to.  The majority of interactions for lifecycle management of the VNFs will be through the VIM whenever possible.
- Company specific requirements: This document is designed to be general enough that most operators and others in the Open Source communities will be able

<!--Separate document w/labels/artifacts
Not part of model but will be applicable to architecture -->
