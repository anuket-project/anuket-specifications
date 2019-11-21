[<< Back](../../ref_model)
# 3 Modelling
<p align="right"><img src="../figures/bogo_lsf.png" alt="bogo" title="Bogo Meter" width="35%"/></p>

## Table of Contents
* [3.1 Model.](#3.1)
* [3.2 Virtual Resources.](#3.2)
  * [3.2.1 Tenant.](#3.2.1)
  * [3.2.2 Compute.](#3.2.2)
  * [3.2.3 Storage.](#3.2.3)
  * [3.2.4 Network.](#3.2.4)
* [3.3 Management Software.](#3.3)
* [3.4 Physical Resources.](#3.4)

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

<p align="center"><img src="../figures/ch03_model_overview.png" alt="NFVI Model Overview" Title="NFVI Model Overview" width="65%"/></p>
<p align="center"><b>Figure 3-1:</b> NFVI Model Overview.</p>

The functionalities of each layer are as follows:
- **Physical Infrastructure Resources:** These consist of physical hardware components such as servers, (including random access memory, local storage, network ports, and hardware acceleration devices), storage devices, network devices, and the basic input output system (BIOS).
- **NFVI Management Software:** This consists of both the host Operating System (OS) responsible for managing the physical infrastructure resources as well as the virtualization/containerization technology which, on request, dynamically allocates hardware components and exposes them as virtual resources.
- **Virtual Infrastructure Resources:** These are all the infrastructure resources (compute, storage and networks) which the NFVI provides to the workloads such as VNFs/CNFs. These virtual resources can be managed by the tenants and tenant workloads directly or indirectly via an application programming interface (API).
- **Workloads (VNFs/CNFs):** These consist of workloads such as virtualized and/or containerized network functions that run on top of a VM or as a Container.

<a name="3.2"></a>
## 3.2 Virtual Resources

The virtual infrastructure resources provided by the NFVI can be grouped into four categories as shown in the diagram below:

<p align="center"><img src="../figures/ch03_model_virtual_resources.png" alt="NFVI Virtual Infrastructure Resources" Title="NFVI Virtual Infrastructure Resources" width="65%"/></p>
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

| Attribute | Description                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------|
| `name`      | name of the logical resource pool                                                                       |
| `type`      | type of tenant (e.g. OpenStack tenant, Kubernetes cluster, …)                                           |
| `vcpus`     | max. number of virtual CPUs                                                                             |
| `ram`       | max. size of random access memory in GB                                                                 |
| `disc`      | max. size of ephemeral disc in GB                                                                       |
| `networks`  | description of external networks required for inter-domain connectivity                                 |
| `metadata`  | key/value pairs for selection of the appropriate physical context (e.g. location, availability zone, …) |

<p align="center"><b>Table 3-1:</b> Attributes of a tenant.</p>

<a name="3.2.2"></a>
### 3.2.2 Compute
A virtual machine or a container/pod belonging to a tenant capable of hosting the application components of workloads (VNFs). A virtual compute therefore requires a tenant context and since it will need to communicate with other communication partners it is assumed that the networks have been provisioned in advance.

_**Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV._

| Attribute | Description |
| --- | --- |
| `name` | name of the virtual host |
| `vcpus` | number of virtual cpus |
| `ram` | size of random access memory in GB |
| `disc` | size of root disc in GB |
| `nics` | sorted list of network interfaces connecting the host to the virtual networks |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |
| `metadata` | key/value pairs for selection of the appropriate redundancy domain |

<p align="center"><b>Table 3-2:</b> Attributes of compute resources.</p>

<a name="3.2.3"></a>
### 3.2.3 Storage
A block device of a certain size for persisting information which can be created and dynamically attached to/detached from a virtual compute. A storage device resides in a tenant context and exists independently from any compute host.

_**Example**: an OpenStack cinder volume._

| Attribute | Description |
| --- | --- |
| `name` | name of storage resources |
| `size` | size of disc in GB |
| `attachments` | list of compute hosts to which the device is currently attached |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |
| `metadata` | key/value pairs for selection of the appropriate redundancy domain |

<p align="center"><b>Table 3-3:</b> Attributes of storage resources.</p>

_**Comments**: we need to be more specific regarding acceleration and metadata._

<a name="3.2.4"></a>
### 3.2.4 Network
A layer 2 / layer 3 communication domain within a tenant. A network requires a tenant context.

_**Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV._

| Attribute | Description |
| --- | --- |
| `name` | name of the network resource |
| `subnet` | network address of the subnet |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |

<p align="center"><b>Table 3-4:</b> Attributes of network resources.</p>

<a name="3.3"></a>
## 3.3 Management Software

Network Function Virtualisation Infrastructure provides the capability to manage virtual resources via Application Programmable Interfaces or graphical user interfaces. The management software allows to:

* setup, manage and delete tenants,
* setup, manage and delete user- and service-accounts,
* manage access privileges and
* provision, manage, monitor and delete virtual resources.

<p align="center"><img src="../figures/ch03_model_management_software.png" alt="NFVI Management Software" Title="NFVI Management Software" width="65%"/></p>
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
: include identity management, policy management (e.g. to enforce security policies), etc.

**Compute Resources Manager**
: provides a mechanism to provision virtual resources with the help of physical compute resources

**Storage Resources Manager**
: provides a mechanism to provision virtual resources with the help of physical storage resources

**Network Resources Manager**
: provides a mechanism to provision virtual resources with the help of physical network resources

<a name="3.4"></a>
## 3.4 Physical Resources

The physical compute, storage and network resources serve as the foundation of the network function virtualisation infrastructure. They are as such not directly exposed to the workloads (VNFs/CNFs).

<p align="center"><img src="../figures/ch03_model_physical_resources.png" alt="NFVI Physical Infrastructure Resources" Title="NFVI Physical Infrastructure Resources" width="65%"/></p>
<p align="center"><b>Figure 3-4:</b> NFVI Physical Resources.</p>
