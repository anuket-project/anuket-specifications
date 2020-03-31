[<< Back](../../openstack)

# 4. NFVI + VIM Component Level Architecture
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Underlying Resources](#4.2)
  * [4.2.1 Virtualisation](#4.2.1)
  * [4.2.2 Compute](#4.2.2)
  * [4.2.3 Network Fabric](#4.2.3)
  * [4.2.4 Storage Backend](#4.2.4)
* [4.3 Virtualised Infrastructure Manager (VIM)](#4.3)
  * [4.3.1 VIM Services](#4.3.1)
  * [4.3.2 Containerised OpenStack Services](#4.3.2)
* [4.4 Consumable Infrastructure Resources and Services](#4.4)
  * [4.4.1 Support for Profiles and T-shirt instance types](#4.4.1)
  * [4.4.2 Logical segregation and high availability](#4.4.2)
  * [4.4.3 Transaction Volume Considerations](#4.4.3)
* [4.5 Cloud Topology.](#4.5)
  * [4.5.1 Cloud Topology Considerations](#4.5.1)



<a name="4.1"></a>
## 4.1 Introduction.

Chapter 3 introduced the components of an OpenStack-based IaaS
-	Consumable Infrastructure Resources and Services
-	NFVI Management Software (VIM: OpenStack) core services and architectural constructs needed to consume and manage the consumable resources
-	Underlying physical compute, storage and networking resources

This chapter delves deeper into the capabilities of these different resources and their needed configurations to create and operate an OpenStack-based IaaS cloud. This chapter specifies details on the structure of control and user planes, operating systems, hypervisors and BIOS configurations, and architectural details of underlay and overlay networking, and storage, and the distribution of OpenStack service components among nodes. The chapter gets into details into items such as the implementation support for flavors. 


<a name="4.2"></a>
## 4.2 Underlying Resources

<a name="4.2.1"></a>
### 4.2.1 Virtualisation
In OpenStack, KVM is configured as the default hypervisor for compute nodes. 
- Configuration: [OpenStack](https://docs.openstack.org/nova/pike/admin/configuration/hypervisor-kvm.html) specifies the following KVM configuration steps/instructions to configure KVM:
  - Enable KVM based hardware virtualisation in BIOS. OpenStack provides instructions on how to enable hardware virtualisation for different hardware platforms (x86, Power)
    - QEMU is similar to KVM in that both are libvirt controlled, have the same feature set and utilize compatible virtual machine images 
  -	Configure Compute backing storage
  -	Specify the CPU Model for KVM guests (VMs)
  -	KVM Performance Tweaks
-	[Hardening](https://docs.openstack.org/security-guide/compute/hardening-the-virtualization-layers.html) 
    - OpenStack recommends minimizing the code base by removing unused components 
    -	sVirt (Secure Virtualisation) provides isolation between VM processes, devices, data files and system processes


<a name="4.2.2"></a>
### 4.2.2. Compute

#### 4.2.2.1. Cloud Deployment (Foundation/management) Node
Minimal configuration: 1 node

#### 4.2.2.2. OpenStack Control Plane Servers (Control Nodes)
- BIOS Requirements
For OpenStack control nodes we use the BIOS parameters for the basic profile defined in [Chapter 5.4 of the Reference Model](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter05.md#5.4). Additionally, for OpenStack we need to set the following boot parameters:

| BIOS/boot Parameter | Value |
|--------------------|--------------------|
| Boot disks |RAID 1 |
| CPU reservation for host (kernel) |1 core per Numa |
| CPU allocation ratio |2:1 |
| <to be filled if needed>|  |
| …|     |

-	How many nodes to meet SLA
    -	Minimum 3 nodes for high availability
-	HW specifications
    -	Boot disks are dedicated with Flash technology disks
-	Sizing rules
    -	It is easy to horizontally scale the number of control nodes
    -	The number of control nodes is determined by a minimum number needed for high availability (viz., 3 nodes) and the extra nodes needed to handle the transaction volumes, in particular, for Messaging service (e.g., RabbitMQ) and Database (e.g., MySQL) to track state. 
    -	The number of control nodes only needs to be increased in environments with a lot of changes, such as a testing lab, or a very large cloud footprint (rule of thumb: number of control nodes = 3 + quotient(number of compute nodes/1000)).
      -	The [Services Placement Summary table](https://fuel-ccp.readthedocs.io/en/latest/design/ref_arch_100_nodes.html) specifies the number of instances that are required based upon the cloud size (number of nodes).


#### 4.2.2.3. Network nodes

Networks nodes are mainly used for L3 traffic management for overlay tenant network (see more detail in section 4.3.1.5 Neutron)

-	BIOS requirements 

| BIOS/boot Parameter | Value |
|--------------------|--------------------|
| Boot disks |RAID 1 |
| <to be filled if needed>|  |
| …|  
 
-	How many nodes to meet SLA
    - Minimum 2 nodes for high availibility using VRRP.
-	HW specifications
    - 3 NICs card are needed if we want to isolate the different flows :
         - 1 NIC for Tenant Network
         - 1 NIC for External Network
         - 1 NIC for Other Networks (PXE, Mngt ...)
-	Sizing rules
    - Scale out of network node is not easy 
    - DVR can be an option for large deployment (see more detail in chapter 4.3.1.5 - Neutron)

#### 4.2.2.4. Storage nodes
-	BIOS requirements

| BIOS/boot Parameter | Value |
|--------------------|--------------------|
| Boot disks |RAID 1 |
| <to be filled if needed>|  |
| …|  
 
-	HW specifications
-	How many nodes to meet SLA
-	Sizing rules

#### 4.2.2.5. Compute Nodes
-	The software and hardware configurations are as specified in the [Reference Model chapter 5.4](../../../ref_model/chapters/chapter05.md#5.4)
-	BIOS requirement
    -	The general bios requirements are described in the [Reference Model chapter 5.4](../../../ref_model/chapters/chapter05.md#5.4)
    -	Additionally, for OpenStack we need to set the following boot parameters:

| BIOS/boot Parameter | Basic  | Network Intensive |
|---------------|-----------|------------------|
| Boot disks | RAID 1 | RAID 1 | 
| CPU reservation for host (kernel) | 1 core per Numa | 1 core per Numa | 
| CPU Pinning | No | Yes | 
| <to be filled if needed> |  |  | 
| … |  |  | <!--- | --->

<!--- 
Had to delete the Column for Compute intensive as commenting in table  didn't work 
Entries were:
Boot Disks: RAID 1
CPU reservation for host: 1 core per NUMA
--->
-	How many nodes to meet SLA
    - minimum: two nodes per profile
-	HW specifications
    -	Boot disks are dedicated with Flash technology disks
    - In case of DPDK usage, cores (together with their sibling threads) must be reserved for DPDK Poll Mode Drivers (PMD), hugepages set to at least 1 GB, and all power settings disabled in the BIOS. The number of cores reserved for this overhead depends on the desired throughput (the number of Mpps we want to deliver).
    
-	Sizing rules

| Number of CPU sockets| s | 
| ------------|--|
| Number of cores| c | 
| SMT| t | 
| RAM| rt | 
| Storage| d | 
| Overcommit| o | 
| Average vCPU per instance | v |
| Average RAM per instance | ri |


| | | Basic | Network Intensive | 
|---------------|------------|------------|------------|
| # of VMs per node (vCPU) | (s*c*t*o)/v | 4*(s*c*t)/v | (s*c*t)/v|  
| # of VMs per node (RAM) | rt/ri | rt/ri | rt/ri |  
| | | | |  
| Max # of VMs per node|  | min(4*(s*c*t)/v, rt/ri)| min((s*c*t)/v, rt/ri)|  

<!--- 
Had to delete the Column for Compute intensive as commenting in table  didn't work 
Entries were:
# of VMs per node (vCPU): s*c*t)/v| (s*c*t)/v
# of VMs per node (RAM): rt/ri
Max # of VMs per node: min((s*c*t)/v, rt/ri)
--->
Caveats:
-	These are theoretical limits
-	Affinity and anti-affinity rules, among other factors, affect the sizing

#### 4.2.2.6. Compute Resource Pooling Considerations

-	Multiple pools of hardware resources where each resource pool caters for workloads of a specific profile (for example, network intensive) leads to inefficient use of the hardware as the server resources are specific to the flavour. If not properly sized or when demand changes can lead to oversupply/starvation scenarios; reconfiguration may not be possible because of the underlying hardware or inability to vacate servers for reconfiguration to support another flavour type. 
-	Single pool of hardware resources including for controllers have the same CPU type. This is operationally efficient as any server can be utilized to support a flavour or controller. The single pool is valuable with unpredictable workloads or when the demand of certain flavours is insufficient to justify individual hardware selection. 

#### 4.2.2.7. Reservation of Compute Node Cores
The [RA-1 2.3.2 Infrastructure Requirements](./chapter02.md#232-infrastructure-requirements) req.inf.com.08 requires the allocation of "certain number of host cores/threads to non-tenant workloads such as for OpenStack services." A number ("n") of random cores can be reserved for host services (including OpenStack services) by specifying the following in nova.conf:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; reserved_host_cpus = n

where n is any positive integer.

If we wish to dedicate specific cores for host processing we need to consider two different use cases:

    1. Require dedicated cores for Guest resources
    2. No dedicated cores are required for Guest resources

Scenario #1, results in compute nodes that host both pinned and unpinned workloads. In the OpenStack Pike release, scenario #1 is not supported; it may also be something that operators may not allow. Scenario #2 is supported through the specification of the cpu_shared_set configuration. The cores and their sibling threads dedicated to the host services are those that do not exist in the cpu_shared_set configuration.

Let us consider a compute host with 20 cores and SMT enabled (let us disregard NUMA) and the following parameters have been specified. The physical cores are numbered '0' to '19' while the sibling threads are numbered '20' to '39' where the vcpus numbered '0' and '20', '1' and '21', etc. are siblings:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cpu_shared_set = 1-7,9-19,21-27,29-39 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (can also be specified as cpu_shared_set = 1-19,^8,21-39,^28)

This implies that the two physical cores '0' and '8' and their sibling threads '20' and '28' are dedicated to the host services, and 19 cores and their sibling threads are available for Guest instances (and can be over allocated as per the specified cpu_allocation_ratio in nova.conf.

#### 4.2.2.8. Pinned and Unpinned CPUs

When a VM instance is created the vCPUs are, by default, not assigned to a particular host CPU. Certain workloads require real-time or near real-time behavior viz., uninterrupted access to their cores. For such workloads, CPU pinning allows us to bind an instance’s vCPUs to particular host cores. To configure a flavor to use pinned vCPUs, we use a dedicated CPU policy.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; openstack flavor set .xlarge --property hw:cpu_policy=dedicated

While an instance with pinned CPUs cannot use CPUs of another pinned instance, this does not apply to unpinned instances; an unpinned instance can utilize the pinned CPUs of another instance. To prevent unpinned instances from disrupting pinned instances, the hosts with CPU pinning enabled are pooled in their own host aggregate and hosts with CPU pinning disabled are pooled in another non-overlapping host aggregate. 

<a name="4.2.3"></a>
### 4.2.3. Network Fabric
**Content to be developed**
-	Physical switches, routers…
-	Switch OS
-	Minimum number of switches etc.
-	Dimensioning for East/West and North/South
-	Spine / Leaf topology – east – west 
-	Global Network parameters
-	OpenStack control plane VLAN / VXLAN layout
-	Provider VLANs

#### 4.2.3.1 Physical Network Topology



#### 4.2.3.2 High Level Logical Network Layout

<p align="center"><img src="../figures/Figure_4_1_OpenStack_Network_Layout_20200110.png" alt="Indicative OpenStack Network Layout"></br>Figure 4-1. Indicative OpenStack Network Layout.</p>

| Network | Description | Characteristics |
|----------|---------|--------------|
| Provisioning & Management | Initial OS bootstrapping of the servers via PXE, deployment of software and thereafter for access from within the control plane. | Security Domain: Management<br />Externally Routable: No<br />Connected to: All nodes | 
| Internal API | Intra-OpenStack service API communications, messaging and database replication | Security Domain: Management<br />Externally Routable: No <br />Connected to: All nodes except foundation | 
| Storage Management | Backend connectivity between storage nodes for heartbeats, data object replication and synchronisation | Security Domain: Storage <br />Externally Routable: No <br />Connected to: All nodes except foundation | 
| Storage Front-end | Block/Object storage access via cinder/swift | Security Domain: Storage<br />Externally Routable: No<br />Connected to: All nodes except foundation | 
| Tenant | VXLAN / Geneve project overlay networks (OVS kernel mode) – i.e. RFC1918 re-usable private networks as controlled by cloud administrator | Security Domain: Underlay<br />Externally Routable: No <br /> Connected to: controllers and computes | 
| External API | Hosts the public OpenStack API endpoints including the dashboard (Horizon) | Security Domain: Public<br />Externally routable: Yes<br />Connected to: controllers | 
| External Provider (FIP) | Network with a pool of externally routable IP addresses used by neutron routers to NAT to/from the tenant RFC1918 private networks | Security Domain: Data Centre<br />Externally routable: Yes<br />Connected to: controllers, OVS computes | 
| External Provider (VLAN) | External Data Centre L2 networks (VLANs) that are directly accessible to the project. Note: External IP address management is required | Security Domain: Data Centre<br />Externally routable: Yes<br />Connected to: OVS DPDK computes | 
| IPMI / Out of Band | The remote “lights-out” management port of the servers e.g. iLO, IDRAC / IPMI / Redfish | Security Domain: Management<br />Externally routable: No<br />Connected to: IPMI port on all servers | 

A VNF application network topology is expressed in terms of VMs, vNIC interfaces with vNet access networks, and WAN Networks while the VNF Application VMs require multiple vNICs, VLANs, and host routes configured within the VM’s Kernel.

#### 4.2.3.3. Octavia v2 API conformant Load Balancing
Load balancing is needed for automatic scaling, managing availability and changes. [Octavia](https://docs.openstack.org/octavia/latest/reference/introduction.html) is an open-source load balancer for OpenStack, based on HAProxy, and replaces the deprecated (as of OpenStack Queens release) Neutron LBaaS. The Octavia v2 API is a superset of the deprecated Neutron LBaaS v2 API and has a similar CLI for seamless transition. 

As a default Octavia utilizes Amphorae Load Balancer. Amphorae consists of a fleet of VMs, containers or bare metal servers and delivers horizontal scaling by managing and spinning these resources on demand. The reference implementation of the Amphorae image is an Ubuntu virtual machine running HAProxy. 

Octavia depends upon a number of OpenStack services including Nova for spinning up compute resources on demand and their life cycle management; Neutron for connectivity between the compute resources, project environment and external networks; Keystone for authentication; and Glance for storing of the compute resource images.

Octavia supports provider drivers which allows third-party load balancing drivers (such as F5, AVI, etc.) to be utilized instead of the default Amphorae load balancer. When creating a third-party load balancer, the **provider** attribute is used to specify the backend to be used to create the load balancer. The **list providers** lists all enabled provider drivers.  Instead of using the provider parameter, an alternate is to specify the flavor_id in the create call where provider-specific Octavia flavors have been created. 


#### 4.2.3.4. Neutron Extensions
OpenStack Neutron is an extensible framework that allows incorporation through plugins and API Extensions. API Extensions provides a method for introducing new functionality and vendor specific capabilities. Neutron plugins support new or vendor-specific functionality. Extensions also allow specifying new resources or extensions to existing resources and the actions on these resources.  Plugins implement these resources and actions.

CNTT Reference Architecture support the ML2 plugin (see below) as well as the service plugins including for [FWaaS (Firewall as a Service)](https://docs.openstack.org/neutron/pike/admin/fwaas.html), [LBaaS (Load Balancer as a Service)](https://governance.openstack.org/tc/reference/projects/octavia.html), and [VPNaaS (VPN as a Service)](https://opendev.org/openstack/neutron-vpnaas/). The OpenStack wiki provides a list of [Neutron plugins](https://wiki.openstack.org/wiki/Neutron#Plugins).

Every Neutron plugin needs to implement a minimum set of common [methods (actions for Pike release)](https://docs.openstack.org/neutron/pike/contributor/internals/api_extensions.html).  Resources can inherit Standard Attributes and thereby have the extensions for these standard attributes automatically incorporated. Additions to resources, such as additional attributes, must be accompanied by an extension. 

[Chapter 5](../chapter05.md), Interfaces and APIs, of this Reference Architecture provides a list of [Neutron Extensions]( ../chapter05.md#525-neutron).  The current available extensions can  be obtained using [List Extensions API](https://docs.openstack.org/api-ref/network/v2/#list-extensions) and details about an extension using [Show extension details API](https://docs.openstack.org/api-ref/network/v2/#show-extension-details).

**Neutron ML2 integration**
The OpenStack Modular Layer 2 (ML2) plugin simplifies adding networking technologies by utilizing drivers that implement these network types and methods for accessing them. Each network type is managed by an ML2 type driver and the mechanism driver exposes interfaces to support the actions that can be performed on the network type resources. The [OpenStack ML2 documentation](https://wiki.openstack.org/wiki/Neutron/ML2) lists example mechanism drivers.

#### 4.2.3.5. Network quality of service
With support of VNF workloads, the resources bottlenecks are not only the CPU and the memory but also the I/O bandwidth and the forwarding capacity of virtual and non-virtual switches and routers within the infrastructure. Several techniques (all complementary) can be used to improve QoS and try to avoid any issue due to a network bottleneck (mentioned per order of importance):
-	Nodes interfaces segmentation: Have separated NIC ports for Storage and Tenant networks. Actually, the storage traffic is bursty, and especially in case of service restoration after some failure or new service implementation, upgrades, etc. Control and management networks should rely on a separate interface from the interface used to handle tenant networks.
-	Capacity planning: FW, physical links, switches, routers, NIC interfaces and DCGW dimensioning (+ load monitoring: each link within a LAG or a bond shouldn’t be loaded over 50% of its maximum capacity to guaranty service continuity in case of individual failure).
-	Hardware choice: e.g. ToR/fabric switches, DCGW and NIC cards should have appropriate buffering and queuing capacity.
-	Network intensive compute node tuning (including OVS-DPDK)

#### 4.2.3.6. Integration Interfaces.
DHCP When the Neutron-DHCP agent is hosted in controller nodes, then VMs, on a Tenant network, that need to acquire an IPv4 and/or IPv6 address, the VLAN for the Tenant must be extended to the control plane servers so that the Neutron agent can receive the DHCP requests from the VM and send the response to the VM with the IPv4 and/or IPv6 addresses and the lease time. Please see OpenStack provider Network.
-	DNS
-	LDAP
-	IPAM

<a name="4.2.4"></a>
### 4.2.4. Storage Backend
Storage systems are available from multiple vendors and can also utilize commodity hardware from any number of open-source based storage packages (such as LVM, Ceph, NFS, etc.). The proprietary and open-source storage systems are supported in Cinder through specific plugin drivers. The OpenStack [Cinder documentation]( https://docs.openstack.org/cinder/latest/reference/support-matrix.html) specifies the minimum functionality that all storage drivers must support. The functions include:
-	Volume: create, delete, attach, detach, extend, clone (volume from volume), migrate
-	Snapshot: create, delete and create volume from snapshot
-	Image: create from volume

The document also includes a matrix for a number of proprietary drivers and some of the optional functions that these drivers support. This matrix is a handy tool to select storage backends that have the optional storage functions needed by the cloud operator. The cloud workload storage requirements helps determine the backends that should be deployed by the cloud operator.   The common storage backend attachment methods include iSCSI, NFS, local disk, etc. and the matrix list the supported methods for each of the vendor drivers. The OpenStack Cinder [Available Drivers]( https://docs.openstack.org/cinder/latest/drivers.html) documentation provides a list of all OpenStack compatible drivers and their configuration options.

The [Cinder Configuration]( https://docs.openstack.org/cinder/latest/configuration/index.html) document provides information on how to configure cinder including CNTT required capabilities for volume encryption, Policy configuration, quotas, etc. The [Cinder Administration]( https://docs.openstack.org/cinder/latest/admin/index.html) document provides information on the capabilities required by CNTT including managing volumes, snapshots, multi-storage backends, migrate volumes, etc. 

[Ceph](https://ceph.io/) is the default CNTT Reference Architecture storage backend and is discussed below.

#### 4.2.4.1. Ceph Storage Cluster
The Ceph storage cluster is deployed on bare metal hardware. The minimal configuration is a cluster of three bare metal servers to ensure High availability. The Ceph Storage cluster consists of the following components:
-	CEPH-MON (Ceph Monitor)
-	OSD (object storage daemon)
-	RadosGW (Rados Gateway)
- Journal
- Manager

Ceph monitors maintain a master copy of the maps of the cluster state required by Ceph daemons to coordinate with each other. Ceph OSD handle the data storage (read/write data on the physical disks), data replication, recovery, rebalancing, and provides some monitoring information to Ceph Monitors. The RadosGW provides Object Storage RESTful gateway with a Swift-compatible API for Object Storage.

<p align="center"><img src="../figures/Figure_4_x_Ceph.png" alt="Ceph Storage System"></br>Figure 4-2. Ceph Storage System.</p>

**BIOS Requirement for Ceph servers**

| BIOS/boot Parameter | Value |
|-------------|----------------|
| Boot disks | RAID 1 |

How many nodes to meet SLA :
-	minimum: three bare metal servers where Monitors are collocated with OSD. Note: at least 3 Monitors and 3 OSDs are required for High AVailability. 

HW specifications :
- Boot disks are dedicated with Flash technology disks
- For an IOPS oriented cluster (Flash technology ), the journal can be hosted on OSD disks
- For a capacity oriented cluster (HDD), the journal must be hosted on dedicated Flash technology disks

Sizing rules :
-	Minimum of 6 disks per server
-	Replication factor : 3
-	1 Core-GHz per OSD
-	16GB RAM baseline + 2-3 GB per OSD

<a name="4.3"></a>
## 4.3 Virtualised Infrastructure Manager (VIM)
This section covers:
-	Detailed breakdown of OpenStack core services 
-	Specific build-time parameters

<a name="4.3.1"></a>
### 4.3.1 VIM Services
A high level overview of the core OpenStack Services was provided in [Chapter 3](./chapter03.md). In this section we describe the core and other needed services in more detail.

#### 4.3.1.1 Keystone
Keystone is the authentication service, the foundation of identity management in OpenStack. Keystone needs to be the first deployed service. Keystone has services running on the control nodes and no services running on the compute nodes:
-	Keystone admin API
-	Keystone public API – in Keystone V3 this is the same as the admin API,

#### 4.3.1.2 Glance
Glance is the image management service. Glance has only a dependency on the Keystone service therefore it is the second one deployed. Glance has services running on the control nodes and no services running on the compute nodes:
-	Glance API
-	Glance Registry

_The Glance backends include Swift, Ceph RBD and NFS_

#### 4.3.1.3 Cinder
Cinder is the block device management service, Cinder depends on Keystone and possibly Glance to be able to create volumes from images. Cinder has services running on the control nodes and no services running on the compute nodes:
-	Cinder API
-	Cinder Scheduler
-	Cinder Volume – the Cinder volume process needs to talk to its backends

_The Cinder backends include SAN/NAS storage, iSCSI drives, Ceph RBD and NFS._ 

#### 4.3.1.4 Swift
Swift is the object storage management service, Swift depends on Keystone and possibly Glance to be able to create volumes from images. Swift has services running on the control nodes and the compute nodes:
-	Proxy Services
-	Object Services
-	Container Services
-	Account Services

_The Swift backends include iSCSI drives, Ceph RBD and NFS._ 

#### 4.3.1.5 Neutron
Neutron is the networking service, Neutron depends on Keystone and has services running on the control nodes and the compute nodes:
-	neutron-api
-	neutron-rpc
-	neutron-*-agent agents which runs on Compute and Network nodes

#### 4.3.1.6 Nova
Nova is the compute management service, Nova depends on all above components and is deployed after. Nova has services running on the control nodes and the compute nodes:
-	nova-metadata-api
-	nova-placement-api
-	nova-compute api
-	nova-consoleauth
-	nova-scheduler
-	nova-conductor
-	nova-novncproxy
-	nova-compute-agent which runs on Compute node

#### 4.3.1.7 Ironic
Ironic is the bare metal provisioning service. Ironic depends on all above components and is deployed after. Ironic has services running on the control nodes and the compute nodes:
-	Ironic API
-	ironic-conductor which executes operation on bare metal nodes

Note: This is an optional service. As Ironic is currently not invoked directly (only invoked through other services such as Nova) hence its APIs will not be specified.

#### 4.3.1.8 Heat
Heat is the orchestration service using template to provision cloud resources, Heat integrates with all OpenStack services. Heat has services running on the control nodes and no services running on the compute nodes:
-	heat-api
-	heat-cfn-api
-	heat-engine

#### 4.3.1.9 Horizon
Horizon is the Web User Interface to all OpenStack services. Horizon has services running on the control nodes and no services running on the compute nodes.

#### 4.3.1.10 Cyborg
Cyborg is the acceleration resources management service. Cyborg depends on Nova and has services running on the control node and compute node. Cyborg-api, cyborg-conductor and cyborg-db are hosted on control nodes.
-	cyborg-api
-	cyborg-conductor
-	cyborg-db
- cyborg-agent  which runs on compute nodes
- *-driver drivers which run on compute nodes and depend on the acceleration hardware

#### 4.3.1.11 Placement
The OpenStack Placement service enables tracking (or accounting) and scheduling of resources. It provides a RESTful API and a data model for the managing of resource provider inventories and usage for different classes of resources. In addition to standard resource classes, such as VCPU, MEMORY_MB and DISK_GB, the Placement service supports custom resource classes (prefixed with “CUSTOM_”).  The placement service is primarily utilized by nova-compute and nova-scheduler. Other OpenStack services such as Neutron or Cyborg can also utilize placement and do so by creating [Provider Trees]( https://docs.openstack.org/placement/latest/user/provider-tree.html). The following data objects are utilized in the [placement service]( https://docs.openstack.org/placement/latest/user/index.html): 

<p>Resource Providers provide consumable inventory of one or more classes of resources (cpu, memory or disk). A resource provider can be a compute host, for example.</p>
    
<p>Resource Classes specifies the type of resources (VCPU, MEMORY_MB and DISK_GB or CUSTOM_\*)</p>
    
<p>Inventory: Each resource provider maintains the total and reserved quantity of one or more classes of resources.  For example, RP_1 has available inventory of 16 VCPU, 16384 MEMORY_MB and 1024 DISK_GB.</p>
    
<p>Traits are qualitative characteristics of the resources from a resource provider. For example, the trait for RPA_1 “is_SSD” to indicate that the DISK_GB provided by RP_1 are solid state drives.</p>
    
<p>Allocations represent resources that have been assigned/used by some consumer of that resource.</p>
    
<p>Allocation candidates is the collection of resource providers that can satisfy an allocation request.</p>


<a name="4.3.2"></a>
### 4.3.2. Containerised OpenStack Services 
Containers are lightweight compared to Virtual Machines and leads to efficient resource utilization. Kubernetes auto manages scaling, recovery from failures, etc. Thus, it is recommended that the OpenStack services be containerized for resiliency and resource efficiency.

In Chapter 3, Figure 3.2 shows a high level Virtualised OpenStack services topology. The containerized OpenStack services topology version is shown in Figure 4-3.

<p align="center"><img src="../figures/Figure_4_2_Containerised_OpenStack_Services.png" alt="Containerised OpenStack Services Topology"></br>Figure 4-3. Containerised OpenStack Services Topology.</p>


<a name="4.4"></a>
## 4.4 Consumable Infrastructure Resources and Services

<a name="4.4.1"></a>
### 4.4.1. Support for Profiles and T-shirt instance types
Reference Model Chapter 4 and  5 provide information about the instance types and size information. OpenStack flavors with their set of properties describe the VM capabilities and size required to determine the compute host which will run this VM. The set of properties must match compute profiles available in the infrastructure. To implement these profiles and sizes requires the setting up of information as specified in the Tables below. As OpenStack no longer provides default flavors, the CNTT pre-defined flavors will have to be created with their various configuration properies.

<!---
Original Table w Compute Intensive
| Flavor Capabilities | Reference<br>RM Chapter 4 and 5 | Basic | Network Intensive | Compute Intensive |
|----------|-------------|--------------|-------------|-------------|
| CPU allocation ratio | nfvi.com.cfg.001| In Nova.conf include <br>cpu_allocation_ratio= 4.0 | In Nova.conf include <br>cpu_allocation_ratio= 1.0 | In Nova.conf include <br>cpu_allocation_ratio= 1.0 |
| NUMA Awareness | nfvi.com.cfg.002 | | In flavor create or flavor set specify<br>--property hw:numa_nodes=<#numa_nodes – 1> | In flavor create or flavor set specify<br>--property hw:numa_nodes=<#numa_nodes – 1> |
| CPU Pinning | nfvi.com.cfg.003| In flavor create or flavor set specify <br> --property hw:cpu_policy=shared (default) | In flavor create or flavor set specify <br>--property hw:cpu_policy=dedicated <br>and<br>--property hw:cpu__thread_policy= <prefer, require, isolate> | In flavor create or flavor set specify <br>--property hw:cpu_policy=dedicated <br>and <br>--property hw:cpu__thread_policy= <prefer, require, isolate>|
| Huge Pages | nfvi.com.cfg.004| | --property hw:mem_page_size=large | --property hw:mem_page_size=large | 
| OVS-DPDK | nfvi.net.acc.cfg.001| | ml2.conf.ini configured to support <br>[OVS] <br>datapath_type=netdev <br><br>Note: huge pages should be configured to large | ml2.conf.ini configured to support <br>[OVS] <br>datapath_type=netdev <br><br>Note: huge pages should be configured to large |
| Local Storage SSD | nfvi.hw.stg.ssd.cfg.002| trait:STORAGE_DISK_SSD=required | trait:STORAGE_DISK_SSD=required | trait:STORAGE_DISK_SSD=required |
| Port speed | nfvi.hw.nic.cfg.002 | --property quota vif_inbound_average=1310720 <br>and<br>vif_outbound_average=1310720<br><br>Note: 10 Gbps = 1250000 kilobytes per second | --property quota vif_inbound_average=3125000 <br>and <br>vif_outbound_average=3125000<br><br>Note: 25 Gbps = 3125000 kilobytes per second | --property quota vif_inbound_average=3125000 <br>and <br>vif_outbound_average=3276800<br><br>Note: 25 Gbps = 3276800 kilobytes per second | 
New Table w/o Compute Intensive column below
--->

| Flavor Capabilities | Reference<br>RM Chapter 4 and 5 | Basic | Network Intensive | 
|----------|-------------|--------------|-------------|
| CPU allocation ratio (custom extra_specs) | nfvi.com.cfg.001| In flavor create or flavor set <br>--property cpu_allocation_ratio=4.0 | In flavor create or flavor set <br>--property cpu_allocation_ratio=1.0 |
| NUMA Awareness | nfvi.com.cfg.002 | | In flavor create or flavor set specify<br>--property hw:numa_nodes=<#numa_nodes – 1> | 
| CPU Pinning | nfvi.com.cfg.003| In flavor create or flavor set specify <br> --property hw:cpu_policy=shared (default) | In flavor create or flavor set specify <br>--property hw:cpu_policy=dedicated <br>and<br>--property hw:cpu__thread_policy= <prefer, require, isolate> |
| Huge Pages | nfvi.com.cfg.004| | --property hw:mem_page_size=large | 
| OVS-DPDK | nfvi.net.acc.cfg.001| | ml2.conf.ini configured to support <br>[OVS] <br>datapath_type=netdev <br><br>Note: huge pages should be configured to large |
| Local Storage SSD | nfvi.hw.stg.ssd.cfg.002| trait:STORAGE_DISK_SSD=required | trait:STORAGE_DISK_SSD=required | 
| Port speed | nfvi.hw.nic.cfg.002 | --property quota vif_inbound_average=1310720 <br>and<br>vif_outbound_average=1310720<br><br>Note: 10 Gbps = 1250000 kilobytes per second | --property quota vif_inbound_average=3125000 <br>and <br>vif_outbound_average=3125000<br><br>Note: 25 Gbps = 3125000 kilobytes per second |

To configure the T-shirt sizes (specified in [Table 4-17](../../../ref_model/chapters/chapter04.md#4211-predefined-compute-flavours) Reference Model Chapter4), the parameters in the following table are specified as part of the flavor create; the parameters are preceded by "--".

| T-Shirt Size | vCPU ("c") | RAM ("r") | Local Disk ("d") |
|-----|------|---------|----------------|
| .tiny | 1<br>-- vcpus 1 | 512 MB<br>-- ram 512 | 1 GB<br>-- disk 1 |
| .small | 1<br>-- vcpus 1 | 2 GB<br>-- ram 2048 | 20 GB<br>-- disk 20 |
| .medium | 2<br>-- vcpus 2 | 4 GB<br>-- ram 4096 | 40 GB<br>-- disk 40 |
| .large | 4<br>-- vcpus 4 | 8 GB<br>-- ram 8192 | 80 GB<br>-- disk 80 |
| .2xlarge* | 8<br>-- vcpus 8 | 16 GB<br>-- ram 16384 | 160 GB<br>-- disk 160 |
| .4xlarge* | 16<br>-- vcpus 16 | 32 GB<br>-- ram 32768 | 320 GB<br>-- disk 320 |

In addition, to configure the storage IOPS the following two parameters need to be specified in the flavor create: --property quota:disk_write_iops_sec=<IOPS#> and --property quota:disk_read_iops_sec=<IOPS#>.  

The flavor create command and the mandatory and optional configuration parameters is documented in https://docs.openstack.org/nova/latest/user/flavors.html.

<a name="4.4.2"></a>
### 4.4.2. Logical segregation and high availability
To Ensure Logical segregation and high availability, the architecture will rely on the following principles:
-	Availability zone: provide resiliency and fault tolerance for VNF deployments, by means of physical hosting distribution of Compute Nodes in separate racks with separate power supply, in the same or different DC room
-	Affinity-groups: allow tenants to make sure that VNFC instances are on the same compute node or are on different compute nodes.

Note: The NFVI doesn’t provide any resiliency mechanisms at the service level. Any VM restart shall be triggered by the VNF Manager instead of OpenStack:
-	It doesn’t implement Instance High Availability which could allow OpenStack Platform to automatically re-spawn instances on a different Compute node when their host Compute node breaks.
-	Physical host reboot does not trigger automatic VM recovery.
-	Physical host reboot does not trigger the automatic start of VM

**Limitations and constraints**
-	NUMA Overhead: isolated core will be used for overhead tasks from the hypervisor 

For Network intensive instances, VNF Component should fit into a single NUMA zone for performance reason.

<a name="4.4.3"></a>
### 4.4.3. Transaction Volume Considerations

Storage transaction volumes impose a requirement on North-South network traffic in and out of the storage backend. Data availability requires that the data be replicated on multiple storage nodes and each new write imposes East-West network traffic requirements.


<a name="4.5"></a>
## 4.5 Cloud Topology

<a name="4.5.1"></a>
### 4.5.1. Cloud Topology Considerations

A Telco cloud will be deployed in multiple locations (“sites”) of varying size and capabilities (HVAC, for example); or stated slightly differently, multiple telco clouds (i.e. OpenStack end points) will be deployed and they all contain isolated resources that do not rely on each other.   The application must span such end points in order to provide the required service SLA Irrespective of the nature of the deployment characteristics (number of racks, number of hosts, etc.), the intent of the architecture would be to allow VNFs to be deployed in these sites as needed without major changes; if not all as many as possible.
-	Large data center capable of hosting thousands of servers and the networking to support them
-	Mini data center (such as a central office) capable of hosting up to a hundred servers
-	Edge (not customer premise) capable of hosting between ten to fifty servers

Host profiles (SW Host profile + HW host profile) “partition” the cloud into pseudo sub-clouds, for example, hosts targeted for basic instance types, network intensive instance types and compute intensive instance types. This can happen, because of specific hardware adds and/or hardware and software configurations.  Depending upon the workload types and the capacity requirements, cloud providers and operators may choose to support the instance types with targeted hardware (different number of sockets, RAM, clock speeds, etc.) and host profiles or choose common hardware and minimize the number of host profiles (for example, network intensive and compute intensive types using a common host profile).

As we get away from the large data centers to the smaller sites it becomes progressively difficult to be able to create enough capacity for each of these instance types in support of their target VNFs or to have a mix of hardware targeted for each instance type.





