[<< Back](../../ref_model)
# 3 Modelling

## Table of Contents
* [3.1 Model](#3.1)
* [3.2 Virtual Resources](#3.2)
  * [3.2.1 Tenant](#3.2.1)
  * [3.2.2 Compute](#3.2.2)
  * [3.2.3 Storage](#3.2.3)
  * [3.2.4 Availability Zone](#3.2.4)
* [3.3 Cloud Infrastructure Management](#3.3)
  * [3.3.1 Virtual Infrastructure Manager](#3.3.1)
  * [3.3.2 Hardware Infrastructure Manager](#3.3.2)
* [3.4 Hardware Infrastructure Resources](#3.4)
  * [3.4.1 Hardware Acceleration Resources](#3.4.1)
* [3.5 Network](#3.5)
* [3.6 Storage](#3.6)
* [3.7 Sample reference model realization](#3.7)
* [3.8 Hardware Acceleration Abstraction](#3.8)
  * [3.8.1 Types of Accelerators](#3.8.1)
  * [3.8.2 Infrastructure and Application Level Acceleration](#3.8.2)
  * [3.8.4 CPU Instructions](#3.8.4)
  * [3.8.5 Fixed Function Accelerators](#3.8.5)

It is necessary to clearly define the infrastructure resources and their capabilities a shared cloud infrastructure (network function virtualisation infrastructure, NFVI) will provide for hosting workloads including virtual network functions (VNFs) and/or cloud-native network functions (CNFs). The lack of a common understanding of which resources and corresponding capabilities a suitable cloud infrastructure should provide may lead to several issues which could negatively impact the time and the cost for on-boarding and maintaining these solutions on top of a virtualised infrastructure.

The abstraction model presented in this Reference Model (RM) specifies a common set of virtual infrastructure resources that a cloud infrastructure will need to provide to be able to host most of the typical VNF/CNF telco workloads. The intention of this Reference Model is to follow the following principles:

- **Scope:** the model should describe the most relevant virtualised infrastructure resources (incl. acceleration technologies) a cloud infrastructure needs to host Telco workloads
- **Separation of Concern:** the model should support a clear distinction between the responsibilities related to maintaining the network function virtualisation infrastructure and the responsibilities related to managing the various VNF workloads
- **Simplicity:** the amount of different types of resources (including their attributes and relationships amongst one another) should be kept to a minimum to reduce the configuration spectrum which needs to be considered
- **Declarative**: the model should allow for the description of the intended state and configuration of the cloud infrastructure resources for automated life cycle management
- **Explicit:** the model needs to be rich enough to allow for the instantiation and the on-going operation of the cloud infrastructure
- **Lifecycle:** the model must distinguish between resources which have independent lifecycles but should group together those resources which share a common lifecycle
- **Aligned:** the model should clearly highlight the dependencies between its components to allow for a well-defined and simplified synchronisation of independent automation tasks.

_**To summarise:** the abstraction model presented in this document will build upon existing modelling concepts and simplify and streamline them to the needs of telco operators who intend to distinguish between infrastructure related and workload related responsibilities._

<a name="3.1"></a>
## 3.1 Model

The abstraction model for the cloud infrastructure is divided into two logical layers: the virtual infrastructure layer and the hardware infrastructure layer, with the intention that only the virtual infrastructure layer will be directly exposed to workloads (VNFs/CNFs):

<p align="center"><img src="../figures/ch03-model-overview.png" alt="Cloud Infrastructure Model Overview" Title="Cloud Infrastructure Model Overview" width="65%"/></p>
<p align="center"><b>Figure 3-1:</b> Cloud Infrastructure Model Overview.</p>

The functionalities of each layer are as follows:
- **Virtual infrastructure resources:** These are all the infrastructure resources (compute, storage and networks) which the cloud infrastructure provides to the workloads such as VNFs/CNFs. These virtual resources can be managed by the tenants and tenant workloads directly or indirectly via an application programming interface (API).
- **Virtual infrastructure manager:** This consists of the software components that manage the virtual resources and make those management capabilities accessible via one or more APIs. The responsibilities of this functionality include the management of logical constructs such as tenants, tenant workloads, resource catalogues, identities, access controls, security policies, etc.
- **Hardware infrastructure manager:** This is a logical block of functionality responsible for the management of the abstracted hardware resources (compute, network and storage) and as such it is shielded from the direct involvement with server host software.
- **Physical Infrastructure Resources:** These consist of physical hardware components such as servers, (including random access memory, local storage, network ports, and hardware acceleration devices), storage devices, network devices, and the basic input output system (BIOS).
- **Workloads (VNFs/CNFs):** These consist of workloads such as virtualized and/or containerized network functions that run within a virtual machine (VM) or as a set of containers.

<a name="3.2"></a>
## 3.2 Virtual Resources

The virtual infrastructure resources provided by the Cloud Infrastructure can be grouped into four categories as shown in the diagram below:

<p align="center"><img src="../figures/ch03-model-virtual-resources.png" alt="NFVI Virtual Infrastructure Resources" Title="NFVI Virtual Infrastructure Resources" width="65%"/></p>
<p align="center"><b>Figure 3-2:</b> Virtual Infrastructure Resources provide virtual compute, storage and networks in a tenant context.</p>

- **Tenants:** represent an isolated and independently manageable elastic pool of compute, storage and network resources
- **Compute resources:** represent virtualised computes for workloads and other systems as necessary
- **Storage resources:** represent virtualised resources for persisting data
- **Network resources:** represent virtual resources providing layer 2 and layer 3 connectivity

The virtualised infrastructure resources related to these categories are listed below.

<a name="3.2.1"></a>
### 3.2.1 Tenant

A cloud infrastructure needs to be capable of supporting multiple tenants and has to isolate sets of infrastructure resources dedicated to specific workloads (VNF/CNF) from one another. Tenants represent an independently manageable logical pool of compute, storage and network resources abstracted from physical hardware.

_**Example**: a tenant within an OpenStack environment or a Kubernetes cluster._


| Attribute  | Description                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------|
| `name`     | name of the logical resource pool                                                                       |
| `type`     | type of tenant (e.g. OpenStack tenant, Kubernetes cluster, …)                                           |
| `vcpus`    | max. number of virtual CPUs                                                                             |
| `ram`      | max. size of random access memory in GB                                                                 |
| `disk`     | max. size of ephemeral disk in GB                                                                       |
| `networks` | description of external networks required for inter-domain connectivity                                 |
| `metadata` | key/value pairs for selection of the appropriate physical context (e.g. location, availability zone, …) |

<p align="center"><b>Table 3-1:</b> Attributes of a tenant</p>

<a name="3.2.2"></a>
### 3.2.2 Compute
A virtual machine or a container/pod is used by a tenant capable of hosting the application components of workloads (VNFs). A virtual compute therefore requires a tenant context and, since it will need to communicate with other communication partners, it is assumed that the networks have been provisioned in advance.

_**Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV._

| Attribute      | Description                                                                   |
|----------------|-------------------------------------------------------------------------------|
| `name`         | name of the virtual host                                                      |
| `vcpus`        | number of virtual CPUs                                                        |
| `ram`          | size of random access memory in GB                                            |
| `disk`         | size of root disc in GB                                                       |
| `nics`         | sorted list of network interfaces connecting the host to the virtual networks |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology      |
| `metadata`     | key/value pairs for selection of the appropriate redundancy domain            |

<p align="center"><b>Table 3-2:</b> Attributes of compute resources</p>

<a name="3.2.3"></a>
### 3.2.3 Storage

A workload can request different types of storage based on data longevity: persistent or ephemeral storage.
Persistent storage outlives the compute instance whereas ephemeral storage is linked to compute instance lifecycle.

There are multiple storage performance requirements such as latency, IOPS and capacity. For example, a workload may require one of its storage device to provide low latency, high IOPS and very large/huge storage capacity (terabytes of data).
Low Latency storage is for workloads which have strong constraints on the time to access the storage.
High IOPS oriented storage is for workloads requiring lots of read/write actions.
Capacity oriented storage is for workloads that need lots of volumetry without strong perfomance constraints.

Storage resources have the following attributes:

| Attribute           | Description                                                              |
|---------------------|--------------------------------------------------------------------------|
| `name`              | name of storage resources                                                |
| `data availibilty`  | persistent or ephemeral                                                  |  
| `performance`       | latency, IOPS, capacity                            |
| `enhanced features` | replication, encryption                                                  |
| `type`              | block, object or file                                                    |
| `size`              | size in GB                                                       |

<p align="center"><b>Table 3-3:</b> Attributes of storage resources</p>


<a name="3.2.4"></a>
### 3.2.4 Availability Zone
An availability zone is a logical pool of physical resources (e.g. compute, block storage, and network).  These logical pools segment the physical resources of a cloud based on factors chosen by the cloud operator. The cloud operator may create availability zones based on location (rack, datacenter), or indirect failure domain dependencies like power sources.  Workloads can leverage availability zones to utilise multiple locations or avoid sharing failure domains for a workload, and thus increase its fault-tolerance.

As a logical group with operator-specified criteria, the only mandatory attribute for an Availability Zone is the name.

| Attribute | Description |
| --- | --- |
| `name` | name of the availability zone |

<p align="center"><b>Table 3-4:</b> Attributes of availability zones</p>

<a name="3.3"></a>
## 3.3 Cloud Infrastructure Management
Cloud infrastructure provides the capability to manage virtual and hardware resources via Application Programmable Interfaces or graphical user interfaces.

<a name="3.3.1"></a>
### 3.3.1 Virtual Infrastructure Manager
The virtual infrastructure manager allows to:

* setup, manage and delete tenants,
* setup, manage and delete user- and service-accounts,
* manage access privileges and
* provision, manage, monitor and delete virtual resources.

<p align="center"><img src="../figures/ch03-model-virtual-manager.png" alt="Virtual Infrastructure Manager" Title="Virtual Infrastructure Manager" width="65%"/></p>
<p align="center"><b>Figure 3-3:</b> Virtual Infrastructure Manager.</p>

 The virtual infrastructure manager needs to support the following functional aspects:

* **API/UI**: an application programming interface / user interface providing access to the virtual resource management function

* **Catalogue**: manages the collection of available templates for virtual resource the cloud infrastructure can provide

* **Inventory**: manages the information related to virtual resources of a cloud infrastructure

* **Scheduler**: receives requests via API/UI, provisions and manages virtual resources by coordinating the activities of the compute-, storage- and network resources managers

* **Monitoring**:  monitors and collects information on all events and the current state of all virtual resources

* **Additional Management Functions**: include identity management, access management, policy management (e.g. to enforce security policies), etc.

* **Compute Resources Manager**: provides a mechanism to provision virtual resources with the help of hardware compute resources

* **Storage Resources Manager**: provides a mechanism to provision virtual resources with the help of hardware storage resources

* **Network Resources Manager**: provides a mechanism to provision virtual resources with the help of hardware network resources

<a name="3.3.2"></a>
### 3.3.2 Hardware Infrastructure Manager
The hardware infrastructure manager allows to:
* provision, manage, monitor and delete hardware resources (underlay network, physical compute, physical storage, accelerators)
* manage hardware resource discovery and topology
* manage equipment
* manage hardware infrastructure telemetry and log collection services

<p align="center"><img src="../figures/ch03-model-hardware-manager.png" alt="Hardware Infrastructure Manager" Title="Hardware Infrastructure Manager" width="65%"/></p>
<p align="center"><b>Figure 3-4:</b> Hardware Infrastructure Manager.</p>

The hardware infrastructure manager needs to support the following functional aspects:

 * **API/UI**: an application programming interface / user interface providing access to the hardware resource management functions

* **Discovery**: discover and manages the information related to hardware resources of a cloud infrastructure

* **Equipment**: discover and manages the information related to hardware resources of a cloud infrastructure

* **Resource Allocation and Composition**: creates and allocates abstracted hardware resources

* **Monitoring**:  monitors and collects information on all events and the current state of all hardware resources

* **Topology**:  manages topological view of hardware resources

* **Additional Management Functions**: include identity management, access management, policy management (e.g. to enforce security policies), etc.

* **Underlay Network Resources Manager**: provides a mechanism to provision hardware resources for the use by the underlay network (e.g. switch fabric, smartNICs)

* **Physical Compute Resources Manager**: provides a mechanism to provision hardware compute resources

* **Physical Storage Resources Manager**: provides a mechanism to provision hardware storage resources

* **Accelerators**: provide a mechanism to provision hardware accelerator services

<a name="3.4"></a>
## 3.4 Hardware Infrastructure Resources

Compute, Storage and Network resources serve as the foundation of the cloud infrastructure. They are exposed to and used by a set of networked Host Operating Systems in a cluster that normally handles the Virtualization Layer offering Virtual Machines or Containers where the application workloads (VNFs/CNFs) runs.

<p align="center"><img src="../figures/ch03-model-hardware-resources.png" alt="Cloud Infrastructure Hardware Resources" Title="Cloud Infrastructure Hardware Resources" width="65%"/></p>
<p align="center"><b>Figure 3-5:</b> Cloud Infrastructure Hardware Resources</p>

In managed Hardware Infrastructure systems, these consumable Compute, Storage and Network resources can be provisioned through operator commands or through software APIs.  There is a need to distinguish between these consumable resources, that are treated as leased resources, from the actual physical hardware resources that are installed in the data center. For this purpose, the hardware resource layer is conceptually split into a Logical Resource Layer that surfaces the consumable resources to the software layer above, and the Physical Resource Layer that is operated and managed by the Data Center Operations team from the HW Infrastructure Management functions.

Some installations might use a cluster of managed switches or storage components controlled by a Switch Fabric controller and/or a Storage Fabric controller acting as an appliance system. These systems should be federated with the HW Infrastructure Management system over some API to facilitate exchange of configuration intent, status and telemetry information allowing the HW Infrastructure Management and Management stack to automate Cloud Infrastructure operations. These appliance systems normally also have their own Equipment Management APIs and procedures for the hardware installation and maintenance staff.

An example could be a  Cloud Infrastructure stack federated with a commercial Switch Fabric where the Cloud Infrastructure shall be able to "send" networking configuration intent to the Switch Fabric and the Switch Fabric shall be able to "send" status and telemetry information to the Cloud Infrastructure e.g. Port/Link Status and packet counters of many sorts. The word "send" is a very lose definition of getting a message across to the other side, and could be implemented in many different ways.
This allows HW Infrastructure Management and Cloud Infrastructure management stack to have network automation that includes the switches that are controlled by the federated Switch Fabric. This would be a rather normal case for Operators  that have a separate Networking Department that owns and runs the Switch Fabric separately from the Data Center.

<a name="3.4.1"></a>
### 3.4.1 Hardware Acceleration Resources

For a given software network function and software infrastructure, Hardware Acceleration resources can be used to achieve requirements or improve cost/performance. Following table gives reasons and examples for using Hardware Acceleration.

| Reason for using Hardware Acceleration | Example | Comment |
|---|---|---|
| Achieve technical requirements | Strict latency or timing accuracy | Must be done by optimizing compute node; cannot be solved by adding more compute nodes |
| Achieve technical requirements | Fit within power or space envelope | Done by optimizing cluster of compute nodes |
| Improve cost/performance | Better cost and less power/cooling by improving performance per node | Used when functionality can be achieved through usage of accelerator or by adding more compute nodes |

<p align="center"><b>Table 3-5:</b> Reasons and examples for using Hardware Acceleration</p>

Hardware Accelerators can be used to offload software execution for purpose of accelerating tasks to achieve faster performance, or offloading the tasks to another execution entity to get more predictable execution times, efficient handling of the tasks or separation of authority regarding who can control the tasks execution.

More details about Hardware Acceleration are in [Section 3.8 Hardware Acceleration Abstraction](chapter03.md#3.8).


<a name="3.5"></a>
## 3.5 Network
Networking, alongside Compute and Storage, is an integral part of the Cloud Infrastructure (Network Function Virtualisation Infrastructure). The general function of networking in this context is to provide the connectivity between various virtual and physical resources required for the delivery of a network service. Such connectivity may manifest itself as a virtualised network between VMs and/or containers (e.g. overlay networks managed by SDN controllers, and/or programmable network fabrics) or as an integration into the infrastructure hardware level for offloading some of the network service functionality.

Normalization of the integration reference points between different layers of the Cloud Infrastructure architecture is one of the main concerns. In the networking context the primary focus is directed on the packet flow and control flow interfaces between the virtual resources (referred to as Software (SW) Virtualisation Layer) and physical resources (referred to as Hardware (HW) Infrastructure Layer), as well as on related integration into the various MANO reference points (hardware/network infrastructure management, orchestration). The identification of these two different layers (SW Virtualisation Layer and HW Infrastructure Layer) remains in alignment with the separation of resources into virtual and physical resources, generally used in this document, see e.g. Figure 3-1. The importance of understanding the separation of concerns between SW Virtualisation Layer and HW Infrastructure Layer is important because without it, the cardinality of having multiple CaaS and IaaS instances executing on their own private virtual resources from the single shared HW Infrastructure Layer cannot be expressed into separate administrative domains.

Principles that should be followed during the development and definition of the networking scope for the Reference Model, Reference Architectures, Reference Implementations and Reference Conformance test suites:

* Abstraction: A standardized network abstraction layer between the Virtualisation Layers and the Network Physical Resources Layer that hides (or abstracts) the details of the Network Physical resources from the Virtualisation Layers.

> **Note:**  In deployment phases this principle may be applied in many different ways e.g. depending on target use case requirements, workload characteristics, different algorithm implementations of pipeline stages and available platforms. The network abstraction layer supports, for example, physical resources with or without programmable hardware acceleration, or programmable network switches

* Agnosticism: Define Network Fabric concepts and models that can carry any type of traffic in terms of:
  * Control, User and Management traffic types
  * Acceleration technologies that can support multiple types of infrastructure deployments and network function workloads

* Automation: Enable end-to-end automation, from Physical Fabric installation and provisioning to automation of workloads (VNF/CNF) onboarding.

* Openness: All networking is based on open source or standardized APIs (North Bound Interfaces (NBI) and South Bound Interfaces (SBI)) and should enable integration of open source networking components such as SDN controllers.

* Programmability: Network model enables a programmable forwarding plane controlled from a separately deployed control plane.

* Scalability: Network model enables scalability to handle all traffic traverse North-South and East-West enabling small up to large deployments in a non-blocking manner.

* Workload agnostic: Network model is capable of providing connectivity to any type of workloads, including VNF, CNF and BareMetal workloads.

* Carrier Grade: Network model is capable of supporting deployments of the carrier grade workloads.

* Future proof: Network model is extendible to support known and emerging technology trends including SmartNICs, FPGAs and Programmable Switches, integrated for multi-clouds, and Edge related technologies.

<a name="3.6"></a>
## 3.6 Storage
The general function of storage subsystem is to provide the needed data store to various virtual and physical resources required for the delivery of a network service. In cloud infrastructure such storage may manifest itself in various ways like storage endpoints being exposed over network from software defined storage dedicated clusters or hyperconverged nodes (combining storage and other functions like compute or networking).
Storage also follows the alignment of separated virtual and physical resources of SW Virtualization Layer and HW infrastructure. Reasons for such alignment are described more in Section 3.5. The following principles apply to Storage scope for the Reference Model, Reference Architectures, Reference Implementations and Reference Conformance test suites:
* Abstraction: A standardized storage abstraction layer between the Virtualisation Layers and the Storage Physical Resources Layer that hides (or abstracts) the details of the Storage Physical resources from the Virtualisation Layers.
* Agnosticism: Define Storage subsystem concepts and models that can provide various storage types and performance requirements (more in Virtual Resources [3.2.3 Storage](#3.2.3)).
* Automation: Enable end-to-end automation, from Physical Storage installation and provisioning to automation of workloads (VNF/CNF) onboarding.
* Openness: All storage is based on open source or standardized APIs (North Bound Interfaces (NBI) and South Bound Interfaces (SBI)) and should enable integration of storage components such as Software Defined Storage controllers.
* Scalability: Storage model enables scalability to enable small up to large deployments.
* Workload agnostic: Storage model can provide storage functionality to any type of workloads, including VNF, CNF and BareMetal workloads.
* Future proof: Storage model is extendible to support known and emerging technology trends covering spectrum of memory-storage technologies including Software Defined Storage with mix of SATA- and NVMe-based SSDs, DRAM and Persistent Memory, integrated for multi-clouds, and Edge related technologies.

<a name="3.7"></a>
## 3.7 Sample reference model realization

The following diagram presents an example of the realization of the reference model, where a virtual infrastructure layer contains three coexisting but different types of implementation: a typical IaaS using VMs and a hypervisor for virtualisation, a CaaS on VM/hypervisor, and a CaaS on bare metal. This diagram is presented for illustration purposes only and it does not preclude validity of many other different combinations of implementation types. Note that the model enables several potentially different controllers orchestrating different type of resources (virtual and/or hardware). Management clients can manage virtual resources via Virtual Infrastructure Manager (Container Infrastructure Service Manager for CaaS, or Virtual Infrastructure Manager for IaaS), or alternatively hardware infrastructure resources via hardware infrastructure manager.  The latter situation may occur for instance when an orchestrator (an example of a management client) is involved in provisioning the physical network resources with the assistance of the controllers. Also, this realization example would enable implementation of a programmable fabric.

<p align="center"><img src="../figures/ch03-model-realization-diagram-2.png" alt="Reference model realization example" Title="Reference model realization example" width="65%"/></p>
<p align="center"><b>Figure 3-6:</b> Reference model realization example</p>

The terms Container Infrastructure Service Instance and Container Infrastructure Service Manager should be understood as defined in ETSI GR NFV-IFA 029 V3.3.1 [4]. More detailed deployment examples can be found in [Section 4.3](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter04.md#43-networking) of this Reference Model document.

<a name="3.8"></a>
## 3.8 Hardware Acceleration Abstraction

<a name="3.8.1"></a>
### 3.8.1 Types of Accelerators

Accelerator technologies can be categorized depending on where they are realized in the hardware product and how they get activated, life cycle managed and supported in running infrastructure.

| Acceleration technology/hardware | Example implementation | Activation/LCM/support | Usage by application tenant |
|---|---|---|---|
| CPU instructions | Within CPU cores | None for hardware | Application to load software library that recognizes and uses CPU instructions |
| Fixed function accelerator | Crypto, vRAN-specific adapter | Rare updates | Application to load software library/driver that recognizes and uses the accelerator |
| Firmware-programmable adapter | Network/storage adapter with programmable part of firmware image | Rare updates | Application normally not modified or aware |
| SmartNIC | Programmable accelerator for vSwitch/vRouter, NF and/or Hardware Infrastructure | Programmable by Infrastructure operator(s) and/or application tenant(s) | 3 types/operational modes: 1. Non-programmable normally with unaware applications; 2. Once programmable to activate; 3 Reprogrammable |
| SmartSwitch-based | Programmable Switch Fabric or TOR switch | Programmable by Infrastructure operator(s) and/or application tenant(s) | 3 operational modes: 1. Non-programmable normally with unaware applications; 2. Once programmable to activate; 3. Reprogrammable |

<p align="center"><b>Table 3-6:</b> Hardware acceleration categories, implementation, activation/LCM/support and usage</p>

<p align="center"><img src="../figures/ch03-example-of-server-and-smartswitch-based-nodes.png" alt="Examples of server- and SmartSwitch-based nodes (for illustration only)" Title="Examples of server- and SmartSwitch-based nodes (for illustration only)" width="65%"/></p>
<p align="center"><b>Figure 3-7:</b> Examples of server- and SmartSwitch-based nodes (for illustration only)</p>



<a name="3.8.2"></a>
### 3.8.2 Infrastructure and Application Level Acceleration

Figure 3-8 gives examples for Hardware Accelerators in [Sample reference model realization](#3.7) diagram.

<p align="center"><img src="../figures/ch03-hardware-acceleration-in-rm-realization-diagram.png" alt="Hardware Acceleration in RM Realization Diagram" Title="Hardware Acceleration in RM Realization Diagram" width="65%"/></p>
<p align="center"><b>Figure 3-6:</b> Hardware Acceleration in RM Realization Diagram</p>

Hardware Accelerators are part of the Hardware Infrastructure Layer. Those that need to be activated/programmed will expose management interfaces and have Accelerator Management software managing them in-band (from host OS) or out of band (OOB, over some network to the adapter without going through host OS). For more flexibility in management, such Accelerator Management can be carried over appropriate service with authentication mechanism before being exposed to Cloud Infrastructure operator and/or Application tenant.

Application uses software library supporting hardware acceleration and running on generic CPU instructions. Mapping workload to acceleration hardware is done with Cyborg in OpenStack or Device Plugin framework in Kubernetes. Hardware accelerator supports both in-band and/or out of band management, with service exposing it to Cloud Infrastructure operator or Application tenant roles.

Hardware Accelerators can be used as:
- Virtualization Infrastructure layer acceleration: Example can be vSwitch, which can be leveraged agnostically by VNFs if standard host interfaces (like VirtIO) are used.
- Application layer acceleration: Example of software library/framework (like DPDK) in VM providing Application level acceleration with (where available) hardware-abstracted APIs to access platform Hardware Acceleration and providing software equivalent libraries when hardware assist not available.
- Hardware Infrastructure layer offload: Example can be an OOB managed underlay network separation providing network separation secured from host OS reach on any provisioned transport switch infrastructure.

Two levels of consumption are for underlay separation or overlay acceleration. Underlay Separation ensures that multiple different Virtualization Infrastructure instances are kept in separate underlay network access domains. Overlay Acceleration offloads Virtualization Infrastructure instance vSwitch/vRouter or virtual termination endpoints (for applications that bypass the Virtualization layer).

Preferably, Application or Infrastructure acceleration can take benefit from underlying hardware acceleration and still be decoupled from it by using open multi-vendor API for Hardware Acceleration devices like for example:
- For Linux IO virtualization: VirtIO
- For Network Functions using DPDK libraries: Crypto Device, EthDev, Event Device and Base Band Device
- For O-RAN Network functions: O-RAN Acceleration Abstraction Layer Interface.



<a name="3.8.4"></a>
### 3.8.4 CPU Instructions

CPU architecture often includes instructions and execution blocks for most common compute-heavy algorithms like block cypher (example AES-NI), Random Number Generator or vector instructions. Those are normally consumed in software infrastructure or application by using enabled software libraries that will run faster when instructions are available in hardware and slower when instructions are not available in hardware, so other more general CPU instructions are used. CPU instructions don’t need to be activated or life-cycle-managed. Finding such compute nodes during scheduling workloads can be done by application control/orchestrator using OpenStack Nova filters or Kubernetes Node Feature Discovery labels, or directly from the Hardware Management layer.


<a name="3.8.5"></a>
### 3.8.5 Fixed Function Accelerators

Fixed function accelerators can come as adapters with in-line (typically PCIe adapter with Ethernet ports or storage drives) or look-aside (typically PCIe adapters without any external ports) functionality, additional chip on motherboard, included into server chipsets or packaged/embedded into main CPU. They can accelerate cryptographic functions, highly parallelized or other specific algorithms. Initial activation and rare life cycle management events (like updating firmware image) can typically be done from the Host OS (e.g. the OS driver or a Library), the Hardware Infrastructure Manager (from a library) or the NF (mostly through a library).

Beyond finding such compute nodes during scheduling workloads, those workloads also need to be mapped to the accelerator, both of which in Kubernetes can be done with Device Plugin framework. Once mapped to the application, the application can use enabled software libraries and/or device drivers that will use hardware acceleration. If hardware acceleration is used to improve cost/performance, then application can also run on generic compute node without hardware accelerator when application will use the same software library to run on generic CPU instructions.


<a name="3.8.3"></a>
### 3.8.3 Decoupling applications from infrastructure with Hardware Acceleration
