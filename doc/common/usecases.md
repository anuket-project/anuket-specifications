[<< Back](https://cntt-n.github.io/CNTT/)
# CNTT Use Cases

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

Based on CNTT's goal and purpose is to develop a robust cloud infrastructure model and define a limited set of discrete architectures built on that model that can be tested and validated for use across the entire member community.

Extend CNTT's Scope beyond the Regional and National Data Center cloud infrastructures to the Edge. The Edge is a disruptive use case where CNTT can add value especially as there are a number of scattered initiatives under various Standard Development Organisations (SDO) and open source communities."

Edge Stream related activities :

- To harmonize the work under Standard Development bodies or Open source communities
- To build Common Cloud infrastructure based on CNTT principles that can be consumed by any operator
- To build Cloud infrastructure that can scale over hundreds of thousands of nodes and cover the Edge Telco use cases that can help operators to monetize the NFV/SDN journey
- Modify the existing RM and RA-s so that they are aligned with the edge requirements

<a name="5.1.3"></a>
### Approach & Scope

All Edge requirement gaps under Reference Model , Reference Architecture 01 (OpenStack), Reference Architecture 02 (Kubernetes) will be identified and fulfilled.

Edge scope under CNTT will cover :

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

This section introduces some principles that should be followed during the definition and development of Edge scope to be covered in CNTT Reference Model, Reference Architectures, Reference Implementations and Reference Conformance test suites.

A main principle is that CNTT Edge will not re-define a new branch of CNTT and target to avoid re-inventing what other organizations already have . CNTT Edge following the same principles that defined in existing [Reference Model Principles](../ref_model/chapters/chapter01.md#13-principles), the [Reference Architecture Principles](../ref_arch#principles) and the Network Principles.

CNTT believes that Edge computing is unique in terms of infrastructure requirements, implementation and deployment, and that's why there some additional principles specific to the edge need to be defined.

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
### Use cases

- **Introduction**

    Telco Edge is commonly coupled with 5G use cases, seen as one of the ingredients of the Ultra-Reliable Low-latency Communication (URLLC) and Enhanced Mobile Broadband (eMBB) Network Slicing. The requirements for user plane Local Breakout / Termination are common mandating that Value Added Services (VASs) & Any Gi-LAN applications are locally hosted at the Edge.

    The Telco Edge is a perfect fit for centralized vRAN deployment and vDU/vCU hosting that satisfy the latency requirements.

    This section illustrates some selected use cases that are aligned with the technology evolution and aligned with the 5G business services offerings as well.

- **Use Case #1 - Edge CDN with eMBB Core Network Slicing**

  - **Business Objectives**
  
      Monetizing 5G by provisioning eMBB network slice with distributed Content Delivery Network (CDN) as a service, that enables Ultra-HD (UHD) streaming, Video Optimization, caching for large files, and other capabilities that can either bundled by the Network Slice offering or implicitly enabled by the operator.

  - **Targeted Segments**
  
    - B2C (Targeting high Tier Packages & Bundles)
    - Content Owners (Potential revenue sharing model)
    - Mobile Virtual Network Operators (MVNOs - Wholesale)
    - Stadiums and Venus.

  - **Architecture**
  
     <img width="1066" alt="Screenshot 2020-05-17 at 11 31 44 PM" src="https://user-images.githubusercontent.com/25845305/82160584-b35db280-9896-11ea-921c-6a7f8e5bb866.png">

- **Use Case #2 - Edge Private 5G with Core Network Slicing**

  - **Business Objectives**
  
      Private 5G is considered one of the most anticipated Business use cases in the coming few years enabling Mobile Operators to provide a standalone private Mobile Network to enterprises that may include all the ingredients of PLMN such as Radio, Core, Infrastructure & Services covering the business requirements in terms of security, performance, reliability, & availability.

  - **Targeted Segments**
  
      - Governmental Sectors & Public Safety (Mission critical applications)
      - Factories and Industry sector.
      - Enterprises with Business-critical applications. 
      - Enterprises with strict security requirements with respect to assets reachability.
      - Enterprises with strict KPIs requirements that mandate the on-premise deployment.

  - **Architecture**

      <img width="1066" alt="Screenshot 2020-05-17 at 11 34 47 PM" src="https://user-images.githubusercontent.com/25845305/82160627-0172b600-9897-11ea-99ec-7339deb19fce.png">
      
        Note (1) - There are multiple flavours for Private 5G deployments or NPN, Non-Public Network as defined by 3GPP.
        
        Note (2) - The use case addresses the technical realization of NPN as a Network Slice of a PLMN as per Annex D – 3GPP TS 23.501 R16 and not covering the other scenarios of deployment.
        
        Note (3) - The use case assumes a network slice that is constructed from a single UPF deployed on Customer premises while sharing the 5G Control Plane (AMF, SMF, & other CP Network Functions) with the PLMN. 
        
        Note (4) - The use case doesn’t cover the requirements of the private Application Servers (ASs) as they may vary with each customer setup.
        
        Note (5) - Hosting the CU/DU on-Customer Infrastructure depends on the enterprise offering by the Mobile Operator and the selected Private 5G setup.
        
        Note (6) – The Edge Cloud Infrastructure can be governed by the client or handled by the Service Provider (Mobile Operator) as part of Managed-services model.

- **Use Case #3 - Edge Automotive (V2X) with uRLLC Core Network Slicing**

  - **Business Objectives**

      The V2X (Viechle-to-everthing) set of use cases provides a 5G Monetization framework for Mobile Operators developing 5G URLLC business use cases targeting the Automotive Industry, Smart City Regulators, & Public Safety. 
      
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

- **Use Case #4 – Edge vRAN Deployments**

  - **Business Objectives**
      vRAN is one of the trending technologies of RAN deployment that fits for all Radio Access Technologies. vRAN helps to provide coverage for rural & uncovered areas with a compelling CAPEX reduction compared to Traditional and legacy RAN deployments. This coverage can be extended to all area types with 5G greenfield deployment as a typical example. 
  
  - **Targeted Segments**
  
      - Private 5G Customers (vRAN Can be part of the Non-Public Network, NPN)
      - B2B Customers & MVNOs (vRAN Can be part of an E2E Network Slicing)
      - B2C (Mobile Consumers Segment).

  
  - **Architecture**
      
      <img width="1068" alt="Screenshot 2020-05-11 at 5 51 34 PM" src="https://user-images.githubusercontent.com/25845305/81582240-15f31200-93b0-11ea-993e-a89f820a5d97.png">
      
        Note (1) – There are multiple deployment models for Centralized Unit (CU) & Distributed Unit (DU). This use case covers the placement case of having the DU & CU collocated & deployed on Telco Edge.
        https://www.ngmn.org/wp-content/uploads/Publications/2018/180226_NGMN_RANFSX_D1_V20_Final.pdf
        
        Note (2) – The use case covers the 5G vRAN deployment. However, this can be extended to cover 4G vRAN as well.
        
        Note (3) – Following Split Option 7.2, The average market latency for RU-DU (Fronthaul) is 100 microsec – 200 microsec      while the latency for DU-CU (MIdhaul) is tens of milliseconds. 
        https://static1.squarespace.com/static/5ad774cce74940d7115044b0/t/5db36ffa820b8d29022b6d08/1572040705841/ORAN-WG4.IOT.0-v01.00.pdf
        

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


