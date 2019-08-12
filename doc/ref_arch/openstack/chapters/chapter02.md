[<< Back](../../openstack)

# 2. Architecture Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction.](#2.1)
* [2.2 Reference Model Requirements.](#2.2)
* [2.3 Open Stack Requirements.](#2.3)

<a name="2.1"></a>
## 2.1 Introduction.

<a name="2.2"></a>
## 2.2 Reference Model Requirements.

Traceability to Reference Model.

<a name="2.3"></a>
## 2.3 Open Stack Requirements.

Proposals (WK): Change title of this section to 2.3 Architectural Requirements; propose the following structure of requirements:

1.	General
    1.	Open source
    1.	Cloud nativeness
    1.	Scalability
    1.	Resiliency
2.	Infrastructure
    1.	Compute
    1.	Storage
    1.	Networking
3.	VIM
4.	APIs
5.	Tenants
6.	LCM
7.	Assurance
8.	Security

Following are Open Stack Reference Architecture requirements:

| Ref | Requirement | Note |
|--------------|-------------|------|
| `rm.req.001` | Support LCM of NFVI resources | includes allocation, release and reclamation |
| `rm.req.002` | Req1 | Note |
| `rm.req.003` | Req1 | Note |


**Backlog of Req**
1. HW virtualization -- compute, storage and network
1. Support LCM of NFVI resources -- allocation, upgrade, release and reclamation
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

<!--
<a name="2.1"></a>
## 2.1 LCM

| # | Requirement | Notes |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| req.lcm.1 | Automated deployment | The Architecture shall allow the “cookie cutter” automated deployment to multiple sites. |
| req.lcm.2 | Automated/ Incremental Upgrade,(Zero Downtime) | The Architecture shall enable automated and incremental upgrade of the various software components in a manner that still allows tenant workloads to continue to operate. |
| req.lcm.3	| Zero Downtime Expansion/Change | The Architecture will support zero downtime expansion/change of physical capacity (compute hosts, storage increase/replacement) |
| req.lcm.4 | Multi-environment support	| The Architecture will support plug-ins to manage deployment of workload to multiple sites and various technology stack. Multi-cloud support through hybrid, migrations, etc. |
| req.lcm.5 | Bare Metal Provisioning |	The Architecture will provide OpenStack Ironic Bare Metal provision to support VIM Instance provisioning (bootstrap), Management System, KVM host provisioning and Kubernetes host provisioning |
| req.lcm.6 | Support CI/CD | Toolchain Integration	The Architecture will include integration with CI/CD Toolchain for the purpose of Infrastructure Automation |
| req.lcm.7 | Support Lifecycle Management | CI/CD for NFVI and VIM components |


<a name="2.2"></a>
## 2.2 Service Assurance

| # | Requirement | Notes |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| req.sa.1 | Integration with Service Assurance (Specify Service Assurance in scope) | The Architecture will define integration with the standard OSS/BSS assurance systems and will support automation of assurance processes. _**Notes/Discussion:** each company’s SA is unique, simplify the interface_ |
| req.sa.2 | Advanced Diagnostics & Monitoring (Network Intelligence - Specify in Scope) | Network Intelligence capabilities that allow richer diagnostic capabilities which take as input broader set of data across the network and from VNF workloads |
| req.sa.3 | Monitoring Interfaces | The Architecture will include integration with various infrastructure components to support collection of telemetry for assurance monitoring and network intelligence |

<a name="2.3"></a>
## 2.3 Networking

| # | Requirement | Notes |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| req.net.1 | Network Integration / SDN Controller | The Architecture will include an SDN integration to support provisioning of network services from host-based OpenStack Neutron networking VTEPs to the Border Edge based VRFs |
| req.net.2 | Networking | Localize intra-host traffic; low latency, high throughput, resiliency |
| req.net.3 | Support service function chaining from data plane and fabric perspective. (Data Plane – Networking) | Prescriptive. Issue : « Must » |
| req.net.4 | Allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay - VXLAN or Geneve) | |	
| req.net.5 | Support Distributed Virtual Routing (DVR) to allow compute nodes to route traffic efficiently | Possibly move to networking). Issue : « Must » |

<a name="2.4"></a>
## 2.4 VIM

| # | Requirement | Notes |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| req.vim.1 | Container Support | The Architecture will provide support for Kubernetes container deployment _**Notes/Discussion:** Open item first pass doesn't necessarily support containers_ |
| req.vim.2 | Block and Object Storage | The Architecture will provide storage solution for VIM Instances and VNFs to support Block/Image and local VNF File system storage|
| req.vim.3 | Software Defined Storage | Resilient and scalable virtualized storage that seamlessly supports Block storage, object storage and flat files |
| req.vim.4 | Infrastructure as a service | VNFI transformed as an IaaS cloud with the clear role to support all use-cases. Allow Infrastructure resource sharing among several service operation teams to avoid per VNF vertical solutions. |


<a name="2.5"></a>
## 2.5 Security / Compliance

| # | Requirement | Notes |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| req.sec.1 | Security | Zoning, identity management (specific roles assigned to a domain or tenant), Storage and password encryption; RBAC for Infrastructure and Tenants; Tenant isolation; authentication management (integration with Corporate Identity Management) |
| req.sec.2 | Compliance | Compliance with standards and regulations |

<a name="2.6"></a>
## 2.6 APIs

| # | Requirement | Notes |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| req.api.1 | Control plane provides the API endpoints, GUI & internal services for the cloud | |
| req.api.2 | Permit external access to the APIs | External access to APIs exposed by the VIM and NFVI |


<a name="2.7"></a>
## 2.7 Tenants

| # | Requirement | Notes |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| req.ten.1 | Multi-tenant Self Service (UI/API) | The Architecture provides for a multi-tenanted solution that allows tenants to deploy workloads using self-service interfaces (both UI and API) |

<a name="2.8"></a>
## 2.8 Infrastructure

| # | Requirement | Notes |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| req.inf.1 | Support Application Specific Acceleration (exposed to VNFs). (Data Plane – Computing) | Issue : « Must » Change |

-->

