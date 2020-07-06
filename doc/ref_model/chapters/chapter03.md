[<< Back](../../ref_model)
# 3 Modelling
<p align="right"><img src="../figures/bogo_lsf.png" alt="bogo" title="Bogo Meter" width="35%"/></p>

## Table of Contents
* [3.1 Model](#3.1)
* [3.2 Virtual Resources](#3.2)
  * [3.2.1 Tenant](#3.2.1)
  * [3.2.2 Compute](#3.2.2)
  * [3.2.3 Storage](#3.2.3)
  * [3.2.4 Availability Zone](#3.2.4)
* [3.3 NFVI Management Software](#3.3)
* [3.4 Physical Resources](#3.4)
* [3.5 Network](#3.5)

There is the necessity to clearly define which kind of infrastructure resources a shared network function virtualisation infrastructure (NFVI) will provide for hosting workloads including virtual network functions (VNFs) and/or cloud-native network functions (CNF), so that the requirements of the workloads match the capabilities of the NFVI.

The lack of a common understanding of which resources and corresponding capabilities a suitable NFVI should provide may lead to several issues which could negatively impact the time and the cost for on-boarding and maintaining these solutions on top of a virtualised infrastructure. For Example:

- Supporting any kind of workload specific requirements (e.g. regarding network acceleration or API access) might result in having to establish different silo of NFVIs for each workload type.
- Synchronising the release cycles of a large set of different technologies will sooner or later lead to situations in which required upgrades cannot be applied easily due to incompatibilities.

The abstraction model presented in this chapter specifies a common set of virtual infrastructure resources which NFVI will need to provide to be able to host most of the typical VNF/CNF workloads required by the operator community.

Although a couple of explicit and implicit abstraction models (e.g. in the context of ETSI NFV) are already available, they fall short when addressing the following design principles:
- **Scope:** the model should describe the most relevant virtualised infrastructure resources (incl. acceleration technologies) an NFVI needs to provide for hosting Telco workloads
- **Separation of Concern:** the model should support a clear distinction between the responsibilities related to maintaining the network function virtualisation infrastructure and the responsibilities related to managing the various VNF workloads
- **Simplicity:** the amount of different types of resources (including their attributes and relationships amongst one another) should be kept to a minimum to reduce the configuration spectrum which needs to be considered
- **Declarative**: the model should allow for the description of the intended state and configuration of the NFVI resources for automated life cycle management
- **Explicit:** the model needs to be rich enough to allow for a direct mapping towards the APIs of NFVIs for the instantiation of virtual infrastructure elements without requiring any additional parameters
- **Lifecycle:** the model must distinguish between resources which have independent lifecycles but should group together those resources which share a common lifecycle
- **Aligned:** the model should clearly highlight the dependencies between the elements to allow for a well-defined and simplified synchronisation of independent automation tasks.

_**To summarise:** the abstraction model presented in this document will build upon existing modelling concepts and simplify and streamline them to the needs of telco operators who intend to distinguish between infrastructure related and workload related responsibilities._

<a name="3.1"></a>
## 3.1 Model

The abstraction model for the NFVI makes use of the following layers (only the virtual infrastructure layer will be directly exposed to workloads (VNFs/CNFs)):

<p align="center"><img src="../figures/ch03-model-overview.png" alt="NFVI Model Overview" Title="NFVI Model Overview" width="65%"/></p>
<p align="center"><b>Figure 3-1:</b> NFVI Model Overview.</p>

The functionalities of each layer are as follows:
- **Virtual Infrastructure Resources:** These are all the infrastructure resources (compute, storage and networks) which the NFVI provides to the workloads such as VNFs/CNFs. These virtual resources can be managed by the tenants and tenant workloads directly or indirectly via an application programming interface (API).
- **NFVI Management Software:** This consists of the software components that manage the physical and virtual resources and make those management capabilities accessible via one or more APIs. The host Operating System (OS) is responsible for managing the physical infrastructure resources and abstracting them from processes running within the OS. Virtualisation / containerisation technology dynamically allocates these abstracted hardware components and exposes them as virtual resources. Additional software is responsible for the management of logical constructs such as tenants, tenant workloads, resource catalogues, identities, access controls, security policies, etc.
- **Physical Infrastructure Resources:** These consist of physical hardware components such as servers, (including random access memory, local storage, network ports, and hardware acceleration devices), storage devices, network devices, and the basic input output system (BIOS).
- **Workloads (VNFs/CNFs):** These consist of workloads such as virtualized and/or containerized network functions that run on top of a VM or as a Container.

<a name="3.2"></a>
## 3.2 Virtual Resources

The virtual infrastructure resources provided by the Cloud Infrastructure can be grouped into four categories as shown in the diagram below:

<p align="center"><img src="../figures/ch03-model-virtual-resources.png" alt="NFVI Virtual Infrastructure Resources" Title="NFVI Virtual Infrastructure Resources" width="65%"/></p>
<p align="center"><b>Figure 3-2:</b> Virtual Infrastructure Resources provides virtual compute, storage and networks in a tenant context.</p>

- **Tenants:** represent an isolated and independently manageable elastic pool of compute, storage and network resources
- **Compute resources:** represent virtualised computes for workloads and other systems as necessary
- **Storage resources:** represent virtualised resources for persisting data
- **Network resources:** represent virtual resources providing layer 2 and layer 3 connectivity

The virtualised infrastructure resources related to these categories are listed below.

<a name="3.2.1"></a>
### 3.2.1 Tenant

A network function virtualisation infrastructure (NFVI) needs to be capable of supporting multiple tenants and has to isolate sets of infrastructure resources dedicated to specific workloads (VNF/CNF) from one another. Tenants represent an independently manageable logical pool of compute, storage and network resources abstracted from physical hardware.

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
A virtual machine or a container/pod belonging to a tenant capable of hosting the application components of workloads (VNFs). A virtual compute therefore requires a tenant context and since it will need to communicate with other communication partners it is assumed that the networks have been provisioned in advance.

_**Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV._

| Attribute      | Description                                                                   |
|----------------|-------------------------------------------------------------------------------|
| `name`         | name of the virtual host                                                      |
| `vcpus`        | number of virtual cpus                                                        |
| `ram`          | size of random access memory in GB                                            |
| `disc`         | size of root disc in GB                                                       |
| `nics`         | sorted list of network interfaces connecting the host to the virtual networks |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology      |
| `metadata`     | key/value pairs for selection of the appropriate redundancy domain            |

<p align="center"><b>Table 3-2:</b> Attributes of compute resources</p>

<a name="3.2.3"></a>
### 3.2.3 Storage
A block device of a certain size for persisting information which can be created and dynamically attached to/detached from a virtual compute. A storage device resides in a tenant context and exists independently from any compute host.

_**Example**: an OpenStack cinder volume._

| Attribute      | Description                                                              |
|----------------|--------------------------------------------------------------------------|
| `name`         | name of storage resources                                                |
| `size`         | size of disc in GB                                                       |
| `attachments`  | list of compute hosts to which the device is currently attached          |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |
| `metadata`     | key/value pairs for selection of the appropriate redundancy domain       |

<p align="center"><b>Table 3-3:</b> Attributes of storage resources</p>

_**Comments**: we need to be more specific regarding acceleration and metadata._


<a name="3.2.4"></a>
### 3.2.4 Availability Zone
An Availability Zone is a logical pool of physical resources (e.g. compute, block storage, network).  These logical pools segment the physical resources of a cloud based on factors chosen by the cloud operator. The cloud operator may create availability zones based on location (rack, datacenter), or indirect failure domain dependencies like power sources.  Workloads can leverage availability zones to utilise multiple locations or avoid sharing failure domains for a workload, and thus increase its fault-tolerance.

As a logical group with operator-specified criteria, the only mandatory attribute for an Availability Zone is the name.

| Attribute | Description |
| --- | --- |
| `name` | name of the availability zone |

<p align="center"><b>Table 3-4:</b> Attributes of availability zones</p>

<a name="3.3"></a>
## 3.3 NFVI Management Software

Network Function Virtualisation Infrastructure provides the capability to manage physical and virtual resources via Application Programmable Interfaces or graphical user interfaces. The management software allows to:

* setup, manage and delete tenants,
* setup, manage and delete user- and service-accounts,
* manage access privileges and
* provision, manage, monitor and delete virtual resources.

<p align="center"><img src="../figures/ch03-model-management-software.png" alt="NFVI Management Software" Title="NFVI Management Software" width="65%"/></p>
<p align="center"><b>Figure 3-3:</b> NFVI Management Software.</p>

 The management software needs to support following functional aspects:

 **API/UI**
 : an application programming interface / user interface providing access to the NFVI management functions

**Catalogue**
: manages the collection of available templates for virtual resource the NFVI can provide

**Inventory**
: manages the information related to all the physical and virtual resources of a NFVI

**Scheduler**
: receives requests via API/UI, provisions and manages virtual resources by coordinating the activities of the compute-, storage- and network resources managers

**Monitoring**
:  monitors and collects information on all events and the current state of all physical and virtual resources

**Additional Management Functions**
: include identity management, access management, policy management (e.g. to enforce security policies), etc.

**Compute Resources Manager**
: provides a mechanism to provision virtual resources with the help of physical compute resources

**Storage Resources Manager**
: provides a mechanism to provision virtual resources with the help of physical storage resources

**Network Resources Manager**
: provides a mechanism to provision virtual resources with the help of physical network resources

<a name="3.4"></a>
## 3.4 Physical Resources

The physical compute, storage and network resources serve as the foundation of the network function virtualisation infrastructure. They are as such not directly exposed to the workloads (VNFs/CNFs).

<p align="center"><img src="../figures/ch03-model-physical-resources.png" alt="NFVI Physical Infrastructure Resources" Title="NFVI Physical Infrastructure Resources" width="65%"/></p>
<p align="center"><b>Figure 3-4:</b> NFVI Physical Resources</p>

<a name="3.5"></a>
## 3.5 Network
Networking, alongside Compute and Storage, is an integral part of the Cloud Infrastructure (Network Function Virtualisation Infrastructure). The general function of networking in this context is to provide the connectivity between various virtual and physical resources required for the delivery of a network service. Such connectivity may manifest itself as a virtualised network between VMs and/or containers (e.g. overlay networks managed by SDN controllers, and/or programmable network fabrics) or as an integration into the infrastructure hardware level for offloading some of the network service functionality.

Normalization of the integration reference points between different layers of the Cloud Infrastructure architecture is one of the main concerns. In the networking context the primary focus is directed on the packet flow and control flow interfaces between the virtual resources (referred to as Software (SW) Virtualisation Layer) and physical resources (referred to as Hardware (HW) Infrastructure Layer), as well as on related integration into the various MANO reference points (hardware/network infrastructure management, orchestration). The identification of these two different layers (SW Virtualisation Layer and HW Infrastructure Layer) remains in alignment with the separation of resources into virtual and physical resources, generally used in this document, see e.g. Figure 3-1. The importance of understanding the separation of concerns between SW Virtualisation Layer and HW Infrastructure Layer is important because without it, the cardinality of having multiple CaaS and IaaS instances executing on their own private virtual resources from the single shared HW Infrastructure Layer cannot be expressed into separate administrative domains.

Principles that should be followed during the development and definition of the networking scope for the Reference Model, Reference Architectures, Reference Implementations and Reference Conformance test suites:

• Abstraction: A standardized network abstraction layer between the Virtualisation Layers and the Network Physical Resources Layer that hides (or abstracts) the details of the Network Physical resources from the Virtualisation Layers.

> **Note:**  In deployment phases this principle may be applied in many different ways e.g. depending on target use case requirements, workload characteristics, different algorithm implementations of pipeline stages and available platforms. The network abstraction layer supports, for example, physical resources with or without programmable hardware acceleration, or programmable network switches

•Agnosticism: Define Network Fabric concepts and models that can carry any type of traffic in terms of:
    Control, User and Management traffic types
    Acceleration technologies supporting multiple types of infrastructure deployments and network function workloads
    
•Automation: Enable end-to-end automation, from Physical Fabric installation and provisioning to automation of workload onboarding.

•Openness: All networking is based on open source or standardized APIs (North Bound Interfaces (NBI) and South Bound Interfaces (SBI)) and should enable integration of open source networking components (e.g. SDN controllers).

•Programmability: Network model enables a programmable forwarding plane controlled from a separately deployed control plane.

•Scalability: Network model enables scalability to handle all traffic traverse North-South and East-West enabling small up to large deployments.

•Workload agnostic: Network model is capable of providing connectivity to any type of workloads, including VNF, CNF and BareMetal workloads.

•Carrier Grade: Network model is capable of supporting deployments of the carrier grade workloads.

•Future proof: Network model is extendible to support known and emerging technology trends including SmartNICs, FPGAs and Programmable Switches, integrated for multi-clouds, and Edge related technologies.
