[<< Back](../../openstack)

# 2. Architecture Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction.](#2.1)
* [2.2 Reference Model Requirements.](#2.2)
* [2.3 Architecture and OpenStack Requirements.](#2.3)

<a name="2.1"></a>
## 2.1 Introduction.

**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the reference architecture and reflected in any implementation targeting this reference architecture. The same applies to _must not_.

**should**: Requirements that are marked as _should_ are expected to be fulfilled by the reference architecture but it is up to each service provider to accept an implementation targeting this reference architecture that is not reflecting on any of those requirements. The same applies to _should not_.
> RFC2119

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.

<a name="2.2"></a>
## 2.2 Reference Model Requirements.

Traceability to Reference Model.

<a name="2.3"></a>
## 2.3 Architecture and OpenStack Requirements.

<a name="2.3.1"></a>
### 2.3.1 General

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.gen.ost.01` | Open source | The Architecture **must** use OpenStack APIs.|
| `req.gen.ost.02` | Open source | The Architecture **must** support dynamic request and configuration of virtual resources (compute, network, storage) through OpenStack APIs. |
| `req.gen.cnt.01` | Cloud nativeness | The Architecture **should** consist of stateless service components. However, where state is required it must be kept external to the component. |
| `req.gen.cnt.02` | Cloud nativeness | The Architecture **should** consist of service components implemented as microservices that are individually dynamically scalable. |
| `req.gen.scl.01` | Scalability | The Architecture **should** support policy driven auto-scaling. |
| `req.gen.rsl.01` | Resiliency | The Architecture **must** support resilient OpenStack components that are required for the continued availability of running workloads. |
| `req.gen.rsl.02` | Resiliency | The Architecture **should** support resilient OpenStack service components that are not subject to `req.gen.rsl.01`. |
| `req.gen.avl.01` | Availability | The Architecture **must** provide High Availability for OpenStack components. |


<p align="center"><b>Table 2-1:</b> OpenStack General Requirements.</p>

<a name="2.3.2"></a>
### 2.3.2 Infrastructure

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.inf.com.01` | Compute | The Architecture **must** provide compute resources for VM instances.  |
| `req.inf.com.02` | Compute | The Architecture **should** include industry standard hardware management systems at both HW device level (embedded) and HW platform level (external to device). |
| `req.inf.com.03` | Compute | The Architecture **should** support symmetrical CPU multi-processing with shared memory access as well as multi-threading. |
| `req.inf.com.04` | Compute | The Architecture **must** be able to support multiple CPU SKU options to support various infrastructure profiles (Base, Network Intensive, and Compute Intensive).|
| `req.inf.com.05` | Compute | The Architecture **must** support Hardware Platforms with NUMA capabilities.|
| `req.inf.com.06` | Compute | The Architecture **must** support CPU Pinning.|
| `req.inf.com.07` | Compute | The Architecture **must** support different hardware configurations to support various infrastructure profiles (Base, Network Intensive, and Compute Intensive).|
| `req.inf.stg.01` | Storage | The Architecture **must** provide shared Block storage for VM Instances.
| `req.inf.stg.02` | Storage | The Architecture **must** provide shared Object storage for VM Instances.
| `req.inf.stg.03` | Storage | The Architecture **may** provide local file system storage solution for VM Instances.
| `req.inf.stg.04` | Storage | The Architecture **may** support Software Defined Storage (SDS) that seamlessly supports shared block storage, object storage and flat files. |
| `req.inf.stg.05` | Storage | The Architecture **should** be able to accommodate VNFs that store back into its image through use of hypervisor attached volumes. |
| `req.inf.stg.06` | Storage | The Architecture **should** make the immutable images available via location independent means. |
| `req.inf.stg.07` | Storage | The Architecture **should** provide high-performance and horizontally scalable VM storage. |
| `req.inf.stg.08` | Storage | The Architecture **should** allow use of externally provided large archival storage for its Backup / Restore / Archival needs. |
| `req.inf.stg.09` | Storage | The Architecture **should** make available all non-host OS / Hypervisor / Host systems storage as network-based Block, File or Object Storage for tenant/management consumption. |
| `req.inf.ntw.01` | Network | The Architecture **must** provide virtual network interfaces to VM instances. |
| `req.inf.ntw.02` | Network | The Architecture **must** include capabilities for integrating SDN controllers to support provisioning of network services, from the OpenStack Neutron service, such as networking of VTEPs to the Border Edge based VRFs. |
| `req.inf.ntw.03` | Network | The Architecture **must** support low latency and high throughput traffic needs. |
| `req.inf.ntw.04` | Network | The Architecture **should** support service function chaining. |
| `req.inf.ntw.05` | Network | The Architecture **must** allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay such as VXLAN or Geneve). |
| `req.inf.ntw.06` | Network | The Architecture **should** support Distributed Virtual Routing (DVR) to allow compute nodes to route traffic efficiently. |
| `req.inf.ntw.07` | Network | The Architecture **must** support network resiliency. |
| `req.inf.ntw.08` | Network | The NFVI Network Fabric **should** embrace the concepts of open networking and disaggregation using commodity networking hardware and disaggregated Network Operating Systems. |
| `req.inf.ntw.09` | Network | The NFVI Network Fabric **should** embrace open-based standards and technologies. |
| `req.inf.ntw.10` | Network | The NFVI Network Fabric **must** be capable of supporting highly available (Five 9’s or better) VNF workloads. |
| `req.inf.ntw.11` | Network | The NFVI Network Fabric **should** be architected to provide a standardised, scalable, and repeatable deployment model across all applicable NFVI sites. |
| `req.inf.ntw.12` | Network | The SDN solution **should** be configurable via orchestration or VIM systems in an automated manner using openly published API definitions. |
| `req.inf.ntw.13` | Network | The SDN solution **should** be able to support federated networks. |
| `req.inf.ntw.14` | Network | The SDN solution **should** be able to be centrally administrated and configured. |
| `req.inf.ntw.15` | Network | The Architecture **must** support multiple networking options for NFVI to support various infrastructure profiles (Base, Network Intensive, and Compute Intensive).|
| `req.inf.ntw.16` | Network | The Architecture **must** support dual stack IPv4 and IPv6 for tenant networks and workloads.|
| `req.inf.ntw.17` | Network | The Architecture **should** use dual stack IPv4 and IPv6 for NFVI internal networks.|
| `req.inf.acc.01` | Acceleration | The Architecture **should** support Application Specific Acceleration (exposed to VNFs). |
| `req.inf.acc.02` | Acceleration | The Architecture **should** support NFVI Acceleration (such as SmartNICs). |
| `req.inf.acc.03` | Acceleration | The Architecture **should not** rely on SR-IOV PCI-Pass through to provide acceleration to VNFs. |

<p align="center"><b>Table 2-2:</b> OpenStack Infrastructure Requirements.</p>

<a name="2.3.3"></a>
### 2.3.3 VIM

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.vim.01` | General | The Architecture **must** allow infrastructure resource sharing. |
| `req.vim.02` | General | The Architecture **should** support deployment of OpenStack components in containers. |
| `req.vim.03` | General | The Architecture **must** allow VIM to discover and manage NFVI resources. |
| `req.vim.04` | General | The Architecture **must** support Enhanced Platform Awareness (EPA). |
| `req.vim.05` | General | The Architecture **must** include image repository management. |
| `req.vim.06` | General | The Architecture **must** allow orchestration solutions to be integrated with VIM. |
| `req.vim.07` | General | The Architecture **must** support a multi-tenanted environment. |
| `req.vim.08` | General | The Architecture **must** support resource tagging. |
| `req.vim.09` | General | The Architecture **must** support horizontal scaling. |

<p align="center"><b>Table 2-3:</b> OpenStack VIM Requirements.</p>


<a name="2.3.4"></a>
### 2.3.4 Interfaces & APIs

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.int.api.01` | API | The Architecture **must** provide Control API endpoints to cloud platform core services. |
| `req.int.api.02` | API | The Architecture **must** provide GUI access to tenant facing cloud platform core services. |
| `req.int.api.03` | API | The Architecture **must** provide APIs needed to discover and manage NFVI resources. |
| `req.int.acc.01` | Acceleration | The Architecture **should** provide an open and standard acceleration interface to VNFs. |
| `req.int.acc.02` | Acceleration | The Architecture **should not** rely on SR-IOV PCI-Pass through for acceleration interface exposed to VNFs. |

<p align="center"><b>Table 2-4:</b> OpenStack Interfaces and APIs Requirements.</p>

<a name="2.3.5"></a>
### 2.3.5 Tenants

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.tnt.gen.01` | General | The Architecture **must** support multi-tenancy. |
| `req.tnt.gen.02` | General | The Architecture **must** support self-service dashboard (GUI) and APIs for users to deploy, configure and manage their workloads. |

<p align="center"><b>Table 2-5:</b> OpenStack Tenants Requirements.</p>

<a name="2.3.6"></a>
### 2.3.6 LCM

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.lcm.gen.01`	| General | The Architecture **must** support zero downtime expansion/change of physical capacity (compute hosts, storage increase/replacement). |
| `req.lcm.adp.01` | Automated deployment | The Architecture **should** allow for “cookie cutter” automated deployment, configuration, provisioning and management of multiple NFVI sites. |
| `req.lcm.adp.02` | Automated deployment | The Architecture **must** support hitless upgrades of software provided by the cloud provider so that the availability of running workloads is not impacted. |
| `req.lcm.adp.03` | Automated deployment | The Architecture **should** support hitless upgrade of all software provided by the cloud provider that are not covered by `req.lcm.adp.02`. Whenever hitless upgrades are not feasible, attempt should be made to minimize the duration and nature of impact. |
| `req.lcm.adp.04` | Automated deployment | The Architecture **should** support declarative specifications of hardware and software assets for automated deployment, configuration, maintenance and management. |
| `req.lcm.adp.05` | Automated deployment | The Architecture **should** support automated process for Deployment and life-cycle management of VIM Instances. |
| `req.lcm.cid.02` | CI/CD | The Architecture **should** support integrating with CI/CD Toolchain for NFVI and VIM components Automation. |

<p align="center"><b>Table 2-6:</b> OpenStack LCM Requirements.</p>

<a name="2.3.7"></a>
### 2.3.7 Assurance

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.asr.mon.01` | Integration | The Architecture **must** include integration with various infrastructure components to support collection of telemetry for assurance monitoring and network intelligence. |
| `req.asr.mon.02` | Monitoring | The Architecture **should** support Network Intelligence capabilities that allow richer diagnostic capabilities which take as input broader set of data across the network and from VNF workloads. |
| `req.asr.mon.03` | Monitoring | The Architecture **must** allow for the collection and dissemination of performance and fault information. |
| `req.asr.mon.04` | Network | The NFVI Network Fabric and Network Operating System **must** provide network operational visibility through alarming and streaming telemetry services for operational management, engineering planning, troubleshooting, and network performance optimisation. |

<p align="center"><b>Table 2-7:</b> OpenStack Assurance Requirements.</p>

<a name="2.3.8"></a>
### 2.3.8 Security

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.sec.gen.01` | General | The Architecture **must** provide tenant isolation. |
| `req.sec.gen.02` | General | The Architecture **must** support policy based RBAC. |
| `req.sec.gen.03` | General | The Architecture **must** support a centralised authentication and authorisation mechanism. |
| `req.sec.zon.01` | Zoning | The Architecture **must** support identity management (specific roles and permissions assigned to a domain or tenant). |
| `req.sec.zon.02` | Zoning | The Architecture **must** support password encryption. |
| `req.sec.zon.03` | Zoning | The Architecture **must** support data, at-rest and in-flight, encryption. |
| `req.sec.zon.04` | Zoning | The Architecture **must** support integration with Corporate Identity Management systems. |
| `req.sec.cmp.02` | Compliance | The Architecture **must** comply with all applicable standards and regulations. |
| `req.sec.cmp.03` | Compliance | The Architecture **must** comply with all applicable regional standards and regulations. |
| `req.sec.ntw.01` | Networking | The Architecture **must** have the underlay network include strong access controls that comply with ISO 27001 and adhere to the V1.1 NIST Cybersecurity Framework. |
| `req.sec.ntw.02` | Networking | The Architecture **must** have all security logs stored in accordance with ISO27001. |
| `req.sec.ntw.03` | Networking | The Architecture **must** have the underlay network incorporate encrypted and/or private communications channels to ensure its security. |
| `req.sec.ntw.04` | Networking | The Architecture **must** configure all of the underlay network components to ensure the complete separation from the overlay customer deployments. |

<p align="center"><b>Table 2-8:</b> OpenStack Security Requirements.</p>

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
