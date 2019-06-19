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

