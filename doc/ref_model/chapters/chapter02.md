[<< Back](../../ref_model)
# 2 Workload Requirements & Analysis

## Table of Contents
* [2.1 Workloads Collateral](#2.1)
* [2.2 Analysis](#2.2)
* [2.3 Cloud Infrastructure Profiles](#2.3)

The Cloud Infrastructure is the totality of all hardware and software components which build up the environment in which VNFs/CNFs (workloads) are deployed, managed and executed. It is, therefore, inevitable that different workloads would require different capabilities and have different expectations from it.

One of the main targets of the CNTT is to define an agnostic cloud infrastructure, to remove any dependencies between workloads and the deployed cloud infrastructure, and offer infrastructure resources to workloads in an abstracted way with defined capabilities and metrics.

This means, operators will be able to host their Telco workloads (VNFs/CNFs) with different traffic types, behaviour and from any vendor on a unified consistent cloud infrastructure.

Additionally, a well defined cloud infrastructure is also needed for other type of workloads such as IT, Machine Learning, and Artificial Intelligence.

This chapter analyses various telco workloads and their requirements, and recommends certain cloud infrastructure parameters needed to specify the desired performance expected by these workloads.

<a name="2.1"></a>
## 2.1 Workloads Collateral

There are different ways that workloads can be classified, for example:
- **By function type:**
  - Data Plane (a.k.a., User Plane, Media Plane, Forwarding Plane)
  - Control Plane (a.k.a, Signalling Plane)
  - Management Plane
  >_**Note**: Data plane workloads also include control and management plane functions ; control plane workloads also include management plane functions._
- **By service offered:**
  - Mobile broadband service
  - Fixed broadband Service
  - Voice Service
  - Value-Added-Services
- **By technology:** 2G, 3G, 4G, 5G, IMS, FTTx, Wi-Fi...

The list of, most likely to be virtualised,  Network Functions below, covering almost _**95%**_ of the Telco workloads, is organised by network segment and function type.
- **Radio Access Network (RAN)**
  - Data Plane
    - BBU: BaseBand Unit
    - CU: Centralised Unit
    - DU: Distributed Unit
- **2G/3G/4G mobile core network**
  - Control Plane
    - MME: Mobility Management Entity
    - 3GPP AAA: Authentication, Authorisation, and Accounting
    - PCRF: Policy and Charging Rules Function
    - OCS: Online Charging system
    - OFCS: Offline Charging System
    - HSS: Home Subscriber Server
    - DRA: Diameter Routing Agent
    - HLR: Home Location Register
    - SGW-C: Serving GateWay Control plane
    - PGW-C: Packet data network GateWay Control plane
  - Data Plane
    - SGW: Serving GateWay
    - SGW-U: Serving GateWay User plane
    - PGW: Packet data network GateWay
    - PGW-U: Packet data network GateWay User plane
    - ePDG: Evolved Packet Data GateWay
    - MSC: Mobile Switching Center
    - SGSN: Serving GPRS Support Node
    - GGSN: Gateway GPRS Support Node
    - SMSC : SMS Center
- **5G core network**
  5G core nodes are virtualisable by design and strong candidate to be onboarded onto Telco Cloud as "cloud native application"
  - Data Plane
    - UPF: User Plane Function
  - Control Plane
    - AMF: Access and Mobility management Function
    - SMF: Session Management Function
    - PCF: Policy Control Function
    - AUSF: Authentication Server Function
    - NSSF: Network Slice Selection Function
    - UDM: Unified Data Management
    - UDR: Unified Data Repository
    - NRF:  Network Repository Function
    - NEF:  Network Exposure Function
    > _**Note:** for Service-based Architecture (SBA) all Network Functions are stateless (store all sessions/ state on unified data repository UDR)_
- **IP Multimedia Subsystem (IMS)**
  - Data Plane
    - MGW: Media GateWay
    - SBC: Session Border Controller
    - MRF: Media Resource Function
  - Control Plane
    - CSCF:  Call Session Control Function
    - MTAS: Mobile Telephony Application Server
    - BGCF: Border Gateway Control Function
    - MGCF: Media Gateway Control Function
- **Fixed network**
  - Data Plane
    - MSAN: MultiService Access Node
    - OLT: Optical Line Termination
    - WLC: WLAN Controller
    - BNG: Border Network Gateway
    - BRAS: Broadband Remote Access Server
    - RGW: Residential GateWay
    - CPE: Customer Premises Equipment
  - Control Plane
    - AAA: Authentication, Authorisation, and Accounting
- **Other network functions**
  - Data Plane
    - LSR: Label Switching Router
    - DPI: Deep Packet Inspection
    - CG-NAT: Carrier-Grade Network Address Translation
    - ADC: Application Delivery Controller
    - FW: FireWall
    - Sec-GW: Security GateWay
    - CDN: Content Delivery Network
  - Control plane
    - RR: Route Reflector
    - DNS: Domain Name System
  - Management Plane
    - NMS: Network Management System
    
    
    
    
### 2.2 Use cases

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
    - Stadiums and Venues.

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
            
    

<a name="2.2"></a>
## 2.2 Analysis

Studying various requirements of workloads helps understanding what expectation they will have from the underlying cloud infrastructure. Following are _some_ of the requirement types on which various workloads might have different expectation levels:

- **Computing**
  - Speed (e.g., CPU clock and physical cores number)
  - Predictability (e.g., CPU and RAM sharing level)
  - Specific processing (e.g., cryptography, transcoding)
- **Networking**
  - Throughput (i.e., bit rate and/or packet rate)
  - Latency
  - Connection points / interfaces number (i.e., vNIC and VLAN)
  - Specific traffic control (e.g., firewalling, NAT, cyphering)
  - Specific external network connectivity (e.g., MPLS, VXLAN)
- **Storage**
  - IOPS (i.e., input/output rate and/or byte rate)
  - Volume
  - Ephemeral or Persistent
  - Specific features (e.g., object storage, local storage)





By trying to sort workloads into different categories based on the requirements observed, below are the different profiles concluded, which are mainly driven by expected performance levels:

- **Profile One**
  - Workload types
    - Control plane functions without specific need, and management plane functions
    - _Examples: OFCS, AAA, NMS_
  - No specific requirement
- **Profile Two**
  - Workload types
    - Data plane functions (i.e., functions with specific networking and computing needs)
    - _Examples: BNG, S/PGW, UPF, Sec-GW, DPI, CDN, SBC, MME, AMF, IMS-CSCF, UDR_
  - Requirements
    - Predictable computing
    - High network throughput
    - Low network latency
<!--
- **Profile Three**
  - Workload types
    - Control plane functions with specific computing needs
    - _Examples: MME, AMF, IMS-CSCF_
  - Requirements
    - Predictable computing
    - Low network latency    

- **Profile Four**
  - Workload types
    - Control plane functions with specific storage needs
    - _Example: UDR_
  - Requirements
    - High storage IOPS
    - High storage volume
-->

<a name="2.3"></a>
## 2.3 Cloud Infrastructure Profiles

Based on the above analysis, following cloud infrastructure profiles are proposed (also shown in **Figure 2-1** below)
- **Basic**: for Workloads that can tolerate resource over-subscription and variable latency.
- **Network Intensive**: for Workloads that require predictable computing performance, high network throughput and low network latency.

<p align="center"><img src="../figures/ch02_infra_profiles.PNG" alt="infra_profiles" title="Infrastructure Profiles" width="100%"/></p>
<p align="center"><b>Figure 2-1:</b> Infrastructure profiles proposed based on VNFs categorisation.</p>

In **[Chapter 4](./chapter04.md)** these **B (Basic)** and **N (Network intensive)** <!--, and **C (Compute intensive)** --> infrastructure profiles will be defined in greater detail for use by workloads: .

>***Note**  
>This is an initial set of proposed profiles and it is expected that more profiles will be added as more requirements are gathered and as technology enhances and matures. For instance, the following profiles may be added in future releases:*
>- **Compute Intensive**: for Workloads that require predictable computing performance and low network latency.
>- ***Storage Intensive**: for Workloads that require low storage latency and/or high storage IOPS.*
>- ***Enhanced Compute Intensive**: for compute intensive Workloads that require higher computing performance and/or specific compute resource (e.g., GPU).*
>- ***Enhanced Network Intensive**: for network intensive Workloads that require higher network performance and/or specific network resource (e.g., crypto acceleration).*
