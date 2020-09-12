[<< Back](../../openstack)

# 2. Architecture Requirements
<p align="right"><img src="../figures/bogo_dfp.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction](#2.1)
* [2.2 Reference Model Requirements](#2.2)
  * [2.2.1 Cloud Infrastructure Software Profile Capabilities](#2.2.1)
  * [2.2.2 Virtual Network Interface Specifications](#2.2.2)
  * [2.2.3 Cloud Infrastructure Software Profile Requirements](#2.2.3)
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


The tables below contains the requirements from the Reference Model to cover the Basic and Network Intensive profiles. 

To ensure alignment with the infrastructure profile catalogue, the following requirements are referenced through:
- Those relating to Cloud Infrastructure Software Profiles
- Those relating to Cloud Infrastructure Hardware Profiles
- Those relating to Storage Extensions (S extension)
- Those relating to Network Acceleration Extensions (A extension)
- Those relating to Cloud Infrastructure Management

> Note: "(if offered)" used in the Reference Model has been replaced with "Optional" in the tables below so as to align with the RFC2119.

<a name="2.2.1"></a>
### 2.2.1 Cloud Infrastructure Software Profile Capabilities (source [RM 4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping))

| Reference  | Description | Requirement for Basic Profile | Requirement for Network Intensive Profile| Specification Reference |
|---|---|---|---|---|
| e.cap.001 | Max number of vCPU that can be assigned to a single VM by the Cloud Infrastructure | At least 16 <sup>(1)</sup> | At least 16 <sup>(1)</sup> | |
| e.cap.002 | Max memory in MB that can be assigned to a single VM by the Cloud Infrastructure | at least 32 GB<sup>(1)</sup> | at least 32 GB<sup>(1)</sup> | |
| e.cap.003 | Max storage in GB that can be assigned to a single VM by the Cloud Infrastructure | at least 320 GB<sup>(1)</sup> | at least 320 GB<sup>(1)</sup> | |
| e.cap.004 | Max number of connection points that can be assigned to a single VM by the Cloud Infrastructure | 6 | 6 | |
| e.cap.005 | Max storage in GB that can be attached / mounted to VM by the Cloud Infrastructure | Up to 16TB<sup>(2)</sup> | Up to 16TB<sup>(2)</sup> | |
| e.cap.006 | CPU pinning support | Not required | Must support | |
| e.cap.007 | NUMA support | Not required | Must support | |
| e.cap.008 | IPSec Acceleration using the virtio-ipsec interface | Not required | Optional | |
| e.cap.009 | Crypto Acceleration using the virtio-crypto interface | Not required | Optional | |
| e.cap.010 | Transcoding Acceleration | Not required | Not required | |
| e.cap.011 | Programmable Acceleration | Not required | Not required | |
| e.cap.012 | Enhanced Cache Management: L=Lean; E=Equal; X=eXpanded | E | E | |
| e.cap.013 | SR-IOV over PCI-PT | Not required | Must support | |
| e.cap.014 | Hardware coprocessor support (GPU/NPU) | Not required | Not required | |
| e.cap.015 | SmartNICs | Not required | Optional | |
| e.cap.016 | FPGA/other Acceleration H/W | Not required | Optional | |
| *e.cap.017* | *Ability to monitor L2-L7 data from workload* | n/a | n/a | |
| i.cap.014 | Indicates the number of CPU cores consumed by the Cloud Infrastructure on the compute nodes | 2 | 2 | |
| i.cap.015 | Indicates the memory consumed by Cloud Infrastructure on the compute nodes | 16 GB | 16GB | |
| i.cap.016 | Number of virtual cores per physical core; also known as CPU overbooking ratio that is required | 1:1 | 1:1 | |
| i.cap.017 | QoS enablement of the connection point (vNIC or interface)| Not required | Must support | |
| i.cap.018 | Support for huge pages | Not required | Must support | |
| i.pm.001  | Monitor compute node CPU usage, per nanosecond | Must support | Must support | |
| i.pm.002  | Monitor VM CPU usage, per nanosecond | Must support | Must support | |
| i.pm.003  | Monitor compute node CPU utilisation (%) | Must support | Must support | |
| i.pm.004  | Monitor VM CPU utilisation | Must support | Must support | |
| i.pm.005  | Measure external storage IOPs | Must support | Must support | |
| i.pm.006  | Measure external storage throughput | Must support | Must support | |
| i.pm.007  | Measure external storage capacity | Must support | Must support | |

<p align="center"><b>Table 2-1:</b> Reference Model Requirements: Cloud Infrastructure Software Profile Capabilities</p>

**(1)** Defined in the `.4xlarge` flavour in section [4.2.1.1 Predefined Compute Flavours](../../../ref_model/chapters/chapter04.md#4211-predefined-compute-flavours)<br>
**(2)** Defined in the `.bronze` configuration in section [4.2.3 Storage Extensions](../../../ref_model/chapters/chapter04.md#423-storage-extensions)<br>


<a name="2.2.2"></a>
### 2.2.2 Virtual Network Interface Specifications (source [RM 4.2.2](../../../ref_model/chapters/chapter04.md#422-virtual-network-interface-specifications))

The required number of connection points to a VM is described in `e.cap.004` above.  This section describes the required bandwidth of those connection points.

| Reference  | Description | Requirement for Basic Profile | Requirement for Network Intensive Profile| Specification Reference |
|---|---|---|---|---|
| n1, n2, n3, n4, n5, n6	| 1, 2, 3, 4, 5, 6 Gbps | Must support | Must support | |
| nn10, n20, n30, n40, n50, n60	| 10, 20, 30, 40, 50, 60 Gbps | Must support | Must support | |
| n25, n50, n75, n100, n125, n150	| 25, 50, 75, 100, 125, 150 Gbps | Must support | Must support | |
| nn50, n100, n150, n200, n250, n300	| 50, 100, 150, 200, 250, 300 Gbps | Must support | Must support | |
| n100, n200, n300, n400, n500, n600	| 100, 200, 300, 400, 500, 600 Gbps | Must support | Must support | |2.2](../../../ref_model/chapters/chapter04.md#422-virtual-network-interface-specifications) | n1, n2, n3, n4, n5, n6	| 1, 2, 3, 4, 5, 6 Gbps | Must support | Must support | |


<p align="center"><b>Table 2-2:</b> Reference Model Requirements: Network Interface Specifications</p>

<a name="2.2.3"></a>
### 2.2.3 Cloud Infrastructure Software Profile Requirements (source [RM 5.2](../../../ref_model/chapters/chapter05.md#5.2))

| Reference  | Description | Requirement for Basic Profile | Requirement for Network Intensive Profile| Specification Reference |
|---|---|---|---|---|
| infra.com.cfg.001 | CPU allocation ratio | 1:1 | 1:1 | |
| infra.com.cfg.002 | NUMA alignment | Not required | Must support | |
| infra.com.cfg.003 | CPU pinning capability | Not required | Must support | |
| infra.com.cfg.004 | Huge Pages | Not required | Must support | |
| infra.stg.cfg.002 | Storage Block | Must support | Must support | |
| infra.stg.cfg.003 | Storage with replication | Not required | Must support | |
| infra.stg.cfg.004 | Storage with encryption | Must support | Must support | |
| infra.stg.acc.cfg.001 | Storage IOPS oriented | Not required | Must support | |
| infra.stg.acc.cfg.002 | Storage capacity oriented | Not required | Not required | |
| infra.net.cfg.001 | IO virtualisation using virtio1.1 | Must support<sup>(1)</sup> | Must support<sup>(1)</sup>| |
| infra.net.cfg.002 | The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric | Must support VXLAN, MPLSoUDP, GENEVE, other | *No requirement specified* | |
| infra.net.cfg.003 | Network Address Translation | Must support | Must support | |
| infra.net.cfg.004 | Security Groups | Must support | Must support | |
| infra.net.cfg.005 | SFC support | Not required | Must support | |
| infra.net.cfg.006 | Traffic patterns symmetry | Must support | Must support | |
| infra.net.acc.cfg.001 | vSwitch optimisation | Not required | Must support DPDK | |
| infra.net.acc.cfg.002 | Support of HW offload | Not required | Must support SmartNiC | |
| infra.net.acc.cfg.003 | Crypto acceleration | Not required | Must support | |
| infra.net.acc.cfg.004 | Crypto Acceleration Interface | Not required | Must support | |

<p align="center"><b>Table 2-3:</b> Reference Model Requirements: Cloud Infrastructure Software Profile Requirements</p>

**(1)** [Workload Transition Guidelines.](../chapters/appendix-a.md) might have other interfaces (such as SR-IOV VFs to be directly passed to a VM) or NIC-specific drivers on guest machines transiently allowed until more mature solutions are available with an acceptable level of efficiency to support telecom workloads (for example regarding CPU and energy consumption).

<a name="2.2.4"></a>
### 2.2.4 Cloud Infrastructure Hardware Profile Requirements (source [RM 5.4](../../../ref_model/chapters/chapter05.md#5.4))

| Reference  | Description | Requirement for Basic Profile | Requirement for Network Intensive Profile| Specification Reference |
|---|---|---|---|---|
| infra.hw.cpu.cfg.001 | Minimum number of CPU (Sockets) | 2 | 2 | |
| infra.hw.cpu.cfg.002 | Minimum number of Cores per CPU | 20 | 20 | |
| infra.hw.cpu.cfg.003 | NUMA | Not required | Must support | |
| infra.hw.cpu.cfg.004 | Simultaneous Multithreading/Symmetric Multiprocessing (SMT/SMP) | Must support | Must support | |
| infra.hw.cac.cfg.001 | GPU | Not required | Not required | |
| infra.hw.stg.hdd.cfg.001 | Local Storage HDD | *No requirement specified* | *No requirement specified* | |
| infra.hw.stg.ssd.cfg.002 | Local Storage SSD | Should support | Should support | |
| infra.hw.nic.cfg.001 | Total Number of NIC Ports available in the host | 4 | 4 | |
| infra.hw.nic.cfg.002 | Port speed specified in Gbps (minimum values) | 10 | 25 | |
| infra.hw.pci.cfg.001 | Number of PCIe slots available in the host | 8 | 8 | |
| infra.hw.pci.cfg.002 | PCIe speed | Gen 3 | Gen 3 | |
| infra.hw.pci.cfg.003 | PCIe Lanes | 8 | 8 | |
| infra.hw.nac.cfg.001 | Cryptographic Acceleration | Not required | Optional | |
| infra.hw.nac.cfg.002 | SmartNiC used to offload vSwitch functionality to hardware | Not required | Optional | |
| infra.hw.nac.cfg.003 | Compression | *No requirement specified* | *No requirement specified* | |

<!--
These rows are removed and commented out as it's not clear what the requirement is.
| infra.stg.cfg.001 | Catalogue storage Types | | Y |
-->
<p align="center"><b>Table 2-4:</b> Reference Model Requirements: Cloud Infrastructure Hardware Profile Requirements</p>


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

#### 2.2.6.1. System Hardening (source [RM 7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening))

| Ref # | sub-category | Description |  Traceability |
|-------|------|------|-------|
| sec.gen.001 | Hardening | The Platform **must** maintain the specified configuration. | [RA-1 6.3.6 "Security LCM"](./chapter06.md#636-security-lcm)  |
| sec.gen.002 | Hardening | All systems part of Cloud Infrastructure **must** support password hardening as defined in [CIS Password Policy Guide](https://www.cisecurity.org/white-papers/cis-password-policy-guide/). | [RA-1 6.3.2.1 "Password policy"](./chapter06.md#6321-password-policy) |
| sec.gen.003 | Hardening | All servers part of Cloud Infrastructure **must** support a root of trust and secure boot. |  |
| sec.gen.004 | Hardening | The Operating Systems of all the servers part of Cloud Infrastructure **must** be hardened by removing or disabling unnecessary services, applications and network protocols, configuring operating system user authentication, configuring resource controls, installing and configuring additional security controls where needed, and testing the security of the Operating System (NIST SP 800-123). | [RA-1 6.3.2 System Hardening"](./chapter06.md#632-system-hardening) |
| sec.gen.005 | Hardening | The Platform **must** support Operating System level access control. | [RA-1 6.3.2.5 "System Access"](./chapter06.md#6325-system-access) |
| sec.gen.006 | Hardening | The Platform **must** support Secure logging. Logging with root account must be prohibited when root privileges are not required. | [RA-1 6.3.2.5 "System Access"](./chapter06.md#6325-system-access) |
| sec.gen.007 | Hardening | All servers part of Cloud Infrastructure **must** be Time synchronized with authenticated Time service. | [RA-1 6.3.7.6 "Security Logs Time Synchronisation"](./chapter06.md#6376-security-logs-time-synchronisation) |
| sec.gen.008 | Hardening | All servers part of Cloud Infrastructure **must** be regularly updated to address security vulnerabilities. | [RA-1 6.3.2.3 "Patches"](./chapter06.md#6323-patches), [RA-1 6.3.6 "Security LCM"](./chapter06.md#636-security-lcm)  |
| sec.gen.009 | Hardening | The Platform **must** support Software integrity protection and verification. | [RA-1 6.3.3.2 "Integrity of OpenStack components configuration"](./chapter06.md#6332-integrity-of-openstack-components-configuration), [RA-1 6.3.5 "Image Security"](./chapter06.md#635-image-security) |
| sec.gen.010 | Hardening | The Cloud Infrastructure **must** support encrypted storage, for example, block, object and file storage, with access to encryption keys restricted based on a need to know ([Controlled Access Based on the Need to Know](https://www.cisecurity.org/controls/controlled-access-based-on-the-need-to-know/)). | [RA-1 6.3.3.3 "Confidentiality and Integrity of tenant data"](./chapter06.md#6333-confidentiality-and-integrity-of-tenant-data-secmon012-and-secmon013) |
| sec.gen.012 | Hardening | The Operator **must** ensure that only authorized actors have physical access to the underlying infrastructure. | This requirement’s verification goes beyond CNTT testing scope  |
| sec.gen.013 | Hardening | The Platform **must** ensure that only authorized actors have logical access to the underlying infrastructure. | [RA-1 6.3.1.3 "Authorization"](./chapter06.md#6313-authorizationchapter06.md#6325-system-access) |
| sec.gen.015 | Hardening | Any change to the Platform **must** be logged as a security event, and the logged event must include the identity of the entity making the change, the change, the date and the time of the change. | [ RA-1 6.3.7 "Security Audit logging"](./chapter06.md#637-security-audit-logging)|


####  2.2.6.2. Platform and Access (source [RM 7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access))

| Ref # | sub-category | Description |  Traceability |
|-------|-------|-------|---------|
| sec.sys.001 | Access | The Platform **must** support authenticated and secure access to API, GUI and command line interfaces | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |
| sec.sys.002 | Access | The Platform **must** support Traffic Filtering for workloads (for example, Fire Wall). | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |
| sec.sys.003 | Access | The Platform **must** support Secure and encrypted communications in order to ensure the confidentiality and integrity of network traffic. | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access)) |
| sec.sys.004 | Access | The Cloud Infrastructure **must** support authentication, integrity and confidentiality on all network channels. | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |
| sec.sys.005 | Access | The Cloud Infrastructure **must** segregate the underlay and overlay networks. | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |
| sec.sys.006 | Access | The Cloud Infrastructure **must** be able to utilize the Cloud Infrastructure Manager identity lifecycle management capabilities. | [RA-1 6.3.1 "Identity"](./chapter06.md#6311-identity) |
| sec.sys.007 | Access | The Platform **must** implement controls enforcing least privilege use, such as Role-Based Access Control. | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |
| sec.sys.008 | Access | The Platform **must** be able to assign the Entities that comprise the tenant networks to different trust domains. (Communication between different trust domains is not allowed, by default.) | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |  
| sec.sys.009 | Access | The Platform **must** support creation of Trust Relationships between trust domains. These maybe uni-directional relationships where the trusting domain trusts another domain (the “trusted domain”) to authenticate users for them or to allow access to its resources from the trusted domain.  In a bidirectional relationship both domain are “trusting” and “trusted”. | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |
| sec.sys.010 | Access | For two or more domains without existing trust relationships, the Platform **must not** allow the effect of an attack on one domain to impact the other domains either directly or indirectly. | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |
| sec.sys.011 | Access | The Platform **must not** reuse the same authentication credentials (e.g., key pairs) on different Platform components (e.g., different hosts, or different services). | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |
| sec.sys.012 | Access | The Platform **must** protect all secrets by using strong encryption techniques and storing the protected secrets externally from the component (e.g., in OpenStack Barbican) | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |
| sec.sys.013 | Access | The Platform **must** generate secrets dynamically as and when needed. | [RA-1 6.3.1 "Platform Access"](./chapter06.md#631-platform-access) |

#### 2.2.6.3. Confidentiality and Integrity (source [RM7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity))

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.ci.001 | Confidentiality/Integrity | The Platform **must** support Confidentiality and Integrity of data at rest and in transit. | [RA-1 6.3.3 Confidentiality and Integrity](./chapter06.md#633-confidentiality-and-integrity) |
| sec.ci.003 | Confidentiality/Integrity | The Platform **must** support Confidentiality and Integrity of data related metadata. |  [RA-1 6.3.3 Confidentiality and Integrity](./chapter06.md#633-confidentiality-and-integrity) |
| sec.ci.004 | Confidentiality | The Platform **must** support Confidentiality of processes and restrict information sharing with only the process owner (e.g., tenant). |  [RA-1 6.3.3 Confidentiality and Integrity](./chapter06.md#633-confidentiality-and-integrity) |
| sec.ci.005 | Confidentiality/Integrity | The Platform **must** support Confidentiality and Integrity of process-related metadata and restrict information sharing with only the process owner (e.g., tenant). |  [RA-1 6.3.3 Confidentiality and Integrity](./chapter06.md#633-confidentiality-and-integrity) |
| sec.ci.006 | Confidentiality/Integrity | The Platform **must** support Confidentiality and Integrity of workload resource utilization (RAM, CPU, Storage, Network I/O, cache, hardware offload) and restrict information sharing with only the workload owner (e.g., tenant). |  [RA-1 6.3.3 Confidentiality and Integrity](./chapter06.md#633-confidentiality-and-integrity) |
| sec.ci.007 | Confidentiality/Integrity | The Platform **must not** allow Memory Inspection by any actor other than the authorized actors for the Entity to which Memory is assigned (e.g., tenants owning the workload), for Lawful Inspection, and for secure monitoring services. Administrative access must be managed using Platform Identity Lifecycle Management.  |  [RA-1 6.3.3 Confidentiality and Integrity](./chapter06.md#633-confidentiality-and-integrity) |
| sec.ci.008 | Confidentiality | The Cloud Infrastructure **must** support tenant networks segregation. | [RA-1 6.3.3 Confidentiality and Integrity](./chapter06.md#633-confidentiality-and-integrity) |


#### 2.2.6.4. Workload Security (source [RM7.11.4](../../../ref_model/chapters/chapter07.md#7114-workload-security))

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.wl.001 | Workload | The Platform **must** support Workload placement policy. | [RA-1 6.3.4 Workload Security](./chapter06.md#634-workload-security) |
| sec.wl.002 | Workload | The Platform **must** support operational security | [RA-1 6.3.4 Workload Security](./chapter06.md#634-workload-security) |
| sec.wl.003 | Workload | The Platform **must** support secure provisioning of Workloads. | [RA-1 6.3.4 Workload Security](./chapter06.md#634-workload-security) |
| sec.wl.004 | Workload | The Platform **must** support Location assertion (for mandated in-country or location requirements). | [RA-1 6.3.4 Workload Security](./chapter06.md#634-workload-security) |
| sec.wl.005 | Workload | The Platform **must** support the separation of production and non-production Workloads. | [RA-1 6.3.4 Workload Security](./chapter06.md#634-workload-security) |
| sec.wl.006 | Workload | The Platform **must** support the separation of Workloads based on their categorisation (for example, payment card information, healthcare, etc.) | [RA-1 6.3.4 Workload Security](./chapter06.md#634-workload-security) |



#### 2.2.6.5. Image Security (source [RM7.11.5](../../../ref_model/chapters/chapter07.md#7115-image-security))

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.img.001 | Image | Images from untrusted sources **must not** be used. | [RA-1 6.3.5 "Image Security"](./chapter06.md#635-image-security) |
| sec.img.002 | Image | Images **must** be maintained to be free from known vulnerabilities. | [RA-1 6.3.5 "Image Security"](./chapter06.md#635-image-security) |
| sec.img.003 | Image | Images **must not** be configured to run with privileges higher than the privileges of the actor authorized to run them. |  |
| sec.img.004 | Image | Images **must** only be accessible to authorized actors. | [RA-1 3.2.1. "Multi-Tenancy"](./chapter03.md#321-multi-tenancy-execution-environment) |
| sec.img.005 | Image | Image Registries **must** only be accessible to authorized actors. | [RA-1 6.3.1.1 "Identity Security"](./chapter06.md#6311-identity-securitychapter06.md#633-confidentiality-and-integrity) |
| sec.img.006 | Image | Image Registries **must** only be accessible over networks that enforce authentication, integrity and confidentiality. | [RA-1 6.3.3.1 "Confidentiality and Integrity of communications"](./chapter06.md#6331-confidentiality-and-integrity-of-communications) |
| sec.img.007 | Image | Image registries **must** be clear of vulnerable and out of date versions. | [RA-1 6.3.3.2 "Confidentiality and Integrity of communications"](./chapter06.md#6332-integrity-of-openstack-components-configuration), [RA-1 6.3.5 "Image Security"](./chapter06.md#635-image-security)  |


#### 2.2.6.6. Security LCM (source [RM7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm))

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.lcm.001 | LCM | The Platform **must** support Secure Provisioning, Availability, and Deprovisioning (Secure Clean-Up) of workload resources where Secure Clean-Up includes tear-down, defense against virus or other attacks. | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |  
| sec.lcm.002 | LCM | Operational **must** use management protocols limiting security risk such as SNMPv3, SSH v2, ICMP, NTP, syslog and TLS v1.2 or higher. | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |
| sec.lcm.003 | LCM | The Cloud Operator **must** implement and strictly follow change management processes for Cloud Infrastructure, Cloud Infrastructure Manager and other components of the cloud, and Platform change control on hardware. | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |  
| sec.lcm.005 | LCM | Platform **must** provide logs and these logs must be monitored for anomalous behavior. | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |
| sec.lcm.006 | LCM | The Platform **must** verify the integrity of all Resource management requests. | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |
| sec.lcm.007 | LCM | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with current time information. | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |
| sec.lcm.008 | LCM | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with relevant DNS information. | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |
| sec.lcm.009 | LCM | The Platform **must** be able to update the tag of newly instantiated, suspended, hibernated, migrated and restarted images with relevant geolocation (geographical) information. | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |
| sec.lcm.010 | LCM | The Platform **must** log all changes to geolocation along with the mechanisms and sources of location information (i.e. GPS, IP block, and timing). | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |
| sec.lcm.011 | LCM | The Platform **must** implement Security life cycle management processes including the proactive update and patching of all deployed Cloud Infrastructure software. | [RA-1 6.3.7 Security Audit Logging](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter06.md#637-security-audit-logging) |


#### 2.2.6.7. Monitoring and Security Audit (source [RM7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit))

The Platform is assumed to provide configurable alerting and notification capability and the operator is assumed to have automated systems, policies and procedures to act on alerts and notifications in a timely fashion. In the following the monitoring and logging capabilities can trigger alerts and notifications for appropriate action.

| Ref # | sub-category | Description |  Traceability |
|---|----|---|----|
| sec.mon.001 | Monitoring/Audit | Platform **must** provide logs and these logs must be regularly monitored for events of interest. | [RA-1 6.3.7.1 "Creating logs"](./chapter06.md#6371-creating-logs) |
| sec.mon.002 | Monitoring | Security logs **must** be time synchronised. | [RA-1 6.3.7.5 "Security Logs Time Synchronisation"](./chapter06.md#6376-security-logs-time-synchronisation) |
| sec.mon.003 | Monitoring | The Platform **must** log all changes to time server source, time, date and time zones. |  |
| sec.mon.004 | Audit | The Platform **must** secure and protect Audit logs (containing sensitive information) both in-transit and at rest. |  |
| sec.mon.005 | Monitoring/Audit | The Platform **must** Monitor and Audit various behaviours of connection and login attempts to detect access attacks and potential access attempts and take corrective actions accordingly | [RA-1 6.3.7.2 "What to log, what not to log"](./chapter06.md#6372-what-to-log--what-not-to-log) |
| sec.mon.006 | Monitoring/Audit | The Platform **must** Monitor and Audit operations by authorized account access after login to detect malicious operational activity and take corrective actions. | [RA-1 6.3.3.2 "Integrity of OpenStack components configuration"](./chapter06.md#6332-integrity-of-openstack-components-configuration), [RA-1 6.3.7 "Security Audit Logging"](./chapter06.md#637-security-audit-logging) |
| sec.mon.007 | Monitoring/Audit | The Platform **must** Monitor and Audit security parameter configurations for compliance with defined security policies. | [RA-1 6.3.3.2 "Integrity of OpenStack components configuration"](./chapter06.md#6332-integrity-of-openstack-components-configuration) |
| sec.mon.008 | Monitoring/Audit | The Platform **must** Monitor and Audit externally exposed interfaces for illegal access (attacks) and take corrective security hardening measures. | [RA-1 6.3.3.1 "Confidentiality and Integrity of communications"](./chapter06.md#6331-confidentiality-and-integrity-of-communications) |
| sec.mon.009 | Monitoring/Audit | The Platform **must** Monitor and Audit service for various attacks (malformed messages, signalling flooding and replaying, etc.) and take corrective actions accordingly. |  |
| sec.mon.010 | Monitoring/Audit | The Platform **must** Monitor and Audit running processes to detect unexpected or unauthorized processes and take corrective actions accordingly. |  |
| sec.mon.011 | Monitoring/Audit | The Platform **must** Monitor and Audit logs from infrastructure elements and workloads to detected anomalies in the system components and take corrective actions accordingly. | [RA-1 6.3.7.1 "Creating logs"](./chapter06.md#6371-creating-logs) |
| sec.mon.012 | Monitoring/Audit | The Platform **must** Monitor and Audit Traffic patterns and volumes to prevent malware download attempts. |  |
| sec.mon.013 | Monitoring | The monitoring system **must not** affect the security (integrity and confidentiality) of the infrastructure, workloads, or the user data (through back door entries). |  |
| sec.mon.015 | Monitoring | The Platform **must** ensure that the Monitoring systems are never starved of resources. |  |
| sec.lcm.017 | Audit | The Platform **must** Audit systems for any missing security patches and take appropriate actions. | [RA-1 6.3.2.3 "Patches"](./chapter06.md#6323-patches) |


#### 2.2.6.8. Compliance with Standards (source [RM7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards))

| Ref # | sub-category | Description |  Traceability |
|---------|---------------|----------------|------------|
| sec.std.018 | Standards | The Public Cloud Operator **must**, and the Private Cloud Operator **may** be certified to be compliant with the International Standard on Awareness Engagements (ISAE) 3402 (in the US: SSAE 16); International Standard on Awareness Engagements (ISAE) 3402. US Equivalent: SSAE16. | |


<p align="center"><b>Table 2-6:</b> Reference Model Requirements: Cloud Infrastructure Security Requirements</p>


<a name="2.3"></a>
## 2.3 Architecture and OpenStack Requirements

"Architecture" in this chapter refers to Cloud infrastructure (referred to as NFVI by ETSI) + VIM (as specified in Reference Model Chapter 3).

<a name="2.3.1"></a>
### 2.3.1 General Requirements

| Ref # | sub-category | Description | Traceability |
|----|---------------|---------------------|---------------|
| `req.gen.ost.01` | Open source | The Architecture **must** use OpenStack APIs.| [RA-1 5.3](./chapter05.md#5.3) |
| `req.gen.ost.02` | Open source | The Architecture **must** support dynamic request and configuration of virtual resources (compute, network, storage) through OpenStack APIs. | [RA-1 5.3](./chapter05.md#53-consolidated-set-of-apis) |
| `req.gen.rsl.01` | Resiliency | The Architecture **must** support resilient OpenStack components that are required for the continued availability of running workloads. | |
| `req.gen.avl.01` | Availability | The Architecture **must** provide High Availability for OpenStack components. | [RA-1 4.2 "Underlying Resources"](./chapter04.md#42-underlying-resources) |


<p align="center"><b>Table 2-7:</b> General Requirements</p>

<a name="2.3.2"></a>
### 2.3.2 Infrastructure Requirements

| Ref # | sub-category | Description |  Traceability |
|----|--------------|---------------------|-----------|
| `req.inf.com.01` | Compute | The Architecture **must** provide compute resources for VM instances. | [RA-1 3.3.1.4 "Cloud Workload Services"](./chapter03.md#3314-cloud-workload-services) |
| `req.inf.com.04` | Compute | The Architecture **must** be able to support multiple CPU SKU options to support various infrastructure profiles (Basic and Network Intensive<!-- , and Compute Intensive -->).| [RA-1 4.4.1. "Support for Profiles and T-shirt instance types"](./chapter04.md#441-support-for-profiles-and-t-shirt-instance-types) |
| `req.inf.com.05` | Compute | The Architecture **must** support Hardware Platforms with NUMA capabilities.| [RA-1 4.4.1. "Support for Profiles and T-shirt instance types"](./chapter04.md#441-support-for-profiles-and-t-shirt-instance-types) |
| `req.inf.com.06` | Compute | The Architecture **must** support CPU Pinning of the vCPUs of VM instance.| [RA-1 4.4.1. "Support for Profiles and T-shirt instance types"](./chapter04.md#441-support-for-profiles-and-t-shirt-instance-types) |
| `req.inf.com.07` | Compute | The Architecture **must** support different hardware configurations to support various infrastructure profiles (Basic and Network Intensive<!-- , and Compute Intensive -->).| [RA-1 3.3.3. "Host aggregates providing resource pooling"](./chapter03.md#333-host-aggregates-providing-resource-pooling) |
| `req.inf.com.08` | Compute | The Architecture **must** support allocating certain number of host cores for all non-tenant workloads such as for OpenStack services. SMT threads can be allocated to individual OpenStack services or their components. | [Dedicating host cores to certain workloads (e.g., OpenStack services)](https://docs.openstack.org/nova/latest/configuration/config.html#compute.cpu_dedicated_set). Please see example, ["Configuring libvirt compute nodes for CPU pinning"](https://docs.openstack.org/nova/latest/admin/cpu-topologies.html) |
| `req.inf.com.09` | Compute | The Architecture **must** ensure that the host cores assigned to non-tenant and tenant workloads are SMT aware: that is, a host core and its associated SMT threads are either all assigned to non-tenant workloads or all assigned to tenant workloads. | Achieved through configuring the "cpu_dedicated_set" and "cpu_shared_set" parameters in nova.conf correctly. |
| `req.inf.stg.01` | Storage | The Architecture **must** provide remote (not directly attached to the host) Block storage for VM Instances. | [RA-1 3.4.2.3. "Storage"](./chapter03.md#3423-storage) |
| `req.inf.stg.02` | Storage | The Architecture **must** provide Object storage for VM Instances. Operators **may** choose not to implement Object Storage but must be cognizant of the risk of "Compliant VNFs" failing in their environment. | OpenStack Swift Service ([RA-1 4.3.1.4 "Swift"](./chapter04.md#4314-swift)) |
| `req.inf.ntw.01` | Network | The Architecture **must** provide virtual network interfaces to VM instances. | [RA-1 5.2.5. "Neutron" ](./chapter05.md#525-neutron) |
| `req.inf.ntw.02` | Network | The Architecture **must** include capabilities for integrating SDN controllers to support provisioning of network services, from the OpenStack Neutron service, such as networking of VTEPs to the Border Edge based VRFs. | [RA-1 3.2.5. "Virtual Networking – 3rd party SDN solution"](./chapter03.md#325-virtual-networking--3rd-party-sdn-solution) |
| `req.inf.ntw.03` | Network | The Architecture **must** support low latency and high throughput traffic needs. | [RA-1 4.2.3. "Network Fabric"](./chapter04.md#423-network-fabric) |
| `req.inf.ntw.05` | Network | The Architecture **must** allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay such as VXLAN or Geneve). | [RA-1 4.2.3. "Network Fabric"](./chapter04.md#423-network-fabric) |
| `req.inf.ntw.07` | Network | The Architecture **must** support network resiliency. | [RA-1 3.4.2.2. "Network"](./chapter03.md#3422-network) |
| `req.inf.ntw.10` | Network | The Cloud Infrastructure Network Fabric **must** be capable of enabling highly available (Five 9’s or better) Cloud Infrastructure. | [RA-1 3.4.2.2. "Network"](./chapter03.md#3422-network) |
| `req.inf.ntw.15` | Network | The Architecture **must** support multiple networking options for Cloud Infrastructure to support various infrastructure profiles (Basic and Network Intensive<!-- , and Compute Intensive -->).| [RA-1 4.2.3.4. "Neutron ML2-plugin Integration"](./chapter04.md#4234-neutron-ml2-integration) and ["OpenStack Neutron Plugins"](https://wiki.openstack.org/wiki/Neutron_Plugins_and_Drivers) |
| `req.inf.ntw.16` | Network | The Architecture **must** support dual stack IPv4 and IPv6 for tenant networks and workloads.| |


<p align="center"><b>Table 2-8:</b> Infrastructure Requirements</p>

<a name="2.3.3"></a>
### 2.3.3 VIM Requirements

| Ref # | sub-category | Description |  Traceability |
|----|----------------|----------------------|-----------|
| `req.vim.01` | General | The Architecture **must** allow infrastructure resource sharing. | [RA-1 3.2. "Consumable Infrastructure Resources and Services"](./chapter03.md#32-consumable-infrastructure-resources-and-services) |
| `req.vim.03` | General | The Architecture **must** allow VIM to discover and manage Cloud Infrastructure resources. | [RA-1 5.2.7. "Placement"](./chapter05.md#527-placement) |
| `req.vim.05` | General | The Architecture **must** include image repository management. | [RA-1 4.3.1.2. "Glance"](./chapter04.md#4312-glance) |
| `req.vim.07` | General | The Architecture **must** support multi-tenancy. | [RA-1 3.2.1. "Multi-Tenancy"](./chapter03.md#321-multi-tenancy-execution-environment) |
| `req.vim.08` | General | The Architecture **must** support resource tagging. | ["OpenStack Resource Tags"](https://specs.openstack.org/openstack/api-wg/guidelines/tags.html) |

<p align="center"><b>Table 2-9:</b> VIM Requirements</p>


<a name="2.3.4"></a>
### 2.3.4 Interfaces & APIs Requirements

| Ref # | sub-category | Description |  Traceability |
|----|----------|--------------------|------------|
| `req.int.api.01` | API | The Architecture **must** provide APIs to access to the authentication service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.1 "Keystone"](./chapter05.md#521-keystone) |
| `req.int.api.02` | API | The Architecture **must** provide APIs to access to the image management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.2 "Glance"](./chapter05.md#522-glance) |
| `req.int.api.03` | API | The Architecture **must** provide APIs to access to the block storage management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.3 "Cinder"](./chapter05.md#523-cinder) |
| `req.int.api.04` | API | The Architecture **must** provide APIs to access to the object storage management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.4 "Swift"](./chapter05.md#524-swift) |
| `req.int.api.05` | API | The Architecture **must** provide APIs to access to the network management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.5 "Neutron"](./chapter05.md#525-neutron) |
| `req.int.api.06` | API | The Architecture **must** provide APIs to access to the compute resources management service and the associated mandatory features detailed in chapter 5. | [RA-1 5.2.6 "Nova"](./chapter05.md#526-nova) |
| `req.int.api.07` | API | The Architecture **must** provide GUI access to tenant facing cloud platform core services. | [RA-1 4.3.1.9 "Horizon"](./chapter04.md#4319-horizon) |
| `req.int.api.08` | API | The Architecture **must** provide APIs needed to discover and manage Cloud Infrastructure resources. | [RA-1 5.2.7. "Placement"](./chapter05.md#527-placement) |
| `req.int.api.09` | API | The Architecture **must** provide APIs to access to the orchestration service. | [RA-1 5.2.8 "Heat"](./chapter05.md#528-heat) |
| `req.int.api.10` | API | The Architecture must expose the latest version and microversion of the APIs for the given CNTT OpenStack release for each of the OpenStack core services. | [RA-1 5.2 Core OpenStack Services APIs](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter05.md#52-core-openstack-services-apis) |


<p align="center"><b>Table 2-10:</b> Interfaces and APIs Requirements</p>

<a name="2.3.5"></a>
### 2.3.5 Tenant Requirements

| Ref # | sub-category | Description |  Traceability |
|----|--------------|---------------|-----------------|
| `req.tnt.gen.01` | General | The Architecture **must** support multi-tenancy. |  **duplicate of req.vim.07** |
| `req.tnt.gen.02` | General | The Architecture **must** support self-service dashboard (GUI) and APIs for users to deploy, configure and manage their workloads. | [RA-1 4.3.1.9 "Horizon"](./chapter04.md#4319-horizon) and [3.3.1.4 Cloud Workload Services](./chapter03.md#3314-cloud-workload-services) |

<p align="center"><b>Table 2-11:</b> Tenant Requirements</p>

<a name="2.3.6"></a>

### 2.3.6 Operations and LCM

| Ref # | sub-category | Description |  Traceability |
|----|----------|-------------|-------------|
| `req.lcm.gen.01`	| General | The Architecture **must** support zero downtime expansion/change of physical capacity (compute hosts, storage increase/replacement). | |
| `req.lcm.adp.02` | Automated deployment | The Architecture **must** support hitless upgrades of software provided by the cloud provider so that the availability of running workloads is not impacted. | |

<p align="center"><b>Table 2-12:</b> LCM Requirements</p>

<a name="2.3.7"></a>
### 2.3.7 Assurance Requirements

| Ref # | sub-category | Description |  Traceability |
|----|--------|-------------------|----------|
| `req.asr.mon.01` | Integration | The Architecture **must** include integration with various infrastructure components to support collection of telemetry for assurance monitoring and network intelligence. | |
| `req.asr.mon.03` | Monitoring | The Architecture **must** allow for the collection and dissemination of performance and fault information. | |
| `req.asr.mon.04` | Network | The Cloud Infrastructure Network Fabric and Network Operating System **must** provide network operational visibility through alarming and streaming telemetry services for operational management, engineering planning, troubleshooting, and network performance optimisation. | |

<p align="center"><b>Table 2-13:</b> Assurance Requirements</p>



<a name="2.4"></a>
### 2.4 Architecture and OpenStack Recommendations

The requirements listed in this section are optional, and are not required in order to be deemed a conformant implementation.

<a name="2.4.1"></a>
### 2.4.1 General Recommendations

| Ref # | sub-category | Description |  Notes |
|----|-------|---------------------|-------------|
| `req.gen.cnt.01` | Cloud nativeness | The Architecture **should** consist of stateless service components. However, where state is required it must be kept external to the component. | OpenStack consists of both stateless and stateful services where the stateful services utilize a database. For latter see "[Configuring the stateful services](https://docs.openstack.org/ha-guide/control-plane-stateful.html)"|
| `req.gen.cnt.02` | Cloud nativeness | The Architecture **should** consist of service components implemented as microservices that are individually dynamically scalable. | |
| `req.gen.scl.01` | Scalability | The Architecture **should** support policy driven auto-scaling. | This requirement is currently not addressed but will likely be supported through [Senlin](https://docs.openstack.org/senlin/train/), cluster management service. |
| `req.gen.rsl.02` | Resiliency | The Architecture **should** support resilient OpenStack service components that are not subject to `req.gen.rsl.01`. | |

<p align="center"><b>Table 2-14:</b> General Recommendations</p>


<a name="2.4.2"></a>
### 2.4.2 Infrastructure Recommendations

| Ref # | sub-category | Description |  Notes |
|----|-------|---------------------|-------------|
| `req.inf.com.02` | Compute | The Architecture **should** include industry standard hardware management systems at both HW device level (embedded) and HW platform level (external to device). | |
| `req.inf.com.03` | Compute | The Architecture **should** support Symmetric Multiprocessing with shared memory access as well as Simultaneous Multithreading. | |
| `req.inf.stg.08` | Storage | The Architecture **should** allow use of externally provided large archival storage for its Backup / Restore / Archival needs. | |
| `req.inf.stg.09` | Storage | The Architecture **should** make available all non-host OS / Hypervisor / Host systems storage as network-based Block, File or Object Storage for tenant/management consumption. | |
| `req.inf.stg.10` | Storage | The Architecture **should** provide local Block storage for VM Instances. | [RA-1 "Virtual Storage"](./chapter03.md#323-virtual-storage) |
| `req.inf.ntw.04` | Network | The Architecture **should** support service function chaining. |  |
| `req.inf.ntw.06` | Network | The Architecture **should** support Distributed Virtual Routing (DVR) to allow compute nodes to route traffic efficiently. | |
| `req.inf.ntw.08` | Network | The Cloud Infrastructure Network Fabric **should** embrace the concepts of open networking and disaggregation using commodity networking hardware and disaggregated Network Operating Systems. | |
| `req.inf.ntw.09` | Network | The Cloud Infrastructure Network Fabric **should** embrace open-based standards and technologies. | |
| `req.inf.ntw.11` | Network | The Cloud Infrastructure Network Fabric **should** be architected to provide a standardised, scalable, and repeatable deployment model across all applicable Cloud Infrastructure sites. | |

<!---
Commented out until RM defines requirements for SDN
| `req.inf.ntw.12` | Network | The SDN solution **should** be configurable via orchestration or VIM systems in an automated manner using openly published API definitions. | |
| `req.inf.ntw.13` | Network | The SDN solution **should** be able to support federated networks. | |
| `req.inf.ntw.14` | Network | The SDN solution **should** be able to be centrally administrated and configured. | |
-->
| `req.inf.ntw.17` | Network | The Architecture **should** use dual stack IPv4 and IPv6 for Cloud Infrastructure internal networks.| |
|----|-------|---------------------|-------------|
| `req.inf.acc.01` | Acceleration | The Architecture **should** support Application Specific Acceleration (exposed to VNFs). | [RA-1 3.2.6. "Acceleration"](./chapter03.md#326-acceleration) |
| `req.inf.acc.02` | Acceleration | The Architecture **should** support Cloud Infrastructure Acceleration (such as SmartNICs). | ["OpenStack Future - Specs defined"](https://specs.openstack.org/openstack/neutron-specs/specs/stein/neutron-ovs-agent-support-baremetal-with-smart-nic.html) |
| `req.inf.acc.03` | Acceleration | The Architecture **should not** rely on SR-IOV PCI-Pass through to provide acceleration to VNFs. | |
| `req.inf.img.01` | Image | The Architecture **should** make the immutable images available via location independent means. | [RA-1 4.3.1.2. "Glance"](./chapter04.md#4312-glance) |
<!--
| `req.inf.stg.11` | Storage | The Architecture **should** support the Block storage capabilities specified in https://docs.openstack.org/api-ref/block-storage/. | [RA-1 5.2.3. "Cinder"](./chapter05.md#523-cinder) |
| `req.inf.ntw.18` | Network | The Architecture **should** support the network extensions specified in https://docs.openstack.org/api-ref/network/v2/.| [RA-1 5.2.5. "Neutron"](./chapter05.md#525-neutron) |
-->

<p align="center"><b>Table 2-15:</b> Infrastructure Recommendations</p>


<a name="2.4.3"></a>
### 2.4.3 VIM Recommendations

| Ref # | sub-category | Description |  Notes |
|----|----------------|----------------------|-----------|
| `req.vim.02` | General | The Architecture **should** support deployment of OpenStack components in containers. | [RA-1 4.3.2. "Containerised OpenStack Services"](./chapter04.md#432-containerised-openstack-services) |
| `req.vim.04` | General | The Architecture **should** support Enhanced Platform Awareness (EPA) only for discovery of infrastructure resource capabilities.| |
| `req.vim.06` | General | The Architecture **should** allow orchestration solutions to be integrated with VIM. |  |
| `req.vim.09` | General | The Architecture **should** support horizontal scaling of OpenStack core services. |  |

<p align="center"><b>Table 2-16:</b> VIM Recommendations</p>


<a name="2.4.4"></a>
### 2.4.4 Interfaces and APIs Recommendations

| Ref # | sub-category | Description |  Notes |
|----|-------|---------------------|-------------|
| `req.int.acc.01` | Acceleration | The Architecture **should** provide an open and standard acceleration interface to VNFs. |  |
| `req.int.acc.02` | Acceleration | The Architecture **should not** rely on SR-IOV PCI-Pass through for acceleration interface exposed to VNFs. | duplicate of `req.inf.acc.03` under "Infrastructure Recommendations" |

<p align="center"><b>Table 2-17:</b> Interfaces and APIs Recommendations</p>


<a name="2.4.5"></a>
### 2.4.5 Tenant Recommendations

| Ref # | sub-category | Description |  Notes |
|----|-------|---------------------|-------------|

<p align="center"><b>Table 2-18:</b> Tenant Recommendations</p>


<a name="2.4.6"></a>
### 2.4.6 Operations and LCM Recommendations

| Ref # | sub-category | Description |  Notes |
|----|----------|-------------|-------------|
| `req.lcm.adp.01` | Automated deployment | The Architecture **should** allow for “cookie cutter” automated deployment, configuration, provisioning and management of multiple Cloud Infrastructure sites. | |
| `req.lcm.adp.03` | Automated deployment | The Architecture **should** support hitless upgrade of all software provided by the cloud provider that are not covered by `req.lcm.adp.02`. Whenever hitless upgrades are not feasible, attempt should be made to minimize the duration and nature of impact. | |
| `req.lcm.adp.04` | Automated deployment | The Architecture **should** support declarative specifications of hardware and software assets for automated deployment, configuration, maintenance and management. | |
| `req.lcm.adp.05` | Automated deployment | The Architecture **should** support automated process for Deployment and life-cycle management of VIM Instances. | |
| `req.lcm.cid.02` | CI/CD | The Architecture **should** support integrating with CI/CD Toolchain for Cloud Infrastructure and VIM components Automation. | |

<p align="center"><b>Table 2-19:</b> LCM Recommendations</p>


<a name="2.4.7"></a>
### 2.4.7 Assurance Recommendations

| Ref # | sub-category | Description |  Notes |
|----|--------|-------------------|----------|
| `req.asr.mon.02` | Monitoring | The Architecture **should** support Network Intelligence capabilities that allow richer diagnostic capabilities which take as input broader set of data across the network and from VNF workloads. | |


<p align="center"><b>Table 2-20:</b> Assurance Recommendations</p>


<a name="2.4.8"></a>
### 2.4.8 Security Recommendations


#### 2.4.8.1. System Hardening (source [RM 7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening))

| Ref # | sub-category | Description |  Notes |
|-------|------|------|-------|
| sec.gen.011 | Hardening | The Cloud Infrastructure **should** support Read and Write only storage partitions (write only permission to one or more authorized actors). |  |
| sec.gen.014 | Hardening | All servers part of Cloud Infrastructure **should** support measured boot and an attestation server that monitors the measurements of the servers. |  |


####  2.4.8.2. Platform and Access (source [RM 7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access))

| Ref # | sub-category | Description |  Notes |
|-------|-------|-------|---------|


#### 2.4.8.3. Confidentiality and Integrity (source [RM7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity))

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.ci.002 | Confidentiality/Integrity | The Platform **should** support self-encrypting storage devices |  |


#### 2.4.8.4. Workload Security (source [RM7.11.4](../../../ref_model/chapters/chapter07.md#7114-workload-security))

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.wl.007 | Workload | The Operator **should** implement processes and tools to verify VNF authenticity and integrity. |  |


#### 2.4.8.5. Image Security (source [RM7.11.5](../../../ref_model/chapters/chapter07.md#7115-image-security))

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|



#### 2.4.8.6. Security LCM (source [RM7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm))

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.lcm.004 | LCM | The Cloud Operator **should** support automated templated approved changes; Templated approved changes for automation where available |  |  



#### 2.4.8.7. Monitoring and Security Audit (source [RM7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit))

The Platform is assumed to provide configurable alerting and notification capability and the operator is assumed to have automated systems, policies and procedures to act on alerts and notifications in a timely fashion. In the following the monitoring and logging capabilities can trigger alerts and notifications for appropriate action.

| Ref # | sub-category | Description |  Notes |
|---|----|---|----|
| sec.mon.014 | Monitoring | The Monitoring systems **should** not impact IAAS, PAAS, and SAAS SLAs including availability SLAs |  |
| sec.mon.016 | Monitoring | The Platform Monitoring components **should** follow security best practices for auditing, including secure logging and tracing |  |



#### 2.4.8.8. Compliance with Standards (source [RM7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards))

| Ref # | sub-category | Description |  Notes |
|---------|---------------|----------------|------------|
| sec.std.001 | Standards | The Cloud Operator **should** comply with Center for Internet Security CIS Controls ([https://www.cisecurity.org/](https://www.cisecurity.org/)); Center for Internet Security - [https://www.cisecurity.org/](https://www.cisecurity.org/) | |
| sec.std.002 | Standards | The Cloud Operator, Platform and Workloads **should** follow the guidance in the CSA Security Guidance for Critical Areas of Focus in Cloud Computing (latest version) [https://cloudsecurityalliance.org/](https://cloudsecurityalliance.org/).  Cloud Security Alliance - [https://cloudsecurityalliance.org/](https://cloudsecurityalliance.org/) | |
| sec.std.003 | Standards | The Platform and Workloads **should** follow the guidance in the OWASP Cheat Sheet Series (OCSS) https://github.com/OWASP/CheatSheetSeries. Open Web Application Security Project [https://www.owasp.org](https://www.owasp.org) | |
| sec.std.004 | Standards | The Cloud Operator, Platform and Workloads **should** ensure that their code is not vulnerable to the OWASP Top Ten Security Risks [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/) |  |
| sec.std.005 | Standards | The Cloud Operator, Platform and Workloads **should** strive to improve their maturity on the OWASP Software Maturity Model (SAMM) https://owaspsamm.org/blog/2019/12/20/version2-community-release/ |  |
| sec.std.006  | Standards | The Cloud Operator, Platform and Workloads **should** utilize the OWASP Web Security Testing Guide https://github.com/OWASP/wstg/tree/master/document |  |
| sec.std.013 | Standards | The Cloud Operator, and Platform **should** satisfy the requirements for Information Management Systems specified in ISO/IEC 27001  https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en; ISO/IEC 27002:2013 - ISO/IEC 27001 is the international Standard for best-practice information security management systems (ISMSs) | |
| sec.std.014 | Standards | The Cloud Operator, and Platform **should** implement the Code of practice for Security Controls specified ISO/IEC 27002:2013 (or latest)  https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:en | |
| sec.std.015 | Standards | The Cloud Operator, and Platform **should** implement the ISO/IEC 27032:2012 (or latest) Guidelines for Cybersecurity techniques  https://www.iso.org/obp/ui/#iso:std:iso-iec:27032:ed-1:v1:en; ISO/IEC 27032 - ISO/IEC 27032is the international Standard focusing explicitly on cybersecurity | |
| sec.std.016 | Standards | The Cloud Operator **should** conform to the ISO/IEC 27035 standard for incidence management; ISO/IEC 27035 - ISO/IEC 27035 is the international Standard for incident management | |
| sec.std.017 | Standards | The Cloud Operator **should** conform to the ISO/IEC 27031 standard for business continuity; ISO/IEC 27031 - ISO/IEC 27031 is the international Standard for ICT readiness for business continuity | |

<p align="center"><b>Table 2-21:</b> Security Recommendations</p>

<!--
**Backlog of Req**

1. Manage discovery of resources, resource capabilities/features
1. Manage repository of resources and their allocations
1. Orchestrate (create, update, delete, …) virtual computes, storage, virtual links, networks, subnets and ports
1. Collect and disseminate performance and fault information
1. Provides transparent, fully automated hardware addition, removal, and replacement with zero to minimal service disruption
1. Provides transparent, fully automated software updates, rollback, and post-install configuration changes with zero to minimal service disruption
1. Automated and validated deployment of Enhanced Platform Awareness (EPA) features across multiple nodes
1. Support tenant isolation
1. Policy driven auto-scaling
1. Image management and provisioning control
1. Policy based RBAC
1. Tenant based (a user may have different access rights in different tenants)
1. **Q:** do site administrators have access to Tenant space and what are their rights (public cloud?)
1. Policy based security
1. Policy driven performance and fault management
1. Principles should apply to all reference architectures we design and develop
1. Traceability between reference model to reference architecture (and vice versa)
1. Implementable and usable for VNF developer community, i.e. with enough specificity to support the design and development of a VNF
1. Define the NFVI so that developers can understand how to build VNFs
1. Design the architectures with common elements so that the VNFs require less operator specific customizations
1. Rationalize need for each discrete architecture
    1. Intention is to minimize the number of discrete reference architectures
1. Architectures should be:
    1. Resilient
    1. Scalable
    1. Elastic
    1. Secure
    1. Low Latency
    1. Resource and Operational Efficiency
    1. E2E Lifecycle Automation (Deployment, Operations, & Maintenance)
    1. High-Availability
1. Prioritize incorporation of open source components
    1. Design architectures to established open standards as much as possible
1. Architectures will evolve over time
1. Mandatory Core services:
    1. Neutron (networking)
    1. Nova (compute)
    1. Cinder (block storage)
    1. Keystone (authentication/authorisation)
    1. Glance (image repository)
    1. Heat (orchestration)

1. Optional Core Services:
    1. Swift (object storage)
    1. Ceilometer / Panko / Aodh (workload monitoring / autoscaling)
    1. Ironic (baremetal)
      … the list could get quite long so perhaps we tier these requirements…
1. Compute:
    1. The hypervisor should be KVM with EMU (we can be prescriptive here as it makes certification simpler)
    1. We could state that we don’t want SR-IOV but any network acceleration should be based on DP-DK or SmartNIC.
    1. I don’t want to be prescriptive over CPU pinning or NUMA but we can discuss.
1. Network:
    1. Load balancing – should we base this on Octavia or do we need a plug-in like AVI / F5?
    1. OpenVSwitch?
    1. Geneve/VXLAN tunnelling?
    1. IPv6… when?

1. Tagging:
    1. We may want to define a standard for tagging resources.

1. Logging, Monitoring, Alerting of the Cloud should ensure any failures in the control plane are either self-healed or alerted on and ideally some sort of centralised log file analysis should be possible without needing to trawl local log files.    Logging in the tenant space is left to the application.
1. Backup of the control plane configuration (keystone DB, other DB, policy.json’s) to a remote object store.

-->
