[<< Back](../../ref_model)
# 2 Workload Requirements & Analysis <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [2.1 Workloads Collateral](#21-workloads-collateral)
- [2.2 Use cases](#22-use-cases)
- [2.3 Analysis](#23-analysis)
- [2.4 Node Profiles & Workload Profiles](#24-node-profiles--workload-profiles)
  - [2.4.1 Node profiles (top-level partitions)](#241-node-profiles-top-level-partitions)
  - [2.4.2 Profile Extensions (specialisations)](#242-profile-extensions-specialisations)

The Cloud Infrastructure is the totality of all hardware and software components which build up the environment in which VNFs/CNFs (workloads) are deployed, managed and executed. It is, therefore, inevitable that different workloads would require different capabilities and have different expectations from it.

One of the main targets of the CNTT is to define an agnostic cloud infrastructure, to remove any dependencies between workloads and the deployed cloud infrastructure, and offer infrastructure resources to workloads in an abstracted way with defined capabilities and metrics.

This means, operators will be able to host their Telco workloads (VNFs/CNFs) with different traffic types, behaviour and from any vendor on a unified consistent cloud infrastructure.

Additionally, a well-defined cloud infrastructure is also needed for other type of workloads such as IT, Machine Learning, and Artificial Intelligence.

This chapter analyses various telco workloads and their requirements, and recommends certain cloud infrastructure parameters needed to specify the desired performance expected by these workloads.

<a name="2.1"></a>
## 2.1 Workloads Collateral

There are different ways that workloads can be classified, for example:
- **By function type:**
  - Data Plane (a.k.a., User Plane, Media Plane, Forwarding Plane)
  - Control Plane (a.k.a, Signalling Plane)
  - Management Plane
  >_**Note**: Data plane workloads also include control and management plane functions; control plane workloads also include management plane functions._
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
    - CHF:  Charging Function part of the converged charging system CCS
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



<a name="2.2"></a>    
## 2.2 Use cases

The intend of this section is to describe some important use cases that are pertinent to this Reference Model.  We start with some typical Edge related use cases. The list of use cases will be extendd in the future releases.  

Telco Edge is commonly coupled with 5G use cases, seen as one of the ingredients of the Ultra-Reliable Low-latency Communication (URLLC) and Enhanced Mobile Broadband (eMBB) Network Slicing. The requirements for user plane Local Breakout / Termination are common mandating that Value Added Services (VASs) & Any Gi-LAN applications are locally hosted at the Edge. The Telco Edge is a perfect fit for centralized vRAN deployment and vDU/vCU hosting that satisfy the latency requirements.

- **Use Case #1 - Edge CDN with eMBB Core Network Slicing**

  - **Business Objectives**

      Monetizing 5G by provisioning eMBB network slice with distributed Content Delivery Network (CDN) as a service, that enables Ultra-HD (UHD) streaming, Video Optimization, caching for large files, and other capabilities that can either bundled by the Network Slice offering or implicitly enabled by the operator.

  - **Targeted Segments**

    - B2C (Targeting high Tier Packages & Bundles)
    - Content Owners (Potential revenue sharing model)
    - Mobile Virtual Network Operators (MVNOs - Wholesale)
    - Stadiums and Venues.

  - **Architecture**
     <p align="center"><img src="../figures/Fig2-1-uc1.png" alt="" Title="Edge CDN with eMBB Core Network Slicing" width="65%"/></p>
     <p align="center"><b>Figure 2-1:</b> Edge CDN with eMBB Core Network Slicing.</p>


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
     <p align="center"><img src="../figures/Fig2-2-uc2.png" alt="" Title="Edge Private 5G with Core Network Slicing" width="65%"/></p>
     <p align="center"><b>Figure 2-2:</b> Edge Private 5G with Core Network Slicing.</p>


       - There are multiple flavours for Private 5G deployments or NPN, Non-Public Network as defined by 3GPP.

       - The use case addresses the technical realization of NPN as a Network Slice of a PLMN as per Annex D – 3GPP TS 23.501 R16 and not covering the other scenarios of deployment.

       - The use case assumes a network slice that is constructed from a single UPF deployed on Customer premises while sharing the 5G Control Plane (AMF, SMF, & other CP Network Functions) with the PLMN.

       - The use case doesn’t cover the requirements of the private Application Servers (ASs) as they may vary with each customer setup.

       - Hosting the CU/DU on-Customer Infrastructure depends on the enterprise offering by the Mobile Operator and the selected Private 5G setup.

       - The Edge Cloud Infrastructure can be governed by the client or handled by the Service Provider (Mobile Operator) as part of Managed-services model.

- **Use Case #3 - Edge Automotive (V2X) with uRLLC Core Network Slicing**

  - **Business Objectives**

      The V2X (Vehicle-to-everything) set of use cases provides a 5G monetization framework for Mobile Operators developing 5G URLLC business use cases targeting the Automotive Industry, Smart City Regulators, & Public Safety.

  - **Targeted Segments**

      - Automotive Industry.
      - Governmental Departments (Smart Cities, Transport, Police, Emergency Services, etc.).
      - Private residencies (Compounds, Hotels and Resorts).
      - Enterprise and Industrial Campuses.

  - **Architecture**
     <p align="center"><img src="../figures/Fig2-3-uc3.png" alt="" Title="Edge Automotive (V2X) with uRLLC Core Network Slicing" width="65%"/></p>
     <p align="center"><b>Figure 2-3:</b>  Edge Automotive (V2X) with uRLLC Core Network Slicing.</p>


       - 5G NR-V2X is a work item in 3GPP Release 16 that is not completed yet by the time of writing this document.

       - C-V2X, Cellular V2X has two modes of communications
         - Direct Mode (Commonly described by SL, Sidelink by 3GPP): This includes the V2V, V2I, & V2P using a direct Interface (PC5) operating in ITS, Intelligent Transport Bands (e.g. 5.9 GHZ).
         - Network Mode (UL/DL): This covers the V2N while operating in the common telecom licensed spectrum. This use case is capitalizing on this mode.

       - The potential use cases that may consume services from Edge is the Network Model (V2N) and potentially the V2I (According on how the Infrastructure will be mapped to an Edge level)

- **Use Case #4 – Edge vRAN Deployments**

  - **Business Objectives**
vRAN is one of the trending technologies of RAN deployment that fits for all Radio Access Technologies. vRAN helps to provide coverage for rural & uncovered areas with a compelling CAPEX reduction compared to Traditional and legacy RAN deployments. This coverage can be extended to all area types with 5G greenfield deployment as a typical example.

  - **Targeted Segments**

      - Private 5G Customers (vRAN Can be part of the Non-Public Network, NPN)
      - B2B Customers & MVNOs (vRAN Can be part of an E2E Network Slicing)
      - B2C (Mobile Consumers Segment).


  - **Architecture**
     <p align="center"><img src="../figures/Fig2-4-uc4.png" alt="" Title="Edge vRAN Deployments" width="65%"/></p>
     <p align="center"><b>Figure 2-4:</b>  Edge vRAN Deployments.</p>


       - There are multiple deployment models for Centralized Unit (CU) & Distributed Unit (DU). This use case covers the placement case of having the DU & CU collocated & deployed on Telco Edge, see NGMN Overview on 5GRAN Functional Decomposition ver 1.0 [12]

       -  The use case covers the 5G vRAN deployment. However, this can be extended to cover 4G vRAN as well.

       -  Following Split Option 7.2, the average market latency for RU-DU (Fronthaul) is 100 microsec – 200 microsec while the latency for DU-CU (MIdhaul) is tens of milliseconds, see ORAN-WG4.IOT.0-v01.00 [13].



<a name="2.3"></a>
## 2.3 Analysis

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

<a name="2.4"></a>
## 2.4 Node Profiles & Workload Profiles

**Node Profiles** are used to tag infrastructure (such as hypervisor hosts, or Kubernetes worker nodes) and associate it with a set of capabilities that are exploitable by the workloads.

**Workload Profiles** are requirements expressed as workload metadata, indicating what kind of infrastructure they must run on to achieve functionality and/or the intended level of performance. They are a resource requesting mechanism, identifying a set of sizing metadata and infrastructure characteristics (such as NUMA alignment, CPU pinning) that are required for the workload to run as intended, then mapped to node flavours at instantiation time.
A resource request by a workload can be met by any infrastructure node that has the same or a more specialised profile and set of flavours, and the necessary capacity.

Two profile *layers* are proposed:

- The top level **profiles** represent macro-characteristics that partition infrastructure into separate pools, i.e.: an infrastructure object can belong to one and only one profile, and workloads can only be created using a single profile. Workloads requesting a given profile **must** be instantiated on infrastructure of that same profile.
- For a given profile, **profile extensions** represent small deviations from (or further qualification, such as infrastructure sizing differences (e.g. memory size)) the profile that do not require partitioning the infrastructure into separate pools, but that have specifications with a finer granularity of the profile. Profile Extensions can be *optionally* requested by workloads that want a more granular control over what infrastructure they run on, i.e.: an infrastructure resource can have **more than one profile extension label** attached to it, and workloads can request resources to be instantiated on infrastructure with a certain profile extension. Workloads requesting a given profile extension **must** be instantiated on infrastructure with that same profile extension. It is allowed to instantiate workloads on infrastructure tagged with more profile extensions than requested, as long as the minimum requirements are satisfied.

<a name="2.4.1"></a>
### 2.4.1 Node profiles (top-level partitions)

Based on the above analysis, the following cloud infrastructure profiles are proposed (also shown in **Figure 2-1** below)
- **Basic**: for Workloads that can tolerate resource over-subscription and variable latency.
- **High Performance**: for Workloads that require predictable computing performance, high network throughput and low network latency.

<p align="center"><img src="../figures/ch02_infra_profiles.PNG" alt="infra_profiles" title="Infrastructure Profiles" width="100%"/></p>
<p align="center"><b>Figure 2-1:</b> Infrastructure profiles proposed based on VNFs categorisation.</p>

In **[Chapter 4](./chapter04.md)** these **B (Basic)** and **H (High) Performance** infrastructure profiles will be defined in greater detail for use by workloads.

Profiles partition the infrastructure: an infrastructure object (host/node) **must** have one and only one profile associated to it.

<a name="2.4.2"></a>
### 2.4.2 Profile Extensions (specialisations)

Profile Extensions are meant to be used as labels for infrastructure, identifying the nodes that implement special capabilities that go beyond the profile baseline. Certain profile pxtensions may be relevant only for some profiles.
The following **profile extensions** are proposed:

Profile Extension Name | Mnemonic | Applicable to Basic Profile | Applicable to High Performance Profile | Description | Notes
|-- | -- | -- | -- | -- | --|
| Compute Intensive High-performance CPU | compute-high-perf-cpu | ❌ | ✅ | Nodes that have predictable computing performance and higher clock speeds. | May use vanilla VIM/K8S scheduling instead. |
| Storage Intensive High-performance storage | storage-high-perf | ❌ | ✅ | Nodes that have low storage latency and/or high storage IOPS | | 
| Compute Intensive High memory | compute-high-memory | ❌ | ✅ | Nodes that have high amounts of RAM. | May use vanilla VIM/K8S scheduling instead. |
| Compute Intensive GPU | compute-gpu | ❌ | ✅ | for compute intensive Workloads that requires GPU compute resource on the node | May use Node Feature Discovery. |
| Network Intensive High speed network (25G) | high-speed-network | ❌ | ✅ | denotes the presence of network links (to the DC network) of speed of 25 Gbps or greater on the node. |  |
| Network Intensive Very High speed network (100G) | very-high-speed-network | ❌ | ✅ | denotes the presence of network links (to the DC network) of speed of 100 Gbps or greater on the node. |   |
| Low Latency - Edge Sites | low-latency-edge | ✅ | ✅ | labels a host/node as located in an edge site, for workloads  requiring low latency (specify value) to final users or geographical  distribution. |   |
| Very Low Latency - Edge Sites | very-low-latency-edge | ✅ | ✅ | labels a host/node as located in an edge site, for workloads  requiring low latency (specify value) to final users or geographical  distribution. |   |
| Ultra Low Latency - Edge Sites | ultra-low-latency-edge | ✅ | ✅ | labels a host/node as located in an edge site, for workloads  requiring low latency (specify value) to final users or geographical  distribution. |   |
| Fixed function accelerator | compute-ffa | ❌ | ✅ | labels a host/node that includes a consumable fixed function accelerator (non programmable, eg Crypto, vRAN-specific adapter). |   |
| Firmware-programmable adapter | compute-fpga | ❌ | ✅ | labels a host/node that includes a consumable Firmware-programmable  adapter (programmable, eg Network/storage FPGA with programmable part of  firmware image). |   |
| SmartNIC enabled | network-smartnic | ❌ | ✅ | labels a host/node that includes a Programmable accelerator for  vSwitch/vRouter, Network Function and/or Hardware Infrastructure. |   |
| SmartSwitch enabled | network-smartswitch | ❌ | ✅ | labels a host/node that is connected to a Programmable Switch Fabric or TOR switch |  |

>***Note:** This is an initial set of proposed profiles and profile extensions and it is expected that more profiles and/or profile extensions will be added as more requirements are gathered and as technology enhances and matures. For instance, the following profiles may be added in future releases:*
>- **Compute Intensive**: for Workloads that require predictable computing performance and low network latency.
>- ***Storage Intensive**: for Workloads that require low storage latency and/or high storage IOPS.*
>- ***Enhanced Compute Intensive**: for compute intensive Workloads that require higher computing performance and/or specific compute resource (e.g., GPU).*
>- ***Enhanced Network Intensive**: for network intensive Workloads that require higher network performance and/or specific network resource (e.g., crypto acceleration).*
