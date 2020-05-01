[<< Back](https://cntt-n.github.io/CNTT/)
# CNTT Use Cases

## Table of Contents
 * [5.1 Edge](#5.1)
   * [5.1.1 Executive Summary](#5.1.1)
   * [5.1.2 Objective](#5.1.2)
   * [5.1.3 Approach & Scope](#5.1.3)
   * [5.1.4 Principle](#5.1.4)
   * [5.1.5 Use cases](#5.1.5)
   * [5.1.6 Terminologies](#5.1.6)
   * [5.1.7 SDO interlocking](#5.1.7)
   

<a name="5.1"></a>
## 5.1 Edge

<a name="5.1.1"></a>
### 5.1.1 Executive Summary

Edge computing, a disruptive technology, that should be considered for adoption by Digital Service Providers (DSP) as it is tightly linked with a number of use cases that monetize 5G. Thus, operators, cloud service providers, content providers and application developers are increasingly focussed on Edge computing.

Edge is considered as one of the main enablers to 5G use cases adoption. There are a number of 5G challenges that Edge will support solve so as to implement the 5G requirements defined by "IMT-2020 and 5G" "https://www.itu.int/pub/T-TUT-IMT" . Edge is required to support enhanced mobile broadband (eMBB), massive machine-type communications (mMTCs) and ultra-reliable low-latency communications (uRLLCs).

With respect to monetization, Edge will help DSPs with their Return on investment (ROI) on 5G and cloud as a number of new services require the Edge. For example, services such as Cloud Gaming, Assisted Reality/Virtual Reality (AR/VR), 5G private networks, and vRAN.

<a name="5.1.2"></a>
### 5.1.2 Objective

Based on CNTT's goal and purpose is to develop a robust cloud infrastructure model and define a limited set of discrete architectures built on that model that can be tested and validated for use across the entire member community.

Extend CNTT's Scope beyond the Regional and National Data Center cloud infrastructures to the Edge. The Edge is a disruptive use case where CNTT can add value especially as there are a number of scattered initiatives under various Standard Development Organisations (SDO) and open source communities."

Edge Stream related activities :

- To harmonize the work under Standard Development bodies or Open source communities
- To build Common Cloud infrastructure based on CNTT principles that can be consumed by any operator
- To build Cloud infrastructure that can scale over hundreds of thousands of nodes and cover the Edge Telco use cases that can help operators to monetize the NFV/SDN journey
- Modify the existing RM and RA-s so that they are aligned with the edge requirements

<a name="5.1.3"></a>
### 5.1.3 Approach & Scope

All Edge requirement gaps under Reference Model , Reference Architecture 01 (OpenStack), Reference Architecture 02 (Kubernetes) will be identified and fulfilled.

Edge scope under CNTT will cover :

-	Define Edge locations based on use case 
-	Define guidelines around factors that can affect the edge, for example, WAN latency based on telco use cases.
-	Define VNF/CNF profiles (if needed) specific to Edge use cases such as profiles required for acceleration technologies. 
-	Define resource requirements in terms of compute, storage and networking; new concepts, such as hyper converged infrastructure, can     be introduced.
-	Define different Architecture models as no one size fits all".
-

Out of Scope 

-	The API that can be exposed to 3rd party application developer. 
-	The Architecture of VNF/CNF ( CNTT Guideline only).
-	Exact location of Edge deployment will vary by Operator. 
-	latency may be vary based on operator transmission type (Microwave,Fixed),a well Transmission network reachability and architecture (Backhaul,front haul, Mid haul).
-	Onboarding of VNF/CNF on edges cloud infrastructure.

<a name="5.1.4"></a>
### 5.1.4 Principle

This section introduces some principles that should be followed during the definition and development of the Edge scope to be covered in CNTT Reference Model, Reference Architectures, Reference Implementations and Reference Conformance test suites.

A main principle is that we shall not re-define a new branch of CNTT and avoid to re-inventing what other organizations already have . we are following the same principles that defined in existing [Reference Model Principles](../ref_model/chapters/chapter01.md#13-principles), the [Reference Architecture Principles](../ref_arch#principles) and the Network Principles.

CNTT believe that Edge is unique in terms of infrastructure requirement ,  Implementation and deployment . that why There are some additional principle be defined covering a specific to the edge.

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
### 5.1.5 Use cases

- **Introduction**

    Telco Edge is commonly coupled with 5G use cases, seen as one of the ingredients of the ultra-low latency/eMBB Network Slicing. The requirements for user plane Local Breakout / Termination are common mandating that VASs & Any Gi-LAN applications are locally hosted at the Edge.

    The Telco Edge is a perfect fit for centralized vRAN deployment and vDU/vCU hosting preserving the latency requirements.

    This section illustrates some selected use cases that are aligned with the technology evolution and aligned with the 5G business services offerings as well.

- **Use Case #1 - eMBB Network Slice with CDN**

  - **Business Objectives**
  
      Monetizing 5G network slicing by providing eMBB Network slice with distributed CDN as a Service providing UHD Streaming Experience, Video Optimization, Caching for Large files, and other Capabilities that can either bundled by the Network Slice offering or implicitly enabled by the operator.

  - **Targeted Segments**
  
    - B2C (Targeting high Tier Packages & Bundles)
    - Content Owners (Potential revenue sharing model)
    - MVNOs (Wholesale)
    - Stadiums and Venus.

  - **Architecture**
  
     <img width="1079" alt="Screenshot 2020-04-14 at 8 37 57 PM" src="https://user-images.githubusercontent.com/25845305/79390856-c536f780-7f70-11ea-88d5-cfd89cf5121a.png">

- **Use Case #2 - Private 5G with Network Slicing**

  - **Business Objectives**
  
      Private 5G is considered one of the most anticipated Business use cases in the coming few years enabling Mobile Operators to provide a standalone private Mobile Network to enterprises that may include all the ingredients of PLMN such as Radio, Core, Infrastructure & Services covering the business requirements in terms of security, performance, reliability, & availability.

  - **Targeted Segments**
  
      - Governmental Sectors & Public Safety (Mission critical applications)
      - Factories and Industry sector.
      - Enterprises with Business-critical applications. 
      - Enterprises with strict security requirements with respect to assets reachability.
      - Enterprises with strict KPIs requirements that mandate the on-premise deployment.

  - **Architecture**

      <img width="1089" alt="Screenshot 2020-04-16 at 6 22 58 PM" src="https://user-images.githubusercontent.com/25845305/79684936-635ae400-8235-11ea-9c97-4774aba24d17.png">
      
        Note (1) - There are multiple flavours for Private 5G deployments or NPN, Non-Public Network as defined by 3GPP.
        
        Note (2) - The use case addresses the technical realization of NPN as a Network Slice of a PLMN as per Annex D – 3GPP TS 23.501 R16 and not covering the other scenarios of deployment.
        
        Note (3) - The use case assumes a network slice that is constructed from a single UPF deployed on Customer premises while sharing the 5G Control Plane (AMF, SMF, & other CP Network Functions) with the PLMN. 
        
        Note (4) - The use case doesn’t cover the requirements of the private Application Servers (ASs) as they may vary with each customer setup.
        
        Note (5) - Hosting the CU/DU on-Customer Infrastructure depends on the enterprise offering by the Mobile Operator and the selected Private 5G setup.
        
        Note (6) – The Cloud Infrastructure can be governed by the client or handled by the Service Provider (Mobile Operator) as part of Managed-services model.

- **Use Case #3 - Edge Automotive (V2X) with uRLLC Network Slicing**

  - **Business Objectives**

      The V2X set of use cases provides a 5G Monetization framework for Mobile Operators developing 5G URLLC business use cases targeting the Automotive Industry, Smart City Regulators, & Public Safety. 
      
  - **Targeted Segments**

      - Automotive Industry.
      - Governmental Departments (Smart Cities, Transport, Police, Emergency Services, etc). 
      - Private residencies (Compounds, Hotels and Resorts).
      - Enterprise and Industrial Campuses.

  - **Architecture**

    <img width="1006" alt="Screenshot 2020-04-19 at 12 17 43 PM" src="https://user-images.githubusercontent.com/25845305/79685269-c8afd480-8237-11ea-90d5-0e7b0edc684e.png">

        Note (1) – 5G NR-V2X is a work item in 3GPP Release 16 that is not completed yet by the time of writing this document.
        
        Note (2) – C-V2X, Cellular V2X has two modes of communications
           1.	Direct Mode (Commonly described by SL, Sidelink by 3GPP)
              This includes the V2V, V2I, & V2P using a direct Interface (PC5) operating in ITS, Intelligent Transport Bands (e.g. 5.9 GHZ).

           2.	Network Mode (UL/DL)
              This covers the V2N while operating in the common telecom licensed spectrum. This use case is capitalizing on this mode.

        Note (3) - The potential use cases that may consume services from Edge is the Network Model (V2N) and potentially the V2I (According on how the Infrastructure will be mapped to an Edge level)

- **Use Case #4**

  - **Business Objectives**

  - **Targeted Segments**

  - **Architecture**

<a name="5.1.6"></a>
### 5.1.6 Terminologies

<a name="5.1.7"></a>
### 5.1.7 SDO interlocking
