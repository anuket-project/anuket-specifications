
[<< Back](../../kubernetes)

# 2. Architecture Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction.](#2.1)
* [2.2 Reference Model Requirements.](#2.2)
* [2.3 Containerised Platform Requirements.](#2.3)

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
## 2.3 Containerised Platform Requirements.

The Reference Model (RM) defines the NFVI to consist of the physical resources, virtualised resources and a software managment system.  In the virtualised world, the NFVI Software Management System (Virtualised Infrastructure Manager -- VIM) consists of the Guest Operating System, Hypervisor and, if needed, other software such as libvirt.  And the VIM is responsible for, among others, tenant management, resources management, inventory, scheduling, and access management. Now consider, the containerisation equivalent.

Containerised Infrastructure Manager (CIM): a functional block that is responsible for controlling and managing the containerised NFVI compute, storage and network resources. Note CIM supports the Life Cycle Management of conatinerised and the underlying physical resources.

<a name="2.3.1"></a>
### 2.3.1 General

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.gen.k8s.01` | Open source | The Architecture **must** use Kubernetes APIs.|
| `req.gen.k8s.02` | Open source | The Architecture **must** support dynamic request and configuration of resources (compute, network, storage) through Kubernetes APIs. |
| `req.gen.cnt.01` | Cloud nativeness | The Architecture **should** consist of stateless service components. However, where state is required it must be kept external to the component. |
| `req.gen.cnt.02` | Cloud nativeness | The Architecture **should** consist of service components implemented as microservices that are individually dynamically scalable. |
| `req.gen.scl.01` | Scalability | The Architecture **should** support policy driven horizontal auto-scaling. |
| `req.gen.rsl.01` | Resiliency | The Architecture **must** support resilient Kubernetes components that are required for the continued availability of running workloads. |
| `req.gen.rsl.02` | Resiliency | The Architecture **should** support resilient Kubernetes service components that are not subject to `req.gen.rsl.01`. |
| `req.gen.avl.01` | Availability | The Architecture **must** provide High Availability for Kubernetes components. |


<p align="center"><b>Table 2-1:</b> Containerised Platform: General Requirements.</p>

<a name="2.3.2"></a>
### 2.3.2 Infrastructure

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.inf.com.01` | Compute | The Architecture **must** provide compute resources for Pods.  |
| `req.inf.com.02` | Compute | The Architecture **should** include industry standard hardware management systems at both HW device level (embedded) and HW platform level (external to device). |
| `req.inf.stg.01` | Storage | The Architecture **must** provide shared Block storage for Containers.
| `req.inf.stg.02` | Storage | The Architecture **must** provide shared Object storage for Containers.
| `req.inf.stg.03` | Storage | The Architecture **may** provide local file system storage solution for Containers.
| `req.inf.stg.04` | Storage | The Architecture **may** support Software Defined Storage (SDS) that seamlessly supports shared block storage, object storage and flat files. |
| `req.inf.stg.05` | Storage | The Architecture **should** provide high-performance and horizontally scalable storage. |
| `req.inf.ntw.01` | Network | The Architecture **must** support intra-pod communications such as between all containers within a pod on localhost |
| `req.inf.ntw.02` | Network | The Architecture **must** support intra-node communications, such as between agents on a node and all pods on that node |
| `req.inf.ntw.03` | Network | The Architecture **must** support inter-node communications without NAT, such as communications between pods on a node with all other pods on all nodes |
| `req.inf.ntw.04` | Network | The Architecture **must** support low latency and high throughput traffic needs. |
| `req.inf.ntw.05` | Network | The Architecture **should** support service function chaining. |
| `req.inf.ntw.06` | Network | The Architecture **must** support network resiliency. |
| `req.inf.ntw.06` | Network | The Architecture **should** embrace the concepts of open networking and disaggregation using commodity networking hardware and disaggregated Network Operating Systems. |
| `req.inf.ntw.06` | Network | The Architecture **should** embrace open-based standards and technologies. |
| `req.inf.ntw.09` | Network | The Architecture **must** be capable of supporting highly available (Five 9’s or better) CNF/VNF workloads. |
| `req.inf.ntw.10` | Network | The Architecture **should** be architected to provide a standardised, scalable, and repeatable deployment model across all applicable NFVI sites. |
| `req.inf.ntw.11` | Network | The SDN solution **should** be configurable in an automated manner using openly published API definitions. |
| `req.inf.ntw.12` | Network | The SDN solution **should** be able to be centrally administrated and configured. |
| `req.inf.ntw.13` | Network | The Architecture **must** support dual stack IPv4 and IPv6 in Pods and Services. |
| `req.inf.acc.01` | Acceleration | The Architecture **should** support Application Specific Acceleration. |
| `req.inf.acc.02` | Acceleration | The Architecture **should** support NFVI Acceleration (such as SmartNICs). |

<p align="center"><b>Table 2-2:</b> Containerised Platform: Infrastructure Requirements.</p>

<a name="2.3.3"></a>
### 2.3.3 Containerised Infrastructure Management (CIM)

| Ref # | sub-category | Description |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.vim.01` | General | The Architecture **must** allow infrastructure resource sharing. |
| `req.vim.02` | General | The Architecture **must** allow discovery and management of NFVI resources. |
| `req.vim.03` | General | The Architecture **must** support Enhanced Platform Awareness (EPA). |
| `req.vim.04` | General | The Architecture **must** include image repository management. |
| `req.vim.05` | General | The Architecture **should** support a multi-tenanted environment. |
| `req.vim.06` | General | The Architecture **must** support resource tagging. |
| `req.vim.07` | General | The Architecture **must** support horizontal scaling. |
| `req.vim.08` | General | The Architecture **must** support workload resiliency. |

<p align="center"><b>Table 2-3:</b> Containerised Platform: CIM Requirements.</p>




