[<< Back](../../ref_model)
# 2	VNF requirements & Analysis
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 VNFs collateral (Sample).](#collateral)
* [2.2 Analysis of requirements.](#analysis)
* [2.3 NFVI Profiles.](#profiles)

The NFV Infrastructure (NFVI) is the totality of all hardware and software components which build up the environment in which VNFs are deployed, managed and executed.

It is inevitable that different VNFs require different capabilities from the underlying infrastructure and therefore metrics that define those capabilities are needed.

<a name="collateral"></a>
## 2.1	VNFs collateral (Sample)
The following is a list of VNFs that have been taken as samples and used to understand requirements and to drive the NFVI metrics definition.
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


<a name="analysis"></a>
## 2.2	Analysis of requirements 
(Key Assumptions and Rationale)
Capturing performance characteristics.

<a name="profiles"></a>
## 2.3	NFVI Profiles
By examining the list of VNFs provided in Section 2.1(VNFs collateral (Sample)) and understand their various requirements of NFVI capabilities and metrics, they can be categorised into the following categories.
- **Basic**: VNFs with VNF-Cs that perform basic compute operations. 
- **Network intensive**: VNFs with VNF-Cs that perform network intensive operations with high throughput and low latency requirements.
- **Compute Intensive**: VNFs with VNF-Cs that perform compute intensive operations with low latency requirements.

**Figure 2-1** shows proposed list of NFVI profiles to match those VNF categories.

>_**Note**: 	This is an initial set of proposed profiles and it is expected that more profiles will be added as more requirements are gathered and as technology enhances and matures._

<p align="center"><img src="../figures/ch02_infra_profiles.PNG" alt="infra_profiles" title="Infrastructure Profiles" width="100%"/></p>
<p align="center"><b>Figure 2-1:</b> Infrastructure profiles proposed based on VNFs categorisation.</p>

In the next chapter, Infrastructure profiles catalogue, those infrastructure profiles will be offered to VNFs in form of different instance types: B (Basic), N (Network intensive), and C (Compute intensive) respectively.




One of the targets of the CNTT is to build an agonist NFVI, which means there is no dependency between VNF/Virtual applications and the deployed infrastructure (NFVI ).

In other words, the NFVI operators need should be to host any Telco Workload (VNF) with all its traffic types, behavior and from any vendor.

Additionally, it needs to be able to host other type of workload such as IT workload, Machine learning, Artificial intelligence, etc. 

In this chapter we try to explore various VNF types in Telco world and how they are different from those of IT world. we also shed light on all NFVI parameters that are required to be tuned to achieve the desired performance claimed by those workloads. 

There are many ways of which VNFs can be classified, for example: 

-	Traffic Type: User plane (payload), Control plane (Signaling), and Management.
-	Service chain 
o	Mobile broadband service: vEPC, vDPI, vGI-FW 
o	Fixed broadband Service vBNG, vDPI
o	VoLTE / VoWifi : vIMS , UDC , HSBC , vEPDG. 
o	VASs : vSMS-C ,  vCDN , vCGNAT 
-	Technology (2G, 3G, 4G, 5G, Fixed...)  


Below is a list of Network Functions that covers almost 95 % of the Telco workload (and that most likely to be virtualized).   

Note: definition of some of the VNFs below is based on 3GPP definitions. 



EPC Nodes (Evolved Packet Core Nodes) – 3GPP TS 23.002 R15 Network architecture [Payload intensive workload]


o	MME: MME is the control plane entity within EPS supporting functions Mobility Management,[ Control plane ]
o	SGW (With CUPS, Control Plane & User Plane Separation, they will be split to SGW-C & SGW-U)
o	PGW (With CUPS, Control Plane & User Plane Separation, they will be split to PGW-C & PGW-U)
o	Serving GW: The Serving GW is the gateway which terminates the interface towards E-UTRAN. [  Control / Data Plane ] 
o	The PDN GW is the gateway which terminates the SGi interface towards the PDN. [ User Plane], mobility anchor for non 3GPP ( Wifi) 
o	EPDG : evolved packet data gateway (ePDG) : interconnect non 3GPP access with 3GPP core ( VoWifi ) [ User Plane / Control Plane ]
o	3GPP AAA
o	PCRF: Policy and Charging Rules Function (PCRF) to provide subscription and policy management for 3G and 4G mobile networks [Control Plane ]
o	OCS: Online Charging system  [Control Plane
o	DRA: Diameter Routing Agent  [Control Plane ]
o	SCEF: Service Capability Exposure Function, Exposing Data via API to its application[Control Plane]
o	Deep packet inspection (DPI) for network data processing for reporting and other services on mobile and fixed networks. [ User Plane ]
o	SBC: Session Border Controller (SBC): Secures voice over IP (VoIP) infrastructures while providing interworking between incompatible signalling messages and media flows (sessions) from end devices or application servers. [[ User Plane ]] 
o	SMS-C : SMS Center [Control Plane ]
o	cRAN – Centralized Unit (CU) BBU, in 5G will be DU and CU 
o	IMS
•	CSCF :  Call Session Control Function [ control ] 
•	MTAS mobile telephony application server[ control ] 
•	MRF: Media Resource Function [ user plane ]
•	BGCF : Border gateway control function [control ] . 
•	MGCF: Media Gateway control function [ user plane ]


o	DNS Domain Name System 
o	AAA: Authentication, authorization, and accounting (AAA) services
o	UDC: User Data Convergence [ Control and Storage intensive ]
•	HSS-FE 
•	HLR –FE
•	AAA-FE
•	MNP-FE
•	EIR – FE
•	UDR
o	Carrier-Grade Network Address Translation (CG-NAT) for IPv4 optimization of mobile and fixed networks. [ control Plane ]
o	Transmission Control Protocol (TCP) optimization for improved customer experience in 3G/4G mobile networks [ user plane ]
o	Gi Firewall [ user plane ]
o	IPSEC GW [ user plane ]
o	IPS/IDS [ user plane ]
o	DDOS[ user plane ]
o	Access : 
•	OLT 
•	BNG: Border Network Gateway  / broadband remote access server[ user plane ]
•	RGW: Residential gateway
•	Wifi Controller [Control Plane ]

CDN: Content delivery network [User Plane ]
 





For 5G Core nodes "virtualized by nature and a strong candidate to be onboard on Telco Cloud" not only virtualized the 5G nodes should be cloud-native application  
•	AMF: The Access and Mobility Management function (AMF)
•	SMF The Session Management function (SMF)
•	UPF: The User plane function (UPF)
•	NSSF: The Network Slice Selection Function (NSSF)
•	NRF: The Network Repository Function (NRF)
•	NEF: The Network Exposure Function (NEF)
•	UDM: The Unified Data Management (UDM)
•	UDR: The Unified Data Repository (UDR
•	PCF: The Policy Control Function (PCF)
•	AUSF: The Authentication Server Function (AUSF)
•	AF: The Application Function (AF) interacts

Note: for 5G Service-based Architecture (SBA) all the function is stateless (store all sessions/ state on unified data repository UDR)


To achieve performance dervien VNF , each VNF from the above list has it’s own paramters which should be tuned on NFVI.

Below are some of the parameters that VNFs rely on in order to achieve their desired performance.

-	Number of VNFC
-	Networking between VNFC
-	Intel Enhanced Platform awareness (EPA)
o	DPDK 
o	CPU Pinning 
o	SR-IOV* ( Out of Scope )
o	Affinity / Anti-affinity rules
o	Huge Pages 
o	NUMA alignment
-	CPU Hyper-Threading required?
-	Packet per Second
-	User Space DPDK 
-	NUMA affinity 
-	Security
o	Advanced Encryption Standard – New Instructions (Intel® AES – NI).
o	SELinux 
-	Storage requirements  
o	(ephemeral or presentence ) 
o	Number of IOPS required 
o	Size 

In order to accommodate every VNF requirement, this will lead to N number of hardware profiles with M number of software profiles

As mentioned earlier, there is a need  to decrease the number of possible configuration of NFVI and this can be done by adopting the concept of software and hardware profiles. 

CNTT defines the following profiles for this purpose:


Profile One : IT, Management OSS/BSS and Non-Teleco workload with below main specification :
-	Throughput not an issue
-	No acceration required 


Profile Two: Playload/User Plane intensive Workload profile with below main specification :
-	High throughput
-	A large number of Network cards
-	High PPS 
-	EPA enabled 
-	Example ( vEPC , vDPI , vBNG )
Profile Three: Signalling / Control Plane  workload profile with below main specification : 
-	Low throughput
-	Low Latency 
-	A small number of Network cards
-	Low PPS 
-	EPA enabled 
-	Example (vIMS, vSMS-C )

Profile Four: Storage intensive workloads which below the main specification 
-	Hight IOPS 
-	Hight capacity
-	EPA enabled 
-	Example (vUDC ,..)

Profile Five: Management OSS/BSS and Non-Teleco workload  
-	No need for EPA

Future profile :
-	GPU 
-	Smart NIC / FPGA

To achieve this Hardware profile there is different approach , the one CNTT to get the benefit of NFVI orchestrator layer ( Virtual infrastructure Manager [VIM] ) to help us to define the Host aggregate which considered as a logical groups where each group has it own characteristic that will match one of HW profiles 

In the below section we will shed light the differences between the IT and Telco
 	Telco	IT
Storage	**	*****
Compute	Depend	Depend
Network	Shared	Dedicated 
EPA	Mandatory	Nice to have if required 
Low Latency 	*	*****
High Availability 	Mandatory	DR
High throughput 	*****	***
Service Chain 	Almost	NA
Granted QOS	Mandatory	NA
Security 	Mandatory	required
Scaling in/out, Up/Down	required 	NA


By this approach, we will have a unified cloud that can carry all VNF and Virtual application form Telco, IT, other application as AI, ML,..with full decoupling between the underneath infrastructure and Application





