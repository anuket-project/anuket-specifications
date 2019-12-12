[<< Back](../../openstack)

# 3. NFVI + VIM Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Introduction](#3.1)
* [3.2 Consumable Infrastructure Resources and Services](#3.2)
  * [3.2.1. Multi-Tenancy (execution environment)](#3.2.1)
  * [3.2.2. Virtual Compute (vCPU and vRAM)](#3.2.2)
  * [3.2.3. Virtual Storage](#3.2.3)
  * [3.2.4. Virtual Networking Neutron standalone](#3.2.4)
  * [3.2.5. Virtual Networking – 3rd party SDN solution](#3.2.5)
* [3.3. Virtualised Infrastructure Manager (VIM)](#3.3)
  * [3.3.1. VIM Core services](#3.3.1)
  * [3.3.2. Tenant Isolation](#3.3.2)
  * [3.3.3. Host aggregates providing resource pooling](#3.3.3)
  * [3.3.4. Flavor management](#3.3.4)
* [3.4. Underlying Resources](#3.4)
  * [3.4.1. Virtualisation](#3.4.1)
  * [3.4.2. Physical Infrastructure](#3.4.2)
* [3.5. Deployment Models](#3.5)
* [3.6. Architectural Drivers – Requirements Traceability](#3.6)


<a name="3.1"></a>
## 3.1 Introduction

The Common Telco NFVI OpenStack Reference Architecture (RA) aims to provide an industry standard reference architecture independent of the many distributions of OpenStack. It does not seek to change any vendor implementation assuming Common Telco NFVI compliance out of the box without vendor specific enhancements that are not up-streamed. This would allow operators to provide a common OpenStack-based architecture allowing any compliant VNF to be deployed and operate as expected.  The purpose of this chapter is to outline all the components required to provide the NFVI and the VIM in a consistent and reliable way. 

OpenStack is already very well documented at http://docs.openstack.org so rather than repeat content from there this and following chapters will describe the specific features used and how we expect them to be implemented.

This reference architecture provides optionality in terms of pluggable components such as SDN, hardware acceleration and support tools however for MVP we will focus on a simplified model based on standard Neutron OVS/OVS-DPDK, standard NIC and no GPU.

The NFVI will be based on physical infrastructure which is then separated into virtual resources via a hypervisor.
The VIM is expected to be OpenStack in line with the OpenStack Foundation core release.

This chapter is organized as follows:
*	Consumable Infrastructure Resources and Services: these are infrastructure services and resources being exposed northbound consumption 
    - Multi-tenancy with quotas
      -	Virtual compute: vCPU / vRAM
      -	Virtual storage: Ephemeral, Persistent and Image
      -	Virtual networking – neutron standalone: network plugin, virtual switch, accelerator features
      -	Virtual networking – 3rd party SDN solution
      -	Additional network services: Firewall, DC Gateway
* NFVI Management Software (VIM): is how we manage the Consumable Infrastructure Resources and Services
    - VIM Core services (keystone, cinder, nova, neutron etc.)
    - Tenant Separation
    - Host aggregates providing resource pooling
    - Flavor management
*	Underlying Resources: are what provides the resources that allow the Consumable Infrastructure Resources and Services to be created and managed by the NFVI Management Software (VIM).
    - Virtualisation
    - Physical infrastructure
      -	Compute
      -	Network: Spine/Leaf; East/West and North/South traffic
      -	Storage

Please note that while requirements are provided in various sections of this chapter for traceability, the source of record is Chapter 2. 

<a name="3.2"></a>
## 3.2. Consumable Infrastructure Resources and Services
This section will describe the different services that are exposed for the VNF consumption within the execution zone:
-	Tenants: to provide isolated environments
-	Virtual Compute: to provide computing resources
-	Virtual Storage: to provide storage capacity and performance
-	Virtual networking: to provide connectivity within NFVI and with external networks

<a name="3.2.1"></a>
### 3.2.1. Multi-Tenancy (execution environment)
The multi tenancy service will permit to host several VNF projects with the insurance to have isolated environment for each project. Tenants or confusingly “Projects” in OpenStack are isolated environments that enable workloads to be logically separated from each other with:
-	differentiated set of associated users
-	role-based access of two levels – admin or member.  (see security section link-TBA for further details). 
-	quota system to provide maximum resources that can be consumed.

This RA does not intend to restrict how workloads are distributed across tenants however where multiple related OpenStack clouds are deployed it is important that naming and quotas are kept consistent.  Chapter 4 provides a proposed naming convention for users and tenants (link-TBA).   

<a name="3.2.2"></a>
### 3.2.2. Virtual Compute (vCPU and vRAM)
The virtual compute resources (vCPU and vRAM) used by the VNFs behave like their physical counterparts.  A physical core is an actual processor and can support multiple vCPUs through Symmetric Multi-Threading (SMT) and CPU overbooking. With no overbooking and SMT of 2 (2 threads per core), each core can support 2 vCPUs. With the same SMT of 2 and overbooking factor of 4, each core can support 8 vCPUs. The performance of a vCPU can be affected by various configurations such as CPU pinning, NUMA alignment, and SMT.

The configuration of the virtual resources will depend on the profile and the flavour needed to host VNF components. Profiles are defined in the chapters 5.1 and 5.2 of the reference model document. Flavors are defined in the chapter 4.2 of the reference model document.

<a name="3.2.3"></a>
### 3.2.3. Virtual Storage
The three storage services offered by NFVI are:
-	Persistent storage 
-	Ephemeral storage
-	Image storage
The different profiles and storage extensions are defined in the reference model document.

Two types of persistent data storage are supported in OpenStack: 
-	Block storage 
-	Object storage
The OpenStack services, Cinder for block storage and Swift for Object Storage, are discussed below in Section 3.3 “NFVI Management Software (VIM)”.

Ephemeral data is typically stored on the compute host’s local disks, except in environments that support live instance migration between compute hosts. In the latter case, the ephemeral data would need to be stored in a storage system shared between the compute hosts such as on persistent block or object storage.
Images are stored using the OpenStack Glance service discussed below in Section 3.3 “NFVI Management Software (VIM)”.  
The [OpenStack Storage Table](https://docs.openstack.org/arch-design/design-storage/design-storage-concepts.html#table-openstack-storage) explains the differences between the storage types and typical use cases. The [OpenStack compatible storage backend drivers](https://docs.openstack.org/cinder/latest/reference/support-matrix.html) table lists the capabilities that each of these drivers support.

<a name="3.2.4"></a>
### 3.2.4. Virtual Networking Neutron standalone 
Neutron is an OpenStack project that provides "network connectivity as a service" between interface devices(e.g., vNICs) managed by other OpenStack services (e.g., nova). Neutron allows users to create networks, subnets, ports, routers etc. Neutron also facilitates traffic isolation between different subnets - within as well as across project(s) by using different type drivers/mechanism drivers that use VLANs, VxLANs, GRE (Generic Routing Encapsulation) tunnels etc. For Neutron API consumer, this is abstracted and provided by Neutron. Multiple network segments are supported by Neutron via ML2 plugins to simultaneously utilize varierty of layer 2 networking technologies like VLAN, VxLAN, GRE etc. Neutron also allows to create routers to connect layer 2 networks via "neutron-l3-agent". In addition, floating IP support is also provided that allows a project VM to be accessed using a public IP.

<a name="3.2.5"></a>
### 3.2.5. Virtual Networking – 3rd party SDN solution
SDN (Software Defined Networking) controllers separate control and data (user) plane functions where the control plane programmatically configures and controls all network data path elements via open APIs. Open Networking Forum (ONF) defines SDN as “Software-Defined Networking (SDN) is an emerging architecture that is dynamic, manageable, cost-effective, and adaptable, making it ideal for the high-bandwidth, dynamic nature of today's applications. This architecture decouples the network control and forwarding functions enabling the network control to become directly programmable and the underlying infrastructure to be abstracted for applications and network services. The OpenFlow protocol is a foundational element for building SDN solutions." While the ONF definition specifically mentions the OpenFlow protocol in practicality other protocols are also supported by SDN controllers. From our perspective the key messages of the SDN definition are:

- Decoupling of control and forwarding functions into control plane and data plane
- Networking capabilities that can be instantiated, deployed, configured and managed like software. Network control is programmable and supports dynamic, manageable and adaptable networking.

OpenStack Neutron supports open APIs and a pluggable backend where different plugins can be incorporated in the neutron-server. Plugins for various SDN controllers include the standard [ML-2 plugin](../chapter04.md#4234-neutron-ml2-integration) and vendor product specific [monolithic plugins](https://wiki.openstack.org/wiki/Neutron_Plugins_and_Drivers).

Neutron supports both core plugins that deal with L2 connectivity and IP address management, and service plugins that support services such as L3 routing, Load Balancers, Firewalls, etc.

<a name="3.3"></a>
## 3.3. Virtualised Infrastructure Manager (VIM)
The NFVI Management Software (VIM) provides the services for the management of Consumable Resources/Services.

<a name="3.3.1"></a>
### 3.3.1. VIM Core services 
OpenStack is a complex, multi-project framework, so we initially will focus on the core services required to provide Infrastructure-as-a-Service (IaaS) as this is generally all that is required for NFVi/VIM use cases. Other components are optional and provide functionality above and beyond NFVi/VIM requirements.

The architecture consists of the services shown in the Figure 3-1; Ironic is an optional OpenStack service needed only for bare-metal containers. The rest of this document will address the specific Common Telco NFVI implementation requirements and recommendations.

The following diagram shows the core OpenStack services that must be provided to be compliant.

<p align="center"><img src="../figures/Figure_3_1_Core_NFVI_Services_v5.png" alt="Core NFVI Software Services" title="core NFVI Software Services" width="100%"/><b>Figure 3-1:</b> OpenStack Core Services</p>

We will refer to the functions above as falling into the following categories to avoid any confusion with other terminology that may be used:
-	Foundation node
-	Control nodes
-	Compute nodes
-	Other supporting service nodes e.g. network, shared storage, logging, monitoring and alerting.

Each deployment of OpenStack should be a unique cloud with its own API endpoint.  Sharing underlying cloud resources across OpenStack clouds is not recommended.

#### 3.3.1.1. OpenStack Services Topology
NFVI software services are distributed over 2 planes:
-	Control Plane that hosts all Control and Management services
-	Data Plane (a.k.a. User plane) that provides physical and virtual resources (compute, storage and networking) for the actual virtual workloads to run.

The architecture based on OpenStack technology relies on different types of nodes associated with specific roles:
-	Controller node types with control and management services, which include VIM functionalities
-	Compute node types running workloads
-	Network node types offering L3 connectivity
-	Storage node types offering external attached storage (block, object, flat files)

The data plane consists of the compute nodes. It is typical to consider the other node types to be part of the control plane. Figure 3-2 depicts the 4 types of nodes constitutive of the Infrastructure: control, compute, network and storage nodes.

<p align="center"><img src="../figures/Figure_3_2_ NFVI_Software_Services_Topology_v2.png" alt="NFVI Software Services Topology" title="NFVI Software Services Topology" width="100%"/><b>Figure 3-2:</b> OpenStack Services Topology</p>

Deployments can be structured using the distribution of services amongst the 4 node types as depicted in Figure 3-2, but depending on workloads requirements, OpenStack services can also be hosted on the same nodes. For instance, services related to Controller, network and storage roles can be hosted on controller nodes.

#### 3.3.1.2. Foundation Services
Foundation Node
To build and lifecycle manage an OpenStack cloud it is typically necessary to deploy a server or virtual machine as a deployment node.

This function must be able to manage the bare-metal provisioning of the hardware resources but since this does not affect cloud execution it can be detached from the OpenStack cloud and an operator can select their own tooling as they wish.
Functional requirements of this node include:
-	Build the cloud (control, compute, storage, network hardware resources)
-	Patch management / upgrades / change management
-	Grow / Shrink resources

#### 3.3.1.3 Cloud Controller Services
The following OpenStack components are deployed on the Infrastructure. Some of them will be only deployed on control hosts and some of them will be deployed within both control and compute hosts. The Table also maps the OpenStack core services to the Reference Model (RM) Management Software components [Reference Model Chapter 3.3 Management Software](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter03.md#3.3").

| RM Management Software| Service| Description| Required / Optional| Deployed on Controller Nodes| Deployed on Compute Nodes |
|-----------------------|-------------|----------------------|----------------|-----------|---------|
| Identity Management (Additional Management Functions) + Catalogue| Keystone| the authentication service| Required| X|  |
| Storage Resources Manager| Glance| the image management service| Required| X|  |
| Storage Resources Manager | Cinder| the block storage management service| Required| X|  |
| Storage Resources Manager| Swift| the Object storage management service| Required| X|   |
| Network Resources Manager| Neutron| the network management service| Required| X| X |
| Compute Resources Manager + Inventory + Scheduler | Nova| the compute resources management service| Required| X| X |
| Compute Resources Manager| Ironic| the Bare Metal Provisioning service| Optional| X| X |
| (Tool that utilizes APIs)| Heat| the orchestration service| Required| X|  |
| UI| Horizon| the WEB UI service| Required| X|  |

All components must be deployed within a high available architecture that can withstand at least a single node failure and respects the anti-affinity rules for the location of the services (i.e. instances of a same service must run on different nodes).

The services can be containerized or VM hosted as long as they provide the high availability principles described above. 

The APIs for these OpenStack services are listed in [Chapter 5: Interfaces and APIs](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter05.md).

#### 3.3.1.4 Cloud Workload Services
This section describes the core set of services and service components needed to run workloads including instances (such as VMs), their networks and storage are referred to as the “Compute Node Services” (a.k.a. user or data plane services). Contrast this with the Controller nodes which host OpenStack services used for cloud administration and management. The Compute Node Services include virtualisation, hypervisor instance creation/deletion, networking and storage services; some of these activities include RabbitMQ queues in the control plane including the scheduling, networking and cinder volume creation / attachment.
*	Compute, Storage, Network services: 
    - Nova Compute service: nova-compute (creating/deleting instances)
    -	Neutron Networking service: neutron-l2-agent (manage local Open vSwitch (OVS) configuration), VXLAN
    -	Local Storage (Ephemeral, Root, etc.)
    -	Attached Storage (using Local drives)

<a name="3.3.2"></a>
### 3.3.2. Tenant Isolation
In Keystone v1 and v2 (both deprecated), the term "tenant" was used in OpenStack. With Keystone v3, the term "project" got adopted and both the terms became interchangeable. However, as CNTT RA uses Keystone v3 in [this](chapter05.md#5.2) section, so it is recommended to use the term "project" when referring to OpenStack and use [tenant](../../../ref_model/chapters/chapter03.md#321-tenant) when referring to multi-tenancy. According to [OpenStack glossary](https://docs.openstack.org/doc-contrib-guide/common/glossary.html), Projects represent the base unit of resources (compute, storage and network) in OpenStack, in that all assigned resources in OpenStack are owned by a specific project.
OpenStack offers multi-tenancy by means of resource (compute, network and storage)separation via projects. OpenStack offers ways to share virtual resources between projects while maintaining logical separation. As an example, traffic separation is provided by creating different VLAN ids for neutron networks of different projects. As another example, if host separation is needed, nova scheduler offers AggregateMultiTenancyIsolation scheduler filter to separate projects in host aggregates. Thus, if a host in an aggregate is configured for a particular project, only the instances from that project are placed on the host. Overall, tenant isolation ensures that the resources of a project are not affected by resources of another project.

<a name="3.3.3"></a>
### 3.3.3. Host aggregates providing resource pooling
Availability zones: provide resiliency and fault tolerance for VM deployments, by means of physical hosting distribution of Compute Nodes in separate racks with separate power supply and eventually in different rooms

Host aggregate: is a Cloud Admin concept which is used to map the VNFC instances on the compute nodes

A host aggregate is a set of hosts with specific properties (multiple software and/or hardware properties); the properties are specified as key-value pairs. Example would be a host aggregate created for a particular flavour or specific hardware. A host can belong to multiple host aggregates. Host aggregates are not visible to users.

Availability Zones are user visible host aggregates where a host can only be in one availability zone. Availability zones partition the cloud independent of the infrastructure layout. Availability zones (AZ) serve a couple of important purposes. Firstly, users can deploy their workloads to create local redundancy for resiliency and high availability. This permits rolling upgrades – an AZ at a time upgrade with enough time between AZ upgrades to allow recovery of tenant workloads on the upgraded AZ. Secondly, AZs can accommodate hosts with special hardware and software characteristics, for example, hosts with hardware accelerators.

An over use of host aggregates and availability zones can result in a granular partition the cloud and, hence, operational complexities and inefficiencies.

Recommendation: Separation of control zone and execution zone into different security zones

<a name="3.3.4"></a>
### 3.3.4. Flavor management
A flavor defines the compute, memory, and storage capacity of nova instances. When instances are spawned, they are mapped to flavors which define the available hardware configuration for them. For simplicity, the flavors can be named as described in RM  like .tiny, .small, .medium, .large, .2xlarge and so on. The specifications for these sizes should map to the predefined compute flavors lister [here](../../../ref_model/chapters/chapter04.md#4211-predefined-compute-flavours).

<a name="3.4"></a>
## 3.4. Underlying Resources
The number of Compute nodes (for workloads) determines the load on the controller nodes and networking traffic and, hence, the number of controller nodes needed in the OpenStack cloud; the number of controller nodes required is determined on the load placed on these controller nodes and the need for High availability and quorum requires at least 3 instances of many of the services on these controller nodes.

<a name="3.4.1"></a>
### 3.4.1. Virtualisation
Virtualisation is a technology that enables a guest Operating System (OS) to be abstracted from the underlying hardware and software. This allows to run multiple Virtual Machines(VMs) on the same hardware. Each such VMs have their own OS and are isolated from each other i.e. application running on one VM does not have the access to resources of another VM. Such virtualisation is supported by various hypervisors available as open-source (KVM, Xen etc.) as well as commercial (Hyper-V, Citrix XenServer etc.). Selecting a hypervisor depends on the workload needs and the features provided by various hypervisors as illustrated in Hypervisor [Feature Support Matrix](https://docs.openstack.org/nova/latest/user/support-matrix.html). OpenStack (Nova) allows the use of various hypervisors within a single installation by means of scheduler filters like ComputeFilter, ImagePropertiesFilter etc.

Virtualisation Services: The OpenStack nova-compute service supports multiple hypervisors natively or through libvirt. The preferred supported hypervisor in this Reference Architecture is KVM. 

*Note*: Other hypervisors (such as ESXI) can also be supported as long as it can interoperate with other OpenStack components in this Reference Architecture using standard interfaces and APIs as specified in Chapter 5.

<a name="3.4.2"></a>
### 3.4.2. Physical Infrastructure
Content to be developed

Aim here is how to deploy from ground up (in a shipping container) or what expectations does the NFVi have of the DC.
*	Servers 
    - Compute
    -	Storage
    -	Control (min 3 for Core DC)
*	Network considerations
    - Data centre gateway
    -	Firewall (around the control plane, storage, etc.)
    -	Data centre network fabric / Clos (spine/leaf) – Horizontal scale 
    -	Storage networking, control plane and data plane
    -	Raw packet – tenant networking allowing “wild west” connection.  
*	Storage 
    - Opensource???? Ceph (move to virtual)
    -	Pluggable into ….   
*	Acceleration


#### 3.4.2.1. Compute
NFVI physical Nodes

The physical resources required for the NFVI are mainly based on COTS X86 hardware for control and data plane nodes. 
HW profiles are defined in the chapters 5.3 and 5.4 of the reference model document.

#### 3.4.2.2. Network
(Spine-Leaf, East/West and North-South Traffic)

NFVI Network & Security

the recommended network architecture is spine and leaf topology however for small sites a legacy topology (access/aggregation switches) can be setup.

Content to be developed along the following lines
- do we include FW to separate control vs data plane?
- do we include DC GW to separate NFVI from external environments?
- do we include OoB switch

Each instance of IaaS relies on physical resource: servers, switches, ToR

<p align="center"><img src="../figures/Figure_4_1_Network_Fabric_Physical.png" alt="Network Fabric -- Physical"></br>Figure 3-3: Network Fabric – Physical</p>
Figure 3-3 shows a physical network layout where each physical server is dual homed to TOR (C/Agg-Leaf) switches with redundant (2x) connections. The Leaf switches are dual homed with redundant connections to spines.

#### 3.4.2.3. Storage
Content to be developed including for Ceph 

[OpenStack](https://docs.openstack.org/arch-design/design-storage.html) supports many different storage architectures and backends. The choice of a particular backend storage is driven by a number of factors including: scalability, resiliency, availability, data durability, capacity and performance. 

Most cloud storage architectures incorporate a number of clustered storage nodes that provide high bandwidth access to physical storage backends connected by high speed networks. The architecture consists of multiple storage controller units, each a generic server (CPU, Cache, storage), managing a number of high-performance hard drives. The distributed block storage software creates an abstract single pool of storage by aggregating all of the controller units. Advanced and high-speed networking (data routing) and global load balancing techniques ensure high-performance, high availability storage system

<a name="3.5"></a>
## 3.5. Deployment Models
Content to be developed along the following lines
*	How do we define the different deployment types?
    - Edge
    -	Core DC 
    -	etc.

<a name="3.6"></a>
## 3.6. Architectural Drivers – Requirements Traceability





