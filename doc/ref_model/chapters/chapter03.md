[<< Back](../../ref_model)
# 3 Modelling

## Table of Contents
* [3.1 Model](#3.1)
* [3.2 Virtual Infrastructure Layer](#3.2)
  * [3.2.1 Virtual Resources](#3.2.1)
    * [3.2.1.1 Tenant](#3.2.1.1)
    * [3.2.1.2 Virtual Compute](#3.2.1.2)
    * [3.2.1.3 Virtual Storage](#3.2.1.3)
    * [3.2.1.4 Virtual Network](#3.2.1.4)
    * [3.2.1.5 Availability Zone](#3.2.1.5)
  * [3.2.2 Virtual Infrastructure Manager](#3.2.2)
* [3.3 Hardware Infrastructure Layer](#3.3)
  * [3.3.1 Hardware Infrastructure Resources](#3.3.1)
    * [3.3.1.1 Hardware Acceleration Resources](#3.3.1.1) 
  * [3.3.2 Hardware Infrastructure Manager](#3.3.2)
* [3.4 Left for future use](#3.4)
* [3.5 Network](#3.5)
  * [3.5.1 Network Introduction](#3.5.1)
  * [3.5.2 Network Principles](#3.5.2)
  * [3.5.3 Service Function Chaining](#3.5.3)
* [3.6 Storage](#3.6)
* [3.7 Sample reference model realization](#3.7)
* [3.8 Hardware Acceleration Abstraction](#3.8)
  * [3.8.1 Types of Accelerators](#3.8.1)
  * [3.8.2 Infrastructure and Application Level Acceleration](#3.8.2)
  * [3.8.3 Workload Placement](#3.8.3)
  * [3.8.4 CPU Instructions](#3.8.4)
  * [3.8.5 Fixed Function Accelerators](#3.8.5)
  * [3.8.6 Firmware-programmable Adapters](#3.8.6)
  * [3.8.7 SmartNICs](#3.8.7)
  * [3.8.8 Smart Switches](#3.8.8)
  * [3.8.9 Decoupling Applications from Infrastructure and Platform with Hardware Acceleration](#3.8.9)

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

**Virtual Infrastructure Layer**
- **Virtual infrastructure resources:** These are all the infrastructure resources (compute, storage and networks) which the cloud infrastructure provides to the workloads such as VNFs/CNFs. These virtual resources can be managed by the tenants and tenant workloads directly or indirectly via an application programming interface (API).
- **Virtual infrastructure manager:** This consists of the software components that manage the virtual resources and make those management capabilities accessible via one or more APIs. The responsibilities of this functionality include the management of logical constructs such as tenants, tenant workloads, resource catalogues, identities, access controls, security policies, etc.

**Hardware Infrastructure Layer**
- **Hardware infrastructure manager:** This is a logical block of functionality responsible for the management of the abstracted hardware resources (compute, network and storage) and as such it is shielded from the direct involvement with server host software.
- **Hardware resources:** These consist of physical hardware components such as servers, (including random access memory, local storage, network ports, and hardware acceleration devices), storage devices, network devices, and the basic input output system (BIOS).

**Worklaod Layer**
- **Workloads (VNFs/CNFs):** These consist of workloads such as virtualized and/or containerized network functions that run within a virtual machine (VM) or as a set of containers.

<a name="3.2"></a>
## 3.2 Virtual Infrastructure Layer
<a name="3.2.1"></a>
### 3.2.1 Virtual Resources

The virtual infrastructure resources provided by the Cloud Infrastructure can be grouped into four categories as shown in the diagram below:

<p align="center"><img src="../figures/ch03-model-virtual-resources.png" alt="NFVI Virtual Infrastructure Resources" Title="NFVI Virtual Infrastructure Resources" width="65%"/></p>
<p align="center"><b>Figure 3-2:</b> Virtual Infrastructure Resources provide virtual compute, storage and networks in a tenant context.</p>

- **Tenants:** represent an isolated and independently manageable elastic pool of compute, storage and network resources
- **Compute resources:** represent virtualised computes for workloads and other systems as necessary
- **Storage resources:** represent virtualised resources for persisting data
- **Network resources:** represent virtual resources providing layer 2 and layer 3 connectivity

The virtualised infrastructure resources related to these categories are listed below.

<a name="3.2.1.1"></a>
#### 3.2.1.1 Tenant

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

<a name="3.2.1.2"></a>
#### 3.2.1.2 Virtual Compute
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

<a name="3.2.1.3"></a>
#### 3.2.1.3 Virtual Storage

A workload can request storage based on data retaining policy (persistent or ephemeral storage), different types of storage (HDD, SSD, etc.) and storage size.
Persistent storage outlives the compute instance whereas ephemeral storage is linked to compute instance lifecycle.

There are multiple storage performance attributes, such as latency, IOPS (Input/Output Operations per second), and throughput. For example, a workload may require one of its storage devices to provide low latency, high IOPS and very large/huge storage size (terabytes of data).
Low Latency storage is for workloads which have strong constraints on the time to access the storage.
High IOPS oriented storage is for workloads requiring lots of read/write actions.
Large size storage is for workloads that need lots of volume without strong performance constraints.
Note that approximate numeric ranges for the qualitative values used above are given in the 
[Storage Extensions](./chapter04.html#4.2.3) section.

Storage resources have the following attributes, with metric definitions that support verification through passive measurements (telemetry) where appropriate:

| Attribute                | Description                                                                                    |
|--------------------------|------------------------------------------------------------------------------------------------|
| `name`                   | name of storage resources                                                                      |
| `data retaining policy`  | persistent or ephemeral                                                                        |
| `performance`            | Read and Write Latency, The average amount of time to perform a R/W operation, in milliseconds |
|                          | Read and Write IOPS, The average rate of performing R/W in IO operations per second            |
|                          | Read and Write Throughput, The average rate of performing R/W operations in Bytes per second   |
| `enhanced features`      | replication, encryption                                                                        |
| `type`                   | block, object or file                                                                          |
| `size`                   | size in GB, telemetery includes the amount of free, used, and reserved disk space, in bytes    |

<p align="center"><b>Table 3-3:</b> Attributes of storage resources</p>

<a name="3.2.1.4"></a>
#### 3.2.1.4 Virtual Network

<a name="3.2.1.5"></a>
#### 3.2.1.5 Availability Zone
An availability zone is a logical pool of physical resources (e.g. compute, block storage, and network).  These logical pools segment the physical resources of a cloud based on factors chosen by the cloud operator. The cloud operator may create availability zones based on location (rack, datacenter), or indirect failure domain dependencies like power sources.  Workloads can leverage availability zones to utilise multiple locations or avoid sharing failure domains for a workload, and thus increase its fault-tolerance.

As a logical group with operator-specified criteria, the only mandatory attribute for an Availability Zone is the name.

| Attribute | Description |
| --- | --- |
| `name` | name of the availability zone |

<p align="center"><b>Table 3-4:</b> Attributes of availability zones</p>


<a name="3.2.2"></a>
### 3.2.2 Virtual Infrastructure Manager
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
<a name="3.3"></a>

## 3.3 Hardware Infrastructure Layer

<a name="3.3.1"></a>
### 3.3.1 Hardware Infrastructure Resources
Compute, Storage and Network resources serve as the foundation of the cloud infrastructure. They are exposed to and used by a set of networked Host Operating Systems in a cluster that normally handles the Virtualization Layer offering Virtual Machines or Containers where the application workloads (VNFs/CNFs) runs.

<p align="center"><img src="../figures/ch03-model-hardware-resources.png" alt="Cloud Infrastructure Hardware Resources" Title="Cloud Infrastructure Hardware Resources" width="65%"/></p>
<p align="center"><b>Figure 3-5:</b> Cloud Infrastructure Hardware Resources</p>

In managed Hardware Infrastructure systems, these consumable Compute, Storage and Network resources can be provisioned through operator commands or through software APIs.  There is a need to distinguish between these consumable resources, that are treated as leased resources, from the actual physical hardware resources that are installed in the data center. For this purpose, the hardware resource layer is conceptually split into a Logical Resource Layer that surfaces the consumable resources to the software layer above, and the Physical Resource Layer that is operated and managed by the Data Center Operations team from the HW Infrastructure Management functions.

Some installations might use a cluster of managed switches or storage components controlled by a Switch Fabric controller and/or a Storage Fabric controller acting as an appliance system. These systems should be federated with the HW Infrastructure Management system over some API to facilitate exchange of configuration intent, status and telemetry information allowing the HW Infrastructure Management and Management stack to automate Cloud Infrastructure operations. These appliance systems normally also have their own Equipment Management APIs and procedures for the hardware installation and maintenance staff.

An example could be a  Cloud Infrastructure stack federated with a commercial Switch Fabric where the Cloud Infrastructure shall be able to "send" networking configuration intent to the Switch Fabric and the Switch Fabric shall be able to "send" status and telemetry information to the Cloud Infrastructure e.g. Port/Link Status and packet counters of many sorts. The word "send" is a very lose definition of getting a message across to the other side, and could be implemented in many different ways.
This allows HW Infrastructure Management and Cloud Infrastructure management stack to have network automation that includes the switches that are controlled by the federated Switch Fabric. This would be a rather normal case for Operators  that have a separate Networking Department that owns and runs the Switch Fabric separately from the Data Center.

<a name="3.3.1.1"></a>
#### 3.3.1.1 Hardware Acceleration Resources

For a given software network function and software infrastructure, Hardware Acceleration resources can be used to achieve requirements or improve cost/performance. Following table gives reasons and examples for using Hardware Acceleration.

| Reason for using Hardware Acceleration | Example | Comment |
|---|---|---|
| Achieve technical requirements | Strict latency or timing accuracy | Must be done by optimizing compute node; cannot be solved by adding more compute nodes |
| Achieve technical requirements | Fit within power or space envelope | Done by optimizing cluster of compute nodes |
| Improve cost/performance | Better cost and less power/cooling by improving performance per node | Used when functionality can be achieved through usage of accelerator or by adding more compute nodes |

<p align="center"><b>Table 3-5:</b> Reasons and examples for using Hardware Acceleration</p>

Hardware Accelerators can be used to offload software execution for purpose of accelerating tasks to achieve faster performance, or offloading the tasks to another execution entity to get more predictable execution times, efficient handling of the tasks or separation of authority regarding who can control the tasks execution.

More details about Hardware Acceleration are in [Section 3.8 Hardware Acceleration Abstraction](chapter03.md#3.8).

<a name="3.3.2"></a>
### 3.3.2 Hardware Infrastructure Manager
The HW Infrastructure Manager shall at least support equipment management for all managed physical hardware resources of the Cloud Infrastructure. For better understanding of some of the hardware resources concepts see chapter 3.4.

In most deployments the HW Infrastructure Manager should also be the HW Infrastructure Layer provisioning manager of the Compute, Storage and Network resources that can be used by the Virtualization Infrastructure Layer instances. It shall provide an API enabling vital resource recovery and control functions of the provisioned functions e.g. Reset and Power control of the Computes.

For deployments with more than one Virtualization Infrastructure Layer instance that will be using a common pool of hardware resources there is a need for a HW Infrastructure Layer provisioning manager of the Compute, Storage and Network resources to handle the resource assignment and arbitration.

The resource allocation could be a simple book-keeping of which Virtualization Infrastructure Layer instance that have been allocated a physical hardware resource or a more advanced resource Composition function that assemble the consumed Compute, Storage and Network resources on demand from the pools of physical hardware resources.

<p align="center"><img src="../figures/ch03-model-hardware-manager.png" alt="Hardware Infrastructure Manager" Title="Hardware Infrastructure Manager" width="65%"/></p>
<p align="center"><b>Figure 3-4:</b> Hardware Infrastructure Manager.</p>

The hardware infrastructure manager allows to:
* provision, manage, monitor and delete hardware resources 
* manage physical hardware resource discovery, monitoring and topology
* manage hardware infrastructure telemetry and log collection services

The hardware infrastructure manager needs to support the following functional aspects:

* **API/UI**: an application programming interface / user interface providing access to the hardware resource management functions

* **API/UI**: an application programming interface / user interface providing access to the hardware resource management functions
* **Discovery**: discover physical hardware resources and collect relevant information about them 
* **Topology**: discover and monitor physical interconnection (e.g. cables) in between the physical hardware resources
* **Equipment**:  manages the physical hardware resources in terms of configuration, firmware status, health/fault status and autonomous environmental control functions such as fan and power conversion regulations
* **Resource Allocation and Composition**: creates, modifies and delete logical Compute, Network and Storage Resources through Composition of allocated physical hardware resources
* **Underlay Network Resources Manager**: provides a mechanism to provision hardware resources and provide separation in between multiple Virtualization Infrastructure instances for the use of the underlay network (e.g. switch fabric, switches, SmartNICs)
* **Monitoring**: monitors and collects information on events, current state and telemetry data of physical hardware resources, Equipment autonomous control functions as well as Switch and Storage Fabric systems
* **Additional Management Functions**: include software and configuration life cycle management, identity management, access management, policy management (e.g. to enforce security policies), etc.

<a name="3.4"></a>
## 3.4 Left for future use
This section is left blank for future use

<a name="3.5"></a>
## 3.5 Network
<a name="3.5.1"></a>
### 3.5.2 Network Introduction
Networking, alongside Compute and Storage, is an integral part of the Cloud Infrastructure (Network Function Virtualisation Infrastructure). The general function of networking in this context is to provide the connectivity between various virtual and physical resources required for the delivery of a network service. Such connectivity may manifest itself as a virtualised network between VMs and/or containers (e.g. overlay networks managed by SDN controllers, and/or programmable network fabrics) or as an integration into the infrastructure hardware level for offloading some of the network service functionality.

Normalization of the integration reference points between different layers of the Cloud Infrastructure architecture is one of the main concerns. In the networking context the primary focus is directed on the packet flow and control flow interfaces between the virtual resources (referred to as Software (SW) Virtualisation Layer) and physical resources (referred to as Hardware (HW) Infrastructure Layer), as well as on related integration into the various MANO reference points (hardware/network infrastructure management, orchestration). The identification of these two different layers (SW Virtualisation Layer and HW Infrastructure Layer) remains in alignment with the separation of resources into virtual and physical resources, generally used in this document, see e.g. Figure 3-1. The importance of understanding the separation of concerns between SW Virtualisation Layer and HW Infrastructure Layer is important because without it, the cardinality of having multiple CaaS and IaaS instances executing on their own private virtual resources from the single shared HW Infrastructure Layer cannot be expressed into separate administrative domains.

<a name="3.5.2"></a>
### 3.5.2 Network Principles
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

<a name="3.5.3"></a>
### 3.5.3 Service Function Chaining
Over the past few years there has been a significant move towards decomposing network functions into smaller sub-functions that can be independently scaled and potentially reused across multiple network functions. A service chain allows composition of network functions by passing selected packets through multiple smaller services.

In order to support this capability in a sustainable manner, there is a need to have the capability to model service chains as a high level abstraction. This is essential to ensure that the underlying connection setup, and (re-)direction of traffic flows can be performed in an automated manner. At a very high level a service chain can be considered a directed acyclic graph with the composing network functions being the vertices. Building on top of this, a service chain can be modelled by defining two parameters:

* An acyclic graph defining the service functions that need to be traversed for the service chain. This allows for multiple paths for a packet to traverse the service chain.
* A set of packet/flow classifiers that determine what packets will enter and exit a given service chain

These capabilities need to be provided for both virtualised and containerised (cloud-native) network functions as there will be a need to support both of them for the foreseeable future. Since virtualised network functions have existed for a while there is existing, albeit partial, support for service chaining in virtualised environments in orchestration platforms like OpenStack. Container orchestration platforms such as Kubernetes don't support service chaining and may require development of new primitives in order to support advanced networking functions.

It is expected that reference architectures will provide a service chain workflow manager that would accept the service function acyclic graph and be able to identify/create the necessary service functions and the networking between them in order to instantiate such a chain.

There is also a need to provide specialised tools to aid troubleshooting of individual services and the communication between them in order to investigate issues in the performance of composed network functions. Minimally, there is a need to provide packet level and byte level counters and statistics as the packets pass through the service chain in order to ascertain any issues with forwarding and performance. Additionally, there is a need for mechanisms to trace the paths of selected subsets of traffic as they flow through the service chain.

<a name="3.5.3.1"></a>
#### 3.5.3.1 Service Function Chaining Model Introduction 
Service Function Chaining (SFC) can be visualized as a layered structure where the Service Function plane (SFC data plane, consists of service function forwarder, classifier, service function, service function proxy) resides over a Service Function overlay network. 
SFC utilizes a service-specific overlay that creates the service topology.  The service overlay provides service function connectivity built "on top" of the existing network topology. It leverages various overlay network technologies (e.g., Virtual eXtensible Local Area Network (VXLAN)) for interconnecting SFC data-plane elements and allows establishing Service Function Paths (SFPs).

In a typical overlay network, packets are routed based on networking principles and use a suitable path for the packet to be routed from a source to its destination. 

However, in a service-specific overlay network, packets are routed based on policies. This requires specific support at network level such as  at CNI in CNF environment to provide such specific routing mechanism.



<a name="3.5.3.2"></a>
#### 3.5.3.2 SFC Architecture

 The SFC Architecture is composed of functional management, control and data components as categorised in the Table 3-6 below. 

The table below highlights areas under which common SFC functional components can be categorized.


| Components | Example         | Responsabilities |
|:---:|:----:|:---|
|**Management** | `SFC orchestrator`  | High Level of orchestrator <br /> Orchestrate the SFC based on SFC Models/Policies with help of control components.| 
| | `SFC OAM Components` | Responsible for SFC OAM functions |
|| `VNF MANO` | NFVO, VNFM, and VIM <br />Responsible for SFC Data components lifecycle |
|| `CNF MANO` | CNF DevOps Components <br />Responsible for SFC data components lifecycle |
| **Control** | `SFC SDN Controller` | SDNC responsible to create the service specific overlay network. <br /> Deploy different techniques to stitch the wiring but provide the same functionality, for example l2xconn, SRv6 , Segment routing etc.  |
|| `SFC Renderer` | Creates and wires ports/interfaces for SF data path |
| **Data** | `Core Components`<br /> SF, SFF, SF Proxy  | Responsible for steering the traffic for intended service functionalities based on Policies |

<p align="center"><b>Table 3-6:</b> SFC Architecture Components</p>


> **Note:** These are logical components and listed for their functionalies only.  

The SFC Architecture components can be viewed as:- 

Figure 3-6 shows a simple architecture of an SFC with multiple VNFs, as SF data plane components, along with SFC management and NFV MANO components. 
<p align="center"><img src="../figures/ch03-model-sfc-architecture-vnf-2.png" alt="SFC Architecture for VNF based SFs" Title="SFC Architecture for VNF based SFs" width="45%"/>
</p>
<p align ="center"><b>Figure 3-6:</b> SFC Architecture for VNF based SFs </p>


Figure 3-7 shows a simple architecture of an SFC with multiple CNFs, as SF data plane components, along with SFC management and CNF MANO components. 
<p align="center"> <img src="../figures/ch03-model-sfc-architecture-cnf-2.png" alt="SFC Architecture for CNF based SFs" Title="SFC Architecture for CNF based SFs" width="45%"/></p>
<p align ="center"><b>Figure 3-7:</b> SFC Architecture for CNF based SFs</p>

The SFC management components together with the control components are responsible for rendering SFC requests to Service Function paths. For this they convert requisite SFC policies into network topology dependent paths and forwarding steering policies. Relevant SFC data components - classifiers, service function forwarders - are responsible for managing the steering policies.

<a name="3.5.3.3"></a>
#### 3.5.3.3 Information Flows in Service Function Chaining
 
<a name="3.5.3.3.1"></a>
##### 3.5.3.3.1 Creation of Service Function Chain
 
The creation of the SFC might include design/preparation phase as: 
-	The service functions that are included in the SFC.
- The routing order in the service function, if the SFC is composed of more than one service function.

Figure 3-8 shows SFC creation call flow, separated logically in two steps.
<p align="center"> <img src="../figures/ch03-model-sfc-info-create-flow.png" alt="Creation of Service Function Chain" Title="Creation of Service Function Chain" width="45%"/></p>
<p align ="center"><b>Figure 3-8:</b> Creation of Service Function Chain</p>

1.	Creation of service functions of SFC.

The flow of steps to enable the SFC creation can be as follows:-

a.	SFC orchestrator creates the SFs with help of VNF MANO or CNF MANO.

b.	SFC Rendere attaches the SFC aware interfaces at SFs to enable Service plane 

c.	NFVO boots up the relevant SF configurations at SF.
> **Note:** These steps are optional, if SFC orchestrator disovers that SFs are already created and existing.

2.	Creation of service function path (SFP) using the created SFs and associated interfaces.

A Service Function Path consists of:
- A set of ports( in VNF environment) or interfaces ( in CNF environment) , that define the sequence of service functions 
- A set of flow classifiers that specify the classified traffic flows entering the chain.

This step creates a new chain policy with chain rules. Chain rules can include the identifier of a traffic flow, service characteristics, the SFC identifier and related information to route the packets along the chain. 

Service characteristics can be application layer matching information (e.g., URL). Traffic flow identifier can be kind of traffic (e.g., Video, TCP, HTTP) flow need to be serviced. It can be specific Subscriber to apply service (e.g., parental control). The SFC identifier to steer the matched traffic along the SFP with SFC encapsulation. 

a.	SFC orchestrator creates SFP with help of SDNC.

b.	SDNC pushes the SFC traffic steering policies to SFF(s).

c.	SFC classifier Policy provided for SFP to SFC classifier by SFC Controller. **Note:** not shown in call flow.

<a name="3.5.3.3.2"></a>
##### 3.5.3.3.2 Updation of Service Function Chain
SFP or SFC can be updated for various reasons and some of them are :-
- SFC controller monitors the SFP status and alerts SFC controller in case of not meeting SLA or some anamoly.
- SFC design changes to update SF order, inclusion/removal of SFs
- SFC Policy Rules changes

<a name="3.5.3.3.3"></a>
##### 3.5.3.3.3 Data Steering in Service Function Chain

Figure 3-9 shows traffic steering along SFP.
<p align="center"> <img src="../figures/ch03-model-sfc-data-flow.png" alt="Data steering in Service Function Chain" Title="Data steering in Service Function Chain" width="45%"/></p>
<p align ="center"><b>Figure 3-9:</b> Data steering in Service Function Chain</p>

- SFC classifier detects the traffic flow based on classification policies. For example, to enable SGi-Lan feature as SFC, UPF acts as SFC classifier.  UPF receives the classification policies from PCF (via SMF) as traffic steering policies. 
- SFC classifier applies the SFC encapsulation (e.g., SCH, NSH) and routes traffic towards SFF, acts as entry point to SFP. The SFC Encapsulation provides, at a minimum, SFP identification, and is used by the SFC-aware functions, such as the SFF and SFC-aware SFs.
- SFF based on SFC encapsulation routes the traffic to SF for service functionalities. 
- SF updates the SFC encapsulation based on its policies for further services.
- At end of SFP, SFC encapsulation is removed and packet is routed out of SFP.


<a name="3.6"></a>
## 3.6 Storage
The general function of storage subsystem is to provide the needed data store to various virtual and physical resources required for the delivery of a network service. In cloud infrastructure such storage may manifest itself in various ways like storage endpoints being exposed over network from software defined storage dedicated clusters or hyperconverged nodes (combining storage and other functions like compute or networking).
Storage also follows the alignment of separated virtual and physical resources of SW Virtualization Layer and HW infrastructure. Reasons for such alignment are described more in Section 3.5. The following principles apply to Storage scope for the Reference Model, Reference Architectures, Reference Implementations and Reference Conformance test suites:
* Abstraction: A standardized storage abstraction layer between the Virtualisation Layers and the Storage Physical Resources Layer that hides (or abstracts) the details of the Storage Physical resources from the Virtualisation Layers.
* Agnosticism: Define Storage subsystem concepts and models that can provide various storage types and performance requirements (more in Virtual Resources [3.2.1.3 Storage](#3.2.1.3)).
* Automation: Enable end-to-end automation, from Physical Storage installation and provisioning to automation of workloads (VNF/CNF) onboarding.
* Openness: All storage is based on open source or standardized APIs (North Bound Interfaces (NBI) and South Bound Interfaces (SBI)) and should enable integration of storage components such as Software Defined Storage controllers.
* Scalability: Storage model enables scalability to enable small up to large deployments.
* Workload agnostic: Storage model can provide storage functionality to any type of workloads, including VNF, CNF and BareMetal workloads.
* Future proof: Storage model is extendible to support known and emerging technology trends covering spectrum of memory-storage technologies including Software Defined Storage with mix of SATA- and NVMe-based SSDs, DRAM and Persistent Memory, integrated for multi-clouds, and Edge related technologies.

<a name="3.7"></a>
## 3.7 Sample reference model realization

The following diagram presents an example of the realization of the reference model, where a virtual infrastructure layer contains three coexisting but different types of implementation: a typical IaaS using VMs and a hypervisor for virtualisation, a CaaS on VM/hypervisor, and a CaaS on bare metal. This diagram is presented for illustration purposes only and it does not preclude validity of many other different combinations of implementation types. Note that the model enables several potentially different controllers orchestrating different type of resources (virtual and/or hardware). Management clients can manage virtual resources via Virtual Infrastructure Manager (Container Infrastructure Service Manager for CaaS, or Virtual Infrastructure Manager for IaaS), or alternatively hardware infrastructure resources via hardware infrastructure manager.  The latter situation may occur for instance when an orchestrator (an example of a management client) is involved in provisioning the physical network resources with the assistance of the controllers. Also, this realization example would enable implementation of a programmable fabric.

<p align="center"><img src="../figures/ch03-model-realization-diagram-2.png" alt="Reference model realization example" Title="Reference model realization example" width="65%"/></p>

<p align="center"><b>Figure 3-10:</b> Reference model realization example</p>


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

<p align="center"><img src="../figures/ch03-examples-of-server-and-smartswitch-based-nodes.png" alt="Examples of server- and SmartSwitch-based nodes (for illustration only)" Title="Examples of server- and SmartSwitch-based nodes (for illustration only)" width="65%"/></p>
<p align="center"><b>Figure 3-11:</b> Examples of server- and SmartSwitch-based nodes (for illustration only)</p>


<a name="3.8.2"></a>
### 3.8.2 Infrastructure and Application Level Acceleration

Figure 3-10 gives examples for Hardware Accelerators in [Sample reference model realization](#3.7) diagram.

<p align="center"><img src="../figures/ch03-hardware-acceleration-in-rm-realization-diagram.png" alt="Hardware Acceleration in RM Realization Diagram" Title="Hardware Acceleration in RM Realization Diagram" width="65%"/></p>

<p align="center"><b>Figure 3-12:</b> Hardware Acceleration in RM Realization Diagram</p>


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

<a name="3.8.3"></a>
### 3.8.3 Workload Placement

Workload placement can be done by a combination of filters/selectors to find appropriate compute resources, subsystems to manage assignment of scheduled workloads to Hardware Accelerator, and intelligence in the workload to detect the presence of Hardware Accelerators.

For initial limited cloud deployments of network functions on private clouds it is possible to have a workload placement orchestrator that handles optimizations of selected virtualisation clusters and available hardware resources. This will however soon become too complex with the increasing number of acceleration devices, hardware composability and hybrid multi-cloud deployments.

Growing lists of individual optimizations including hardware acceleration during scheduling makes it more complex to map workloads to lists of individual optimizations, so such optimizations get grouped together into higher level categories. An example is having category for real-time and dataplane-optimized category instead of specifying individual optimizations required to reach it.

With further growth in size of clusters and the variety of hardware acceleration, in a hybrid or multi-cloud deployment, it will be necessary to enable separate optimization levels for the workload placement and each Cloud Infrastructure provider. The workload placement orchestrator will operate on one or several Cloud Infrastructures resources to satisfy the workloads according to Service Level Agreements (SLA) that do not specify all implementation and resource details. Each Cloud Infrastructure provider will make internal Infrastructure optimisations towards their own internal optimisation targets whilst fulfilling the SLAs.

<a name="3.8.4"></a>
### 3.8.4 CPU Instructions

The CPU architecture often includes instructions and execution blocks for most common compute-heavy algorithms like block cypher (example AES-NI), Random Number Generator or vector instructions. These functions are normally consumed in infrastructure software or applications by using enabled software libraries that run faster when custom CPU instructions for the execution of such functions are available in hardware and slower when these specific instructions are not available in hardware as only the general CPU instructions are used. Custom CPU instructions don’t need to be activated or life-cycle-managed. When scheduling workloads, compute nodes with such custom CPU instructions can be found by applications or an orchestrator using OpenStack Nova filters or Kubernetes Node Feature Discovery labels, or directly from the Hardware Management layer.

<a name="3.8.5"></a>
### 3.8.5 Fixed Function Accelerators

Fixed function accelerators can come as adapters with in-line (typically PCIe adapter with Ethernet ports or storage drives) or look-aside (typically PCIe adapters without any external ports) functionality, additional chip on motherboard, included into server chipsets or packaged/embedded into main CPU. They can accelerate cryptographic functions, highly parallelized or other specific algorithms. Initial activation and rare life cycle management events (like updating firmware image) can typically be done from the Host OS (e.g. the OS driver or a Library), the Hardware Infrastructure Manager (from a library) or the NF (mostly through a library).

Beyond finding such compute nodes during scheduling workloads, those workloads also need to be mapped to the accelerator, both of which in Kubernetes can be done with Device Plugin framework. Once mapped to the application, the application can use enabled software libraries and/or device drivers that will use hardware acceleration. If hardware acceleration is used to improve cost/performance, then application can also run on generic compute node without hardware accelerator when application will use the same software library to run on generic CPU instructions.

<a name="3.8.6"></a>
### 3.8.6 Firmware-programmable Adapters

Firmware-programmable network adapters with programmable pipeline are types of network adapters where usual Ethernet controller functionality (accelerates common network overlays, checksums or protocol termination) can be extended with partially programmable modules so that additional protocols can be recognized, parsed and put into specific queues, which helps increase performance and reduce load on main CPU.

Firmware-programmable storage adapters can offload some of the storage functionality and include storage drive emulation to enable partial drive assignments up to the accessing host OS. These adapters can over time include more supported storage offload functions or support more drive emulation functions.

Before being used, such adapters have to be activated by loading programmable module that typically accelerates the Virtualization Infrastructure, so it is not often reprogrammed. Doing this in multivendor environments can lead to complexities because the adapter hardware is typically specified, installed and supported by server vendor while the programmable image on the adapter is managed by SDN, Storage Controller or Software Infrastructure vendor.

<a name="3.8.7"></a>
### 3.8.7 SmartNICs

Programmable SmartNIC accelerators can come as programmable in-line adapters (typically PCIe adapter with Ethernet ports), or network connected pooled accelerators like farms of GPU or FPGA where the normal CPU PCIe connection is extended with an Ethernet hop.

There are two main types of Smart NICs that can accelerate network functions in-line between CPU and Ethernet ports of servers. The simpler types have a configurable or programmable packet pipeline that can implement offload for the infrastructure virtual switching or part of an application functions data plane. The more advanced type, often called Data Processing Unit (DPU), have a programmable pipeline and some strong CPU cores that simultaneously can implement underlay networking separation and trusted forwarding functions, infrastructure virtual switching data and control plane as well as part of an application functions control plane.

<p align="center"><img src="../figures/ch03-example-smartnic-deployment-model.png" alt="Example SmartNIC Deployment Model That Accelerates Two Workloads and Has OOB Management" Title="Example SmartNIC Deployment Model That Accelerates Two Workloads and Has OOB Management" width="65%"/></p>

<p align="center"><b>Figure 3-13:</b> Example SmartNIC Deployment Model That Accelerates Two Workloads and Has OOB Management</p>



#### Simple SmartNIC

The preferred usage of a simple SmartNIC is for the Virtualization Infrastructure usage that typically implements the data (forwarding) plane of the virtual switch or router. These deployments can offer a standardized higher-level abstract interface towards the application tenants such as VirtIO that supports good portability and is by that the preferred usage method.

Simple SmartNICs direct usage by the application tenant (VNF or CNF), where it acts as a dedicated accelerator appliance, require the application tenant to manage loading and the function that is loaded in the SmartNIC as well as any interface to the offloaded network functions. Such deployment is similar to the NIC PCI Pass-Through in that it bypasses the Virtualization Infrastructure layer’s virtual switching, which require all network encapsulation, mapping and separation to be done by the underlay network, often by manual provisioning and therefore is not a preferred usage method.

#### DPU

The DPU can accelerate software infrastructure functions (vSwitch/vRouter) from the main CPU and simultaneously offer networking services e.g. load balancers, firewalls and application tenant offload functions. Through Out of band management it can also ensure underlay separation and map a selected part of the underlay network to the specific Virtualization Infrastructure instance that the server it is mounted on requires allowing them to be used on any statically provisioned underlay network.

The forwarding path (data plane) needs to be installed and controlled by the Hardware Infrastructure Manager through an isolated Out of band management channel into the DPU control and operating system completely out of reach for the main CPU Host SW. All content in the forwarding path must come from Hardware Infrastructure operator trusted code since any fault or malicious content can seriously disturb the whole network for all connected devices.

The trusted forwarding functions must be handled through a Hardware Infrastructure Management repository and have APIs for their respective control functions. These APIs must have an ability to handle some version differences since the forwarding and control planes life cycle management will not be atomic. The offload functions that should be offered as services must have published and preferably standardized open APIs, but the application specific forwarding functions do not have to be open APIs since they will only communicate with the application tenant provided control functions. [P4](https://p4.org/) and [OpenConfig](https://openconfig.net/) are examples of suitable languages and models, with different levels of flexibility, usable for these forwarding and control functions.

The separated management channel could either come in through the BMC, a direct management port on the DPU or through a management VPN on the switch ports. This enable the Hardware Infrastructure Management to automate its networking through the DPU without any need to dynamically manage the switch fabric, thereby enabling a free choice of switch fabric vendor. These deployments allow the switch fabric to be statically provisioned by the operators networking operation unit, as it is often required.

The DPU can offload control and data plane of the virtual switching to the DPU as well as trusted hardware offload for virtualized Packet Core and Radio data plane networking and transport related functionality in a power efficient way. It can also offload relevant application tenant control functions if the DPU offers an Execution Environment for VMs or containers and there is space and performance headroom. In such cases the DPU must also setup a communication channel into respective application tenant environment.


<a name="3.8.8"></a>
### 3.8.8 Smart Switches

Smart Switches can be broadly categorized into Configurable Switches and Programmable Switches.

Configurable Smart Switches run generic “smart” configurable network operating system offering full range of network functionality and are flexible enough to support most network solutions. The most common such network operating system is Linux-based [SONiC](https://azure.github.io/SONiC/) allowing hardware and software disaggregation by running on switches from multiple switch vendors with different types of vendor fixed-function ASICs. Still, SONiC today cannot implement new type of data plane functionality or patch/modify/correct an ASIC, which is the type of support offered by programmable smart switches.

Programmable Smart Switches make it possible to quickly support new or correct/modify existing protocols and network functions, allow end customers to implement network functions, and to only implement and load functionality that is needed. Such switches contain one or more programmable switch ASICs of the same or different types. The two most used programming languages are [P4](https://p4.org/) and [NPL](https://nplang.org/), and both can be used with vendor-specific toolchains to program their switch ASICs and/or FPGAs. Open Networking Foundation [Stratum](https://opennetworking.org/stratum/) is an example of network operating system that offers generic life cycle management control services for the P4 components and a management API. The control API for the individual network functions are not part of the Stratum APIs.

Based on Smart Switches, products exist for fully integrated edge and fabric solutions from vendors like Arista, Cisco or Kaloom.


<a name="3.8.9"></a>
### 3.8.9 Decoupling Applications from Infrastructure and Platform with Hardware Acceleration

[Decoupling](https://github.com/cntt-n/CNTT/blob/master/doc/common/glossary.md#cloud-platform-abstraction-related-terminology) applications from hardware accelerator is normally accomplished using drivers that, if available, are preferred with standardised interfaces across vendors and their products, or if not available then through drivers specific to the vendor hardware device. Decoupling infrastructure software from hardware accelerators is also preferred using standard interfaces. If those are not available for target hardware accelerator, coupling one or limited number of software infrastructures is less of an issue compared to coupling multiple applications.

Taking advantage of RM and RA environments with common capabilities, applications can be developed and deployed more rapidly, providing more service agility and easier operations. The extent to which this can be achieved will depend on levels of decoupling between application and infrastructure or platform underneath the application:

#### 1. Infrastructure:
- a) Application functionality or application control requires infrastructure components beyond RM profiles or infrastructure configuration changes beyond APIs specified by RA. Generally, such an application is tightly coupled with the infrastructure which results in an [Appliance deployment model](../../common/glossary.md#cloud-platform-abstraction-related-terminology).
- b) Application control using APIs specified by RA finds nodes (already configured in support of the profiles) with the required infrastructure component(s), and in that node using APIs specified by RA configures infrastructure components that make application work. Example is an application that to achieve latency requirements needs certain hardware acceleration available in RM profile and is exposed through APIs specified by RA.
- c) Application control using APIs specified by RA finds nodes (already configured in support of the profiles) with optional infrastructure component(s), and in these nodes using APIs specified by RA configures infrastructure component(s) that make application work better (like more performant) than without that infrastructure component. Example is an application that would have better cost/performance with certain acceleration adapter but can also work without it.
- d) Application control using APIs specified by RA finds general profile nodes without any specific infrastructure components.

#### 2. Platform Services:
- a) Application functionality or application control can work only with its own components instead of using defined Platform Services. Example is an application that brings its own Load Balancer.
- b) With custom integration effort, application can be made to use defined Platform Services. Example is application that with custom integration effort can use defined Load Balancer which can be accelerated with hardware acceleration in way that is fully decoupled from application (i.e. application does not have awareness of Load Balancer being hardware-accelerated).
- c) Application is designed and can be configured for running with defined Platform Services. Example is application that can be configured to use defined Load Balancer which can be accelerated with hardware acceleration.
