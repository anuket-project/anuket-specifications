[<< Back](../../ref_model)
# 1. Introduction
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [1.1 Overview.](#overview)
* [1.2 Problem Statement.](#problemstatement)
* [1.3 Terminology.](#1.3)
* [1.4 Principles.](#1.4)
* [1.5 Scope.](#scope)
* [1.6 Relations to other industry projects.](#relation)
* [1.7 How this document works.](#docu)
* [1.8 What this document is not covering.](#notcovering)
* [1.9 Bogo-Meter.](#bogometer)
* [1.10 Roadmap.](#roadmap)

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

<a name="1.3"></a>
## 1.3	Terminology

- **Physical Network Function (PNF)**: [Walter] Implementation of a network function that relies on dedicated hardware and software (for part of its functionality). Walter + Fred to finalise.
- **Tenant**: A logical construct that defines the boundaries (e.g., security boundary, operational boundary, billing boundary, etc.) around a collection of resources. Tenant users can share access to a set of physical, virtual or service resources.
- **Workload**: Workload refers to software running on top of NFVI resources such as VMs or containers.
- **VNF**: ETSI describes a VNF as an implementation of a network function that can be deployed on an NFVI. 
  - Any extra additional details will be covered in their corresponding chapter/section.
- **CNF**: from CNCF. 
- **VNFC**: [ETSI] internal component of a VNF providing a VNF Provider a defined sub-set of that VNF's functionality.
  - Any extra additional details will be covered in their corresponding chapter/section.
- **NFVI**:
  - **Tenant resources**:
    - **Virtual Compute resources**: [Pankaj] ETSI – virtualised container] partition of a compute node that provides an isolated virtualized computation environment.
      - **Compute flavour**: [Pankaj] define the compute, memory, and storage capacity of a virtual compute resource 
    - **Virtual Storage resources**: [Pankaj] [ETSI] virtualised non-volatile storage allocated to a
    - **Virtual Networking resources**: [Pankaj] [ETSI] routes information among the network interfaces of a virtual compute resource and physical network interfaces, providing the necessary connectivity.
    - **Virtual Acceleration resources**:
  - **Software Layer**: [Walter] Responsible for the abstraction of the underlying hardware resources and typically implemented using VM/hypervisor or container-based technology.
    - **Virtualisation layer**: [Walter] Compute/Storage/Network hardware resources on which the NFVi platform software runs.
  - **Hardware Layer**: [Pankaj] The physical resources/devices providing the NFVi services/functions required to support the execution environment for VNFs.
    - **Hardware resources**: [Walter] Compute/Storage/Network hardware resources on which the NFVi platform software runs.
- **Node**: [Pankaj] a virtualised compute resource instance that runs on a physical host.
- **NFVI Software Profile**: [Rabi] This defines the behaviour, capabilities and metrics provided by an NFVI Software Layer. 
- **NFVI SW Configuration**: [Rabi] is a set of settings (Key:Value) that are applied to NFVI SW layers to behalf as their corresponding NFVI SW Profile. 
- **NFVI Hardware Profile**: [Rabi] This defines the behaviour, capabilities and metrics provided by an NFVI Hardware Layer. 
- **NFVI HW configurations**: [Rabi] is a set of settings (Key:Value) that are applied to NFVI HW layers to behalf as their corresponding NFVI HW Profile.
  - **Host Profile**: [Pankaj] is a configuration template used to configure physical hosts (servers)
- **Hardware Platform**:
  - **CPU Socket**:
  - **PCIe Slot**:
  - **NIC**: 
  - **SmartNIC**: 
  - **Hardware Acceleration**:
- **Cluster**:
- **Virtual data centre**:
  - **Provider Virtual Data Center (PVDC)**: [Sammuel] A PVDC combines the compute and memory resources of a single VIM (virtual infrastructure manager) resource pool with the storage resources of one or more datastores connected to that resource pool. A provider virtual data center is defined as a resource cluster residing in a resource site.
  - **Organisation Virtual Data Center (OVDC)**: [Sammuel] A subgrouping of compute, memory, storage and network resources allocated from a PVDC. A virtual data center is a deployment environment where vApps can be instantiated, deployed, and powered on. Virtual data centers cannot span multiple organisations. An organisation virtual data center allocates resources using one of the following allocation models:
    - Pay-As-You-Go.
    - Reservation.
    - Allocation.
- **Organisation**: [Sammuel] The unit of multi-tenancy representing a single logical security boundary. An organisation contains users and organisational virtual data centres. On the NFV platform, this is referred to as an NFVI tenant.
- **Others?**

<a name="1.4"></a>
## 1.4	Principles

This section specifies the principles of infrastructure abstraction and profiling work presented by this document.

1. Infrastructure abstraction is aiming to abstract resources provided to VNFs/CNFs (network applications) by NFVI. Those resources include:
   - Compute resources.
   - Storage resources.
   - Networking resources. (Limited to connectivity services).
   - Acceleration resources.
1.	NFVI exposed resources should not have any dependency on any particular suppliers. All APIs implemented must be standard and open, to allow substitution of components.
1. NFVI resources are consumed by VNFs/CNFs through standard/Open Interfaces and APIs.
   - By convention, resource consumption is through an “Interface”, while resource configuration is through an “API”.
1.	NFVI resources are configured on behalf of VNFs/CNFs through standard/Open Interfaces and APIs.
1.	NFVI resources are discovered/monitored by management entities (such as orchestration) through standard/Open Interfaces and APIs.
1.	VNFs/CNFs should be designed to be modular and utilise minimum resources. 
1. NFVI exposes pre-defined and expandable T-shirt sizes that determine the dimensions/class of those resources in conjunction with the NFVI profile.
   - VNFs/CNFs requiring custom T-Shirt sizes or different T-shirt sizes can still do that and it will be up to each individual service provider to allow it.
   - T-Shirt sizes will evolve with time.
1.	VNFs/CNFs should only consume resources and take advantage of capabilities and features (such as for performance optimisation) as offered by the targeted NFVI profile.
1. (rephrase) VNFs/CNFs running targeting a given profile should be able to run on it without requiring specific features that are supported by the profile such as acceleration, etc.
   - Performance might be impacted.
1. An objective of CNTT is to have a single Reference Model and the smallest number of Reference Architectures as is practical. Two principles are introduced in support of these objectives:

   - **Principle #1 – Minimize Architecture proliferation by stipulating compatible features be contained within a single Architecture:**
   
          - Features which are compatible, meaning they are not mutually exclusive and can coexist in the same NFVI instance, shall be incorporated into the same Reference Architecture. For example, IPv4 and IPv6 should be captured in the same Architecture, because they don’t interfere with each other
 
   - **Principle #2 – Create an additional Architecture only when incompatible elements are unavoidable:** 
   
          - Creating additional Architectures is limited to when incompatible elements are desired by Taskforce members. For example, if one member desires KVM be used as the hypervisor, and another desires ESXi be used as the hypervisor, and no compromise or mitigation* can be negotiated, the Architecture could be forked, subject to review and vote to approve by the CNTT technical Working Group, such that one Architecture would be KVM-based and the other would be ESXi-based. 
 
   *Depending on the relationships and substitutability of the component(s) in question, it may be possible to mitigate component incompatibility by creating annexes to a single Architecture, rather than creating an additional Architecture. With this approach, designers at a Telco would implement the Architecture as described in the reference document and when it came to the particular component in question, they would select from one of the relevant annexes, their preferred option. For example, if one member wanted to use Ceph, and another member wanted to use Swift, assuming the components are equally compatible with the rest of the Architecture, there could be one annex for the Ceph implementation and one annex for the Swift implementation. 


<a name="scope"></a>
## 1.5	Scope
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
## 1.6	Relations to other industry projects 
(clarify ETSI discussion re: what part of ETSI NFVi arch)
Software Stack Model (Abstracted)

Regarding the ETSI NFV architecture specified by ETSI GS NFV002 [link to ref: NFV Architectural framework v1.2.1], the scope of this document is only, but all, the NFVI part, including its external reference points.
A mapping of the functional blocks considered in that document to that NFV architecture is illustrated in **Figure 2** below

<p align="center"><img src="../figures/ch01_etsi_archi_mapping.PNG" alt="mapping" title="Mapping to ETSI NFV architecture" width="100%"/></p>
<p align="center"><b>Figure 2:</b> Mapping to ETSI NFV architecture</p>

Following ETSI model, **Figure 2**, the VIM, Virtualised Infrastructure Manager, which controls and manages the NFVI, is not included into NFVI. Nevertheless, the interactions between NFVI and VIM will be part of this document as infrastructure resources management and orchestration have a strong impact on NFVI. These interactions will be detailed in Chapter 7 "API & Interfaces".

<a name="docu"></a>
## 1.7	How this document works
How to engage with it 
How the model links to reference

<a name="notcovering"></a>
## 1.8	What this document is not covering 
Separate document w/labels/artifacts
Not part of model but will be applicable to architecture 

<a name="bogometer"></a>
## 1.9	Bogo-Meter
A carefully chosen “Bogo-Meter” rating at the beginning of each chapter indicates the completeness and maturity each chapter’s content, at a glance.

<a name="roadmap"></a>
## 1.10	Roadmap
What’s next in further releases/what’s the backlog and priority roadmap


