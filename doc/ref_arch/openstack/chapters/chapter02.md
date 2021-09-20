[<< Back](../../openstack)

# 2. Architecture Requirements
<p align="right"><img src="../figures/bogo_dfp.png" alt="Dickering over the final points" title="Bogo: Dickering over the final points" width="35%"/></p>

## Table of Contents
* [2.1 Introduction](#2.1)
* [2.2 Reference Model Requirements](#2.2)
  * [2.2.1 Cloud Infrastructure Software Profile Requirements for Compute](#2.2.1)
  * [2.2.2 Cloud Infrastructure Software Profile Requirements for Netwokring](#2.2.2)
  * [2.2.3 Cloud Infrastructure Software Profile Requirements for Storage](#2.2.3)
  * [2.2.4 Cloud Infrastructure Hardware Profile Requirements](#2.2.4)
  * [2.2.5 Cloud Infrastructure Management Requirements](#2.2.5)
  * [2.2.6 Cloud Infrastructure Security Requirements](#2.2.6)  
* [2.3 Architecture and OpenStack Requirements](#2.3)
  * [2.3.1 General Requirements](#2.3.1)
  * [2.3.2 Infrastructure Requirements](#2.3.2)
  * [2.3.3 VIM Requirements](#2.3.3)
  * [2.3.4 Interfaces & APIs Requirements](#2.3.4)
  * [2.3.5 Tenant Requirements](#2.3.5)
  * [2.3.6 LCM Requirements](#2.3.6)
  * [2.3.7 Assurance Requirements](#2.3.7)
* [2.4 Architecture and OpenStack Recommendations](#2.4)
  * [2.4.1 General Recommendationss](#2.4.1)
  * [2.4.2 Infrastructure Recommendations](#2.4.2)
  * [2.4.3 VIM Recommendations](#2.4.3)
  * [2.4.4 Interfaces & APIs Recommendations](#2.4.4)
  * [2.4.5 Tenant Recommendations](#2.4.5)
  * [2.4.6 LCM Recommendations](#2.4.6)
  * [2.4.7 Assurance Recommendations](#2.4.7)
  * [2.4.8 Security Recommendations](#2.4.8)

<a name="2.1"></a>
## 2.1 Introduction

**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the reference architecture and reflected in any implementation targeting this reference architecture. The same applies to _must not_.

**should**: Requirements that are marked as _should_ are expected to be fulfilled by the reference architecture but it is up to each service provider to accept an implementation targeting this reference architecture that is not reflecting on any of those requirements. The same applies to _should not_.
> RFC2119

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.

This chapter includes both "Requirements" that must be satisifed in an RA-1 conformant implementation and "Recommendations" that are optional for implementation.

<a name="2.2"></a>
## 2.2 Reference Model Requirements

The tables below contain the requirements from the Reference Model to cover the Basic and High-Performance profiles.

To ensure alignment with the infrastructure profile catalogue, the following requirements are referenced through:
- Those relating to Cloud Infrastructure Software Profiles
- Those relating to Cloud Infrastructure Hardware Profiles
- Those relating to Storage Extensions (S extension)
- Those relating to Network Acceleration Extensions (A extension)
- Those relating to Cloud Infrastructure Management

> Note: "(if offered)" used in the Reference Model has been replaced with "Optional" in the tables below so as to align with RFC2119.

<a name="2.2.1"></a>
### 2.2.1 Cloud Infrastructure Software Profile Requirements for Compute (source [RM 5.2](../../../ref_model/chapters/chapter05.md#5.2))

| Reference  | Description | Requirement for Basic Profile | Requirement for High Performance Profile| Specification Reference |
|---|---|---|---|---|
| e.cap.001 | Max number of vCPU that can be assigned to a single VM by the Cloud Infrastructure | At least 16 | At least 16 | |
| e.cap.002 | Max memory that can be assigned to a single VM by the Cloud Infrastructure | at least 32 GB | at least 32 GB | |
| e.cap.003 | Max storage that can be assigned to a single VM by the Cloud Infrastructure | at least 320 GB | at least 320 GB | |
| e.cap.004 | Max number of connection points that can be assigned to a single VM by the Cloud Infrastructure | 6 | 6 | |
| e.cap.005 | Max storage that can be attached / mounted to VM by the Cloud Infrastructure | Up to 16TB<sup>1</sup> | Up to 16TB<sup>1</sup> | |
| e.cap.006/ infra.com.cfg.003 | CPU pinning support | Not required | Must support | |
| e.cap.007/ infra.com.cfg.002 | NUMA support | Not required | Must support | |
| e.cap.018/ infra.com.cfg.005 | Simultaneous Multithreading (SMT) enabled | Not required | Must support | |
| i.cap.018/ infra.com.cfg.004 | Huge Pages configured | Not required | Must support | |

<p align="center"><b>Table 2-1:</b> Reference Model Requirements: Cloud Infrastructure Software Profile Capabilities</p>

> **<sup>1</sup>** Defined in the `.bronze` configuration in [RM section 4.2.6 Storage Extensions](../../../ref_model/chapters/chapter04.md#4.2.6)<br> 

<a name="2.2.1.1"></a>
### 2.2.1.1 Cloud Infrastructure Software Profile Extensions Requirements for Compute

| Reference  | Description | Profile Extensions | Profile Extra-Specs| Specification Reference |
|---|---|---|---|---|
| e.cap.008/ infra.com.acc.cfg.001 | IPSec Acceleration using the virtio-ipsec interface | Compute Intensive GPU | | |
| e.cap.010/ infra.com.acc.cfg.002 | Transcoding Acceleration | Compute Intensive GPU | Video Transcoding | |
| e.cap.011/ infra.com.acc.cfg.003 | Programmable Acceleration | Firmware-programmable adapter | Accelerator | |
| e.cap.012 | Enhanced Cache Management: L=Lean; E=Equal; X=eXpanded | E | E | |
| e.cap.014/ infra.com.acc.cfg.004 | Hardware coprocessor support (GPU/NPU) | Compute Intensive GPU | | |
| e.cap.016/ infra.com.acc.cfg.005 | FPGA/other Acceleration H/W | Firmware-programmable adapter | | |

<p align="center"><b>Table 2-1a:</b> Cloud Infrastructure Software Profile Extensions Requirements for Compute</p>

<a name="2.2.2"></a>
### 2.2.2 Cloud Infrastructure Software Profile Requirements for Netwokring (source [RM 5.2.3](../../../ref_model/chapters/chapter05.md#5.2.3))

The features and configuration requirements related to virtual networking for the two (2) types of Cloud Infrastructure Profiles are specified below followed by networking bandwidth requirements.

| Reference  | Description | Requirement for Basic Profile | Requirement for High-Performance Profile| Specification Reference |
|---|---|---|---|---|
| infra.net.cfg.001 |	IO virtualisation using	virtio1.1 | Must support | Must support | |
| infra.net.cfg.002 |	The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric | Must support VXLAN, MPLSoUDP, GENEVE, other | *No requirement specified* | |
| infra.net.cfg.003 | Network Address Translation | Must support | Must support | |
| infra.net.cfg.004 | Security Groups | Must support | Must support | |
| infra.net.cfg.005 | SFC support | Not required | Must support | |
| infra.net.cfg.006 | Traffic patterns symmetry | Must support | Must support | |

<p align="center"><b>Table 2-2a:</b> Reference Model Requirements - Virtual Networking</p>

The required number of connection points to a VM is described in `e.cap.004` [above](#2.2.1).  The table below specifies the required bandwidth of those connection points.

| Reference  | Description | Requirement for Basic Profile | Requirement for High Performance Profile| Specification Reference |
|---|---|---|---|---|
| n1, n2, n3, n4, n5, n6	| 1, 2, 3, 4, 5, 6 Gbps | Must support | Must support | |
| n10, n20, n30, n40, n50, n60	| 10, 20, 30, 40, 50, 60 Gbps | Must support | Must support | |
| n25, n50, n75, n100, n125, n150	| 25, 50, 75, 100, 125, 150 Gbps | Optional | Must support | |
| n50, n100, n150, n200, n250, n300	| 50, 100, 150, 200, 250, 300 Gbps | Optional | Must support | |
| n100, n200, n300, n400, n500, n600	| 100, 200, 300, 400, 500, 600 Gbps | Optional | Must support | |

<p align="center"><b>Table 2-2b:</b> Reference Model Requirements - Network Interface Specifications</p>

<a name="2.2.2.1"></a>
### 2.2.2.1 Cloud Infrastructure Software Profile Extensions Requirements for Networking

| Reference  | Description | Requirement for Basic Profile | Requirement for High-Performance Profile| Specification Reference |
|---|---|---|---|---|
| e.cap.013/ infra.hw.nac.cfg.004  |	SR-IOV over PCI-PT |	N |	Y | |
| e.cap.019/ infra.net.acc.cfg.001 |	vSwitch optimisation (DPDK) |	N |	Y | |
| e.cap.015/ infra.net.acc.cfg.002 |	SmartNIC (for HW Offload) |	N |	Optional | |
| e.cap.009/ infra.net.acc.cfg.003 |	Crypto acceleration |	N |	Optional | |
| infra.net.acc.cfg.004 |	Crypto Acceleration Interface |	N |	Optional | |

<p align="center"><b>Table 2-2c:</b> Cloud Infrastructure Software Profile Extensions Requirements for Networking</p>

<a name="2.2.3"></a>
### 2.2.3 Cloud Infrastructure Software Profile Requirements for Storage (source [RM 5.2](../../../ref_model/chapters/chapter05.md#5.2))

| Reference  | Description | Requirement for Basic Profile | Requirement for High-Performance Profile| Specification Reference |
|---|---|---|---|---|
| infra.stg.cfg.002 | Storage Block | Must support | Must support | |
| infra.stg.cfg.003 | Storage with replication | Not required | Must support | |
| infra.stg.cfg.004 | Storage with encryption | Must support | Must support | |
| infra.stg.acc.cfg.001 | Storage IOPS oriented | Not required | Must support | |
| infra.stg.acc.cfg.002 | Storage capacity oriented | Not required | Not required | |

<p align="center"><b>Table 2-3a:</b> Reference Model Requirements - Cloud Infrastructure Software Profile Requirements for Storage</p>


<a name="2.2.3.1"></a>
### 2.2.3.1 Cloud Infrastructure Software Profile Extensions Requirements for Storage

| Reference  | Description | Profile Extensions | Profile Extra-Specs | Specification Reference |
|---|---|---|---|---|
| infra.stg.acc.cfg.001 | Storage IOPS oriented | Storage Intensive High-performance storage | | |
| infra.stg.acc.cfg.002 | Storage capacity oriented | High Capacity | | |

<p align="center"><b>Table 2-3b:</b> Reference Model Requirements - Cloud Infrastructure Software Profile Extensions Requirements for Storage</p>

<a name="2.2.4"></a>
### 2.2.4 Cloud Infrastructure Hardware Profile Requirements (source [RM 5.4](../../../ref_model/chapters/chapter05.md#5.4))

| Reference  | Description | Requirement for Basic Profile | Requirement for High-Performance Profile| Specification Reference |
|---|---|---|---|---|
| infra.hw.001 |	CPU Architecture (Values such as x64, ARM, etc.) | | | |
| infra.hw.cpu.cfg.001 | Minimum number of CPU (Sockets) | 2 | 2 | |
| infra.hw.cpu.cfg.002 | Minimum number of Cores per CPU | 20 | 20 | |
| infra.hw.cpu.cfg.003 | NUMA | Not required | Must support | |
| infra.hw.cpu.cfg.004 | Simultaneous Multithreading/Symmetric Multiprocessing (SMT/SMP) | Must support | Must support | |
| infra.hw.stg.hdd.cfg.001 | Local Storage HDD | *No requirement specified* | *No requirement specified* | |
| infra.hw.stg.ssd.cfg.002 | Local Storage SSD | Should support | Should support | |
| infra.hw.nic.cfg.001 | Total Number of NIC Ports available in the host | 4 | 4 | |
| infra.hw.nic.cfg.002 | Port speed specified in Gbps (minimum values) | 10 | 25 | |
| infra.hw.pci.cfg.001 | Number of PCIe slots available in the host | 8 | 8 | |
| infra.hw.pci.cfg.002 | PCIe speed | Gen 3 | Gen 3 | |
| infra.hw.pci.cfg.003 | PCIe Lanes | 8 | 8 | |
| infra.hw.nac.cfg.003 | Compression | *No requirement specified* | *No requirement specified* | |

<p align="center"><b>Table 2-4a:</b> Reference Model Requirements - Cloud Infrastructure Hardware Profile Requirements</p>

<a name="2.2.4.1"></a>
#### 2.2.4.1 Cloud Infrastructure Hardware Profile-Extensions Requirements (source [RM 5.4](../../../ref_model/chapters/chapter05.md#5.4))


| Reference  | Description | Requirement for Basic Profile | Requirement for High-Performance Profile| Specification Reference |
|---|---|---|---|---|
| e.cap.014/  infra.hw.cac.cfg.001 | GPU | N | Optional | |
| e.cap.016/  infra.hw.cac.cfg.002 |FPGA/other Acceleration H/W | N | Optional | |
| e.cap.009/ infra.hw.nac.cfg.001 | Crypto Acceleration |  N | Optional | |
| e.cap.015/ infra.hw.nac.cfg.002 | SmartNIC |  N | Optional | |
| infra.hw.nac.cfg.003 | Compression | Optional | Optional | |
| e.cap.013/ infra.hw.nac.cfg.004 | SR-IOV over PCI-PT | N | Yes | |

<p align="center"><b>Table 2-4b:</b> Reference Model Requirements - Cloud Infrastructure Hardware Profile Extensions Requirements</p>

<a name="2.2.5"></a>
### 2.2.5 Cloud Infrastructure Management Requirements (source [RM 4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities))

| Reference | Description | Requirement (common to all Profiles) | Specification Reference |
|---|---|---|---|
| e.man.001 | Capability to allocate virtual compute resources to a workload | Must support | |
| e.man.002 | Capability to allocate virtual storage resources to a workload | Must support | |
| e.man.003 | Capability to allocate virtual networking resources to a workload | Must support | |
| e.man.004 | Capability to isolate resources between tenants | Must support | |
| e.man.005 | Capability to manage workload software images | Must support | |
| e.man.006 | Capability to provide information related to allocated virtualised resources per tenant | Must support | |
| e.man.007 | Capability to notify state changes of allocated resources | Must support | |
| e.man.008 | Capability to collect and expose performance information on virtualised resources allocated | Must support | |
| e.man.009 | Capability to collect and notify fault information on virtualised resources | Must support | |

<p align="center"><b>Table 2-5:</b> Reference Model Requirements: Cloud Infrastructure Management Requirements</p>

<a name="2.2.6"></a>
### 2.2.6 Cloud Infrastructure Security Requirements

#### 2.2.6.1. System Hardening (source [RM 7.9.1](../../../ref_model/chapters/chapter07.md#791-system-hardening))

| Ref # | sub-category | Description |  Traceability |
|-------|------|------|-------|
| sec.gen.001 | Hardening | The Platform **must** maintain the specified configuration. | [RA-1 6.3.6 "Security LCM"](./chapter06.md#636-security-lcm), [RA-1 7.2 "Cloud Infrastructure and VIM configuration management"](./chapter07.md#72-cloud-infrastructure-and-vim-configuration-management)  |
| sec.gen.002 | Hardening | All systems part of Cloud Infrastructure **must** support password hardening as defined in [CIS Password Policy Guide](https://www.cisecurity.org/white-papers/cis-password-policy-guide/). | [RA-1 6.3.1.3 "Password policy"](./chapter06.md#6313-password-policy) |
| sec.gen.003 | Hardening | All servers part of Cloud Infrastructure **must** support a root of trust and secure boot. | [RA-1 6.3.1.1 "Server boot hardening"](./chapter06.md#6311-server-boot-hardening) |
| sec.gen.004 | Hardening | The Operating Systems of all the servers part of Cloud Infrastructure **must** be hardened by removing or disabling unnecessary services, applications and network protocols, configuring operating system user authentication, configuring resource controls, installing and configuring additional security controls where needed, and testing the security of the Operating System (NIST SP 800-123). | [RA-1 6.3.1.4 "Function and Software"](./chapter06.md#6314-function-and-software) |
| sec.gen.005 | Hardening | The Platform **must** support Operating System level access control. | [RA-1 6.3.1.2 "System Access"](./chapter06.md#6312-system-access) |
| sec.gen.006 | Hardening | The Platform **must** support Secure logging. Logging with root account must be prohibited when root privileges are not required. | [RA-1 6.3.1.2 "System Access"](./chapter06.md#6312-system-access) |
| sec.gen.007 | Hardening | All servers part of Cloud Infrastructure **must** be Time synchronised with authenticated Time service. | [RA-1 6.3.7.6 "Security Logs Time Synchronisation"](./chapter06.md#6376-security-logs-time-synchronisation) |
| sec.gen.008 | Hardening | All servers part of Cloud Infrastructure **must** be regularly updated to address security vulnerabilities. | [RA-1 6.3.1.5 "Patches"](./chapter06.md#6315-patches), [RA-1 6.3.6 "Security LCM"](./chapter06.md#636-security-lcm)  |
| sec.gen.009 | Hardening | The Platform **must** support software integrity protection and verification. | [RA-1 6.3.3.2 "Integrity of OpenStack components configuration"](./chapter06.md#6332-integrity-of-openstack-components-configuration), [RA-1 6.3.5 "Image Security"](./chapter06.md#635-image-security) |
| sec.gen.010 | Hardening | The Cloud Infrastructure **must** support encrypted storage, for example, block, object and file storage, with access to encryption keys restricted based on a need to know ([Controlled Access Based on the Need to Know](https://www.cisecurity.org/controls/controlled-access-based-on-the-need-to-know/)). | [RA-1 6.3.3.3 "Confidentiality and Integrity of tenant data"](./chapter06.md#6333-confidentiality-and-integrity-of-tenant-data-secmon012-and-secmon013) |
| sec.gen.012 | Hardening | The Operator **must** ensure that only authorised actors have physical access to the underlying infrastructure. | This requirement’s verification goes beyond Anuket testing scope  |
| sec.gen.013 | Hardening | The Platform **must** ensure that only authorised actors have logical access to the underlying infrastructure. | [RA-1 6.3.1.2 "System Access"](./chapter06.md#6312-system-access) |
| sec.gen.015 | Hardening | Any change to the Platform **must** be logged as a security event, and the logged event must include the identity of the entity making the change, the change, the date and the time of the change. | [RA-1 6.3.6 "Security LCM"](./chapter06.md#636-security-lcm) |

<p align="center"><b>Table 2-6:</b> Reference Model Requirements - System Hardening Requirements</p>

####  2.2.6.2. Platform and Access (source [RM 7.9.2](../../../ref_model/chapters/chapter07.md#792-platform-and-access))

| Ref # | sub-category | Description |  Traceability |
|-------|-------|-------|---------|
| sec.sys.001 | Access | The Platform **must** support authenticated and secure access to API, GUI and command line interfaces | [RA-1 6.3.2.4 "RBAC"](./chapter06.md#6324-rbac) |
| sec.sys.002 | Access | The Platform **must** support Traffic Filtering for workloads (for example, Fire Wall). | [RA-1 6.3.4 "Workload Security"](./chapter06.md#634-workload-security) |
| sec.sys.003 | Access | The Platform **must** support Secure and encrypted communications, and confidentiality and integrity of network traffic. | [RA-1 6.3.3.1 "Confidentiality and Integrity of communications"](./chapter06.md#6331-confidentiality-and-integrity-of-communications)  |
| sec.sys.004 | Access | The Cloud Infrastructure **must** support authentication, integrity and confidentiality on all network channels. | [RA-1 6.3.3.1 "Confidentiality and Integrity of communications"](./chapter06.md#6331-confidentiality-and-integrity-of-communications)|
| sec.sys.005 | Access | The Cloud Infrastructure **must** segregate the underlay and overlay networks. | [RA-1 6.3.3.1 "Confidentiality and Integrity of communications"](./chapter06.md#6331-confidentiality-and-integrity-of-communications) |
| sec.sys.006 | Access | The Cloud Infrastructure **must** be able to utilise the Cloud Infrastructure Manager identity lifecycle management capabilities. | [RA-1 6.3.2.1 "Identity Security"](./chapter06.md#6321-identity-security) |
| sec.sys.007 | Access | The Platform **must** implement controls enforcing separation of duties and privileges, least privilege use and least common mechanism (Role-Based Access Control). | [RA-1 6.3.2.4 "RBAC"](./chapter06.md#6324-rbac) |
| sec.sys.008 | Access | The Platform **must** be able to assign the Entities that comprise the tenant networks to different trust domains. (Communication between different trust domains is not allowed, by default.) | [RA-1 6.3.4 "Workload Security"](./chapter06.md#634-workload-security) |  
| sec.sys.009 | Access | The Platform **must** support creation of Trust Relationships between trust domains. These maybe uni-directional relationships where the trusting domain trusts another domain (the “trusted domain”) to authenticate users for them or to allow access to its resources from the trusted domain.  In a bidirectional relationship both domain are “trusting” and “trusted”. |  |
| sec.sys.010 | Access | For two or more domains without existing trust relationships, the Platform **must not** allow the effect of an attack on one domain to impact the other domains either directly or indirectly. |  |
| sec.sys.011 | Access | The Platform **must not** reuse the same authentication credentials (e.g., key pairs) on different Platform components (e.g., different hosts, or different services). | [RA-1 6.3.1.2 "System Access"](./chapter06.md#6312-system-access) |
| sec.sys.012 | Access | The Platform **must** protect all secrets by using strong encryption techniques and storing the protected secrets externally from the component (e.g., in OpenStack Barbican) |  |
| sec.sys.013 | Access | The Platform **must** generate secrets dynamically as and when needed. |  |
| sec.sys.015 | Access | The Platform **must not** contain back door entries (unpublished access points, APIs, etc.). |  |
| sec.sys.016 | Access | Login access to the Platform's components **must** be through encrypted protocols such as SSH v2 or TLS v1.2 or higher. Note: Hardened jump servers isolated from external networks are recommended | [RA-1 6.3.6 "Security LCM"](./chapter06.md#636-security-lcm) |
| sec.sys.017 | Access | The Platform **must** provide the capability of using digital certificates that comply with X.509 standards issued by a trusted Certification Authority. | [RA-1 6.3.3.1 "Confidentiality and Integrity of communications"](./chapter06.md#6331-confidentiality-and-integrity-of-communications) |
| sec.sys.018 | Access | The Platform **must** provide the capability of allowing certificate renewal and revocation. |  |
| sec.sys.019 | Access | The Platform **must** provide the capability of testing the validity of a digital certificate (CA signature, validity period, non revocation, identity). |  |

<p align="center"><b>Table 2-7:</b> Reference Model Requirements - Platform and Access Requirements</p>

#### 2.2.6.3. Confidentiality and Integrity (source [RM7.9.3](../../../ref_model/chapters/chapter07.md#793-confidentiality-and-integrity))

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.ci.001 | Confidentiality/Integrity | The Platform **must** support Confidentiality and Integrity of data at rest and in transit. | [RA-1 6.3.3 "Confidentiality and Integrity"](./chapter06.md#633-confidentiality-and-integrity) |
| sec.ci.003 | Confidentiality/Integrity | The Platform **must** support Confidentiality and Integrity of data related metadata. |   |
| sec.ci.004 | Confidentiality | The Platform **must** support Confidentiality of processes and restrict information sharing with only the process owner (e.g., tenant). |   |
| sec.ci.005 | Confidentiality/Integrity | The Platform **must** support Confidentiality and Integrity of process-related metadata and restrict information sharing with only the process owner (e.g., tenant). |   |
| sec.ci.006 | Confidentiality/Integrity | The Platform **must** support Confidentiality and Integrity of workload resource utilisation (RAM, CPU, Storage, Network I/O, cache, hardware offload) and restrict information sharing with only the workload owner (e.g., tenant). |  |
| sec.ci.007 | Confidentiality/Integrity | The Platform **must not** allow Memory Inspection by any actor other than the authorised actors for the Entity to which Memory is assigned (e.g., tenants owning the workload), for Lawful Inspection, and for secure monitoring services. Administrative access must be managed using Platform Identity Lifecycle Management.  |  |
| sec.ci.008 | Confidentiality | The Cloud Infrastructure **must** support tenant networks segregation. | [RA-1 6.3.4 "Workload Security"](./chapter06.md#634-workload-security) |

<p align="center"><b>Table 2-8:</b> Reference Model Requirements: Confidentiality and Integrity Requirements</p>

#### 2.2.6.4. Workload Security (source [RM7.9.4](../../../ref_model/chapters/chapter07.md#794-workload-security))

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.wl.001 | Workload | The Platform **must** support Workload placement policy. | [RA-1 6.3.4 "Workload Security"](./chapter06.md#634-workload-security) |
| sec.wl.002 | Workload | The Cloud Infrastructure **must** provide methods to ensure the platform’s trust status and integrity (e.g., remote attestation, Trusted Platform Module). |  |
| sec.wl.003 | Workload | The Platform **must** support secure provisioning of Workloads. | [RA-1 6.3.4 "Workload Security"](./chapter06.md#634-workload-security) |
| sec.wl.004 | Workload | The Platform **must** support Location assertion (for mandated in-country or location requirements). | [RA-1 6.3.4 "Workload Security"](./chapter06.md#634-workload-security) |
| sec.wl.005 | Workload | The Platform **must** support the separation of production and non-production Workloads. | This requirement’s verification goes beyond Anuket testing scope |
| sec.wl.006 | Workload | The Platform **must** support the separation of Workloads based on their categorisation (for example, payment card information, healthcare, etc.) | [RA-1 6.3.4 "Workload Security"](./chapter06.md#634-workload-security) |

<p align="center"><b>Table 2-9:</b> Reference Model Requirements - Workload Security Requirements</p>

#### 2.2.6.5. Image Security (source [RM7.9.5](../../../ref_model/chapters/chapter07.md#795-image-security))

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.img.001 | Image | Images from untrusted sources **must not** be used. | [RA-1 6.3.5 "Image Security"](./chapter06.md#635-image-security) |
| sec.img.002 | Image | Images **must** be scanned to be maintained free from known vulnerabilities. | [RA-1 6.3.5 "Image Security"](./chapter06.md#635-image-security) |
| sec.img.003 | Image | Images **must not** be configured to run with privileges higher than the privileges of the actor authorised to run them. |  |
| sec.img.004 | Image | Images **must** only be accessible to authorised actors. | [RA-1 6.3.3.2 "Confidentiality and Integrity of communications"](./chapter06.md#6332-integrity-of-openstack-components-configuration)|
| sec.img.005 | Image | Image Registries **must** only be accessible to authorised actors. | [RA-1 6.3.3.2 "Confidentiality and Integrity of communications"](./chapter06.md#6332-integrity-of-openstack-components-configuration) |
| sec.img.006 | Image | Image Registries **must** only be accessible over networks that enforce authentication, integrity and confidentiality. | [RA-1 6.3.3.2 "Confidentiality and Integrity of communications"](./chapter06.md#6332-integrity-of-openstack-components-configuration) |
| sec.img.007 | Image | Image registries **must** be clear of vulnerable and out of date versions. | [RA-1 6.3.3.2 "Confidentiality and Integrity of communications"](./chapter06.md#6332-integrity-of-openstack-components-configuration), [RA-1 6.3.5 "Image Security"](./chapter06.md#635-image-security)  |

<p align="center"><b>Table 2-10:</b> Reference Model Requirements - Image Security Requirements</p>

#### 2.2.6.6. Security LCM (source [RM7.9.6](../../../ref_model/chapters/chapter07.md#796-security-lcm))

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.lcm.001 | LCM | The Platform **must** support Secure Provisioning, Availability, and Deprovisioning (Secure Clean-Up) of workload resources where Secure Clean-Up includes tear-down, defense against virus or other attacks. | [RA-1 6.3.7 "Monitoring and Security Audit"](./chapter06.md#637-monitoring-and-security-audit) |  
| sec.lcm.002 | LCM | The Cloud Operator **must** use management protocols limiting security risk such as SNMPv3, SSH v2, ICMP, NTP, syslog and TLS v1.2 or higher. | [RA-1 6.3.6 "Security LCM"](./chapter06.md#636-security-lcm) |
| sec.lcm.003 | LCM | The Cloud Operator **must** implement and strictly follow change management processes for Cloud Infrastructure, Cloud Infrastructure Manager and other components of the cloud, and Platform change control on hardware. | [RA-1 6.3.7 "Monitoring and Security Audit"](./chapter06.md#637-monitoring-and-security-audit) |  
| sec.lcm.005 | LCM | Platform **must** provide logs and these logs must be monitored for anomalous behaviour. | [RA-1 6.3.7 "Monitoring and Security Audit"](./chapter06.md#637-monitoring-and-security-audit) |
| sec.lcm.006 | LCM | The Platform **must** verify the integrity of all Resource management requests. | [RA-1 6.3.3.3 "Confidentiality and Integrity of tenant data"](./chapter06.md#6333-confidentiality-and-integrity-of-tenant-data-secmon012-and-secmon013) |
| sec.lcm.007 | LCM | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with current time information. |  |
| sec.lcm.008 | LCM | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with relevant DNS information. |  |
| sec.lcm.009 | LCM | The Platform **must** be able to update the tag of newly instantiated, suspended, hibernated, migrated and restarted images with relevant geolocation (geographical) information. |  |
| sec.lcm.010 | LCM | The Platform **must** log all changes to geolocation along with the mechanisms and sources of location information (i.e. GPS, IP block, and timing). |  |
| sec.lcm.011 | LCM | The Platform **must** implement Security life cycle management processes including the proactive update and patching of all deployed Cloud Infrastructure software. | [RA-1 6.3.1.5 "Patches"](./chapter06.md#6315-patches)  |
| sec.lcm.012 | LCM | The Platform **must** log any access privilege escalation. | [RA-1 6.3.7.2 "What to Log"](./chapter06.md#6372-what-to-log--what-not-to-log) |

<p align="center"><b>Table 2-11:</b> Reference Model Requirements - Security LCM Requirements</p>

#### 2.2.6.7. Monitoring and Security Audit (source [RM7.9.7](../../../ref_model/chapters/chapter07.md#797-monitoring-and-security-audit))

The Platform is assumed to provide configurable alerting and notification capability and the operator is assumed to have automated systems, policies and procedures to act on alerts and notifications in a timely fashion. In the following the monitoring and logging capabilities can trigger alerts and notifications for appropriate action.

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.mon.001 | Monitoring/Audit | Platform **must** provide logs and these logs must be regularly monitored for events of interest. The logs **must** contain the following fields: event type, date/time, protocol, service or program used for access, success/failure, login ID or process ID, IP address and ports (source and destination) involved.| [RA-1 6.3.7.1 "Creating logs"](./chapter06.md#6371-creating-logs), [RA-1 6.3.7.4 "Required Fields"](./chapter06.md#6374-required-fields) |
| sec.mon.002 | Monitoring | Security logs **must** be time synchronised. | [RA-1 6.3.7.6 "Security Logs Time Synchronisation"](./chapter06.md#6376-security-logs-time-synchronisation) |
| sec.mon.003 | Monitoring | The Platform **must** log all changes to time server source, time, date and time zones. | [RA-1 6.3.7.6 "Security Logs Time Synchronisation"](./chapter06.md#6376-security-logs-time-synchronisation) |
| sec.mon.004 | Audit | The Platform **must** secure and protect Audit logs (containing sensitive information) both in-transit and at rest. | [RA-1 6.3.6 "Security LCM"](./chapter06.md#636-security-lcm)  |
| sec.mon.005 | Monitoring/Audit | The Platform **must** Monitor and Audit various behaviours of connection and login attempts to detect access attacks and potential access attempts and take corrective actions accordingly | [RA-1 6.3.3.2 "Confidentiality and Integrity of communications"](./chapter06.md#6332-integrity-of-openstack-components-configuration), [RA-1 6.3.7.2 "What to log, what not to log"](./chapter06.md#6372-what-to-log--what-not-to-log) |
| sec.mon.006 | Monitoring/Audit | The Platform **must** Monitor and Audit operations by authorised account access after login to detect malicious operational activity and take corrective actions. | [RA-1 6.3.3.2 "Integrity of OpenStack components configuration"](./chapter06.md#6332-integrity-of-openstack-components-configuration), [RA-1 6.3.7 "Monitoring and Security Audit"](./chapter06.md#637-monitoring-and-security-audit) |
| sec.mon.007 | Monitoring/Audit | The Platform **must** Monitor and Audit security parameter configurations for compliance with defined security policies. | [RA-1 6.3.3.2 "Integrity of OpenStack components configuration"](./chapter06.md#6332-integrity-of-openstack-components-configuration) |
| sec.mon.008 | Monitoring/Audit | The Platform **must** Monitor and Audit externally exposed interfaces for illegal access (attacks) and take corrective security hardening measures. | [RA-1 6.3.3.1 "Confidentiality and Integrity of communications"](./chapter06.md#6331-confidentiality-and-integrity-of-communications) |
| sec.mon.009 | Monitoring/Audit | The Platform **must** Monitor and Audit service for various attacks (malformed messages, signalling flooding and replaying, etc.) and take corrective actions accordingly. | [RA-1 6.3.3.2 "Confidentiality and Integrity of communications"](./chapter06.md#6332-integrity-of-openstack-components-configuration), [RA-1 6.3.7 "Monitoring and Security Audit"](./chapter06.md#637-monitoring-and-security-audit)  |
| sec.mon.010 | Monitoring/Audit | The Platform **must** Monitor and Audit running processes to detect unexpected or unauthorised processes and take corrective actions accordingly. | [RA-1 6.3.7 "Monitoring and Security Audit"](./chapter06.md#637-monitoring-and-security-audit)  |
| sec.mon.011 | Monitoring/Audit | The Platform **must** Monitor and Audit logs from infrastructure elements and workloads to detected anomalies in the system components and take corrective actions accordingly. | [RA-1 6.3.7.1 "Creating logs"](./chapter06.md#6371-creating-logs) |
| sec.mon.012 | Monitoring/Audit | The Platform **must** Monitor and Audit Traffic patterns and volumes to prevent malware download attempts. | [RA-1 6.3.3.3 "Confidentiality and Integrity of tenant data"](./chapter06.md#6333-confidentiality-and-integrity-of-tenant-data-secmon012-and-secmon013) |
| sec.mon.013 | Monitoring | The monitoring system **must not** affect the security (integrity and confidentiality) of the infrastructure, workloads, or the user data (through back door entries). |  |
| sec.mon.015 | Monitoring | The Platform **must** ensure that the Monitoring systems are never starved of resources and **must** activate alarms when resource utilisation exceeds a configurable threshold. | [RA-1 6.3.7 "Monitoring and Security Audit"](./chapter06.md#637-monitoring-and-security-audit)  |
| sec.mon.017 | Audit | The Platform **must** audit systems for any missing security patches and take appropriate actions. | [RA-1 6.3.1.5 "Patches"](./chapter06.md#6315-patches) |
| sec.mon.018 | Monitoring | The Platform, starting from initialisation, **must** collect and analyse logs to identify security events, and store these events in an external system. | [RA-1 6.3.7.3 "Where to Log"](./chapter06.md#6373-where-to-log) |
| sec.mon.019 | Monitoring | The Platform’s components **must not** include an authentication credential, e.g., password, in any logs, even if encrypted. | [RA-1 6.3.7.2 "What to Log"](./chapter06.md#6372-what-to-log--what-not-to-log) |
| sec.mon.020 | Monitoring/Audit | The Platform’s logging system **must** support the storage of security audit logs for a configurable period of time. | [RA-1 6.3.7.5 "Data Retention](./chapter06.md#6375-data-retention)  |
| sec.mon.021 | Monitoring | The Platform **must** store security events locally if the external logging system is unavailable and shall periodically attempt to send these to the external logging system until successful. | [RA-1 6.3.7.3 "Where to Log"](./chapter06.md#6373-where-to-log) |

<p align="center"><b>Table 2-12:</b> Reference Model Requirements - Monitoring and Security Audit Requirements</p>

#### 2.2.6.9. Open Source Software (source [RM7.9.8](../../../ref_model/chapters/chapter07.md#798-open-source-sotfware))

| Ref # | sub-category | Description |  Traceability |
|---------|---------------|----------------|------------|
| sec.oss.001 | Software | Open-source code **must** be inspected by tools with various capabilities for static and dynamic code analysis. |  |
| sec.oss.002 | Software | The CVE(Common Vulnerabilities and Exposures) **must** be used to identify vulnerabilities and their severity rating for open-source code part of Cloud Infrastructure and workloads software, https://cve.mitre.org/ |  |
| sec.oss.003 | Software | High severity rated vulnerabilities **must** be fixed. Refer to the CVSS (Common Vulnerability Scoring System) to know a vulnerability score. | |
| sec.oss.004 | Software | A dedicated internal isolated repository separated from the production environment **must** be used to store vetted open-source content. |  |

<p align="center"><b>Table 2-13:</b> Reference Model Requirements - Open-Source Software Security Requirements</p>

#### 2.2.6.9. IaaC security (source [RM7.9.9](../../../ref_model/chapters/chapter07.md#799-iaac---secure-design-and-architecture-stage-requirements))

**Secure Code Stage Requirements**

| Ref # | sub-category | Description |  Traceability |
|---------|---------------|----------------|------------|
| sec.code.001 | IaaC | SAST -Static Application Security Testing **must** be applied during Secure Coding stage triggered by Pull, Clone or Comment trigger. Security testing that analyses application source code for software vulnerabilities and gaps against best practices. Example: open source OWASP range of tools.|  |

<p align="center"><b>Table 2-14:</b> Reference Model Requirements: IaaC Security Requirements, Secure Code Stage </p>

**Continuous Build, Integration and Testing Stage Requirements**

| Ref # | sub-category | Description |  Traceability |
|---------|---------------|----------------|------------|
| sec.bld.003 | IaaC | Container and Image Scan **must** be applied during the Continuous Build, Integration and Testing stage triggered by Package trigger. Example: A push of a container image to a container registry may trigger a vulnerability scan before the image becomes available in the registry.  |  |

<p align="center"><b>Table 2-15:</b> Reference Model Requirements - IaaC Security Requirements, Continuous Build, Integration and Testing Stage </p>

**Continuous Delivery and Deployment Stage Requirements**

| Ref # | sub-category | Description |  Traceability |
|---------|---------------|----------------|------------|
| sec.del.001 | IaaC | Image Scan **must** be applied during the Continuous Delivery and Deployment stage triggered by Publish to Artifact and Image Repository trigger. Example: GitLab uses the open source Clair engine for container image scanning.|  |
| sec.del.002 | IaaC | Code Signing **must** be applied during the Continuous Delivery and Deployment stage triggered by Publish to Artifact and Image Repository trigger. Code Signing provides authentication to assure that downloaded files are form the publisher named on the certificate.  |  |
| sec.del.004 | IaaC | Component Vulnerability Scan **must** be applied during the Continuous Delivery and Deployment stage triggered by Instantiate Infrastructure trigger. The vulnerability scanning system is deployed on the cloud platform to detect security vulnerabilities of specified components through scanning and to provide timely security protection. Example: OWASP Zed Attack Proxy (ZAP). |  |

<p align="center"><b>Table 2-16:</b> Reference Model Requirements - IaaC Security Requirements, Continuous Delivery and Deployment Stage</p>

**Runtime Defence and Monitoring Requirements**

| Ref # | sub-category | Description |  Traceability |
|---------|---------------|----------------|------------|
| sec.run.001 | IaaC | Component Vulnerability Monitoring **must** be continuously applied during the Runtime Defence and Monitoring stage. Security technology that monitors components like virtual servers and assesses data, applications, and infrastructure for security risks.|  |

<p align="center"><b>Table 2-17:</b> Reference Model Requirements - IaaC Security Requirements, Runtime Defence and Monitoring Stage</p>

#### 2.2.6.10. Compliance with Standards (source [RM7.9.10](../../../ref_model/chapters/chapter07.md#7910-compliance-with-standards))

| Ref # | sub-category | Description |  Traceability |
|---------|---------------|----------------|------------|
| sec.std.012 | Standards | The Public Cloud Operator **must**, and the Private Cloud Operator **may** be certified to be compliant with the International Standard on Awareness Engagements (ISAE) 3402 (in the US: SSAE 16); International Standard on Awareness Engagements (ISAE) 3402. US Equivalent: SSAE16. | |

<p align="center"><b>Table 2-18:</b> Reference Model Requirements: Cloud Infrastructure Security Requirements</p>


<a name="2.3"></a>
## 2.3 Architecture and OpenStack Requirements

"Architecture" in this chapter refers to Cloud infrastructure (referred to as NFVI by ETSI) + VIM (as specified in Reference Model Chapter 3).

<a name="2.3.1"></a>
### 2.3.1 General Requirements

| Ref # | sub-category | Description | Traceability |
|----|---------------|---------------------|---------------|
| gen.ost.01 | Open source | The Architecture **must** use OpenStack APIs.| [RA-1 5.3](./chapter05.md#5.3) |
| gen.ost.02 | Open source | The Architecture **must** support dynamic request and configuration of virtual resources (compute, network, storage) through OpenStack APIs. | [RA-1 5.3](./chapter05.md#53-consolidated-set-of-apis) |
| gen.rsl.01 | Resiliency | The Architecture **must** support resilient OpenStack components that are required for the continued availability of running workloads. | |
| gen.avl.01 | Availability | The Architecture **must** provide High Availability for OpenStack components. | [RA-1 4.2 "Underlying Resources"](./chapter04.md#42-underlying-resources) |

<p align="center"><b>Table 2-19:</b> General Requirements</p>

<a name="2.3.2"></a>
### 2.3.2 Infrastructure Requirements

| Ref # | sub-category | Description |  Traceability |
|----|--------------|---------------------|-----------|
| inf.com.01 | Compute | The Architecture **must** provide compute resources for VM instances. | [RA-1 3.3.1.4 "Cloud Workload Services"](./chapter03.md#3314-cloud-workload-services) |
| inf.com.04 | Compute | The Architecture **must** be able to support multiple CPU type options to support various infrastructure profiles (Basic and High Performance).| [RA-1 4.4.1. "Support for Cloud Infrastructure Profiles and flavors"](./chapter04.md#4.4.1) |
| inf.com.05 | Compute | The Architecture **must** support Hardware Platforms with NUMA capabilities.| [RA-1 4.4.1. "Support for Cloud Infrastructure Profiles and flavors"](./chapter04.md#4.4.1) |
| inf.com.06 | Compute | The Architecture **must** support CPU Pinning of the vCPUs of VM instance.| [RA-1 4.4.1. "Support for Cloud Infrastructure Profiles and flavors"](./chapter04.md#4.4.1) |
| inf.com.07 | Compute | The Architecture **must** support different hardware configurations to support various infrastructure profiles (Basic and High Performance).| [RA-1 3.3.3. "Host aggregates providing resource pooling"](./chapter03.md#333-host-aggregates-providing-resource-pooling) |
| inf.com.08 | Compute | The Architecture **must** support allocating certain number of host cores for all non-tenant workloads such as for OpenStack services. SMT threads can be allocated to individual OpenStack services or their components. | [Dedicating host cores to certain workloads (e.g., OpenStack services)](https://docs.openstack.org/nova/latest/configuration/config.html#compute.cpu_dedicated_set). Please see example, ["Configuring libvirt compute nodes for CPU pinning"](https://docs.openstack.org/nova/latest/admin/cpu-topologies.html) |
| inf.com.09 | Compute | The Architecture **must** ensure that the host cores assigned to non-tenant and tenant workloads are SMT aware: that is, a host core and its associated SMT threads are either all assigned to non-tenant workloads or all assigned to tenant workloads. | Achieved through configuring the "cpu_dedicated_set" and "cpu_shared_set" parameters in nova.conf correctly. |
| inf.stg.01 | Storage | The Architecture **must** provide remote (not directly attached to the host) Block storage for VM Instances. | [RA-1 3.4.2.3. "Storage"](./chapter03.md#3423-storage) |
| inf.stg.02 | Storage | The Architecture **must** provide Object storage for VM Instances. Operators **may** choose not to implement Object Storage but must be cognizant of the risk of "Compliant VNFs" failing in their environment. | OpenStack Swift Service ([RA-1 4.3.1.4 "Swift"](./chapter04.md#4314-swift)) |
| inf.ntw.01 | Network | The Architecture **must** provide virtual network interfaces to VM instances. | [RA-1 5.2.5. "Neutron" ](./chapter05.md#525-neutron) |
| inf.ntw.02 | Network | The Architecture **must** include capabilities for integrating SDN controllers to support provisioning of network services, from the OpenStack Neutron service, such as networking of VTEPs to the Border Edge based VRFs. | [RA-1 3.2.5. "Virtual Networking – 3rd party SDN solution"](./chapter03.md#325-virtual-networking--3rd-party-sdn-solution) |
| inf.ntw.03 | Network | The Architecture **must** support low latency and high throughput traffic needs. | [RA-1 4.2.3. "Network Fabric"](./chapter04.md#423-network-fabric) |
| inf.ntw.05 | Network | The Architecture **must** allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay such as VXLAN or Geneve). | [RA-1 4.2.3. "Network Fabric"](./chapter04.md#423-network-fabric) |
| inf.ntw.07 | Network | The Architecture **must** support network [resiliency](../../../common/glossary.md#cloud-platform-abstraction-related-terminology). | [RA-1 3.4.2.2. "Network"](./chapter03.md#3422-network) |
| inf.ntw.10 | Network | The Cloud Infrastructure Network Fabric **must** be capable of enabling highly available (Five 9’s or better) Cloud Infrastructure. | [RA-1 3.4.2.2. "Network"](./chapter03.md#3422-network) |
| inf.ntw.15 | Network | The Architecture **must** support multiple networking options for Cloud Infrastructure to support various infrastructure profiles (Basic and High Performance).| [RA-1 4.2.3.4. "Neutron ML2-plugin Integration"](./chapter04.md#4234-neutron-ml2-integration) and ["OpenStack Neutron Plugins"](https://wiki.openstack.org/wiki/Neutron_Plugins_and_Drivers) |
| inf.ntw.16 | Network | The Architecture **must** support dual stack IPv4 and IPv6 for tenant networks and workloads.| |

<p align="center"><b>Table 2-20:</b> Infrastructure Requirements</p>


<a name="2.3.3"></a>
### 2.3.3 VIM Requirements

| Ref # | sub-category | Description |  Traceability |
|----|----------------|----------------------|-----------|
| vim.01 | General | The Architecture **must** allow infrastructure resource sharing. | [RA-1 3.2. "Consumable Infrastructure Resources and Services"](./chapter03.md#32-consumable-infrastructure-resources-and-services) |
| vim.03 | General | The Architecture **must** allow VIM to discover and manage Cloud Infrastructure resources. | [RA-1 5.2.7. "Placement"](./chapter05.md#527-placement) |
| vim.05 | General | The Architecture **must** include image repository management. | [RA-1 4.3.1.2. "Glance"](./chapter04.md#4312-glance) |
| vim.07 | General | The Architecture **must** support multi-tenancy. | [RA-1 3.2.1. "Multi-Tenancy"](./chapter03.md#321-multi-tenancy-execution-environment) |
| vim.08 | General | The Architecture **must** support resource tagging. | ["OpenStack Resource Tags"](https://specs.openstack.org/openstack/api-wg/guidelines/tags.html) |

<p align="center"><b>Table 2-21:</b> VIM Requirements</p>

<a name="2.3.4"></a>
### 2.3.4 Interfaces & APIs Requirements

| Ref # | sub-category | Description |  Traceability |
|----|----------|--------------------|------------|
| int.api.01 | API | The Architecture **must** provide APIs to access the authentication service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.1 "Keystone"](./chapter05.md#521-keystone) |
| int.api.02 | API | The Architecture **must** provide APIs to access the image management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.2 "Glance"](./chapter05.md#522-glance) |
| int.api.03 | API | The Architecture **must** provide APIs to access the block storage management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.3 "Cinder"](./chapter05.md#523-cinder) |
| int.api.04 | API | The Architecture **must** provide APIs to access the object storage management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.4 "Swift"](./chapter05.md#524-swift) |
| int.api.05 | API | The Architecture **must** provide APIs to access the network management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.5 "Neutron"](./chapter05.md#525-neutron) |
| int.api.06 | API | The Architecture **must** provide APIs to access the compute resources management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.6 "Nova"](./chapter05.md#526-nova) |
| int.api.07 | API | The Architecture **must** provide GUI access to tenant facing cloud platform core services except at Edge/Far Edge clouds. | [RA-1 4.3.1.9 "Horizon"](./chapter04.md#4319-horizon) |
| int.api.08 | API | The Architecture **must** provide APIs needed to discover and manage Cloud Infrastructure resources. | [RA-1 5.2.7. "Placement"](./chapter05.md#527-placement) |
| int.api.09 | API | The Architecture **must** provide APIs to access the orchestration service. | [RA-1 5.2.8 "Heat"](./chapter05.md#528-heat) |
| int.api.10 | API | The Architecture must expose the latest version and microversion of the APIs for the given Anuket OpenStack release for each of the OpenStack core services. | [RA-1 5.2 Core OpenStack Services APIs](./chapter05.md#52-core-openstack-services-apis) |

<p align="center"><b>Table 2-22:</b> Interfaces and APIs Requirements</p>

<a name="2.3.5"></a>
### 2.3.5 Tenant Requirements

| Ref # | sub-category | Description |  Traceability |
|----|--------------|---------------|-----------------|
| tnt.gen.01 | General | The Architecture **must** support self-service dashboard (GUI) and APIs for users to deploy, configure and manage their workloads. | [RA-1 4.3.1.9 "Horizon"](./chapter04.md#4319-horizon) and [3.3.1.4 Cloud Workload Services](./chapter03.md#3314-cloud-workload-services) |

<p align="center"><b>Table 2-23:</b> Tenant Requirements</p>

<a name="2.3.6"></a>

### 2.3.6 Operations and LCM

| Ref # | sub-category | Description |  Traceability |
|----|----------|-------------|-------------|
| lcm.gen.01	| General | The Architecture must support zero downtime of running workloads when the number of compute hosts and/or the storage capacity is being expanded or unused capacity is being removed. | |
| lcm.adp.02 | Automated deployment | The Architecture must support upgrades of software, provided by the cloud provider, so that the running workloads are not impacted (viz., hitless upgrades). Please note that this means that the existing data plane services should not fail (go down). | |

<p align="center"><b>Table 2-24:</b> LCM Requirements</p>

<a name="2.3.7"></a>
### 2.3.7 Assurance Requirements

| Ref # | sub-category | Description |  Traceability |
|----|--------|-------------------|----------|
| asr.mon.01 | Integration | The Architecture **must** include integration with various infrastructure components to support collection of telemetry for assurance monitoring and network intelligence. | |
| asr.mon.03 | Monitoring | The Architecture **must** allow for the collection and dissemination of performance and fault information. | |
| asr.mon.04 | Network | The Cloud Infrastructure Network Fabric and Network Operating System **must** provide network operational visibility through alarming and streaming telemetry services for operational management, engineering planning, troubleshooting, and network performance optimisation. | |

<p align="center"><b>Table 2-25:</b> Assurance Requirements</p>

<a name="2.4"></a>
### 2.4 Architecture and OpenStack Recommendations

The requirements listed in this section are optional, and are not required in order to be deemed a conformant implementation.

<a name="2.4.1"></a>
### 2.4.1 General Recommendations

| Ref # | sub-category | Description |  Notes |
|----|-------|---------------------|-------------|
| gen.cnt.01 | Cloud nativeness | The Architecture **should** consist of stateless service components. However, where state is required it must be kept external to the component. | OpenStack consists of both stateless and stateful services where the stateful services utilise a database. For latter see "[Configuring the stateful services](https://docs.openstack.org/ha-guide/control-plane-stateful.html)"|
| gen.cnt.02 | Cloud nativeness | The Architecture **should** consist of service components implemented as microservices that are individually dynamically scalable. | |
| gen.scl.01 | Scalability | The Architecture **should** support policy driven auto-scaling. | This requirement is currently not addressed but will likely be supported through [Senlin](https://docs.openstack.org/senlin/train/), cluster management service. |
| gen.rsl.02 | Resiliency | The Architecture **should** support resilient OpenStack service components that are not subject to gen.rsl.01. | |

<p align="center"><b>Table 2-26:</b> General Recommendations</p>

<a name="2.4.2"></a>
### 2.4.2 Infrastructure Recommendations

| Ref # | sub-category | Description |  Notes |
|----|-------|---------------------|-------------|
| inf.com.02 | Compute | The Architecture **should** include industry standard hardware management systems at both HW device level (embedded) and HW platform level (external to device). | |
| inf.com.03 | Compute | The Architecture **should** support Symmetric Multiprocessing with shared memory access as well as Simultaneous Multithreading. | |
| inf.stg.08 | Storage | The Architecture **should** allow use of externally provided large archival storage for its Backup / Restore / Archival needs. | |
| inf.stg.09 | Storage | The Architecture **should** make available all non-host OS / Hypervisor / Host systems storage as network-based Block, File or Object Storage for tenant/management consumption. | |
| inf.stg.10 | Storage | The Architecture **should** provide local Block storage for VM Instances. | [RA-1 "Virtual Storage"](./chapter03.md#323-virtual-storage) |
| inf.ntw.04 | Network | The Architecture **should** support service function chaining. |  |
| inf.ntw.06 | Network | The Architecture **should** support Distributed Virtual Routing (DVR) to allow compute nodes to route traffic efficiently. | |
| inf.ntw.08 | Network | The Cloud Infrastructure Network Fabric **should** embrace the concepts of open networking and disaggregation using commodity networking hardware and disaggregated Network Operating Systems. | |
| inf.ntw.09 | Network | The Cloud Infrastructure Network Fabric **should** embrace open-based standards and technologies. | |
| inf.ntw.11 | Network | The Cloud Infrastructure Network Fabric **should** be architected to provide a standardised, scalable, and repeatable deployment model across all applicable Cloud Infrastructure sites. | |
| inf.ntw.17 | Network | The Architecture **should** use dual stack IPv4 and IPv6 for Cloud Infrastructure internal networks. | |
| inf.acc.01 | Acceleration | The Architecture **should** support Application Specific Acceleration (exposed to VNFs). | [RA-1 3.2.6. "Acceleration"](./chapter03.md#326-acceleration) |
| inf.acc.02 | Acceleration | The Architecture **should** support Cloud Infrastructure Acceleration (such as SmartNICs). | ["OpenStack Future - Specs defined"](https://specs.openstack.org/openstack/neutron-specs/specs/stein/neutron-ovs-agent-support-baremetal-with-smart-nic.html) |
| inf.acc.03 | Acceleration | The Architecture **may** rely on SR-IOV PCI-Pass through to provide acceleration to VNFs. | |
| inf.img.01 | Image | The Architecture **should** make the immutable images available via location independent means. | [RA-1 4.3.1.2. "Glance"](./chapter04.md#4312-glance) |

<p align="center"><b>Table 2-27:</b> Infrastructure Recommendations</p>


<a name="2.4.3"></a>
### 2.4.3 VIM Recommendations

| Ref # | sub-category | Description |  Notes |
|----|----------------|----------------------|-----------|
| vim.02 | General | The Architecture **should** support deployment of OpenStack components in containers. | [RA-1 4.3.2. "Containerised OpenStack Services"](./chapter04.md#432-containerised-openstack-services) |
| vim.04| General | The Architecture **should** support Enhanced Platform Awareness (EPA) only for discovery of infrastructure resource capabilities.| |
| vim.06 | General | The Architecture **should** allow orchestration solutions to be integrated with VIM. |  |
| vim.09 | General | The Architecture **should** support horizontal scaling of OpenStack core services. |  |

<p align="center"><b>Table 2-28:</b> VIM Recommendations</p>

<a name="2.4.4"></a>
### 2.4.4 Interfaces and APIs Recommendations

| Ref # | sub-category | Description |  Notes |
|----|-------|---------------------|-------------|
| int.acc.01 | Acceleration | The Architecture **should** provide an open and standard acceleration interface to VNFs. |  |
| int.acc.02 | Acceleration | The Architecture **should not** rely on SR-IOV PCI-Pass through for acceleration interface exposed to VNFs. | duplicate of inf.acc.03 under "Infrastructure Recommendations" |

<p align="center"><b>Table 2-29:</b> Interfaces and APIs Recommendations</p>

<a name="2.4.5"></a>
### 2.4.5 Tenant Recommendations

This section is left blank for future use.

| Ref # | sub-category | Description |  Notes |
|----|-------|---------------------|-------------|

<p align="center"><b>Table 2-30:</b> Tenant Recommendations</p>

<a name="2.4.6"></a>
### 2.4.6 Operations and LCM Recommendations

| Ref # | sub-category | Description |  Notes |
|----|----------|-------------|-------------|
| lcm.adp.01 | Automated deployment | The Architecture **should** allow for “cookie cutter” automated deployment, configuration, provisioning and management of multiple Cloud Infrastructure sites. | |
| lcm.adp.03 | Automated deployment | The Architecture **should** support hitless upgrade of all software provided by the cloud provider that are not covered by lcm.adp.02. Whenever hitless upgrades are not feasible, attempt should be made to minimise the duration and nature of impact. | |
| lcm.adp.04 | Automated deployment | The Architecture **should** support declarative specifications of hardware and software assets for automated deployment, configuration, maintenance and management. | |
| lcm.adp.05 | Automated deployment | The Architecture **should** support automated process for Deployment and life-cycle management of VIM Instances. | |
| lcm.cid.02 | CI/CD | The Architecture **should** support integrating with CI/CD Toolchain for Cloud Infrastructure and VIM components Automation. | |

<p align="center"><b>Table 2-31:</b> LCM Recommendations</p>

<a name="2.4.7"></a>
### 2.4.7 Assurance Recommendations

| Ref # | sub-category | Description |  Notes |
|----|--------|-------------------|----------|
| asr.mon.02 | Monitoring | The Architecture **should** support Network Intelligence capabilities that allow richer diagnostic capabilities which take as input broader set of data across the network and from VNF workloads. | |

<p align="center"><b>Table 2-32:</b> Assurance Recommendations</p>

<a name="2.4.8"></a>
### 2.4.8 Security Recommendations

#### 2.4.8.1. System Hardening (source [RM 7.9.1](../../../ref_model/chapters/chapter07.md#791-system-hardening))

| Ref # | sub-category | Description |  Notes |
|-------|------|------|-------|
| sec.gen.011 | Hardening | The Cloud Infrastructure **should** support Read and Write only storage partitions (write only permission to one or more authorised actors). |  |
| sec.gen.014 | Hardening | All servers part of Cloud Infrastructure **should** support measured boot and an attestation server that monitors the measurements of the servers. |  |

<p align="center"><b>Table 2-33:</b> System Hardening Recommendations</p>

####  2.4.8.2. Platform and Access (source [RM 7.9.2](../../../ref_model/chapters/chapter07.md#792-platform-and-access))

| Ref # | sub-category | Description |  Notes |
|-------|-------|-------|---------|
| sec.sys.014 | Access | The Platform **should** use Linux Security Modules such as SELinux to control access to resources. | |
| sec.sys.020 | Access | The Cloud Infrastructure architecture **should** rely on Zero Trust principles to build a secure by design environment. | Zero Trust Architecture (ZTA) described in NIST SP 800-207 |

<p align="center"><b>Table 2-34:</b> Platform and Access Recommendations</p>

#### 2.4.8.3. Confidentiality and Integrity (source [RM7.9.3](../../../ref_model/chapters/chapter07.md#793-confidentiality-and-integrity))

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.ci.002 | Confidentiality/Integrity | The Platform **should** support self-encrypting storage devices |  |
| sec.ci.009 | Confidentiality/Integrity |For sensitive data encryption, the key management service **should** leverage a Hardware Security Module to manage and protect cryptographic keys. | |

<p align="center"><b>Table 2-35:</b> Confidentiality and Integrity Recommendations</p>

#### 2.4.8.4. Workload Security (source [RM7.9.4](../../../ref_model/chapters/chapter07.md#794-workload-security))

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.wl.007 | Workload | The Operator **should** implement processes and tools to verify VNF authenticity and integrity. |  |

<p align="center"><b>Table 2-36:</b> Workload Security Recommendations</p>

#### 2.4.8.5. Image Security (source [RM7.9.5](../../../ref_model/chapters/chapter07.md#795-image-security))

This section is left blank for future use.

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|

<p align="center"><b>Table 2-37:</b> Image Security Recommendations</p>

#### 2.4.8.6. Security LCM (source [RM7.9.6](../../../ref_model/chapters/chapter07.md#796-security-lcm))

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.lcm.004 | LCM | The Cloud Operator **should** support automated templated approved changes; Templated approved changes for automation where available |  |  

<p align="center"><b>Table 2-38:</b> LCM Security Recommendations</p>

#### 2.4.8.7. Monitoring and Security Audit (source [RM7.9.7](../../../ref_model/chapters/chapter07.md#797-monitoring-and-security-audit))

The Platform is assumed to provide configurable alerting and notification capability and the operator is assumed to have automated systems, policies and procedures to act on alerts and notifications in a timely fashion. In the following the monitoring and logging capabilities can trigger alerts and notifications for appropriate action.

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.mon.014 | Monitoring | The Monitoring systems **should** not impact IaaS, PaaS, and SaaS SLAs including availability SLAs |  |
| sec.mon.016 | Monitoring | The Platform Monitoring components **should** follow security best practices for auditing, including secure logging and tracing |  |

<p align="center"><b>Table 2-39:</b> Monitoring and Security Audit Recommendations</p>

#### 2.4.8.8. Open Source Software Security (source [RM7.9.8](../../../ref_model/chapters/chapter07.md#798-open-source-sotfware))

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.oss.004 | Software | A Software Bill of Materials (SBOM) **should** be provided or build, and maintained to identify the software components and their origins. Inventory of software components | https://www.ntia.gov/SBOM. | 

p align="center"><b>Table 2-40:</b> Open Source Software Security Recommendations</p>

#### 2.4.8.9. IaaC security (source [RM7.9.9](../../../ref_model/chapters/chapter07.md#799-iaac---secure-design-and-architecture-stage-requirements))

**Secure Design and Architecture Stage**

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.arch.001 | IaaC | Threat Modelling methodologies and tools **should** be used during the Secure Design and Architecture stage triggered by Software Feature Design trigger. Methodology to identify and understand threats impacting a resource or set of resources. | It may be done manually or using tools like open source OWASP Threat Dragon |
| sec.arch.002 | IaaC | Security Control Baseline Assessment **should** be performed during the Secure Design and Architecture stage triggered by Software Feature Design trigger.| Typically done manually by internal or independent assessors.  | 

<p align="center"><b>Table 2-41:</b> Reference Model Requirements: IaaC Security, Design and Architecture Stage</p>

**Secure Code Stage Requirements**

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.code.002 | IaaC | SCA – Software Composition Analysis **should** be applied during Secure Coding stage triggered by Pull, Clone or Comment trigger. Security testing that analyses application source code or compiled code for software components with known vulnerabilities. | Example: open source OWASP range of tools.  | 
| sec.code.003 | IaaC | Source Code Review **should** be performed continuously during Secure Coding stage. | Typically done manually.  | 
| sec.code.004 | IaaC | Integrated SAST via IDE Plugins **should** be used during Secure Coding stage triggered by Developer Code trigger. On the local machine: through the IDE or integrated test suites; triggered on completion of coding by developer. |  |
| sec.code.005 | IaaC | SAST of Source Code Repo **should** be performed during Secure Coding stage triggered by Developer Code trigger. Continuous delivery pre-deployment: scanning prior to deployment. |  |

<p align="center"><b>Table 2-42:</b> Reference Model Requirements: IaaC Security, Secure Code Stage </p>

**Continuous Build, Integration and Testing Stage Requirements**

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.bld.001 | IaaC | SAST -Static Application Security Testing **should** be applied during the Continuous Build, Integration and Testing stage triggered by Build and Integrate trigger. | Example: open source OWASP range of tools.| 
| sec.bld.002 | IaaC | SCA – Software Composition Analysis **should** be applied during the Continuous Build, Integration and Testing stage triggered by Build and Integrate trigger.| Example: open source OWASP range of tools.  |
| sec.bld.004 | IaaC | DAST – Dynamic Application Security Testing **should** be applied during the Continuous Build, Integration and Testing stage triggered by Stage & Test trigger. Security testing that analyses a running application by exercising application functionality and detecting vulnerabilities based on application behaviour and response. | Example: OWASP ZAP. |
| sec.bld.005 | IaaC | Fuzzing **should** be applied during the Continuous Build, Integration and testing stage triggered by Stage & Test trigger. Fuzzing or fuzz testing is an automated software testing technique that involves providing invalid, unexpected, or random data as inputs to a computer program. | Example: GitLab Open Sources Protocol Fuzzer Community Edition. |
| sec.bld.006 | IaaC | IAST – Interactive Application Security Testing **should** be applied during the Continuous Build, Integration and Testing stage triggered by Stage & Test trigger. Software component deployed with an application that assesses application behaviour and detects presence of vulnerabilities on an application being exercised in realistic testing scenarios. | Example:  Contrast Community Edition. |

<p align="center"><b>Table 2-43:</b> Reference Model Requirements: IaaC Security, Continuous Build, Integration and Testing Stage </p>

**Continuous Delivery and Deployment Stage Requirements**

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.del.003 | IaaC | Artifact and Image Repository Scan **should** be continuously applied during the Continuous Delivery and Deployment stage. | Example: GitLab uses the open source Clair engine for container scanning. | 

<p align="center"><b>Table 2-44:</b> Reference Model Requirements: IaaC Security, Continuous Delivery and Deployment Stage </p>

**Runtime Defence and Monitoring Requirements**

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.run.002 | IaaC | RASP – Runtime Application Self-Protection **should** be continuously applied during the Runtime Defence and Monitoring stage. Security technology deployed within the target application in production for detecting, alerting, and blocking attacks.  |  |
| sec.run.003 | IaaC | Application testing and Fuzzing **should** be continuously applied during the Runtime Defence and Monitoring stage. Fuzzing or fuzz testing is an automated software testing technique that involves providing invalid, unexpected, or random data as inputs to a computer program. | Example: GitLab Open Sources Protocol Fuzzer Community Edition.  |
| sec.run.004 | IaaC | Penetration Testing **should** be continuously applied during the Runtime Defence and Monitoring stage. | Typically done manually. |

<p align="center"><b>Table 2-45:</b> Reference Model Requirements: Iaac Security, Runtime Defence and Monitoring Stage </p>

#### 2.4.8.10. Compliance with Standards (source [RM7.9.10](../../../ref_model/chapters/chapter07.md#7910-compliance-with-standards))

| Ref # | sub-category | Description |  Notes |
|---------|---------------|----------------|------------|
| sec.std.001 | Standards | The Cloud Operator **should** comply with Center for Internet Security CIS Controls ([https://www.cisecurity.org/](https://www.cisecurity.org/)); Center for Internet Security - [https://www.cisecurity.org/](https://www.cisecurity.org/) | |
| sec.std.002 | Standards | The Cloud Operator, Platform and Workloads **should** follow the guidance in the CSA Security Guidance for Critical Areas of Focus in Cloud Computing (latest version) [https://cloudsecurityalliance.org/](https://cloudsecurityalliance.org/).  Cloud Security Alliance - [https://cloudsecurityalliance.org/](https://cloudsecurityalliance.org/) | |
| sec.std.003 | Standards | The Platform and Workloads **should** follow the guidance in the OWASP Cheat Sheet Series (OCSS) https://github.com/OWASP/CheatSheetSeries. Open Web Application Security Project [https://www.owasp.org](https://www.owasp.org) | |
| sec.std.004 | Standards | The Cloud Operator, Platform and Workloads **should** ensure that their code is not vulnerable to the OWASP Top Ten Security Risks [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/) |  |
| sec.std.005 | Standards | The Cloud Operator, Platform and Workloads **should** strive to improve their maturity on the OWASP Software Maturity Model (SAMM) https://owaspsamm.org/blog/2019/12/20/version2-community-release/ |  |
| sec.std.006  | Standards | The Cloud Operator, Platform and Workloads **should** utilise the OWASP Web Security Testing Guide https://github.com/OWASP/wstg/tree/master/document |  |
| sec.std.007 | Standards | The Cloud Operator, and Platform **should** satisfy the requirements for Information Management Systems specified in ISO/IEC 27001  https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en; ISO/IEC 27002:2013 - ISO/IEC 27001 is the international Standard for best-practice information security management systems (ISMSs) | |
| sec.std.008 | Standards | The Cloud Operator, and Platform **should** implement the Code of practice for Security Controls specified ISO/IEC 27002:2013 (or latest)  https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:en | |
| sec.std.009 | Standards | The Cloud Operator, and Platform **should** implement the ISO/IEC 27032:2012 (or latest) Guidelines for Cybersecurity techniques  https://www.iso.org/obp/ui/#iso:std:iso-iec:27032:ed-1:v1:en; ISO/IEC 27032 - ISO/IEC 27032is the international Standard focusing explicitly on cybersecurity | |
| sec.std.010 | Standards | The Cloud Operator **should** conform to the ISO/IEC 27035 standard for incidence management; ISO/IEC 27035 - ISO/IEC 27035 is the international Standard for incident management | |
| sec.std.011 | Standards | The Cloud Operator **should** conform to the ISO/IEC 27031 standard for business continuity; ISO/IEC 27031 - ISO/IEC 27031 is the international Standard for ICT readiness for business continuity | |

<p align="center"><b>Table 2-46:</b> Security Recommendations</p>
