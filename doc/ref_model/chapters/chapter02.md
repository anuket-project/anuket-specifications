[<< Back](../../ref_model)
# 2 VNF Requirements & Analysis
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 VNFs Collateral.](#2.1)
* [2.2 Analysis.](#2.2)
* [2.3 NFVI Profiles.](#2.3)

The NFV Infrastructure (NFVI) is the totality of all hardware and software components which build up the environment in which VNFs/VAs are deployed, managed and executed. It is, therefore, inevitable that different VNFs/VAs would require different capabilities and have different expectations from it.

One of the main targets of the CNTT is to define an agnostic NFVI and removes any dependencies between VNFs/VAs and the deployed Infrastructure (NFVI) and offer NFVI to VNFs/VAs in an abstracted way with defined capabilities and metrics.

This means, operators will be able to host their Telco Workload (VNF) with different traffic types, behaviour and from any vendor on a unified consistent Infrastructure.

Additionally, a well defined NFVI is also needed for other type of workloads than NFV such as IT, Machine learning, Artificial Intelligence, etc.

In this chapter we try to analyse various VNF types used in telco and examine their requirements. We will also highlight some of the NFVI parameters needed to achieve the desired performance expected by various workloads.

<a name="2.1"></a>
# 2.1 VNFs Collateral

There are different ways that VNFs can be classified, for example:
- **By function type:**
  - Data Plane (a.k.a., User Plane, Media Plane, Forwarding Plane)
  - Control Plane (a.k.a, Signalling Plane)
  - Management Plane
  >_**Note**: Data plane VNFs also include control and management plane functions ; control plane VNFs also include management plane functions._
- **By service offered:**
  - Mobile broadband service
  - Fixed broadband Service
  - Voice Service
  - Value-Added-Services
- **By technology:** 2G, 3G, 4G, 5G, IMS, FTTx, Wi-Fi...

Below is a list of Network Functions that covers almost _**95%**_ of the Telco workload (and the most likely to be virtualized). They are gathered by network segment and function type.
- **Radio Access Network (RAN)**
  - Data Plane
    - BBU: BaseBand Unit
    - CU: Centralized Unit
    - DU: Distributed Unit
- **2G/3G/4G mobile core network**
  - Control Plane
    - MME: Mobility Management Entity
    - 3GPP AAA: Authentication, Authorization, and Accounting
    - PCRF: Policy and Charging Rules Function
    - OCS: Online Charging system
    - OFCS: OFfline Charging System
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
  5G core nodes are virtualizable by design and strong candidate to be onboarded onto Telco Cloud as "cloud-native application"
  - Data Plane
    - UPF: User Plane Function
  - Control Plane
    - AMF: Access and Mobility management Function
    - SMF: Session Management Function
    - PCF: Policy Control Function
    - AUSF: AUthentication Server Function
    - NSSF: Network Slice Selection Function
    - UDM: Unified Data Management
    - UDR: Unified Data Repositery
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
    - AAA: Authentication, Authorization, and Accounting
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

<a name="2.2"></a>
# 2.2 Analysis

Studying various requirements of VNFs helps understanding what expectation they will have from the underlying NFVI. Following are _some_ of the requirement types on which various workloads might have different expectation levels:

- **Computing**
  - Speed (e.g., CPU clock and physical cores number)
  - Predictability (e.g., CPU and RAM sharing level)
  - Specific processing (e.g., cryptography, transcoding)
- **Networking**
  - Throughput (i.e., bit rate and/or packet rate)
  - Latency
  - interfaces number (i.e., vNIC and VLAN)
  - Specific traffic control (e.g., firewalling, NAT, cyphering)
  - Specific external network connectivity (e.g., MPLS, VXLAN)
- **Storage**
  - IOPS (i.e., input/output rate and/or byte rate)
  - Volume
  - Ephemeral or Persistent
  - Specific features (e.g., object storage, local storage)

By trying to sort VNFs into different categories based on the requirements observed, below are the different profiles concluded, which are mainly driven by expected performance levels:

- **Profile One**
  - VNF types
    - Control plane functions without specific need, and management plane functions
    - _Examples: OFCS, AAA, NMS_
  - No specific requirement
- **Profile Two**
  - VNF types
    - Data plane functions (i.e., functions with specific networking and computing needs)
    - _Examples: BNG, S/PGW, UPF, Sec-GW, DPI, CDN, SBC_
  - Requirements
    - Predictable computing
    - High network throughput
    - Low network latency
- **Profile Three**
  - VNF types
    - Control plane functions with specific computing needs
    - _Examples: MME, AMF, IMS-CSCF_
  - Requirements
    - Predictable computing
    - Low network latency    
<!--
- **Profile Four**
  - VNF types
    - Control plane functions with specific storage needs
    - _Example: UDR_
  - Requirements
    - High storage IOPS
    - High storage volume
-->

<a name="2.3"></a>
# 2.3 NFVI Profiles

Based on the above analysis, following NFVI profiles are proposed (Also shown in **Figure 2-1** below) 
- **Basic**: for VNFCs that can tolerate resource over-subscription and variable latency.
- **Network Intensive**: for VNFCs that require predictable computing performance, high network throughput and low network latency.
- **Compute Intensive**: for VNFCs that require predictable computing performance and low network latency.

<p align="center"><img src="../figures/ch02_infra_profiles.PNG" alt="infra_profiles" title="Infrastructure Profiles" width="100%"/></p>
<p align="center"><b>Figure 2-1:</b> Infrastructure profiles proposed based on VNFs categorisation.</p>

On **Chapter 4** later in the document, these infrastructure profiles will be offered to VNFs in form of instance types: **B (Basic)**, **N (Network intensive)**, and **C (Compute intensive)** respectively.

>***Note**  
>This is an initial set of proposed profiles and it is expected that more profiles will be added as more requirements are gathered and as technology enhances and matures. For instance, the following profiles may be added in future releases:* 
>- ***Storage Intensive**: for VNFCs that require low storage latency and/or high storage IOPS.* 
>- ***Enhanced Compute Intensive**: for compute intensive VNFCs that require higher computing performance and/or specific compute resource (e.g., GPU).* 
>- ***Enhanced Network Intensive**: for network intensive VNFCs that require higher network performance and/or specific network resource (e.g., crypto acceleration).*
