[<< Back](../../ref_model)
# 2	VNF requirements & Analysis
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 VNFs collateral.](#2.1)
* [2.2 Analysis.](#2.2)
* [2.3 NFVI Profiles.](#2.3)

The NFV Infrastructure (NFVI) is the totality of all hardware and software components which build up the environment in which VNFs/VAs are deployed, managed and executed. It is, therefore, inevitable that different VNFs/VAs would require different capabilities and have different expectations from it.

One of the main targets of the CNTT is to define an agnostic NFVI and removes any dependencies between VNFs/VAs and the deployed Infrastructure (NFVI) and offer NFVI to VNFs/VAs in an abstracted way with defined capabilities and metrics.

This means, operators will be able to host their Telco Workload (VNF) with different traffic types, behaviour and from any vendor on a unified consistent Infrastructure.

Additionally, a well defined NFVI is also needed for other type of workloads than NFV such as IT, Machine learning, Artificial Intelligence, etc. 

In this chapter we try to analyse various VNF types used in telco and examine their requirements. We will also highlight some of the NFVI parameters needed to achieve the desired performance expected by various workloads.

<a name="2.1"></a>
# 2.1 VNFs collateral

There are many ways that VNFs can be classified, for example: 

- **By Traffic Type:** 
    - User Plane (Data Plane)
    - Control Plane (Signalling Plane).  
    - Management Plane.
-	**By Service offered:**
    - Mobile broadband service: vEPC, vDPI, vGI-FW 
    - Fixed broadband Service vBNG, vDPI
    - VoLTE / VoWifi : vIMS , UDC , HSBC , vEPDG. 
    - VASs : vSMS-C ,  vCDN , vCGNAT 
-	**By Technology:** (2G, 3G, 4G, 5G, Fixed...)  

Below is a list of Network Functions that covers almost _**95%**_ of the Telco workload (and the most likely to be virtualized/moved to cloud). They don't follow any specific categorisation.

_**Note:** definition of some of the VNFs below is based on 3GPP definitions._


- EPC Nodes (Evolved Packet Core Nodes) – 3GPP TS 23.002 R15 Network architecture
  - MME: MME is the control plane entity within EPS supporting functions Mobility Management,[ Control Plane ]
  - SGW (With CUPS, Control Plane & User Plane Separation, they will be split to SGW-C & SGW-U)
  - PGW (With CUPS, Control Plane & User Plane Separation, they will be split to PGW-C & PGW-U)
  - Serving GW: The Serving GW is the gateway which terminates the interface towards E-UTRAN. [  Control / Data Plane ] forwarding traffic from/toward RAN, Mobility anchor for 3GPP access [ Control / Data Plane ]
  - The PDN GW is the gateway which terminates the SGi interface towards the PDN. [ User Plane], mobility anchor for non 3GPP ( Wifi) [ User Plane].
  - EPDG : evolved packet data gateway (ePDG) : interconnect non 3GPP access with 3GPP core ( VoWifi ) [ User Plane / Control Plane ]
  - 3GPP AAA: Authentication, Authorization, and Accounting
  - PCRF: Policy and Charging Rules Function (PCRF) to provide subscription and policy management for 3G and 4G mobile networks [Control Plane ]
  - OCS: Online Charging system  [Control Plane]
  - HSS: The Home Subscriber Server, The HSS is the master database for a given user. It is the entity containing the subscription-related information to support the network entities actually handling calls/sessions. [Control Plane ]
  - HLR: The Home Location Register (HLR) [Control Plane ]
  - DRA: Diameter Routing Agent  [Control Plane ]
  - SCEF: Service Capability Exposure Function, to securely expose the services and capabilities provided by the 3GPP network interfaces.
  - Circuit Switched - Media Gateway Function (CS-MGW)
  - MSC Server
  - Serving GPRS Support Node (SGSN); The location register function in the SGSN stores two types of subscriber data needed to handle originating and terminating packet data transfer:
  - Gateway GPRS Support Node (GGSN); The location register function in the GGSN stores subscriber data received from the HLR and the SGSN

  - Deep packet inspection (DPI) for network data processing for reporting and other services on mobile and fixed networks.
  - SBC: Session Border Controller (SBC): Secures voice over IP (VoIP) infrastructures while providing interworking between incompatible signalling messages and media flows (sessions) from end devices or application servers. [ Payload ] 
  - SMS-C : SMS Center [Control Plane ]

- Other Core/Main VNFs - 3GPP TS 23.002 R15 Network architecture
  - cRAN – Centralized Unit (CU) BBU, in 5G will be DU and CU 
  - IMS (IP-Multimedia Subsystem ):
    - CSCF :  Call Session Control Function [ control ] 
    - MTAS mobile telephony application server[ control ] 
    - MRF: Media Resource Function [ user plane ]
    - Enum : [ control ]
    - BGCF : Border gateway control function [ control ] . interconnect
    - MGCF: Media Gateway control function :
  - DNS Domain Name System 
  - AAA: Authentication, authorization, and accounting (AAA) services
  - UDC: User Data Convergence
    - HSS-FE: Home Subscriber Server) is a database that contains user-related and subscriber-related information
    - HLR–FE: Home Location Register
    - AAA-FE
    - MNP-FE: Mobile Number Portability
    - EIR–FE: Equipment Identity Register 
    - UDR: User Data Repository  is a functional entity that acts as a single logical repository that stores converged user data
  - Carrier-Grade Network Address Translation (CG-NAT) for IPv4 optimization of mobile and fixed networks.
  - Transmission Control Protocol (TCP) optimization for improved customer experience in 3G/4G mobile networks
  - Gi Firewall
  - IPSEC GW
  - IPS/IDS
  - DDOS
  - Access : 
    - OLT 
    - BNG: Border Network Gateway  / broadband remote access server
    - RGW: Residential gateway
    - Wifi Controller [Control Plane ]
  - CDN: Content delivery network 

- **For 5G:**
  - Core nodes: Virtualized by nature and strong candidate to be onboarded onto Telco Cloud as "cloud-native application"  
    - AMF: The Access and Mobility Management function (AMF)
    - SMF The Session Management function (SMF)
    - UPF: The User plane function (UPF)
    - NSSF: The Network Slice Selection Function (NSSF)
    - NRF: The Network Repository Function (NRF)
    - NEF: The Network Exposure Function (NEF)
    - UDM: The Unified Data Management (UDM)
    - UDR: The Unified Data Repository (UDR
    - PCF: The Policy Control Function (PCF)
    - AUSF: The Authentication Server Function (AUSF)
    - AF: The Application Function (AF) interacts.

    >_**Note:** for 5G Service-based Architecture (SBA) all Network Functions are stateless (store all sessions/ state on unified data repository UDR)_

<!--
The following is a list of VNFs that are considered for analysis in this chapter:

- **Management and Control Plane**: EPC (MME, P/S-GW, S/G-GSN), IMS, SBC, PCRF, SDM, mVAS, DRA
- **User Plane and network**: RAN, BBU, MRF, BNG, CDN, PE, Switch, Router, RR, CPE
- **Security & testing**: FW, LB, DNS, AES, DPI, NAT/CGN, SecGW, Probe
- **Data Core**:
  - Packet Core: GGSN, SGW, PGW, SGSN, MME, CSGN.
  - Subscriber Management: HSS.
  - Policy & Traffic Management: PCRF, TMF
  - Optimizer: MSP.
- **Voice Core**:
  - IP Multimedia: CSCF, ENUM, TAS, SBC.
  - Database: CSDB
  - Circuit Switched: MSC-S(MSS), MGW.
  - Signalling: DRA, SGW, STP.
  - Messaging
  - Security
- **IP Core**: SEC-GW
- **SDO**:
  - Convergent Charging: CCS
  - Smart Pricing: SPO.
  - NGIN, Gi-LAN
  - SecureNet: Clean Pipe.
  - Network Security: SS7FW, CMS, SIG.
  - Others: Web RTC GW, Service integration GW
- **Fixed Access**:
  - BNG, CPE
- **Radio (Cloud RAN)**.

-->

<a name="2.2"></a>
# 2.2 Analysis

Studying various requirements of VNFs helps understanding what expectation they will have from the underlying NFVI. Following are _some_ of the requirements that various workloads might expected:

- Computing
  - Parallelized processing
  - Memory access intensity
  - Latency sensitivy
  - Specific processing (e.g., cryptography, transcoding)
- Networking
  - Throughput (bit rate and/or packet rate)
  - Latency
  - Filtering/NAT
  - vNIC / VLAN number
  - Specific external network connectivity (e.g.,  MPLS)
- Storage
  - IOPS
  - Volume
  - Ephemeral or Persistent
  - Specific storage (e.g., object)



By trying to sort VNF components into different categories based on the requirements observed, below are the different profiles concluded, which are mainly performance-oriented:

- **Profile One **

  - Workload types
    - Control plane, management plane and non-Telco functions
    - _Examples: PCRF, NMS, BSS_
  - Nos specific requirements

- **Profile Two **

  - Workload types
    - Data plane functions without specific computing need
    - _Examples: BNG, PGW, CDN_
  - Requirements
    - High bit rate
    - High packet rate
    - Low latency

- **Profile Three ** 

  - Workload types
    - Data plane functions with specific computing need
    - _Examples: SEC-GW, Firewall, DPI_
  - Requirements
    - Algorithmic-intensive
    - Fast computation
    - Low latency

- **Profile Four**

  - Workload types

    - Control plane functions with specific storage need
    - _Example: UDR_

  - Requirements

    - High storage IOPS	 
    - High storage capacity

<a name="2.3"></a>
# 2.3 NFVI Profiles

Based on the above analysis, following NFVI profiles are proposed (Also shown in **Figure 2-1** below)

- **Basic**: VNFs with VNF-Cs that perform basic compute operations. 
- **Network intensive**: VNFs with VNF-Cs that perform network intensive operations with high throughput and low latency requirements.
- **Compute Intensive**: VNFs with VNF-Cs that perform compute intensive operations with low latency requirements.
- **Storage Intensive**: VNFs with VNF-Cs that perform storage intensive operations with high IPOS requirements. (_**Note:** Storage Intensive Profile will not be defined in initial CNTT releases_)

>_**Note**: 	This is an initial set of proposed profiles and it is expected that more profiles will be added as more requirements are gathered and as technology enhances and matures._

<p align="center"><img src="../figures/ch02_infra_profiles.PNG" alt="infra_profiles" title="Infrastructure Profiles" width="100%"/></p>
<p align="center"><b>Figure 2-1:</b> Infrastructure profiles proposed based on VNFs categorisation.</p>

On **Chapter 4** later in the document, those infrastructure profiles will be offered to VNFs in form of instance types: **B (Basic)**, **N (Network intensive)**, and **C (Compute intensive)** respectively.


