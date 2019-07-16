[<< Back](../../ref_arch)

# 2. Architecture Requirements

## Table of Contents
* [2.1 Foundation Requirements (includes Management Plane).](#2.1)
* [2.2 Control Plane.](#2.2)
* [2.3 Data Plane.](#2.3)
* [2.4 Networking.](#2.4)


1. Automated deployment: The Architecture will allow the “cookie cutter” automated deployment to multiple sites.
1. Automated / Incremental Upgrade (Zero Downtime) 
	The Architecture will enable automated and incremental upgrade of the various software components in a manner that still allows tenant workloads to continue to operate.
1.	Zero Downtime Expansion/Change 
	The Architecture  will support zero downtime expansion/change of physical capacity (compute hosts, storage increase/replacement)
1.	Multi-tenant Self Service (UI/API)
	The Architecture provides for a multi-tenanted solution that allows tenants to deploy workloads using self-service interfaces (both UI and API)
1.	Integration with Service Assurance (Specify Service Assurance in scope)
	The Architecture will define integration with the standard OSS/BSS assurance systems and will support automation of assurance processes.
    >Notes/Discussion: each companies SA is unique, simplify the interface
1.	Advanced Diagnostics and Monitoring (Req) (Network Intelligence - Specify in Scope)
	Network Intelligence capabilities that allow richer diagnostic capabilities which take as input broader set of data across the network and from VNF workloads
1.	Workload HA Migration (Req)
    e.g. Multi-region support
	To support non-disruptive update and expansion the Architecture will provide mechanisms to allow migration of workloads across hosts to allow these to be available for upgrade.
1.	Multi-environment support	Multi-cloud support through hybrid, migrations, etc.
Common Cloud Deployment Interface (Dupe of 8)	The Architecture will  support plug-ins to manage deployment of workload to multiple sites and various technology stacks
1.	Monitoring Interfaces	The Architecture will include integration with various infrastructure components to support collection of telemetry for assurance monitoring and network intelligence.
1.	Bare Metal Provisioning 	The Architecture will provide OpenStack Ironic Bare Metal provision to support VIM Instance provisioning (bootstrap), Management System KVM host provisioning and Kubernetes host provisioning.
1.	Container Support	The Architecture will provide support for Kubernetes container deployment 
Notes/Discussion: open item first pass doesn’t necessarily support containers
1.	Network Integration / SDN Controller	The Architecture will include an SDN integration  to support provisioning of network services from host based OpenStack Neutron networking VTEPs to the Border Edge based VRFs
1.	Ability to Support CI/CD Toolchain Integration	The Architecture will include integration with CI/CD Toolchain for the purpose of Infrastructure Automation
1.	Ability to support Lifecycle Management	CI/CD for NFVI and VIM components
Services Catalog Integration (Out of Scope)	The Architecture will allow tenants to create new services within the Service Catalog and allow tenants to use provided shared services within the Catalog
1.	Block and Object Storage	The Architecture will provide storage solution for VIM Instances and VNFs to support Block/Image and local VNF File system storage
1.	Software Defined Storage	Resiliency, scalability.

1. Infrastructure sharing (Add to Principles)	Architecture must allow resources sharing between the different workloads and between different VNF within the network workload	Allow economy of scale in term of resource consumption

1. Infrastructure as a service (Add to Scope)	Share and propose the infrastructure in a IaaS mode with a clear role of infrastructure operator common for all use-case	Allow Infrastructure resource consumption by several service operation teams and avoid per VNF vertical solutions

1. Open Architecture (Already in Principles)	Leverage on open-source communities 	Avoid suck with vendor proprietary solution
Programmability, automation (Already on WKs)	Dynamicity and automation of provisioning through APIs	Conformance with the “on-demand” and “time-to-market” objective

1. Programmability, automation (Already on WKs)	Dynamicity and automation of provisioning through APIs	Conformance with the “on-demand” and “time-to-market” objective

1.	Security	Zoning, identities management (specific roles assigned to a domain or tenant), Storage and password encryption; RBAC for Infrastructure and Tenants; Tenant isolation; authentication management (integration with Corporate Identity Management)
1.	Compliance	Compliance with standards and regulations.

1. Monitoring (already covered in WKs)

1. LCM (Already covered in WKs)

1.	Networking	Localize intra-host traffic ; Low latency and High throughput ; resiliancy 
1.	Control Plane Resiliancy	No single point of hardware/software failure

1. Service Orchestration 	Open Item – (NFVO Out-of-Scope)
1. Workflow Support	Open Items - Ability to change and manage workflows (NFVO Out-of Scope)


1. Bare-Metal provisioning. (Dupe)
1. Enabler services: NAT, DHCP, DNS, IDS/IPS and Load Balancing (Dupe add to integration)

1. Control plane provides the API endpoints, GUI and internal services for the cloud. 
1. All control plane components must be configured to be highly available (HA) and deployed across multiple physical nodes. (Dupe)
1. API endpoints and supporting services need to handle failures of an underlying component. (Dupe add to Platform resiliancy)
1. Control plane must support Logging, monitoring and alerting to manage the cloud. Control plane must be Telemetry enabled to provide insight into utilisation and usage reporting (Dupe – add to monitoring)

1. Must allow for tenant networking within a single server and across servers. (Dupe)
1. Must support Service function chaining from data plane and fabric perspective. (Data Plane – Networking) 
1. Must provide high throughput and low latency. 
    1. Depending on the targeted profile. (Dupe – add to section already) 
1. Must support Network Acceleration (in-line and Look-Aside) – This is a solution.
1. Must support Application Specific Acceleration (exposed to VNFs). (Data Plane – Computing) 

1. Must allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay - VXLAN or Geneve)
1. Must allow for management traffic of the cloud (Dupe in Management networking above or add detail)
1. Must allow for management traffic of the servers     i.e. IPMI (Dupe in Management networking above or add detail)
1. Must allow for external access to the API 
1. Must allow for tenant external access from other systems or users e.g. Internet/DC networks (Dupe in Management networking above or add detail)
1. Must allow for storage access network and replication (Dupe in Storage Resiliancy req)
1. Must support VXLAN/Geneve over L3 (Dupe of 24)
1. Must support Distributed Virtual Routing (DVR) to allow compute nodes to route traffic efficiently. (Possibly move to networking)
1. Notes/Discussion: concern about ‘must have…’ wording

>Section A - Control plane: the control plane delivers API and User Interface to manage NFVI resources (compute, storage, and network) to users
Section B - Data plane: delivers various classes of services for compute, storage and network used to deploy application workloads.