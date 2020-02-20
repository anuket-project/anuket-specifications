
[<< Back](../../kubernetes)

# 2. Architecture Requirements
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [2.1 Introduction](#2.1)
* [2.2 Reference Model Requirements](#2.2)
* [2.2.1 Network Acceleration Extensions](#2.2.1)
* [2.2.2 Network Interface Options](#2.2.2)
* [2.2.3 VIM Capabilities](#2.2.3)
* [2.2.4 Instance Capabilities Mapping](#2.2.4)
* [2.3 Kubernetes Architecture Requirements](#2.3)
  * [2.3.1 General Requirements](#2.3.1)
  * [2.3.2 Infrastructure Requirements](#2.3.2)
  * [2.3.3 Kubernetes Cluster Requirements](#2.3.3)
  * [2.3.4 Interfaces and APIs Requirements](#2.3.4)
  * [2.3.5 Operations and LCM Requirements](#2.3.5)
  * [2.3.6 Assurance Requirements](#2.3.6)
  * [2.3.7 Security Requirements](#2.3.7)

<a name="2.1"></a>
## 2.1 Introduction

**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the Reference Architecture and reflected in any Reference Implementation or Vendor Implementation targeting this Reference Architecture. The same applies to _must not_.

**should**: Requirements that are marked as _should_ are expected to be fulfilled by the Reference Architecture but it is up to each service provider to accept a Vendor Implementation targeting this Reference Architecture that is not reflecting on any of those requirements. The same applies to _should not_.

- ***NOTE:*** Some of these **must** and **should** requirements may be optional when it comes to an operator **deployment** (i.e. an operator may choose whether or not to deploy or not, depending on the NFVI Software Profiles required for each specific deployment). These will be marked with "(*optional for deployment*)" within the requirements tables in section 2.3.

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.

> [RFC2119](https://www.ietf.org/rfc/rfc2119.txt)

<a name="2.2"></a>
## 2.2 Reference Model Requirements

This reference model intends to implement both the Basic, Network Intensive and Compute Intensive Instance types defined in the Reference Model. The following table contains the requirements of the Reference Model and indicates if the Reference Architecture supports them.

<a name="2.2.1"></a>
### 2.2.1 Network Acceleration Extensions

From Reference Model section [4.2.4.2.1 Network Acceleration Extensions](../../../ref_model/chapters/chapter04.md#42421-network-acceleration-extensions)

| Attribute | Description | Supported |
|-----------|----------------------------------|-------|
| .il-ipsec | In-line IPSec acceleration | optional and only if the CNI plugin is OVS |
| .la-crypto | Look-Aside encryption/decryption engine | optional and only if the CNI plugin is OVS |
| .la-trans | Look-Aside Transcoding acceleration | optional and only if the CNI plugin is OVS |
| .la-programmable | Look-Aside programmable acceleration | optional and only if the CNI plugin is OVS |

<a name="2.2.2"></a>
### 2.2.2 Network Interface Options

From Reference Model section [4.2.4.4 Network Interface Options](../../../ref_model/chapters/chapter04.md#4244-network-interface-options)

| Attribute | Description | Supported |
|-----------|----------------------------------|-------|
| n1, n2, n3, n4, n5, n6 | | Y |
| n10, n20, n30, n40, n50, n60 | | Y |
| n25, n50, n75, n100, n125, n150 | | Y |
| n50, n100, n150, n200, n250, n300 | | Y |
| n100, n200, n300, n400, n500, n600 | | Y |

<a name="2.2.3"></a>
### 2.2.3 VIM Capabilities

From Reference Model section [4.1.6 VIM Capabilities](../../../ref_model/chapters/chapter04.md#416-vim-capabilities)

| Attribute | Description | Value | Supported |
|-----------|---------------------------|-------|-------|
| e.vim.cap.001 | Virtual Compute allocation | | Y |
| e.vim.cap.002 | Virtual Storage allocation | | Y |
| e.vim.cap.003 | Virtual Networking resources allocation | | Y |
| e.vim.cap.004 | Multi-tenant isolation | | N <sup>1)</sup> |
| e.vim.cap.005 | Images management | | Y |
| e.vim.cap.006 | Virtual resources inventory per tenant | | Y |
| e.vim.cap.007 | Resources Monitoring | | Y |
| e.vim.cap.008 | Virtual resources Performance  |  | Y |
| e.vim.cap.009 | Virtual resources Fault information | | Y |

**1)** In a Kubernetes based infrastructure within one Kubernetes cluster multitenacy is provided only in resource management level. Isolation of execution environments requires separate Kubernetes clusters or worker nodes.

<a name="2.2.4"></a>
### 2.2.4 Instance Capabilities Mapping

From Reference Model section [4.2.5 Instance Capabilities Mapping](../../../ref_model/chapters/chapter04.md#4.2.5)

| Attribute | Description | Value | Supported |
|-----------|---------------------------|-------|-------|
| e.nfvi.res.cap.001 | Max number of vCPU that can be assigned to a single pod by the NFVI | at least 16<sup>1)</sup> | Y |
| e.nfvi.res.cap.002 | Max memory in MB that can be assigned to a single pod by the NFVI | at least 32 GB<sup>1)</sup> | Y |
| e.nfvi.res.cap.003 | Max storage in GB that can be assigned to a single pod by the NFVI | at least 320 GB<sup>1)</sup> | Y |
| e.nfvi.res.cap.004 | # Connection Points | 6 | Y |
| e.nfvi.res.cap.005 | Total instance (persistent) storage (GB) | 300 GB | Y |
| e.nfvi.per.cap.001 | CPU pinning support | | Y |
| e.nfvi.per.cap.002 | NUMA support | | Y |
| e.nfvi.per.cap.003 | IPSec Acceleration | | Yes (if offered) see section [2.2.1 Network Acceleration Extensions](#2.2.1) |
| e.nfvi.per.cap.004 | Crypto Acceleration | | Yes (if offered) see section [2.2.1 Network Acceleration Extensions](#2.2.1) |
| e.nfvi.per.cap.005 | Transcoding Acceleration | | Yes (if offered) see section [2.2.1 Network Acceleration Extensions](#2.2.1) |
| e.nfvi.per.cap.006 | Programmable Acceleration | | Yes (if offered) see section [2.2.1 Network Acceleration Extensions](#2.2.1) |
| e.nfvi.per.cap.007 | Enhanced Cache Management | | X (if offered) |
| e.nfvi.mon.cap.001 | Monitoring of L2-7 data | | N<sup>2)</sup> |
| i.nfvi.sla.cap.001 | CPU overbooking | 1:1, 1:4 | Y |
| i.nfvi.sla.cap.002 | vNIC QoS | | Y |
| i.nfvi.per.cap.001 | Huge page support |  | Y |
| i.nfvi.mon.cap.001 | Monitor host CPU usage |  | Y |
| i.nfvi.mon.cap.002 | Monitor virtual compute CPU usage | | Y |
| i.nfvi.mon.cap.003 | Monitor host CPU utilization | | Y |
| i.nfvi.mon.cap.004 | Monitor virtual compute CPU utilization | | Y |
| i.nfvi.mon.cap.007 | Monitor external storage capacity | | Y |
| nfvi.com.cfg.002 | NUMA awareness | | Y |
| nfvi.com.cfg.003 | CPU pinning capability | | Y |
| nfvi.com.cfg.004 | Huge Pages  | | Y |
| nfvi.stg.cfg.001 | Catalogue storage Types | | Y |
| nfvi.stg.cfg.002 | Storage Block |  | Y |
| nfvi.stg.cfg.003 | Storage Object | | N<sup>3)</sub> |
| nfvi.stg.cfg.004 | Storage with replication | | Y |
| nfvi.stg.cfg.005 | Storage with encryption | | Y |
| nfvi.stg.acc.cfg.001 | Storage IOPS oriented | | Y |
| nfvi.stg.acc.cfg.002 | Storage capacity oriented | | Y |
| nfvi.net.cfg.001 | vNIC interface | | N<sup>4)</sup>|
| nfvi.net.cfg.002 | Overlay protocol | | Y<sup>5)</sup>|
| nfvi.net.cfg.003 | NAT | | |
| nfvi.net.cfg.004 | Security Group | | |
| nfvi.net.cfg.005 | SFC support | | |
| nfvi.net.cfg.006 | Traffic patterns symmetry | | |
| nfvi.net.acc.cfg.001 | vSwitch optimisation | | N <sup>6)</sup>|
| nfvi.net.acc.cfg.002 | Support of HW offload | |Y, support of SmartNic |
| nfvi.net.acc.cfg.003 | Crypto acceleration | | Y |
| nfvi.net.acc.cfg.004 | Crypto Acceleration Interface | | ? |
| nfvi.hw.cpu.cfg.001 | Number of CPU (Sockets) |  2 | Y |
| nfvi.hw.cpu.cfg.002 | Number of Cores per CPU | 20 | Y |
| nfvi.hw.cpu.cfg.003 | NUMA | | Y |
| nfvi.hw.cpu.cfg.004 | Simultaneous Multithreading/Hyperthreading (SMT/HT) | | Y |
| nfvi.hw.cac.cfg.001 | GPU | | Y |
| nfvi.hw.stg.hdd.cfg.001 | Local Storage HDD | | Optional |
| nfvi.hw.stg.ssd.cfg.002 | Local Storage SSD | | Recommended |
| nfvi.hw.nic.cfg.001 | Total Number of NIC Ports available in the host | 4 | Y |
| nfvi.hw.nic.cfg.002 | Port speed specified in Gbps (minimum values) | 25 | Y |
| nfvi.hw.pci.cfg.001 |  Number of PCIe slots available in the host | 8 | Y |
| nfvi.hw.pci.cfg.002 | PCIe speed | Gen 3 | Y |
| nfvi.hw.pci.cfg.003 | PCIe Lanes | 8 | Y |
| nfvi.hw.nac.cfg.001 | Cryptographic Acceleration | | Optional |
| nfvi.hw.nac.cfg.002 | A SmartNIC that is used to offload vSwitch functionality to hardware | | Optional<sup>7)</sup> |
| nfvi.hw.nac.cfg.003 | Compression |  | |

**1)** Defined in the `.4xlarge` flavour in section [4.2.1.1 Predefined Compute Flavours](../../../ref_model/chapters/chapter04.md#4211-predefined-compute-flavours)
**2)** In Kubernetes based infrastructures the packet monitoring is out of the scope of the infrastructure.<br>
**3)** In Kubernetes based infrastructures object storage is considered as a PaaS capability and excluded from the infrastructures scope.<br>
**4)** There is no vNIC in case of containers.<br>
**5)** In Kubernetes based infrastructures network separation is possible withtout an overlay (e.g.: with IPVLAN)<br>
**6)** This feature is not applicable for Kubernetes based infrastructures due to lack of vSwitch however workloads need access to user space networking solutions.<br>
**7)** There is no vSwitch in case of containers, but a SmartNIC can be used to offload any other network processing.<br>

<a name="2.3"></a>
## 2.3 Kubernetes Architecture Requirements

The Reference Model (RM) defines the NFVI to consist of the physical resources, virtualised resources and a software managment system.  In the virtualised world, the NFVI Software Management System (Virtualised Infrastructure Manager -- VIM) consists of the Guest Operating System, Hypervisor and, if needed, other software such as libvirt.  And the VIM is responsible for, among others, tenant management, resources management, inventory, scheduling, and access management. Now consider, the containerisation equivalent.

Reference to "Architecture" in this chapter refers to the NFVI Hardware (e.g. physical resources), NFVI Software (e.g. Hypervisor, Container Runtime, virtual or container Orchestrator(s), Operating System), and infrastructure resources consumed by virtual machines or containers.

<a name="2.3.1"></a>
### 2.3.1 General Requirements

| Ref # | sub-category | Description |
|---|---|---|
| `req.gen.cnt.02` | Cloud nativeness | The Architecture **should** consist of service components implemented as microservices that are individually dynamically scalable. |
| `req.gen.cnt.03` | Cloud nativeness | The Architecture **must** support immutable infrastructure. |
| `req.gen.cnt.04` | Cloud nativeness | The Architecture **must** run conformant Kubernetes as defined by the [CNCF](https://github.com/cncf/k8s-conformance). |
| `req.gen.scl.01` | Scalability | The Architecture **should** support policy driven horizontal auto-scaling of workloads. |
| `req.gen.rsl.01` | Resiliency | The Architecture **must** support resilient Kubernetes components that are required for the continued availability of running workloads. |
| `req.gen.rsl.02` | Resiliency | The Architecture **should** support resilient Kubernetes service components that are not subject to `req.gen.rsl.01`. |
| `req.gen.avl.01` | Availability | The Architecture **must** provide High Availability for Kubernetes components. |
| `req.gen.ref.01` | Model | The Architecture **must** support the Reference Model defined profiles (instance types: Basic, Network Intensive, Compute Intensive). |

<!--
| `req.gen.k8s.01` | Open source | The Architecture **must** use Kubernetes APIs.|
| `req.gen.k8s.02` | Open source | The Architecture **must** support dynamic request and configuration of resources (compute, network, storage) through Kubernetes APIs. |
| `req.gen.cnt.01` | Cloud nativeness | The Architecture **should** consist of stateless service components. However, where state is required it must be kept external to the component. |
-->

<p align="center"><b>Table 2-1:</b> Kubernetes Architecture: General Requirements</p>

<a name="2.3.2"></a>
### 2.3.2 Infrastructure Requirements

| Ref # | sub-category | Description |
|---|---|---|
| `req.inf.com.01` | Compute | The Architecture **must** provide compute resources for Pods.  |
| `req.inf.com.03` | Network | The Architecture **must** support Container Runtime Interface (CRI). |
| `req.inf.stg.01` | Storage | The Architecture **must**  support Kubernetes Volumes for container storage.
| `req.inf.stg.02` | Storage | The Architecture **may** provide shared Object storage as a service for Containers workload.
| `req.inf.stg.03` | Storage | The Architecture **must** support Container Storage Interfaces (CSI).
| `req.inf.stg.04` | Storage | The Architecture **may** support Software Defined Storage (SDS) that seamlessly supports shared block storage, object storage and flat files. |
| `req.inf.stg.05` | Storage | The Architecture **should** provide high-performance and horizontally scalable storage. |
| `req.inf.stg.06` | Storage | The Architecture **must** support ephemeral storage (non-persistent) storage for Pods. |
| `req.inf.stg.07` | Storage | The Architecture **must** support persistent storage for Pods (*optional for deployment*). |
| `req.inf.ntw.01` | Network | The Architecture **must** support Container Network Interface (CNI). |
| `req.inf.ntw.02` | Network | The Architecture **must** support intra-node communications, such as between agents on a node and all pods on that node |
| `req.inf.ntw.03` | Network | The Architecture **must** support inter-node communications without NAT, such as communications between pods on a node with all other pods on all nodes |
| `req.inf.ntw.04` | Network | The Architecture **must** support low latency and high throughput traffic needs. |
| `req.inf.ntw.06` | Network | The Architecture **must** support network resiliency. |
| `req.inf.ntw.07` | Network | The Architecture **should** embrace open-based standards and technologies. |
| `req.inf.ntw.08` | Network | The Architecture **must** be fully redundant. |
| `req.inf.ntw.09` | Network | The Architecture **must** support API driven life-cycle management (LCM) of the infrastructure that allows repeatable, scalable and standardised handling of K8s clusters. LCM use cases to cover are: instantiation, termination, upgrade, scaling, and healing. |
| `req.inf.ntw.10` | Network | The networking solution **should** be configurable in an automated manner using openly published API definitions. |
| `req.inf.ntw.11` | Network | The networking solution **should** be able to be centrally administrated and configured. |
| `req.inf.ntw.12` | Network | The Architecture **must** support dual stack IPv4 and IPv6 for Kubernetes workloads. |
| `req.inf.ntw.14` | Network | The Architecture **must** support capabilities for integrating SDN controllers. |
| `req.inf.ntw.15` | Network | The Architecture **should** support Service Mesh Interface (SMI). |
| `req.inf.ntw.16` | Network | The Architecture **should**  support coexistence of multiple connection points in a pod. |
| `req.inf.acc.01` | Acceleration | The Architecture **should** support Application Specific Acceleration. |
| `req.inf.acc.02` | Acceleration | The Architecture **should** support NFVI Acceleration (such as SmartNICs). |
| `req.inf.vir.01`   | Virtual Infrastructure | The Architecture must support the capability for Containers to consume infrastructure resources abstracted by Host Operating Systems that are running within a virtual machine. |
| `req.inf.phy.01`  |  Physical Infrastructure | The Architecture must support the capability for Containers to consume infrastructure resources abstracted by Host Operating Systems that are running within a physical server. |

<!--
| `req.inf.com.02` | Compute | The Architecture **should** include industry standard hardware management systems at both HW device level (embedded) and HW platform level (external to device). |
| `req.inf.ntw.05` | Network | The Architecture **should** support service function chaining. |
| `req.inf.vir.01`   | Virtualisation |   The Architecture **must** support the capability for Containers to consume virtualised compute, storage and network resources.|
-->

<p align="center"><b>Table 2-2:</b> Kubernetes Architecture: Infrastructure Requirements</p>
Please note that "shared" is a reference to multi-tenant support and pooled storage resources.

<a name="2.3.3"></a>
### 2.3.3 Kubernetes Cluster Requirements

| Ref # | sub-category | Description |
|---|---|---|
| `req.kcm.07` | General | The Architecture **must** support policy driven horizontal auto-scaling of Kubernetes cluster. |

<!--
| `req.kcm.01` | General | The Architecture **must** allow infrastructure resource sharing within a Kubernetes cluster. |
| `req.kcm.02` | General | The Architecture **must** support discoverability of nodes and their features. |
| `req.kcm.03` | General | The Architecture **must** support scheduling of workloads based on Enhanced Platform Awareness (EPA) features such as CPU Pinning, huge-pages and SR-IOV. |
| `req.kcm.04` | General | The Architecture **must** include kubernetes artefacts (e.g., images, Helm charts, etc.) repository capabilities. |
| `req.kcm.05` | General | The Architecture **should** support multi-tenancy in Kubernetes cluster. |
| `req.kcm.06` | General | The Architecture **must** support resource tagging. |
| `req.kcm.08` | General | The Architecture **must** support workload resiliency. |
-->

<p align="center"><b>Table 2-3:</b> Kubernetes Architecture: Kubernetes Cluster Requirements</p>

<a name="2.3.4"></a>
### 2.3.4 Interfaces & APIs Requirements

| Ref # | sub-category | Description |
|---|---|---|
| `req.int.api.02` | API | The Architecture **must** leverage the Kubernetes APIs to discover and declaratively manage compute (NFVI and bare metal resources), network, and storage. |
| `req.int.api.03` | API | The Architecture **must** support the usage of a Kubernetes Application package manager using the Kubernetes API-s, like Helm v3. |
<!--
| `req.int.api.01` | API | The Architecture **must** provide Control API endpoints to cloud platform core services. |
-->

<p align="center"><b>Table 2.2.</b> Kubernetes Architecture: Interfaces and APIs Requirements </p>

<a name="2.3.5"></a>
### 2.3.5 Operations and LCM Requirements

| Ref # | sub-category | Description |
|---|---|---|
| `req.lcm.gen.01`	| General | The Architecture **must** support zero downtime expansion/change of physical capacity (compute hosts, storage increase/replacement). |
| `req.lcm.adp.01` | Automated deployment | The Architecture **must** allow for automated deployment, configuration, provisioning and life cycle management of multiple - declaratively specified - kubernetes clusters. |
| `req.lcm.adp.04` | Automated deployment | The Architecture **must** support declarative specifications of hardware, including compute, network, and storage, and software assets for automated deployment, configuration, maintenance, and life cycle management. |
| `req.lcm.adp.05` | Automated deployment | The Architecture **should** support automated process for Deployment and life-cycle management of CIM Instances. |
| `req.lcm.cid.01` | CI/CD | The Architecture **should** support integration with CI/CD Toolchain for NFVI and CIM components Automation. |

<!--
| `req.lcm.adp.02` | Automated deployment | The Architecture **must** support hitless upgrades of software provided by the cloud provider so that the availability of running workloads is not impacted. |
| `req.lcm.adp.03` | Automated deployment | The Architecture **should** support hitless upgrade of all software provided by the cloud provider that are not covered by `req.lcm.adp.02`. Whenever hitless upgrades are not feasible, attempt should be made to minimize the duration and nature of impact. |
-->

<p align="center"><b>Table 2-5:</b> Kubernetes Architecture: Operations and LCM Requirements </p>


<a name="2.3.6"></a>
### 2.3.6 Assurance Requirements

| Ref # | sub-category | Description |
|---|---|---|
| `req.asr.mon.01` | Integration | The Architecture **must** include integration with infrastructure components to support collection of telemetry for assurance monitoring and network intelligence. |
| `req.asr.mon.02` | Monitoring | The Architecture **should** support Network Intelligence capabilities that allow richer diagnostic capabilities which take as input broader set of data across the network and from CNF workloads. |
| `req.asr.mon.03` | Monitoring | The Architecture **must** allow for the collection and dissemination of performance and fault information. |
| `req.asr.mon.04` | Network | The NFVI Network Fabric and Network Operating System **must** provide network operational visibility through alarming and streaming telemetry services for operational management, engineering planning, troubleshooting, and network performance optimisation. |

<p align="center"><b>Table 2-6:</b> Kubernetes Architecture: Assurance Requirements</p>

<a name="2.3.7"></a>
### 2.3.7 Security Requirements

| Ref # | sub-category | Description |
|---|---|---|
| `req.sec.gen.01` | General | The Architecture **must** provide workload isolation. |
| `req.sec.gen.02` | General | The Architecture **must** support policy based RBAC. |
| `req.sec.gen.03` | General | The Architecture **must** support a centralised authentication and authorisation mechanism. |
| `req.sec.gen.04` | General | The Architecture **should** provide Operating System kernel isolation. |
| `req.sec.gen.05` | General | The Architecture **must** provide compute resources isolation. |
| `req.sec.gen.06` | General | The Architecture **must** provide storage resources isolation. |
| `req.sec.gen.07` | General | The Architecture **must** provide network resources isolation. |
| `req.sec.gen.08` | General | The Architecture **should** minimise the attack surface by ensuring only required services and processes are running on the Node Operating System. |
| `req.sec.gen.09` | General | The Architecture **should** support the ability to restrict resource, service, capabilities and interface permissions based on the principles of least privilege. |
| `req.sec.gen.10` | General | The Architecture **should** support the ability to conform to the Center for Internet Security (CIS) Benchmark for Kubernetes. |
| `req.sec.gen.11` | General | The Architecture **should** support the ability to secure API communications. |
| `req.sec.zon.01` | Zoning | The Architecture **must** support identity management. |
| `req.sec.zon.02` | Zoning | The Architecture **must** support password encryption. |
| `req.sec.zon.03` | Zoning | The Architecture **must** support data, at-rest and in-flight, encryption. |
| `req.sec.zon.04` | Zoning | The Architecture **must** support integration with Corporate Identity Management systems. |
| `req.sec.cmp.01` | Compliance | The Architecture **must** comply with all applicable national standards and regulations. |
| `req.sec.cmp.02` | Compliance | The Architecture **must** comply with all applicable regional standards and regulations. |
| `req.sec.ntw.01` | Networking | The Architecture **must** have the underlay network include strong access controls that comply with ISO 27001 and adhere to the V1.1 NIST Cybersecurity Framework. |
| `req.sec.ntw.02` | Networking | The Architecture **must** have all security audit logs stored in accordance with ISO27001. |
| `req.sec.ntw.03` | Networking | The Architecture **must** have the underlay network incorporate encrypted and/or private communications channels to ensure its security. |
| `req.sec.ntw.04` | Networking | The Architecture **must** configure all of the underlay network components to ensure the complete separation from the overlay customer deployments. |

<p align="center"><b>Table 2-7:</b> Kubernetes Architecture: Security Requirements </p>
