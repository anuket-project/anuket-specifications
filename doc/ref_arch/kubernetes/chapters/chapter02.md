
[<< Back](../../kubernetes)

# 2. Architecture Requirements
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [2.1 Introduction](#2.1)
  * [2.1.1 Definitions](#2.1.1)
* [2.2 Reference Model Requirements](#2.2)
  * [2.2.1 Cloud Infrastructure Software Profile Capabilities](#2.2.1)
  * [2.2.2 Virtual Network Interface Specifications](#2.2.2)
  * [2.2.3 Cloud Infrastructure Software Profile Requirements](#2.2.3)
  * [2.2.4 Cloud Infrastructure Hardware Profile Requirements](#2.2.4)
  * [2.2.5 Cloud Infrastructure Management Requirements](#2.2.5)
  * [2.2.6 Cloud Infrastructure Security Requirements](#2.2.6)
* [2.3 Kubernetes Architecture Requirements](#2.3)

<a name="2.1"></a>
## 2.1 Introduction

This chapter will use the requirements defined in the overall Reference Model and only make additional entries in section [2.3](#2.3) if there are additional requirements needed for this Reference Architecture.

<a name="2.1.1"></a>
## 2.1.1 Definitions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC2119](https://www.ietf.org/rfc/rfc2119.txt).

<a name="2.2"></a>
## 2.2 Reference Model Requirements

The tables below contains the requirements from the Reference Model to cover the Basic and Network Intensive profiles.  The table also includes a reference to the specification from [Chapter 04 - Architecture Specification](./chapter04.md) to ensure traceability.

To ensure alignment with the infrastructure profile catalogue, the following requirements are referenced through:
- Those relating to Cloud Infrastructure Software Profiles
- Those relating to Cloud Infrastructure Hardware Profiles
- Those relating to Storage Extensions (S extension)
- Those relating to Network Acceleration Extensions (A extension)
- Those relating to Cloud Infrastructure Management

> Note; where "(if offered)" is used in the Reference Model, this has been replaced with "Optional" in the table below in order to align with the RFC2119 wording.

<a name="2.2.1"></a>
### 2.2.1 Cloud Infrastructure Software Profile Capabilities

| Reference Model Section | Reference  | Description | Requirement for Basic Profile | Requirement for Network Intensive Profile| Specification Reference |
|---|---|---|---|---|---|
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.001 | Max number of vCPU that can be assigned to a single Pod by the Cloud Infrastructure | At least 16 <sup>(1)</sup> | At least 16 <sup>(1)</sup> | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.002 | Max memory in MB that can be assigned to a single Pod by the Cloud Infrastructure | at least 32 GB<sup>(1)</sup> | at least 32 GB<sup>(1)</sup> | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.003 | Max storage in GB that can be assigned to a single Pod by the Cloud Infrastructure | at least 320 GB<sup>(1)</sup> | at least 320 GB<sup>(1)</sup> | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.004 | Max number of connection points that can be assigned to a single Pod by the Cloud Infrastructure | 6 | 6 | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.005 | Max storage in GB that can be attached / mounted to Pod by the Cloud Infrastructure | Up to 16TB<sup>(2)</sup> | Up to 16TB<sup>(2)</sup> | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.006 | CPU pinning support | Not required | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.007 | NUMA support | Not required | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.008 | IPSec Acceleration using the virtio-ipsec interface | Not required | Optional | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.009 | Crypto Acceleration using the virtio-crypto interface | Not required | Optional | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.010 | Transcoding Acceleration | Not required | Not required | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.011 | Programmable Acceleration | Not required | Not required | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.012 | Enhanced Cache Management: L=Lean; E=Equal; X=eXpanded | E | E | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.013 | SR-IOV over PCI-PT | Must support | Not required | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.014 | Hardware coprocessor support (GPU/NPU) | Not required | Not required | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.015 | SmartNICs | Optional | Not required | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | e.cap.016 | FPGA/other Acceleration H/W | Optional | Not required | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | *e.cap.017* | *Ability to monitor L2-L7 data from workload* | *n/a<sup>(3)</sup>* | *n/a<sup>(3)</sup>* | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.cap.014 | Indicates the number of CPU cores consumed by the Cloud Infrastructure on the worker nodes | 2 | 2 | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.cap.015 | Indicates the memory consumed by Cloud Infrastructure on the worker nodes | 16 GB | 16GB | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.cap.016 | Number of virtual cores per physical core; also known as CPU overbooking ratio that is required | 1:1 | 1:1 | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.cap.017 | QoS enablement of the connection point (vNIC or interface)| Not required | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.cap.018 | Support for huge pages | Not required | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.pm.001  | Monitor worker node CPU usage, per nanosecond | Must support | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.pm.002  | Monitor pod CPU usage, per nanosecond | Must support | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.pm.003  | Monitor worker node CPU utilisation (%) | Must support | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.pm.004  | Monitor pod CPU utilisation | Must support | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.pm.005  | Measure external storage IOPs | Must support | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.pm.006  | Measure external storage throughput | Must support | Must support | |
| [4.2.5](../../../ref_model/chapters/chapter04.md#425-cloud-infrastructure-profile-capabilities-mapping) | i.pm.007  | Measure external storage capacity | Must support | Must support | |

<p align="center"><b>Table 2-1:</b> Reference Model Requirements: Cloud Infrastructure Software Profile Capabilities</p>

**(1)** Defined in the `.4xlarge` flavour in section [4.2.1.1 Predefined Compute Flavours](../../../ref_model/chapters/chapter04.md#4211-predefined-compute-flavours)<br>
**(2)** Defined in the `.bronze` configuration in section [4.2.3 Storage Extensions](../../../ref_model/chapters/chapter04.md#423-storage-extensions)<br>
**(3)** In Kubernetes based infrastructures packet monitoring is out of the scope for the infrastructure.

<a name="2.2.2"></a>
### 2.2.2 Virtual Network Interface Specifications

The required number of connection points to a Pod is described in `e.cap.004` above.  This section describes the required bandwidth of those connection points.

| Reference Model Section | Reference  | Description | Requirement for Basic Profile | Requirement for Network Intensive Profile| Specification Reference |
|---|---|---|---|---|---|
| [4.2.2](../../../ref_model/chapters/chapter04.md#422-virtual-network-interface-specifications) | n1, n2, n3, n4, n5, n6	| 1, 2, 3, 4, 5, 6 Gbps | Must support | Must support | |
| [4.2.2](../../../ref_model/chapters/chapter04.md#422-virtual-network-interface-specifications) | nn10, n20, n30, n40, n50, n60	| 10, 20, 30, 40, 50, 60 Gbps | Must support | Must support | |
| [4.2.2](../../../ref_model/chapters/chapter04.md#422-virtual-network-interface-specifications) | n25, n50, n75, n100, n125, n150	| 25, 50, 75, 100, 125, 150 Gbps | Must support | Must support | |
| [4.2.2](../../../ref_model/chapters/chapter04.md#422-virtual-network-interface-specifications) | nn50, n100, n150, n200, n250, n300	| 50, 100, 150, 200, 250, 300 Gbps | Must support | Must support | |
| [4.2.2](../../../ref_model/chapters/chapter04.md#422-virtual-network-interface-specifications) | n100, n200, n300, n400, n500, n600	| 100, 200, 300, 400, 500, 600 Gbps | Must support | Must support | |

<p align="center"><b>Table 2-2:</b> Reference Model Requirements: Network Interface Specifications</p>

<a name="2.2.3"></a>
### 2.2.3 Cloud Infrastructure Software Profile Requirements

| Reference Model Section | Reference  | Description | Requirement for Basic Profile | Requirement for Network Intensive Profile| Specification Reference |
|---|---|---|---|---|---|
| [5.2.1](../../../ref_model/chapters/chapter05.md#521-virtual-compute) | infra.com.cfg.001 | CPU allocation ratio | 1:1 | 1:1 | |
| [5.2.1](../../../ref_model/chapters/chapter05.md#521-virtual-compute) | infra.com.cfg.002 | NUMA awareness | Must support | Must support | |
| [5.2.1](../../../ref_model/chapters/chapter05.md#521-virtual-compute) | infra.com.cfg.003 | CPU pinning capability | Must support | Must support | |
| [5.2.1](../../../ref_model/chapters/chapter05.md#521-virtual-compute) | infra.com.cfg.004 | Huge Pages | Must support | Must support | |
| [5.2.2](../../../ref_model/chapters/chapter05.md#522-virtual-storage) | infra.stg.cfg.002 | Storage Block | Must support | Must support | |
| [5.2.2](../../../ref_model/chapters/chapter05.md#522-virtual-storage) | infra.stg.cfg.003 | Storage with replication | Not required | Must support | |
| [5.2.2](../../../ref_model/chapters/chapter05.md#522-virtual-storage) | infra.stg.cfg.004 | Storage with encryption | Must support | Must support | |
| [5.2.2](../../../ref_model/chapters/chapter05.md#522-virtual-storage) | infra.stg.acc.cfg.001 | Storage IOPS oriented | Not required | Must support | |
| [5.2.2](../../../ref_model/chapters/chapter05.md#522-virtual-storage) | infra.stg.acc.cfg.002 | Storage capacity oriented | Not required | Not required | |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.cfg.001 | IO virtualisation using virtio1.1 | Must support<sup>(1)</sup> | Must support<sup>(1)</sup>| |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.cfg.002 | The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric.<sup>(2)</sup> | Must support VXLAN, MPLSoUDP, GENEVE, other | *No requirement specified* | |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.cfg.003 | Network Address Translation | Must support | Must support | |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.cfg.004 | Security Groups | Must support | Must support | |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.cfg.005 | SFC support | Not required | Must support | |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.cfg.006 | Traffic patterns symmetry | Must support | Must support | |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.acc.cfg.001 | vSwitch optimisation | Not required | Must support DPDK<sup>(3)</sup>| |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.acc.cfg.002 | Support of HW offload | Not required | Must support SmartNic | |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.acc.cfg.003 | Crypto acceleration | Not required | Must support | |
| [5.2.3](../../../ref_model/chapters/chapter05.md#523-virtual-networking) | infra.net.acc.cfg.004 | Crypto Acceleration Interface | Not required | Must support | |

<p align="center"><b>Table 2-3:</b> Reference Model Requirements: Cloud Infrastructure Software Profile Requirements</p>

**(1)** [Workload Transition Guidelines.](../chapters/appendix-a.md) might have other interfaces (such as SR-IOV VFs to be directly passed to a VM or a Pod) or NIC-specific drivers on guest machines transiently allowed until more mature solutions are available with an acceptable level of efficiency to support telecom workloads (for example regarding CPU and energy consumption).<br>
**(2)** In Kubernetes based infrastructures network separation is possible without an overlay (e.g.: with IPVLAN)<br>
**(3)** This feature is not applicable for Kubernetes based infrastructures due to lack of vSwitch however workloads need access to user space networking solutions.

<a name="2.2.4"></a>
### 2.2.4 Cloud Infrastructure Hardware Profile Requirements

| Reference Model Section | Reference  | Description | Requirement for Basic Profile | Requirement for Network Intensive Profile| Specification Reference |
|---|---|---|---|---|---|
| [5.4.1](../../../ref_model/chapters/chapter05.md#541-compute-resources) | infra.hw.cpu.cfg.001 | Number of CPU (Sockets) | 2 | 2 | |
| [5.4.1](../../../ref_model/chapters/chapter05.md#541-compute-resources) | infra.hw.cpu.cfg.002 | Number of Cores per CPU | 20 | 20 | |
| [5.4.1](../../../ref_model/chapters/chapter05.md#541-compute-resources) | infra.hw.cpu.cfg.003 | NUMA | Not required | Must support | |
| [5.4.1](../../../ref_model/chapters/chapter05.md#541-compute-resources) | infra.hw.cpu.cfg.004 | Simultaneous Multithreading/Symmetric Multiprocessing (SMT/SMP) | Must support | Must support | |
| [5.4.1](../../../ref_model/chapters/chapter05.md#541-compute-resources) | infra.hw.cac.cfg.001 | GPU | Not required | Not required | |
| [5.4.2](../../../ref_model/chapters/chapter05.md#542-storage-configurations) | infra.hw.stg.hdd.cfg.001 | Local Storage HDD | *No requirement specified* | *No requirement specified* | |
| [5.4.2](../../../ref_model/chapters/chapter05.md#542-storage-configurations) | infra.hw.stg.ssd.cfg.002 | Local Storage SSD | Should support | Should support | |
| [5.4.3](../../../ref_model/chapters/chapter05.md#543-network-resources) | infra.hw.nic.cfg.001 | Total Number of NIC Ports available in the host | 4 | 4 | |
| [5.4.3](../../../ref_model/chapters/chapter05.md#543-network-resources) | infra.hw.nic.cfg.002 | Port speed specified in Gbps (minimum values) | 10 | 25 | |
| [5.4.3](../../../ref_model/chapters/chapter05.md#543-network-resources) | infra.hw.pci.cfg.001 | Number of PCIe slots available in the host | 8 | 8 | |
| [5.4.3](../../../ref_model/chapters/chapter05.md#543-network-resources) | infra.hw.pci.cfg.002 | PCIe speed | Gen 3 | Gen 3 | |
| [5.4.3](../../../ref_model/chapters/chapter05.md#543-network-resources) | infra.hw.pci.cfg.003 | PCIe Lanes | 8 | 8 | |
| [5.4.3](../../../ref_model/chapters/chapter05.md#543-network-resources) | infra.hw.nac.cfg.001 | Cryptographic Acceleration | Not required | Optional | |
| [5.4.3](../../../ref_model/chapters/chapter05.md#543-network-resources) | infra.hw.nac.cfg.002 | A SmartNIC that is used to offload vSwitch functionality to hardware | Not required | Optional<sup>(1)</sup> | |
| [5.4.3](../../../ref_model/chapters/chapter05.md#543-network-resources) | infra.hw.nac.cfg.003 | Compression | *No requirement specified* | *No requirement specified* | |

<p align="center"><b>Table 2-4:</b> Reference Model Requirements: Cloud Infrastructure Hardware Profile Requirements</p>

**(1)** There is no vSwitch in case of containers, but a SmartNIC can be used to offload any other network processing.

<a name="2.2.5"></a>
### 2.2.5 Cloud Infrastructure Management Requirements

| Reference Model Section | Reference | Description | Requirement (common to all Profiles) | Specification Reference |
|---|---|---|---|---|
| [4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities) | e.man.001 | Capability to allocate virtual compute resources to a workload | Must support | |
| [4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities) | e.man.002 | Capability to allocate virtual storage resources to a workload | Must support | |
| [4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities) | e.man.003 | Capability to allocate virtual networking resources to a workload | Must support | |
| [4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities) | e.man.004 | Capability to isolate resources between tenants | Must support | |
| [4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities) | e.man.005 | Capability to manage workload software images | Must support | |
| [4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities) | e.man.006 | Capability to provide information related to allocated virtualised resources per tenant | Must support | |
| [4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities) | e.man.007 | Capability to notify state changes of allocated resources | Must support | |
| [4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities) | e.man.008 | Capability to collect and expose performance information on virtualised resources allocated | Must support | |
| [4.1.5](../../../ref_model/chapters/chapter04.md#415-cloud-infrastructure-management-capabilities) | e.man.009 | Capability to collect and notify fault information on virtualised resources | Must support | |

<!--
These rows are removed and commented out as it's not clear what the requirement is.
| infra.stg.cfg.001 | Catalogue storage Types | | Y |
-->
<p align="center"><b>Table 2-5:</b> Reference Model Requirements: Cloud Infrastructure Management Requirements</p>

<a name="2.2.6"></a>
### 2.2.6 Cloud Infrastructure Security Requirements

| Reference Model Section | Reference | Requirement (common to all Profiles) | Specification Reference |
|---|---|---|---|
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.001 | The Platform **must** maintain the state to what it is specified to be and does not change unless through change management process. |   |  |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.002 | All systems part of Cloud Infrastructure **must** support password hardening (strength and rules for updates (process), storage and transmission, etc.) |  | Hardening: NIST SP 800-63B |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.003 | All servers part of Cloud Infrastructure **must** support a root of trust and secure boot |  |  |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.004 | The Operating Systems of all the servers part of Cloud Infrastructure **must** be hardened |  | NIST SP 800-123 |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.005 | The Platform **must** support Operating System level access control |  | Details on OS |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.006 | The Platform **must** support Secure logging |  | Details |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.007 | All servers part of Cloud Infrastructure **must** be Time synchronized with authenticated Time service |  | |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.008 | All servers part of Cloud Infrastructure **must** be regularly updated to address security vulnerabilities |  | |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.009 | The Platform **must** support Software integrity protection and verification |  | |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.010 | The Cloud Infrastructure **must** support Secure storage (all types) |  | Expand/Delete based on other requirements |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.011 | The Cloud Infrastructure **should** support Read and Write only storage partitions (write only permission to one or more authorized actors) |  | |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.012 | The Operator **must** ensure that only authorized actors have physical access to the underlying infrastructure. |  | |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.013 | The Platform **must** ensure that only authorized actors have logical access to the underlying infrastructure. |  | |
| [7.11.1](../../../ref_model/chapters/chapter07.md#7111-system-hardening) | sec.gen.014 | All servers part of Cloud Infrastructure **should** support measured boot and an attestation server that monitors the measurements of the servers. |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.001 | The Platform **must** support authenticated and secure APIs, API endpoints |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | | The Platform **must** implement authenticated and secure access to GUI |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.002 | The Platform **must** support Traffic Filtering for workloads (for example, Fire Wall) |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.003 | The Platform **must** support Secure and encrypted communications, and confidentiality and integrity of network traffic |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.004 | The Cloud Infrastructure **must** support Secure network channels |  | A secure channel enables transferring of data that is resistant to overhearing and tampering |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.005 | The Cloud Infrastructure **must** segregate the underlay and overlay networks |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.006 | The Cloud Infrastructure must be able to utilize the Cloud Infrastructure Manager identity management capabilities |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.007 | The Platform **must** implement controls enforcing separation of duties and privileges, least privilege use and least common mechanism (Role-Based Access Control) |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.008 | The Platform **must** be able to assign the Entities that comprise the tenant networks to different trust domains. |  | Communication between different trust domains is not allowed, by default.  |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.009 | The Platform **must** support creation of Trust Relationships between trust domains |  | These maybe uni-directional relationships where the trusting domain trusts anther domain (the “trusted domain”) to authenticate users for them or to allow access to its resources from the trusted domain.  In a bidirectional relationship both domain are “trusting” and “trusted” |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.010 | For two or more domains without existing trust relationships, the Platform **must not** allow the effect of an attack on one domain to impact the other domains either directly or indirectly |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.011 | The Platform **must not** reuse the same authentication key-pair (for example, on different hosts, for different services) |  | |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.012 | The Platform **must** only use secrets encrypted using strong encryption techniques, and stored externally from the component |  | e.g., Barbican (OpenStack) |
| [7.11.2](../../../ref_model/chapters/chapter07.md#7112-platform-and-access) | sec.sys.013 | The Platform **must** provide secrets dynamically as and when needed |  | |
| [7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity) | sec.ci.001 | The Platform **must** support Confidentiality and Integrity of data at rest and in-transit |  | |
| [7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity) | sec.ci.002 | The Platform **should** support self-encrypting storage devices |  | |
| [7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity) | sec.ci.003 | The Platform **must** support Confidentiality and Integrity of data related metadata |  | |
| [7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity) | sec.ci.004 | The Platform **must** support Confidentiality of processes and restrict information sharing with only the process owner (e.g., tenant). |  | |
| [7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity) | sec.ci.005 | The Platform **must** support Confidentiality and Integrity of process-related metadata and restrict information sharing with only the process owner (e.g., tenant). |  | |
| [7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity) | sec.ci.006 | The Platform **must** support Confidentiality and Integrity of workload resource utilization (RAM, CPU, Storage, Network I/O, cache, hardware offload) and restrict information sharing with only the workload owner (e.g., tenant). |  | |
| [7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity) | sec.ci.007 | The Platform **must not** allow Memory Inspection by any actor other than the authorized actors for the Entity to which Memory is assigned (e.g., tenants owning the workload), for Lawful Inspection, and by secure monitoring services |  | Admin access must be carefully regulated |
| [7.11.3](../../../ref_model/chapters/chapter07.md#7113-confidentiality-and-integrity) | sec.ci.008 | The Cloud Infrastructure **must** support tenant networks segregation |  | |
| [7.11.4](../../../ref_model/chapters/chapter07.md#7114-workload-security) | sec.wl.001 | The Platform **must** support Workload placement policy |  | |
| [7.11.4](../../../ref_model/chapters/chapter07.md#7114-workload-security) | sec.wl.002 | The Platform **must** support operational security |  | |
| [7.11.4](../../../ref_model/chapters/chapter07.md#7114-workload-security) | sec.wl.003 | The Platform **must** support secure provisioning of workloads  |  | |
| [7.11.4](../../../ref_model/chapters/chapter07.md#7114-workload-security) | sec.wl.004 | The Platform **must** support Location assertion (for mandated in-country or location requirements) |  | |
| [7.11.4](../../../ref_model/chapters/chapter07.md#7114-workload-security) | sec.wl.005 | Production workloads **must** be separated from non-production workloads |  | |
| [7.11.4](../../../ref_model/chapters/chapter07.md#7114-workload-security) | sec.wl.006 | Workloads **must** be separable by their categorisation (for example, payment card information, healthcare, etc.) |  | |
| [7.11.4](../../../ref_model/chapters/chapter07.md#7114-workload-security) | sec.wl.007 | The Operator **should** implement processes and tools to verify VNF authenticity and integrity. |  | |
| [7.11.5](../../../ref_model/chapters/chapter07.md#7115-image-security) | sec.img.001 | Images from untrusted sources **must not** be used |  | |
| [7.11.5](../../../ref_model/chapters/chapter07.md#7115-image-security) | sec.img.002 | Images **must** be maintained to be free from known vulnerabilities |  | |
| [7.11.5](../../../ref_model/chapters/chapter07.md#7115-image-security) | sec.img.003 | Images **must not** be configured to run with privileges higher than the privileges of the actor authorized to run them |  | |
| [7.11.5](../../../ref_model/chapters/chapter07.md#7115-image-security) | sec.img.004 | Images **must** only be accessible to authorized actors |  | |
| [7.11.5](../../../ref_model/chapters/chapter07.md#7115-image-security) | sec.img.005 | Image Registries **must** only be accessible to authorized actors |  | |
| [7.11.5](../../../ref_model/chapters/chapter07.md#7115-image-security) | sec.img.006 | Image Registries **must** only be accessible over secure networks |  | |
| [7.11.5](../../../ref_model/chapters/chapter07.md#7115-image-security) | sec.img.007 | Image registries **must** be clear of vulnerable and stale (out of date) versions |  | |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.001 | The Platform **must** support Secure Provisioning, Maintaining availability, Deprovisioning (secure Clean-Up) of workload resources |  | Secure clean-up: tear-down, defending against virus or other attacks, or observing of cryptographic or user service data |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.002 | Operational **must** use management protocols limiting security risk such as SNMPv3, SSH v2, ICMP, NTP, syslog and TLS |  | |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.003 | The Cloud Operator **must** implement change management for Cloud Infrastructure, Cloud Infrastructure Manager and other components of the cloud |  | Platform change control on hardware |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.004 | The Cloud Operator **should** support automated templated approved changes |  | Templated approved changes for automation where available |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.005 | Platform **must** provide logs and these logs must be regularly scanned |  | |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.006 | The Platform **must** verify the integrity of all Resource management requests | | |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.007 | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with current time information |  | |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.008 | The Platform **must** be able to update newly instantiated, suspended, hibernated, migrated and restarted images with relevant DNS information. |  | |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.009 |  The Platform **must** be able to update the tag of newly instantiated, suspended, hibernated, migrated and restarted images with relevant geolocation (geographical) information |  | |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.010 | The Platform **must** log all changes to geolocation along with the mechanisms and sources of location information (i.e. GPS, IP block, and timing). |  | |
| [7.11.6](../../../ref_model/chapters/chapter07.md#7116-security-lcm) | sec.lcm.011 | The Platform **must** implement Security life cycle management processes including proactively update and patch all deployed Cloud Infrastructure    software. | | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.001 | Platform must provide logs and these logs must be regularly scanned for events of interest |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.002 | Security logs must be time synchronised |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.003 | The Platform must log all changes to time server source, time, date and time zones |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.004 | The Platform must secure and protect Audit logs (contain sensitive information) both in-transit and at rest |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.005 | The Platform must Monitor and Audit various behaviours of connection and login attempts to detect access attacks and potential access attempts and take corrective actions accordingly |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.006 | The Platform must Monitor and Audit operations by authorized account access after login to detect malicious operational activity and take corrective actions accordingly |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.007 | The Platform must Monitor and Audit security parameter configurations for compliance with defined security policies |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.008 | The Platform must Monitor and Audit externally exposed interfaces for illegal access (attacks) and take corrective security hardening measures |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.009 | The Platform must Monitor and Audit service handling for various attacks (malformed messages, signalling flooding and replaying, etc.) and take corrective actions accordingly |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.010 | The Platform must Monitor and Audit running processes to detect unexpected or unauthorized processes and take corrective actions accordingly |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.011 | The Platform must Monitor and Audit logs from infrastructure elements and workloads to detected anomalies in the system components and take corrective actions accordingly |  |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.012 | The Platform must Monitor and Audit Traffic patterns and volumes to prevent malware download attempts |  | |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.013 | The monitoring system must not affect the security (integrity and confidentiality) of the infrastructure, workloads, or the user data (through back door entries). |  |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.014 | The Monitoring systems should not impact IAAS, PAAS, and SAAS SLAs including availability SLAs |  |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.015 | The Platform must ensure that the Monitoring systems are never starved of resources |  |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.mon.016 | The Platform Monitoring components should follow security best practices for auditing, including secure logging and tracing |  |
| [7.11.7](../../../ref_model/chapters/chapter07.md#7117-monitoring-and-security-audit) | sec.lcm.017 | The Platform must Audit systems for any missing security patches and take appropriate actions |  |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.001 | The Cloud Operator **should** comply with Center for Internet Security CIS Controls ([https://www.cisecurity.org/](https://www.cisecurity.org/)) | |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.002 | The Cloud Operator, Platform and Workloads **should** follow the guidance in the CSA Security Guidance for Critical Areas of Focus in Cloud Computing (latest version) [https://cloudsecurityalliance.org/](https://cloudsecurityalliance.org/) | |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.003 | The Platform and Workloads **should** follow the guidance in the OWASP Cheat Sheet Series (OCSS) https://github.com/OWASP/CheatSheetSeries |  |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.004 | The Cloud Operator, Platform and Workloads **should** ensure that their code is not vulnerable to the OWASP Top Ten Security Risks [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/) |  |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.005 | The Cloud Operator, Platform and Workloads **should** strive to improve their maturity on the OWASP Software Maturity Model (SAMM) https://owaspsamm.org/blog/2019/12/20/version2-community-release/ |  |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | | The Cloud Operator, Platform and Workloads **should** utilize the OWASP Web Security Testing Guide https://github.com/OWASP/wstg/tree/master/document |  |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.013 | The Cloud Operator, and Platform **should** satisfy the requirements for Information Management Systems specified in ISO/IEC 27001  https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en. ISO/IEC 27002:2013 - ISO/IEC 27001 is the international Standard for best-practice information security management systems (ISMSs). | |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.014 | The Cloud Operator, and Platform **should** implement the Code of practice for Security Controls specified ISO/IEC 27002:2013 (or latest)  https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:v1:en | | |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.015 | The Cloud Operator, and Platform **should** implement the ISO/IEC 27032:2012 (or latest) Guidelines for Cybersecurity techniques  https://www.iso.org/obp/ui/#iso:std:iso-iec:27032:ed-1:v1:en. ISO/IEC 27032 - ISO/IEC 27032is the international Standard focusing explicitly on cybersecurity. | |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.016 | The Cloud Operator **should** conform to the ISO/IEC 27035 standard for incidence management. ISO/IEC 27035 - ISO/IEC 27035 is the international Standard for incident management. | |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.017 | The Cloud Operator **should** conform to the ISO/IEC 27031 standard for business continuity. ISO/IEC 27031 - ISO/IEC 27031 is the international Standard for ICT readiness for business continuity. | |
| [7.11.8](../../../ref_model/chapters/chapter07.md#7118-compliance-with-standards) | sec.std.018 | The Public Cloud Operator **must**, and the Private Cloud Operator **may** be certified to be compliant with the International Standard on Awareness Engagements (ISAE) 3402 (in the US: SSAE 16). International Standard on Awareness Engagements (ISAE) 3402. US Equivalent: SSAE16. | |

<p align="center"><b>Table 2-6:</b> Reference Model Requirements: Cloud Infrastructure Security Requirements</p>

<a name="2.3"></a>
## 2.3 Kubernetes Architecture Requirements

The Reference Model (RM) defines the Cloud Infrastructure, which consists of the physical resources, virtualised resources and a software management system.  In the virtualised world, the Cloud Infrastructure consists of the Guest Operating System, Hypervisor and, if needed, other software such as libvirt.  The Cloud Infrastructure Management component is responsible for, among others, tenant management, resources management, inventory, scheduling, and access management.

Now consider the containerisation equivalent, references to "Architecture" in this chapter refer to the Cloud Infrastructure Hardware (e.g. physical resources), Cloud Infrastructure Software (e.g. Hypervisor (optional), Container Runtime, virtual or container Orchestrator(s), Operating System), and infrastructure resources consumed by virtual machines or containers.

The requirements in this section are to be delivered in addition to those in [section 2.2](#2.2), and have been created to support the Principles defined in [Chapter 1 of this Reference Architecture](./chapter01.md).

| Ref # | Category | Sub-category | Description | Specification Reference |
|---|---|---|---|---|
| `req.gen.cnt.01` | General | Cloud nativeness | The Architecture **should** consist of service components implemented as microservices that are individually dynamically scalable. | |
| `req.gen.cnt.02` | General | Cloud nativeness | The Architecture **must** support immutable infrastructure. | |
| `req.gen.cnt.03` | General | Cloud nativeness | The Architecture **must** run conformant Kubernetes as defined by the [CNCF](https://github.com/cncf/k8s-conformance). | |
| `req.gen.cnt.04` | General | Cloud nativeness | The Architecture **must** support clearly defined abstraction layers. | |
| `req.gen.cnt.05` | General | Cloud nativeness | The Architecture **should** support configuration of all components in an automated manner using openly published API definitions. |
| `req.gen.scl.01` | General | Scalability | The Architecture **should** support policy driven horizontal auto-scaling of workloads. | |
| `req.gen.rsl.01` | General | Resiliency | The Architecture **must** support resilient Kubernetes components that are required for the continued availability of running workloads. | |
| `req.gen.rsl.02` | General | Resiliency | The Architecture **should** support resilient Kubernetes service components that are not subject to `req.gen.rsl.01`. | |
| `req.gen.avl.01` | General | Availability | The Architecture **must** provide High Availability for Kubernetes components. | |
| `req.gen.ost.01` | General | Openness | The Architecture **should** embrace open-based standards and technologies. |
| `req.inf.com.01` | Infrastructure | Compute | The Architecture **must** provide compute resources for Pods.  | |
| `req.inf.stg.01` | Infrastructure | Storage | The Architecture **must** support the ability for an operator to choose whether or not to deploy persistent storage for Pods. | |
| `req.inf.ntw.01` | Infrastructure | Network | The Architecture **must** support network resiliency. | |
| `req.inf.ntw.02` | Infrastructure | Network | The Architecture **must** be fully redundant. | |
| `req.inf.ntw.03` | Infrastructure | Network | The networking solution **should** be able to be centrally administrated and configured. | |
| `req.inf.ntw.04` | Infrastructure | Network | The Architecture **must** support dual stack IPv4 and IPv6 for Kubernetes workloads. | |
| `req.inf.ntw.05` | Infrastructure | Network | The Architecture **must** support capabilities for integrating SDN controllers. | |
| `req.inf.ntw.06` | Infrastructure | Network | The Architecture **must**  support more than one networking solution. | |
| `req.inf.ntw.07` | Infrastructure | Network | The Architecture **must** support the ability for an operator to choose whether or not to deploy more than one networking solution. | |
| `req.inf.ntw.08` | Infrastructure | Network | The Architecture **must**  provide a default network which implements the Kubernetes network model. | |
| `req.inf.ntw.09` | Infrastructure | Network | The networking solution **must not** interfere with or cause interference to any interface or network it does not own. | |
| `req.inf.ntw.10` | Infrastructure | Network | The Architecture **must** support cluster wide coordination of IP address assignment. | |
| `req.inf.ntw.11` | Infrastructure |	Network | The networking solution to support multiple connection points (e.cap.004 - please see [Section 2.2.1](#2.2.1)) must conform to the [Multi-Network CRD Specification from the Kubernetes Network Plumbing Working Group](https://github.com/k8snetworkplumbingwg/multi-net-spec). | |
| `req.inf.ntw.12` | Infrastructure | Network | The networking solution to support multiple connection points (e.cap.004 - please see [Section 2.2.1](#2.2.1)) must support any Kubernetes conformant CNI plugin to be incorporated as a networking solution. | |
| `req.inf.ntw.13` | Infrastructure | Network | The platform must allow specifying multiple separate IP pools. Tenants are required to select at least one IP pool that is different from the control infrastructure IP pool or other tenant IP pools. | |
| `req.inf.vir.01` | Infrastructure | Virtual Infrastructure | The Architecture must support the capability for Containers to consume infrastructure resources abstracted by Host Operating Systems that are running within a virtual machine. | |
| `req.inf.phy.01`  | Infrastructure |  Physical Infrastructure | The Architecture must support the capability for Containers to consume infrastructure resources abstracted by Host Operating Systems that are running within a physical server. | |
| `req.kcm.gen.01` | Kubernetes Cluster | General | The Architecture **must** support policy driven horizontal auto-scaling of Kubernetes cluster. | |
| `req.kcm.gen.02` | Kubernetes Cluster | General | The Architecture **must** enable workload resiliency. | |
| `req.int.api.01` | API | General | The Architecture **must** leverage the Kubernetes APIs to discover and declaratively manage compute (virtual and bare metal resources), network, and storage. | |
| `req.int.api.02` | API | General | The Architecture **must** support the usage of a Kubernetes Application package manager using the Kubernetes API, like Helm v3. | |

<!--
| `req.inf.com.02` | Compute | The Architecture **should** include industry standard hardware management systems at both HW device level (embedded) and HW platform level (external to device). |
-->

<p align="center"><b>Table 2-7:</b> Kubernetes Architecture Requirements</p>
