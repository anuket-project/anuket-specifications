[<< Back](../)

# 3. Cloud Infrastructure + VNF Target State & Specification
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Introduction](#3.1)
* [3.2 VNF profile](#3.2)
* [3.3 Cloud Infrastructure SW profile](#3.3)
* [3.4 Cloud Infrastructure Hardware Profile](#3.4)
* [3.5 Cloud Infrastructure Required State](#3.5)
* [3.6 Cloud Infrastructure and VIM Architecture](#3.6)
* [3.7 Cloud Infrastructure and VIM Component Level Architecture](#3.7)
* [3.8 Interface and API for Reference Implementation 1](#3.8)



<a name="3.1"></a>
## 3.1 Introduction

The VNF profile is used to describe every workload running on top of Cloud Infrastructure. The Cloud Infrastructure SW profile is used to describe the list of features provided by the hypervisor and host OS.

The CNTT Reference Model will be referenced as **RM** to avoid long and duplicated reference titles.

<a name="3.2"></a>
## 3.2 VNF profile


Any virtual network functions and/or cloud-native network functions must choose to run on one of the pre-defined of entries in Cloud Infrastructure Infrastructure Profiles Catalogue. As states in [RM: 4 Infrastructure Capabilities, Measurements and Catalogue: 4.2 Catalogue](../../../ref_model/chapters/chapter04.md#4.2), the entry uses the following naming convention.


`B/N <I opt> . <Flavour> . <S ext> . <A ext>`

B/N is used to specify the instance type (Basic, Network Intensive), different instance types are associated with different acceleration extensions, network characteristics ([RM: 4.2.4 Instance Types](../../../ref_model/chapters/chapter04.md#4.2.4)) and instance capabilities([RM: 4.2.5 Instance Capabilities Mapping](../../../ref_model/chapters/chapter04.md#4.2.5)).

Whereas:

  - `<I opt>` stands for network interface options, e.g., the range of vNIC Bandwidth of B instance shall be selected from n1 to n60, for C instance is from n10 to n300, for N instance is from n10 to n600. (RM: 4.2.2 Virtual Network Interface Specifications and Table 4-23: Virtual NIC Interfaces Options)

  - Instance capabilities do not explicitly appear on the naming convention, because some are common to all instance types so they are covered in the `<Flavour>` (RM: 4.2.1 Compute Flavours), additionally there are a few capabilities which bind to certain types, e.g., CPU pinning or NUMA support are only available for N instances, while CPU overbooking can only happen to B instance types but not for N. (See RM: Table 4-24 Mapping of Cloud Infrastructure Capabilities to Instance Types for full mapping details)

  - `<S ext>` stands for persistent storage extensions, contains the size and the performance settings (RM: Table 4-20: Storage Extension Options), note the storage extension is common to all instance types as <Flavours>
  - `<A ext>` stands for accelaration extensions, features like Transcoding and Programmable are associated with C instances (RM: 4.2.4.3.1 Compute Accleration Extensions), while IPSec and Crypto features only make scene with N instance (RM: 4.2.4.2.1 Network Acceleration Extensions),

Every VNF instance must declare its profiles explicitly, which can be used by VIM to allocate resources duration instantiation, also it would be useful to evaluate portability of workload.

|.conf | Basic | Network Intensive |
|------|-------|-------------------|
|#vCPU cores |Per selected \<Flavour>|Per selected \<Flavour>|
|Amount of RAM |Per selected \<Flavour>|Per selected \<Flavour>|
|Total instance (ephemeral) storage (GB) |Per selected \<Flavour>|Per selected \<Flavour>|
|Total instance (persistent) storage (GB) |Per selected |Per selected |
|n1, n2, n3, n4, n5, n6 | Y | N |
|n10, n20, n30, n40, n50, n60 | Y | Y |
|n25, n50, n75, n100, n125, n150 | N | Y |
|n50, n100, n150, n200, n250, n300 | N | Y |
|n100, n200, n300, n400, n500, n600 | N | Y |
|CPU pinning support | N | Y |
|NUMA support | N | Y |
|IPSec Acceleration) | N | Y |
|Crypto Acceleration | N | Y |
|Transcoding Acceleration | N | N |
|Programmable Acceleration | N | N |
|Enhanced Cache Management | E | E |
|Monitoring of L2-7 data | N | Y |
|CPU overbooking | 1:4 | 1:1 |
|vNIC QoS | N | Y |
|Huge page support | N | Y |
|Host CPU usage | Y | Y |
|Virtual compute resource (vCPU) usage | Y | Y |
|Host CPU utilization | Y | Y |
|Virtual compute resource (vCPU) utilization | Y | Y |
|External storage capacity | N | N |

> Open Point 1: Does ONAP have some relevant spec or VNF declaration schema so that CNTT can re-use/revise to cover what we need ? Or define a new one ?

> Open Point 2: What principles should be followed if some the pre-define VNF profile items does not match what actual requires ? How to adjust, "ceiling", "floor", "customise" ?

<a name="3.3"></a>
## 3.3 Cloud Infrastructure SW profile


[RM: 5.2 Cloud Infrastructure Software Profiles features and requirements](../../../ref_model/chapters/chapter05.md#5.2) defines the Cloud Infrastructure software layer. The profile depicts the feature status of the
  - virtual Compute (**nfvi.com.cfg.xxx** in RM Table 5-7: Virtual Compute features and configuration for the 3 types of SW profiles and **nfvi.com.acc.cfg.xxx** in Table 5-8: Virtual Compute Acceleration features),
  - storage (**nfvi.stg.cfg.xxx** in RM1: Table 5-9: Virtual Storage features and configuration for the 3 types of SW profiles and **nfvi.stg.acc.cfg.xxx** in Table 5-10: Virtual Storage Acceleration features)
  - networking configuration(see **nfvi.net.cfg.xxx** in Table 5-11 Virtual Networking features and configuration for the 3 types of SW profiles and **nfvi.net.acc.cfg.xxx** in Table 5-12 Virtual Networking Acceleration features)

This profile is the global settings for the whole Cloud Infrastructure, which means there should be only one entry per Cloud Infrastructure resource pool, i.e., Basic/Network

| .conf | Basic | Network Intensive |
|-------|----------------|----------------|
| CPU allocation ratio  | 4:1 | 1:1  |
| NUMA awareness | N | Y |
| CPU pinning capability | N | Y |
| Huge Pages | N | Y |
| Catalogue storage Types | Y  | Y  |
| Storage Block | Y | Y |
| Storage Object | Y | Y |
| Storage with replication | N | Y |
| Storage with encryption | Y | Y |
| Storage IOPS oriented | N | Y |
| Storage capacity oriented | N | N |
| vNIC interface | virtio1.1 |  virtio1.1|
| Overlay protocol | VXLAN, MPLSoUDP, GENEVE, other |  VXLAN, MPLSoUDP, GENEVE, other |
| NAT | Y | Y |
| Security Group | Y | Y |
| SFC support | N | Y |
| Traffic patterns symmetry | Y | Y |
| vSwitch optimisation | N | Y, DPDK |
| Support of HW offload | N | Y, support of SmartNic |
| Crypto acceleration | N  | Y |
| Crypto Acceleration Interface | N  | Y |

<a name="3.4"></a>
## 3.4 Cloud Infrastructure Hardware Profile
[RM1: 5.4 Cloud Infrastructure Hardware Profiles features and requirements](../../../ref_model/chapters/chapter05.md#5.4) defines the Cloud Infrastructure hardware layer profiles.The labs are typically provisioned with the minimal required hardware and thus it is difficult to partition the available hardware to provision/configure multiple Cloud Infrastructure profiles. However, when reference implementations and the follow up testing and verification are conducted, the hardware profile need to be clearly described. This is especially important for performance testing and verification.


| Reference | Feature | Description | Basic Type | Network Intensive |
|---------------------|-----------|---------------------------|--------|--------|
| nfvi.hw.cpu.cfg.001 | Number of CPU sockets | This determines the minimum number of CPU sockets within each host | 2| 2|
| nfvi.hw.cpu.cfg.002 | Number of cores per CPU | This determines the number of cores needed per each CPU. | 20 | 20 |
| nfvi.hw.cpu.cfg.003 | NUMA | NUMA support and BIOS configured to enable NUMA | N | Y | Y |
| nfvi.hw.cpu.cfg.004 | Simultaneous Multithreading (SMT) | This permits multiple independent threads of execution on a single core. | Y | Y|
| nfvi.hw.cac.cfg.001 | GPU | GPU | N | N |
| nfvi.hw.stg.hdd.cfg.001* | Local Storage HDD | Hard Disk Drive |  |  |
| nfvi.hw.stg.ssd.cfg.002* | Local Storage SSD | Solid State Drive | Recommended | Recommended |
| nfvi.hw.nic.cfg.001 | NIC Ports | Total Number of NIC Ports available in the host | 4 | 4 |
| nfvi.hw.nic.cfg.002 | Port Speed | Port speed specified in Gbps (minimum values) | 10 | 25 |
| nfvi.hw.pci.cfg.001 | PCIe slots | Number of PCIe slots available in the host | 8 | 8 |
| nfvi.hw.pci.cfg.002 | PCIe speed |  | Gen 3 | Gen 3 |
| nfvi.hw.pci.cfg.003 | PCIe Lanes |  | 8 | 8 |
| nfvi.hw.bdc.cfg.001 | Bonded VLAN ports |  | Y | Y |
| nfvi.hw.nac.cfg.001 | Cryptographic Acceleration | IPSec, Crypto |  N | Optional |
| nfvi.hw.nac.cfg.002 | SmartNIC | A SmartNIC that is used to offload network functionality to hardware | N | Optional  |
| nfvi.hw.nac.cfg.003 | Compression |  |  |


## 3.5 Cloud Infrastructure Required State
This sections describes the readiness of Cloud Infrastructure before the certification process can begin. Once the Cloud Infrastructure is configured with either of the profiles - B, N, a set of tests (for example functests) should be run in order to determine the readiness of the Cloud Infrastructure for certification.
#TODO : Identify the tests for this section


[RA1: Chapter 2.3 OpenStack Requirements](../../../ref_arch/openstack/chapters/chapter02.md#2.3) describes the requirements related to the following 8 domains: general(gen), infrastructure(inf), VIM(vim), Interface & API(int), Tenants(tnt), LCM(lcm), Assurance(asr), Security(sec).

| Ref # | Description |
|----|-------------------------------------------------------------------------------|
| `req.gen.ost.01` | **must** use OpenStack APIs.|
| `req.gen.ost.02` | **must** support dynamic request and configuration of virtual resources through APIs. |
| `req.gen.cnt.01` | **should** consist of stateless service components. However, where state is required it must be kept external to the components. |
| `req.gen.cnt.02` | **should** consist of service components implemented as microservices that are individually dynamically scalable. |
| `req.gen.scl.01` | **should** support policy driven auto-scaling. |
| `req.gen.rsl.01` | **must** support resilient OpenStack components that are required for the continued availability of running workloads. |
| `req.gen.rsl.02` | **should** support resilient OpenStack service components that are not subject to `req.gen.rsl.01`. |
| `req.gen.avl.01` | **must** provide High Availability for OpenStack components. |
| `req.inf.com.01` | **must** provide compute resources for VM instances.  |
| `req.inf.com.02` | **should** include industry standard hardware management systems at both HW device and platform level |
| `req.inf.com.03` | **should** support symmetrical CPU multi-processing with shared memory access as well as multi-threading. |
| `req.inf.com.04` | **must** be able to support multiple CPU Types to support Base, Network Intensive infrastructure profiles. |
| `req.inf.com.05` | **must** support Hardware Platforms with NUMA capabilities.|
| `req.inf.com.06` | **must** support CPU Pinning.|
| `req.inf.com.07` | **must** support different hardware configurations to support Base, Network Intensive infrastructure profiles. |
| `req.inf.stg.01` | **must** provide shared Block storage for VM Instances. |
| `req.inf.stg.02` | **must** provide shared Object storage for VM Instances. |
| `req.inf.stg.03` | **may** provide local file system storage solution for VM Instances. |
| `req.inf.stg.04` | **may** support Software Defined Storage (SDS) that seamlessly supports shared block storage, object storage and flat files. |
| `req.inf.stg.05` | **should** be able to accommodate VNFs that store back into its image through use of hypervisor attached volumes. |
| `req.inf.stg.06` | **should** make the immutable images available via location independent means. |
| `req.inf.stg.07` | **should** provide high-performance and horizontally scalable VM storage. |
| `req.inf.stg.08` | **should** allow use of externally provided large archival storage for its Backup / Restore / Archival needs. |
| `req.inf.stg.09` | **should** make available all non-host OS / Hypervisor / Host systems storage as network-based Block, File or Object Storage for tenant/management consumption. |
| `req.inf.ntw.01` | **must** provide virtual network interfaces to VM instances. |
| `req.inf.ntw.02` | **must** include capabilities for integrating SDN controllers to support provisioning of network services, from the OpenStack Neutron service, such as networking of VTEPs to the Border Edge based VRFs. |
| `req.inf.ntw.03` | **must** support low latency and high throughput traffic needs. |
| `req.inf.ntw.04` | **should** support service function chaining. |
| `req.inf.ntw.05` | **must** allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay such as VXLAN or Geneve). |
| `req.inf.ntw.06` | **should** support Distributed Virtual Routing (DVR) to allow compute nodes to route traffic efficiently. |
| `req.inf.ntw.07` | **must** support network resiliency. |
| `req.inf.ntw.08` | The NFVI Network Fabric **should** embrace the concepts of open networking and disaggregation using commodity networking hardware and disaggregated Network Operating Systems. |
| `req.inf.ntw.09` | The NFVI Network Fabric **should** embrace open-based standards and technologies. |
| `req.inf.ntw.10` | The NFVI Network Fabric **must** be capable of supporting highly available (Five 9’s or better) VNF workloads. |
| `req.inf.ntw.11` | The NFVI Network Fabric **should** be architected to provide a standardised, scalable, and repeatable deployment model across all applicable NFVI sites. |
| `req.inf.ntw.12` | The SDN solution **should** be configurable via orchestration or VIM systems in an automated manner using openly published API definitions. |
| `req.inf.ntw.13` | The SDN solution **should** be able to support federated networks. |
| `req.inf.ntw.14` | The SDN solution **should** be able to be centrally administrated and configured. |
| `req.inf.ntw.15` | **must** support multiple networking options for NFVI to support Base, Network Intensive infrastructure profiles. |
| `req.inf.ntw.16` | **must** support dual stack IPv4 and IPv6 for tenant networks and workloads. |
| `req.inf.ntw.17` | **should** use dual stack IPv4 and IPv6 for NFVI internal networks. |
| `req.inf.acc.01` | **should** support Application Specific Acceleration (exposed to VNFs). |
| `req.inf.acc.02` | **should** support NFVI Acceleration (such as SmartNICs). |
| `req.inf.acc.03` | **should not** rely on SR-IOV PCI-Pass through to provide acceleration to VNFs. |
| `req.vim.01` | **must** allow infrastructure resource sharing. |
| `req.vim.02` | **should** support deployment of OpenStack components in containers. |
| `req.vim.03` | **must** allow VIM to discover and manage NFVI resources. |
| `req.vim.04` | **must** support Enhanced Platform Awareness (EPA). |
| `req.vim.05` | **must** include image repository management. |
| `req.vim.06` | **must** allow orchestration solutions to be integrated with VIM. |
| `req.vim.07` | **must** support a multi-tenanted environment. |
| `req.vim.08` | **must** support resource tagging. |
| `req.vim.09` | **must** support horizontal scaling. |
| `req.int.api.01` | **must** provide Control API endpoints to cloud platform core services. |
| `req.int.api.02` | **must** provide GUI access to tenant facing cloud platform core services. |
| `req.int.api.03` | **must** provide APIs needed to discover and manage NFVI resources. |
| `req.int.acc.01` | **should** provide an open and standard acceleration interface to VNFs. |
| `req.int.acc.02` | **should not** rely on SR-IOV PCI-Pass through for acceleration interface exposed to VNFs. |
| `req.tnt.gen.01` | **must** support multi-tenancy. |
| `req.tnt.gen.02` | **must** support self-service dashboard (GUI) and APIs for users to deploy, configure and manage their workloads. |
| `req.lcm.gen.01`	| **must** support zero downtime expansion/change of physical capacity (compute hosts, storage increase/replacement). |
| `req.lcm.adp.01` | **should** allow for “cookie cutter” automated deployment, configuration, provisioning and management of multiple NFVI sites. |
| `req.lcm.adp.02` | **must** support hitless upgrades of software provided by the cloud provider so that the availability of running workloads is not impacted. |
| `req.lcm.adp.03` | **should** support hitless upgrade of all software provided by the cloud provider that are not covered by `req.lcm.adp.02`. Whenever hitless upgrades are not feasible, attempt should be made to minimize the duration and nature of impact. |
| `req.lcm.adp.04` | **should** support declarative specifications of hardware and software assets for automated deployment, configuration, maintenance and management. |
| `req.lcm.adp.05` | **should** support automated process for Deployment and life-cycle management of VIM Instances. |
| `req.lcm.cid.02` | **should** support integrating with CI/CD Toolchain for NFVI and VIM components Automation. |
| `req.asr.mon.01` | **must** include integration with various infrastructure components to support collection of telemetry for assurance monitoring and network intelligence. |
| `req.asr.mon.02` | **should** support Network Intelligence capabilities that allow richer diagnostic capabilities which take as input broader set of data across the network and from VNF workloads. |
| `req.asr.mon.03` | **must** allow for the collection and dissemination of performance and fault information. |
| `req.asr.mon.04` | The NFVI Network Fabric and Network Operating System **must** provide network operational visibility through alarming and streaming telemetry services for operational management, engineering planning, troubleshooting, and network performance optimisation. |
| `req.sec.gen.01` | **must** provide tenant isolation. |
| `req.sec.gen.02` | **must** support policy based RBAC. |
| `req.sec.gen.03` | **must** support a centralised authentication and authorisation mechanism. |
| `req.sec.zon.01` | **must** support identity management (specific roles and permissions assigned to a domain or tenant). |
| `req.sec.zon.02` | **must** support password encryption. |
| `req.sec.zon.03` | **must** support data, at-rest and in-flight, encryption. |
| `req.sec.zon.04` | **must** support integration with Corporate Identity Management systems. |
| `req.sec.cmp.02` | **must** comply with all applicable standards and regulations. |
| `req.sec.cmp.03` | **must** comply with all applicable regional standards and regulations. |
| `req.sec.ntw.01` | **must** have the underlay network include strong access controls that comply with ISO 27001 and adhere to the V1.1 NIST Cybersecurity Framework. |
| `req.sec.ntw.02` | **must** have all security logs stored in accordance with ISO27001. |
| `req.sec.ntw.03` | **must** have the underlay network incorporate encrypted and/or private communications channels to ensure its security. |
| `req.sec.ntw.04` | **must** configure all of the underlay network components to ensure the complete separation from the overlay customer deployments. |

[RA1: Chapter 5 Interfaces and APIs](../../../ref_arch/openstack/chapters/chapter05.md) describes the baseline version regarding to OpenStack Service APIs.

| OpenStack Service | Link for API list | Baseline Version | Minimal API Microversion |
|------------------|--------------------|------------------------|------------------------|
| Identity: Keystone | https://docs.openstack.org/api-ref/identity/v3/index.html?expanded=#identity-api-operations  | 3 | 3.8 |
| Compute: Nova | https://docs.openstack.org/api-ref/compute/  | v2.1 | 2.53 |
| Networking: Neutron | https://docs.openstack.org/api-ref/network/  | v2.0 | NA |
| Imaging: Glance | https://docs.openstack.org/api-ref/image/v2/index.html#images  | v2 | 2.5 |
| Block Storage: Cinder | https://docs.openstack.org/api-ref/block-storage/v3/index.html#api-versions  | v3 | 3.43 |
| Object Storage: Swift | https://docs.openstack.org/api-ref/object-store/  | v1 | NA |
| Orchestration: Heat | https://docs.openstack.org/api-ref/orchestration/v1/index.html#api-versions  | v1.0 | NA |
| Acceleration: Cyborg | https://docs.openstack.org/cyborg/pike/userdoc/api.html | v1.0 | NA |

## 3.6 Cloud Infrastructure and VIM Architecture
This sections concludes the expectation for Cloud Infrastructure and VIM architecture according to [RA1: Chapter 3 Cloud Infrastructure + VIM Architecture](../../../ref_arch/openstack/chapters/chapter03.md)

| Requirement Area | Description |
|----|-------------------------------------------------------------------------------|
| Multi-Tenancy | permit to host several VNF projects with the insurance to have isolated environment for each. Naming and quotas are kept consistent (details TBD)|
|Virtual Compute |The virtual compute resources (vCPU and vRAM) used by the VNFs behave like their physical counterparts. The configuration of the virtual resources will depend on the profile and the flavour needed to host VNF components.|
|Virtual Storage|The three storage services offered by NFVI are:Persistent storage, Ephemeral storage, Image storage |
|Virtual Networking Neutron standalone|Allows users to create networks, subnets, ports, routers etc. Facilitates traffic isolation between different subnets. Support multiple network segments. Create routers to connect layer 2 networks|
|Virtual Networking – 3rd party SDN solution|Utilize OpenStack Neutron to support plugins for various SDN controllers include the standard ML-2 plugin and vendor product specific monolithic plugins.|
|Acceleration|The hardware accelerator covers the options for ASICs, SmartNIC, FPGAs, GPU etc. to offload the main CPU, and to accelerate workload performance. NFVI should manage the accelerators by plugins and provide the acceleration capabilities to VNFs.With the acceleration abstraction layer defined, hardware accelerators as well as software accelerators can be abstracted as a set of acceleration functions (or acceleration capabilities) which exposes a common API to either the VNF or the host.|
|VIM core services| horizon, heat, keystone, nova, neutron, cinder, glance, swift, Ironic(optional only for bare-metal management)|
|Foundation services| Foundation Node To build and lifecycle manage an OpenStack cloud it is typically necessary to deploy a server or virtual machine as a deployment node. This function must be able to manage the bare-metal provisioning of the hardware resources( can be detached from the OpenStack cloud). Capabilities include building the cloud (control, compute, storage, network hardware resources), Patch management / upgrades / change management, Grow / Shrink resources|
|Cloud Controller Services|All components must be deployed within a high available architecture that can withstand at least a single node failure and respects the anti-affinity rules for the location of the services|
|Physical Network|The recommended network architecture is spine and leaf topology; however, for small sites, a legacy topology (access/aggregation switches) can be set up.

## 3.7 Cloud Infrastructure and VIM Component Level Architecture
This sections concludes the expectation for Cloud Infrastructure and VIM component level architecture according to [RA1: Chapter 4 Cloud Infrastructure + VIM Component Level Architecture](../../../ref_arch/openstack/chapters/chapter04.md)

Requirement for control node:

| Requirement Area | Description |
|----|-------------------------------------------------------------------------------|
|SLA |Minimum 3 nodes for high availability|
|HW specifications |Boot disks are dedicated with Flash technology disks|

Requirement for compute node:

| Requirement Area | Description |
|----|-------------------------------------------------------------------------------|
|BIOS requirement| boot parameters should follow the table defined in [RA1: 4.2.2.5 Compute Nodes](../../../ref_arch/openstack/chapters/chapter04.md#4.2.2.5) |
|SLA|minimum: two nodes per profile|
|sizing rules| should follow the table defined in [RA1: 4.2.2.5 Compute Nodes](../../../ref_arch/openstack/chapters/chapter04.md#4.2.2.5) |

Requirement for network fabric:

| Requirement Area | Description |
|----|-------------------------------------------------------------------------------|
|Network Layout| should follow the table in [RA1: 4.2.3.2 High Level Logical Network Layout](../../../ref_arch/openstack/chapters/chapter04.md#4.2.3.2)|

Consumable Infrastructure Resources and Services

| Requirement Area | Description |
|----|-------------------------------------------------------------------------------|
|Support for Profiles and T-shirt instance types| should follow tabels specified in [RA1: 4.4.1 Support for Profiles and T-shirt instance types](../../../ref_arch/openstack/chapters/chapter04.md#4.4.1)
|Availability| The NFVI doesn’t provide any resiliency mechanisms at the service level. Any VM restart shall be triggered by the VNF Manager instead of OpenStack|
|NUMA | For Network intensive instances, VNF Component should fit into a single NUMA zone for performance reason|

## 3.8 Interface and API for Reference Implementation 1

The following table lists the interface for RI1.

| OpenStack Service     | Link for API list                                    | **API Version** | **Minimal API Microversion** |
|-----------------------|------------------------------------------------------|------|------|
| Identity: Keystone    | https://docs.openstack.org/api-ref/identity/v3/      | 3    | 3.8  |
| Compute: Nova         | https://docs.openstack.org/api-ref/compute/          | v2.1 | 2.53 |
| Networking: Neutron   | https://docs.openstack.org/api-ref/network/v2/       | v2.0 |      |
| Image: Glance         | https://docs.openstack.org/api-ref/image/v2/         | v2   | 2.5  |
| Block Storage: Cinder | https://docs.openstack.org/api-ref/block-storage/v3/ | v3   | 3.43 |
| Object Storage: Swift | https://docs.openstack.org/api-ref/object-store/     | v1   |      |
| Placement             | https://docs.openstack.org/api-ref/placement/        | v1   | 1.10 |
| Orchestration: Heat   | https://docs.openstack.org/api-ref/orchestration/v1/ | v1   |      |
| Acceleration: Cyborg  | https://docs.openstack.org/api-ref/accelerator/v2/   | v2   |      |
| K8S API               | https://kubernetes.io/docs/concepts/overview/kubernetes-api/ |  |  |
| KVM APIs              | https://www.kernel.org/doc/Documentation/virtual/kvm/api.txt |  |  |
| Libvirt APIs          | https://libvirt.org/html/index.html                  |      |      |
