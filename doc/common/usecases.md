[<< Back](https://cntt-n.github.io/Anuket CNTT/)
# Anuket CNTT Use Cases

## Table of Contents
 * [Edge](#5.1)
   * [Executive Summary](#5.1.1)
   * [Objective](#5.1.2)
   * [Approach & Scope](#5.1.3)
   * [Principles](#5.1.4)
   * [Use cases](#5.1.5)
   * [Terminologies](#5.1.6)
   * [SDO interlocking](#5.1.7)
   

<a name="5.1"></a>
## Edge

<a name="5.1.1"></a>
### Executive Summary

Edge computing, a disruptive technology, that should be considered for adoption by Digital Service Providers (DSP) as it is tightly linked with a number of use cases that monetize 5G. Thus, operators, cloud service providers, content providers and application developers are increasingly focussed on Edge computing.

Edge is considered as one of the main enablers to 5G use cases adoption. There are a number of 5G challenges that Edge will support solve so as to implement the 5G requirements defined by "IMT-2020 and 5G" "https://www.itu.int/pub/T-TUT-IMT" . Edge is required to support enhanced mobile broadband (eMBB), massive machine-type communications (mMTCs) and ultra-reliable low-latency communications (uRLLCs).

With respect to monetization, Edge will help DSPs with their Return on investment (ROI) on 5G and cloud as a number of new services require the Edge. For example, services such as Cloud Gaming, Assisted Reality/Virtual Reality (AR/VR), 5G private networks, and vRAN.

<a name="5.1.2"></a>
### Objective

Based on Anuket CNTT's goal and purpose is to develop a robust cloud infrastructure model and define a limited set of discrete architectures built on that model that can be tested and validated for use across the entire member community.

Extend Anuket CNTT's Scope beyond the Regional and National Data Center cloud infrastructures to the Edge. The Edge is a disruptive use case where Anuket CNTT can add value especially as there are a number of scattered initiatives under various Standard Development Organisations (SDO) and open source communities."

Edge Stream related activities :

- To harmonize the work under Standard Development bodies or Open source communities
- To build Common Cloud infrastructure based on Anuket CNTT principles that can be consumed by any operator
- To build Cloud infrastructure that can scale over hundreds of thousands of nodes and cover the Edge Telco use cases that can help operators to monetize the NFV/SDN journey
- Modify the existing RM and RA-s so that they are aligned with the edge requirements

<a name="5.1.3"></a>
### Approach & Scope

All Edge requirement gaps under Reference Model , Reference Architecture 01 (OpenStack), Reference Architecture 02 (Kubernetes) will be identified and fulfilled.

Edge scope under Anuket CNTT will cover :

-	Define Edge locations based on use case 
-	Define guidelines around factors that can affect the edge, for example, WAN latency based on telco use cases.
-	Define Edge use case specific hardware and software profiles, if needed. 
-	Define resource requirements in terms of compute, storage and networking; new concepts, such as hyper converged infrastructure, can     be introduced.
-	Define different architecture models as no one size fits all".


Out of Scope 

-	APIs exposed to 3rd party applications. 
-	VNF/CNF Architecture.
-	Edge deployment locations as they will vary by operator. 

<a name="5.1.4"></a>
### Principles

This section introduces some principles that should be followed during the definition and development of Edge scope to be covered in Anuket CNTT Reference Model, Reference Architectures, Reference Implementations and Reference Conformance test suites.

A main principle is that Anuket CNTT Edge will not re-define a new branch of Anuket CNTT and target to avoid re-inventing what other organizations already have . Anuket CNTT Edge following the same principles that defined in existing [Reference Model Principles](../ref_model/chapters/chapter01.md#13-principles), the [Reference Architecture Principles](../ref_arch#principles) and the Network Principles.

Anuket CNTT believes that Edge computing is unique in terms of infrastructure requirements, implementation and deployment, and that's why there some additional principles specific to the edge need to be defined.

-	Distribution into many small sites
-  Deployment automation
-  Cloud Infrastructure API accessibility
-  Automated lifecycle management
-  Automated scalability
-  Automated closed loop assurance
-  On-Site staff trust and competence availability
-  Security concerns
-  On-Site access restrictions (distance, accessibility, cost)
-  Remote analysis, isolation and serviceability
-  Resource restrictions
-  Cloud Infrastructure overhead minimization
-	 Separation of concerns.
-	 Cloud nativeness.
-  Geographical presence and data origin.
-  Data locality, protection and regulatory fulfilments.
-	 Resilience and Availability.
-  WAN connectivity availability, capabilities and quality.
-  Autonomous local infrastructure functionality and operations.
-  Heterogeneous Infrastructure.
-	 Workload diversity. 
-  Support of Telco and non-Telco workloads.
-  Specific priority, control and orchestration concerns.

<a name="5.1.5"></a>


<a name="5.1.6"></a>
### Terminologies

<a name="5.1.7"></a>
### Standard Developing Bodies (SDO) and Open Source Communities Interlock 

-	OpenStack Edge Computing Group 
    - Working will OpenStack ECG on defining various architecture that will be fit in RA01 & RA02
- Linux Foundation - Edge (LF-Edge)
- GMSA - operator Platform Group (OPG) & Telco Edge Cloud (TEC)
- ETSI MEC
- ETSI NFV 
- Telecom Infra Project (TIP)
    - Working will TIP for Requirements gathering to be adopted from Telco Edge cloud infrastructure prospective


