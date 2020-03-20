[<< Back](../../openstack)

# 2. Architecture Requirements
<p align="right"><img src="../figures/bogo_dfp.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction](#2.1)
* [2.2 Reference Model Requirements](#2.2)
* [2.3 Architecture and OpenStack Requirements](#2.3)
  * [2.3.1 General Requirements](#2.3.1)
  * [2.3.2 Infrastructure Requirements](#2.3.2)
  * [2.3.3 VIM Requirements](#2.3.3)
  * [2.3.4 Interfaces & APIs Requirements](#2.3.4)
  * [2.3.5 Tenant Requirements](#2.3.5)
  * [2.3.6 LCM Requirements](#2.3.6)
  * [2.3.7 Assurance Requirements](#2.3.7)
  * [2.3.8 Security Requirements](#2.3.8)
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
## 2.1 Introduction.

**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the reference architecture and reflected in any implementation targeting this reference architecture. The same applies to _must not_.

**should**: Requirements that are marked as _should_ are expected to be fulfilled by the reference architecture but it is up to each service provider to accept an implementation targeting this reference architecture that is not reflecting on any of those requirements. The same applies to _should not_.
> RFC2119

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.

This chapter includes both "Requirements" that must be satisifed in an RA-1 conformant implementation and "Recommendations" that are optional for implementation.

<a name="2.2"></a>
## 2.2 Reference Model Requirements.

Traceability to Reference Model.

<a name="2.3"></a>
## 2.3 Architecture and OpenStack Requirements

"Architecture" in this chapter refers to NFVI + VIM (as specified in Reference Model Chapter 3).

<a name="2.3.1"></a>
### 2.3.1 General Requirements

| Ref # | sub-category | Description | Traceability |
|----|---------------|---------------------|---------------|
| `req.gen.ost.01` | Open source | The Architecture **must** use OpenStack APIs.| [RA-1 5.3](./chapter05.md#53-consolidated-set-of-apis) |
| `req.gen.ost.02` | Open source | The Architecture **must** support dynamic request and configuration of virtual resources (compute, network, storage) through OpenStack APIs. | [RA-1 5.3](./chapter05.md#53-consolidated-set-of-apis) |
| `req.gen.rsl.01` | Resiliency | The Architecture **must** support resilient OpenStack components that are required for the continued availability of running workloads. | |
| `req.gen.avl.01` | Availability | The Architecture **must** provide High Availability for OpenStack components. | [RA-1 4.2 "Underlying Resources"](./chapter04.md#42-underlying-resources) |


<p align="center"><b>Table 2-1:</b> General Requirements</p>

<a name="2.3.2"></a>
### 2.3.2 Infrastructure Requirements

| Ref # | sub-category | Description |  Traceability |
|----|--------------|---------------------|-----------|
| `req.inf.com.01` | Compute | The Architecture **must** provide compute resources for VM instances. | [RA-1 3.3.1.4 "Cloud Workload Services"](./chapter03.md#3314-cloud-workload-services) |
| `req.inf.com.04` | Compute | The Architecture **must** be able to support multiple CPU SKU options to support various infrastructure profiles (Base, and Network Intensive<!-- , and Compute Intensive -->).| [RA-1 4.4.1. "Support for Profiles and T-shirt instance types"](./chapter04.md#441-support-for-profiles-and-t-shirt-instance-types) |
| `req.inf.com.05` | Compute | The Architecture **must** support Hardware Platforms with NUMA capabilities.| [RA-1 4.4.1. "Support for Profiles and T-shirt instance types"](./chapters/chapter04.md#441-support-for-profiles-and-t-shirt-instance-types) |
| `req.inf.com.06` | Compute | The Architecture **must** support CPU Pinning of the vCPUs of VM instance.| [RA-1 4.4.1. "Support for Profiles and T-shirt instance types"](./chapter04.md#441-support-for-profiles-and-t-shirt-instance-types) |
| `req.inf.com.07` | Compute | The Architecture **must** support different hardware configurations to support various infrastructure profiles (Base, and Network Intensive<!-- , and Compute Intensive -->).| [RA-1 3.3.3. "Host aggregates providing resource pooling"](./chapter03.md#333-host-aggregates-providing-resource-pooling) |
| `req.inf.com.08` | Compute | The Architecture **must** support allocating certain number of host cores/threads to non-tenant workloads such as for OpenStack services. | [Dedicating host core/sibling threads to certain workloads (e.g., OpenStack services](https://docs.openstack.org/nova/latest/configuration/config.html#compute.cpu_dedicated_set). Please see example, ["Configuring libvirt compute nodes for CPU pinning"](https://docs.openstack.org/nova/latest/admin/cpu-topologies.html) |
| `req.inf.com.09` | Compute | The Architecture **must** ensure that the host cores/threads assigned to a workload are thread-sibling aware: that is, that a core and its associated SMT threads are either all assigned to non-tenant workloads or all assigned to tenant workloads. | Achieved through configuring the "cpu_dedicated_set" and "cpu_shared_set" parameters in nova.conf correctly. |
| `req.inf.stg.01` | Storage | The Architecture **must** provide remote (not directly attached to the host) Block storage for VM Instances. | [RA-1 3.4.2.3. "Storage"](./chapter03.md#3423-storage) |
| `req.inf.stg.02` | Storage | The Architecture **should** provide Object storage for VM Instances. | OpenStack Swift Service ([RA-1 4.3.1.4 "Swift"](./chapter04.md#4314-swift)) |
| `req.inf.stg.03` | Storage | The Architecture **may** provide a file system service (file system storage solution) for VM Instances. | [RA-1 4.2.4. "Storage Backend"](./chapter04.md#424-storage-backend) |
| `req.inf.stg.04` | Storage | The Architecture **may** support Software Defined Storage (SDS) that seamlessly supports shared block storage, object storage and flat files. | [RA-1 4.2.4.1. "Ceph Storage Cluster"](./chapter04.md#4241-ceph-storage-cluster) |
| `req.inf.stg.06` | Storage | The Architecture **should** make the immutable images available via location independent means. | [RA-1 4.3.1.2. "Glance"](./chapter04.md#4312-glance) |
| `req.inf.stg.07` | Storage | The Architecture **should** provide high-performance and horizontally scalable VM storage. | [RA-1 4.2.4.1. "Ceph Storage Cluster"](./chapter04.md#4241-ceph-storage-cluster) |
| `req.inf.stg.10` | Storage | The Architecture **should** provide local Block storage for VM Instances. | [RA-1 "Virtual Storage"](./chapter03.md#323-virtual-storage) |
| `req.inf.stg.11` | Storage | The Architecture **should** support the Block storage capabilities specified in https://docs.openstack.org/api-ref/block-storage/. | [RA-1 5.2.3. "Cinder"](./chapter05.md#523-cinder) |
| `req.inf.ntw.01` | Network | The Architecture **must** provide virtual network interfaces to VM instances. | [RA-1 5.2.5. "Neutron" ](./chapter05.md#525-neutron) |
| `req.inf.ntw.02` | Network | The Architecture **must** include capabilities for integrating SDN controllers to support provisioning of network services, from the OpenStack Neutron service, such as networking of VTEPs to the Border Edge based VRFs. | [RA-1 3.2.5. "Virtual Networking – 3rd party SDN solution"](./chapter03.md#325-virtual-networking--3rd-party-sdn-solution) |
| `req.inf.ntw.03` | Network | The Architecture **must** support low latency and high throughput traffic needs. | [RA-1 4.2.3. "Network Fabric"](./chapter04.md#423-network-fabric) |
| `req.inf.ntw.05` | Network | The Architecture **must** allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay such as VXLAN or Geneve). | [RA-1 4.2.3. "Network Fabric"](./chapter04.md#423-network-fabric) |
| `req.inf.ntw.07` | Network | The Architecture **must** support network resiliency. | [RA-1 3.4.2.2. "Network"](./chapter03.md#3422-network) |
| `req.inf.ntw.10` | Network | The NFVI Network Fabric **must** be capable of enabling highly available (Five 9’s or better) NFVI. | [RA-1 3.4.2.2. "Network"](./chapter03.md#3422-network) |
| `req.inf.ntw.15` | Network | The Architecture **must** support multiple networking options for NFVI to support various infrastructure profiles (Base, Network Intensive<!-- , and Compute Intensive -->).| [RA-1 4.2.3.4. "Neutron ML2-plugin Integration"](./chapter04.md#4234-neutron-ml2-integration) and ["OpenStack Neutron Plugins"](https://wiki.openstack.org/wiki/Neutron_Plugins_and_Drivers) |
| `req.inf.ntw.16` | Network | The Architecture **must** support dual stack IPv4 and IPv6 for tenant networks and workloads.| |
| `req.inf.ntw.17` | Network | The Architecture **should** use dual stack IPv4 and IPv6 for NFVI internal networks.| |
| `req.inf.ntw.17` | Network | The Architecture **should** support the network extensions specified in https://docs.openstack.org/api-ref/network/v2/.| [RA-1 5.2.5. "Neutron"](./chapter05.md#525-neutron) |
| `req.inf.acc.01` | Acceleration | The Architecture **should** support Application Specific Acceleration (exposed to VNFs). | [RA-1 3.2.6. "Acceleration"](./chapter03.md#326-acceleration) and [RA-1 4.3.1.10. "Cyborg"](./chapter04.md#43110-cyborg) |
| `req.inf.acc.02` | Acceleration | The Architecture **should** support NFVI Acceleration (such as SmartNICs). | ["OpenStack Future - Specs defined"](https://specs.openstack.org/openstack/neutron-specs/specs/stein/neutron-ovs-agent-support-baremetal-with-smart-nic.html) |

<p align="center"><b>Table 2-2:</b> Infrastructure Requirements</p>

<a name="2.3.3"></a>
### 2.3.3 VIM Requirements

| Ref # | sub-category | Description |  Traceability |
|----|----------------|----------------------|-----------|
| `req.vim.01` | General | The Architecture **must** allow infrastructure resource sharing. | [RA-1 3.2. "Consumable Infrastructure Resources and Services"](./chapter03.md#32-consumable-infrastructure-resources-and-services) |
| `req.vim.02` | General | The Architecture **should** support deployment of OpenStack components in containers. | [RA-1 4.3.2. "Containerised OpenStack Services"](./chapter04.md#432-containerised-openstack-services) |
| `req.vim.03` | General | The Architecture **must** allow VIM to discover and manage NFVI resources. | [RA-1 5.2.7. "Placement"](./chapter05.md#527-placement) |
| `req.vim.05` | General | The Architecture **must** include image repository management. | [RA-1 4.3.1.2. "Glance"](./chapter04.md#4312-glance) |
| `req.vim.07` | General | The Architecture **must** support multi-tenancy. | [RA-1 3.2.1. "Multi-Tenancy"](./chapter03.md#321-multi-tenancy-execution-environment) |
| `req.vim.08` | General | The Architecture **must** support resource tagging. | ["OpenStack Resource Tags"](https://specs.openstack.org/openstack/api-wg/guidelines/tags.html) |

<p align="center"><b>Table 2-3:</b> VIM Requirements</p>


<a name="2.3.4"></a>
### 2.3.4 Interfaces & APIs Requirements

| Ref # | sub-category | Description |  Traceability |
|----|----------|--------------------|------------|
| `req.int.api.01` | API | The Architecture **must** provide APIs to access all mandatory features of the cloud platform core services for the given CNTT OpenStack release. | [RA-1 5.3. "Consolidated Set of APIs"](.s/chapter05.md#53-consolidated-set-of-apis) |
| `req.int.api.02` | API | The Architecture **must** provide GUI access to tenant facing cloud platform core services. | [RA-1 4.3.1.9 "Horizon"](./chapter04.md#4319-horizon) |
| `req.int.api.03` | API | The Architecture **must** provide APIs needed to discover and manage NFVI resources. | [RA-1 5.2.7. "Placement"](./chapter05.md#527-placement) |
| `req.int.api.04` | API | The Architecture must expose the latest version and microversion of the APIs for the given CNTT OpenStack release for each of the OpenStack core services | [RA-1 5.2 Core OpenStack Services APIs](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter05.md#52-core-openstack-services-apis) |
| `req.int.acc.01` | Acceleration | The Architecture **should** provide an open and standard acceleration interface to VNFs. | [RA-1 5.3.4. "Cyborg"](./chapter05.md#534-cyborg) |


<p align="center"><b>Table 2-4:</b> Interfaces and APIs Requirements</p>

<a name="2.3.5"></a>
### 2.3.5 Tenant Requirements

| Ref # | sub-category | Description |  Traceability |
|----|--------------|---------------|-----------------|
| `req.tnt.gen.01` | General | The Architecture **must** support multi-tenancy. |  **duplicate of req.vim.07** |
| `req.tnt.gen.02` | General | The Architecture **must** support self-service dashboard (GUI) and APIs for users to deploy, configure and manage their workloads. | [RA-1 4.3.1.9 "Horizon"](./chapter04.md#4319-horizon) and [3.3.1.4 Cloud Workload Services](./chapter03.md#3314-cloud-workload-services) |

<p align="center"><b>Table 2-5:</b> Tenant Requirements</p>

<a name="2.3.6"></a>

### 2.3.6 Operations and LCM

| Ref # | sub-category | Description |  Traceability |
|----|----------|-------------|-------------|
| `req.lcm.gen.01`	| General | The Architecture **must** support zero downtime expansion/change of physical capacity (compute hosts, storage increase/replacement). | |
| `req.lcm.adp.02` | Automated deployment | The Architecture **must** support hitless upgrades of software provided by the cloud provider so that the availability of running workloads is not impacted. | |

<p align="center"><b>Table 2-6:</b> LCM Requirements</p>

<a name="2.3.7"></a>
### 2.3.7 Assurance Requirements

| Ref # | sub-category | Description |  Traceability |
|----|--------|-------------------|----------|
| `req.asr.mon.01` | Integration | The Architecture **must** include integration with various infrastructure components to support collection of telemetry for assurance monitoring and network intelligence. | |
| `req.asr.mon.03` | Monitoring | The Architecture **must** allow for the collection and dissemination of performance and fault information. | |
| `req.asr.mon.04` | Network | The NFVI Network Fabric and Network Operating System **must** provide network operational visibility through alarming and streaming telemetry services for operational management, engineering planning, troubleshooting, and network performance optimisation. | |

<p align="center"><b>Table 2-7:</b> Assurance Requirements</p>

<a name="2.3.8"></a>
### 2.3.8 Security Requirements

| Ref # | sub-category | Description |  Traceability |
|----|-------|---------------------|-------------|
| `req.sec.gen.01` | General | The Architecture **must** provide tenant isolation. | |
| `req.sec.gen.02` | General | The Architecture **must** support policy based RBAC. | |
| `req.sec.gen.03` | General | The Architecture **must** support a centralised authentication and authorisation mechanism. | |
| `req.sec.zon.01` | Zoning | The Architecture **must** support identity management (specific roles and permissions assigned to a domain or tenant). | |
| `req.sec.zon.02` | Zoning | The Architecture **must** support password encryption. | |
| `req.sec.zon.03` | Zoning | The Architecture **must** support data, at-rest and in-flight, encryption. | |
| `req.sec.zon.04` | Zoning | The Architecture **must** support integration with Corporate Identity Management systems. | |
| `req.sec.cmp.02` | Compliance | The Architecture **must** comply with all applicable standards and regulations. | |
| `req.sec.cmp.03` | Compliance | The Architecture **must** comply with all applicable regional standards and regulations. | |
| `req.sec.ntw.03` | Networking | The Architecture **must** have the underlay network incorporate encrypted and/or private communications channels to ensure its security. | |
| `req.sec.ntw.04` | Networking | The Architecture **must** configure all of the underlay network components to ensure the complete separation from the overlay customer deployments. | |
| `req.sec.ntw.05` | Networking | The Architecture **must** have the underlay network include strong access controls that adhere to the V1.1 NIST Cybersecurity Framework. | |

<!-- | `req.sec.ntw.01` | Networking | The Architecture **must** have the underlay network include strong access controls that comply with the applicable security standard (national, regional), for example ISO27001. | |
| `req.sec.ntw.02` | Networking | The Architecture **must** have all security logs stored in accordance with applicable security standard (national, regional), for example ISO27001. | | -->


<p align="center"><b>Table 2-8:</b> OpenStack Security Requirements.</p>



<a name="2.4"></a>
### 2.4 Architecture and OpenStack Recommendations

The requirements listed in this section are optional, and are not required in order to be deemed a conformant implementation.

<a name="2.4.1"></a>
2.4.1 General Recommendations

| Ref # | sub-category | Description |  Traceability |
|----|-------|---------------------|-------------|
| `req.gen.cnt.01` | Cloud nativeness | The Architecture **should** consist of stateless service components. However, where state is required it must be kept external to the component. | OpenStack consists of both stateless and stateful services where the stateful services utilize a database. For latter see "[Configuring the stateful services](https://docs.openstack.org/ha-guide/control-plane-stateful.html)"|
| `req.gen.cnt.02` | Cloud nativeness | The Architecture **should** consist of service components implemented as microservices that are individually dynamically scalable. | |
| `req.gen.scl.01` | Scalability | The Architecture **should** support policy driven auto-scaling. | This requirement is currently not addressed but will likely be supported through [Senlin](https://docs.openstack.org/senlin/pike/index.html), cluster management service. |
| `req.gen.rsl.02` | Resiliency | The Architecture **should** support resilient OpenStack service components that are not subject to `req.gen.rsl.01`. | |

<p align="center"><b>Table 2-9:</b> General Recommendations</p>


<a name="2.4.2"></a>
2.4.2 Infrastructure Recommendations

| Ref # | sub-category | Description |  Traceability |
|----|-------|---------------------|-------------|
| `req.inf.com.02` | Compute | The Architecture **should** include industry standard hardware management systems at both HW device level (embedded) and HW platform level (external to device). | |
| `req.inf.com.03` | Compute | The Architecture **should** support symmetrical CPU multi-processing with shared memory access as well as multi-threading. | |
| `req.inf.stg.08` | Storage | The Architecture **should** allow use of externally provided large archival storage for its Backup / Restore / Archival needs. | |
| `req.inf.stg.09` | Storage | The Architecture **should** make available all non-host OS / Hypervisor / Host systems storage as network-based Block, File or Object Storage for tenant/management consumption. | |
| `req.inf.ntw.04` | Network | The Architecture **should** support service function chaining. | **Is this VNFM/NFVO requirement** |
| `req.inf.ntw.06` | Network | The Architecture **should** support Distributed Virtual Routing (DVR) to allow compute nodes to route traffic efficiently. | |
| `req.inf.ntw.08` | Network | The NFVI Network Fabric **should** embrace the concepts of open networking and disaggregation using commodity networking hardware and disaggregated Network Operating Systems. | |
| `req.inf.ntw.09` | Network | The NFVI Network Fabric **should** embrace open-based standards and technologies. | |
| `req.inf.ntw.11` | Network | The NFVI Network Fabric **should** be architected to provide a standardised, scalable, and repeatable deployment model across all applicable NFVI sites. | |
| `req.inf.ntw.12` | Network | The SDN solution **should** be configurable via orchestration or VIM systems in an automated manner using openly published API definitions. | |
| `req.inf.ntw.13` | Network | The SDN solution **should** be able to support federated networks. | |
| `req.inf.ntw.14` | Network | The SDN solution **should** be able to be centrally administrated and configured. | |
| `req.inf.acc.03` | Acceleration | The Architecture **should not** rely on SR-IOV PCI-Pass through to provide acceleration to VNFs. | |

<p align="center"><b>Table 2-10:</b> Infrastructure Recommendations</p>


<a name="2.4.3"></a>
2.4.3 VIM Recommendations

| Ref # | sub-category | Description |  Traceability |
|----|----------------|----------------------|-----------|
| `req.vim.04` | General | The Architecture **should** support Enhanced Platform Awareness (EPA) only for discovery of infrastructure resource capabilities.| |
| `req.vim.06` | General | The Architecture **should** allow orchestration solutions to be integrated with VIM. | **Orchestration of what** |
| `req.vim.09` | General | The Architecture **should** support horizontal scaling of OpenStack core services. |  |

<p align="center"><b>Table 2-11:</b> VIM Recommendations</p>


<a name="2.4.4"></a>
2.4.4 Interfaces and APIs Recommendations

| Ref # | sub-category | Description |  Traceability |
|----|-------|---------------------|-------------|
| `req.int.acc.02` | Acceleration | The Architecture **should not** rely on SR-IOV PCI-Pass through for acceleration interface exposed to VNFs. | duplicate of `req.inf.acc.03` under "Infrastructure Recommendations" |

<p align="center"><b>Table 2-12:</b> Interfaces and APIs Recommendations</p>


<a name="2.4.5"></a>
2.4.5 Tenant Recommendations

| Ref # | sub-category | Description |  Traceability |
|----|-------|---------------------|-------------|

<p align="center"><b>Table 2-13:</b> Tenant Recommendations</p>


<a name="2.4.6"></a>
2.4.6 Operations and LCM Recommendations

| Ref # | sub-category | Description |  Traceability |
|----|----------|-------------|-------------|
| `req.lcm.adp.01` | Automated deployment | The Architecture **should** allow for “cookie cutter” automated deployment, configuration, provisioning and management of multiple NFVI sites. | |
| `req.lcm.adp.03` | Automated deployment | The Architecture **should** support hitless upgrade of all software provided by the cloud provider that are not covered by `req.lcm.adp.02`. Whenever hitless upgrades are not feasible, attempt should be made to minimize the duration and nature of impact. | |
| `req.lcm.adp.04` | Automated deployment | The Architecture **should** support declarative specifications of hardware and software assets for automated deployment, configuration, maintenance and management. | |
| `req.lcm.adp.05` | Automated deployment | The Architecture **should** support automated process for Deployment and life-cycle management of VIM Instances. | |
| `req.lcm.cid.02` | CI/CD | The Architecture **should** support integrating with CI/CD Toolchain for NFVI and VIM components Automation. | |

<p align="center"><b>Table 2-14:</b> LCM Recommendations</p>


<a name="2.4.7"></a>
2.4.7 Assurance Recommendations

| Ref # | sub-category | Description |  Traceability |
|----|--------|-------------------|----------|
| `req.asr.mon.02` | Monitoring | The Architecture **should** support Network Intelligence capabilities that allow richer diagnostic capabilities which take as input broader set of data across the network and from VNF workloads. | |


<p align="center"><b>Table 2-15:</b> Assurance Recommendations</p>


<a name="2.4.8"></a>
2.4.8 Security Recommendations

| Ref # | sub-category | Description |  Traceability |
|----|-------|---------------------|-------------|


<p align="center"><b>Table 2-16:</b> Security Recommendations</p>
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
