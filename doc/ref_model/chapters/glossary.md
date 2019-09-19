[<< Back](../../ref_model)
# Glossary - Terminology
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [11.1 Terminology.](#11.1)
  * [11.1.1 Software layers terminology.](#11.1.1)
  * [11.1.2 Hardware layers terminology.](#11.1.2)
  * [11.1.3 Operational and administrative terminology.](#11.1.3)
  * [11.1.4 Other terminology.](#11.1.4)

<a name="11.1"></a>
## 11.1 Terminology.

To help guide the reader, this glossary provides an introduction to the terminology used within this document. These definitions are, with a few exceptions, based on the ETSI GS NFV 003 V1.4.1 (2018-08) definitions.  In a few cases, they have been modified to avoid deployment technology dependencies only when it seems necessary to avoid confusion.

<a name="11.1.1"></a>
### 1.2.1 Software Layer Terminology

- **Network Function Virtualisation (NFV)**: The concept of separating network functions from the hardware they run on by using a virtual hardware abstraction layer.
- **Network Function Virtualisation Infrastructure (NFVI)**: The totality of all hardware and software components used to build the environment in which a set of VAs are deployed.
 >_*Note:*_ The NFV-Infrastructure can span across many locations, e.g. places where data centres or edge nodes are operated. The network providing connectivity between these locations is regarded to be part of the NFVI. NFVI and VNF are the top-level conceptual entities in the scope of Network Function Virtualisation. All other components are sub-entities of these two main entities.

- **Network Function (NF)**:  functional block or application within a network infrastructure that has well-defined external interfaces and well-defined functional behaviour.
  - Within **NFV**, A **Network Function** is implemented in a form of **Virtualised NF** or a **Containerised NF**.
- **Network Service (NS)**: composition of **Network Function**(s) and/or **Network Service**(s), defined by its functional and behavioural specification, including the service lifecycle.
- **Virtual Network Function (VNF)**: a software implementation of a **Network Function**, capable of running on the **NFVi**.
  - **VNF**s are built from one or more VNF Components (**VNFC**) and, in most cases,  the VNFC is hosted on a single VM or Container.
- **Cloud-native (containerised) Network Function (CNF)**: **VNF** with a full adherence to cloud native principles, or a **VNF** that is transitioning to cloud native.
  >_*Note:*_ A containerised **VNF** is microservices-oriented, to increase agility and maintainability, and can be dynamically orchestrated and managed to optimize resource utilization. The containers run on an application orchestration layer, not directly on the underlaying infrastructure itself. the containers themselves may be Linux, Docker or other similar container technology.
- **Virtual Application (VA)**: A general term for software which can be loaded into a Virtual Machine.
  >_*Note:*_ a **VNF** is one type of VA.
- **Workload**: Workload refers to software running on top of compute resources such as **VMs** or **Container**s. Most relevant workload categories in context of NFVI are:
  - **Data Plane Workloads**: are related to packet handling of the end-to-end communication between applications. These tasks are expected to be very I/O and memory read/write operations intensive.
  - **Control Plane Workloads**: are the task related to any other communication between NFs that is not directly related to the end-to-end data communication between applications. For example, this category includes session management, routing or authentication.
  - **Storage Workloads**: are all tasks related to disk storage (either SSD or HDD or other).  Examples range from non-intensive router logging to more intensive database read/write operations.
- **Virtual Machine (VM)**: virtualised computation environment that behaves like a physical computer/server.
  >_*Note:*_ A **VM** consists of all of the components (processor (CPU), memory, storage, interfaces/ports, etc.) of a physical computer/server. It is created using Instance Type together with sizing information or Compute Flavour.
- **Instance type**: Specifies a set of virtualized hardware resources and capabilities used for the creation of a virtual compute on which a workload runs on, includes capability specifications characterizing compute, storage and memory.
- **Instance**: is a virtual compute resource, in a known state such as running or suspended, that can be used like a physical server.  >_*Note:*_ Can be used to specify VM Instance or Container Instance.
- **Compute flavour**: defines the sizing of the virtualised resources (compute, memory, and storage) required to run a workload.
     >_*Note:*_ used to define the configuration/capacity limit of a virtualised container.
- **VM instances Catalogue**: Pre-defined instance types and compute flavours.
- **Container**: a container provides operating-system-level virtualization by abstracting the “user space”. One big difference between **Containers** and **VM**s is that unlike VMs, where each **VM** is self-contained with all the operating systems components are within the **VM** package, containers "share" the host system’s kernel with other containers.
- **Virtual resources**:
  - **Virtual Compute resource (a.k.a. virtualised container)**: partition of a compute node that provides an isolated virtualised computation environment.
  - **Virtual Storage resource**: virtualised non-volatile storage allocated to a virtualised computation environment hosting a **VNFC**
  - **Virtual Networking resource**: routes information among the network interfaces of a virtual compute resource and physical network interfaces, providing the necessary connectivity
- **Hypervisor**: A piece of software with management components that allows the user to partition the underlying physical resources and allocate them to Virtual Machines. Typically, the hypervisor is managed by a cloud management software such as OpenStack.
- **Container Engine**: Software components used to create, destroy, and manage containers on top of an operating system.
- **NFVI Software Profile (NFVI SW Profile)**: defines the behaviour, capabilities and metrics provided by an NFVI Software Layer
- **NFVI Software Configuration (NFVI SW Configuration)**: a set of settings (Key:Value) that are applied/mapped to **NFVI** SW deployment.

<a name="11.1.2"></a>
### 11.1.2 Hardware Layer Terminology

- **Physical Network Function (PNF)**: Implementation of a network function via tightly coupled dedicated hardware and software system. >_*Note:*_ This is a physical NFVI resource with the NF software.
- **Hardware resources**: Compute/Storage/Network hardware resources on which the NFVI platform software, virtual machines and containers run on.
- **NFVI Hardware Profile**: defines the behaviour, capabilities and metrics provided by an NFVI Hardware Layer.
  - **Host Profile**: is another term for a **NFVI hardware profile**.
- **NFVI Hardware Configuration**: a set of settings (Key:Value) that are applied/mapped to **NFVI** HW deployment.

<a name="11.1.3"></a>
### 11.1.3 Operational and Administrative Terminology

- **Tenant**: Tenants represent an independently manageable logical pool of compute, storage and network resources abstracted from physical hardware.
- **Tenant (Internal) Networks**: Virtual networks that are internal to tenant instances.
- **External Network**: External networks provide network connectivity for an NFVI tenant to resources outside of the tenant space.
- **Quota**: An imposed upper limit on specific types of resources, usually used to prevent excessive resource consumption in the **VIM** by a given consumer (tenant).
- **Resource pool**: A logical grouping of NFVI hardware and software resources. A resource pool can be based on a certain resource type (for example, compute, storage, network) or a combination of resource types. An **NFVI** resource can be part of none, one or more resource pools.
- **Compute Node**: An abstract definition of a server.
>_*Note:*_ A compute node can refer to a set of hardware and software that support the VMs or Containers running on it. 
- **Service Assurance (SA)**: collects alarm and monitoring data. Applications within SA or interfacing with SA can then use this data for fault correlation, root cause analysis, service impact analysis, SLA management, security, monitoring and analytic, etc.

<a name="11.1.4"></a>
### 1.1.4 Other Referenced Terminology

- **Virtualised Infrastructure Manager (VIM)**: responsible for controlling and managing the **NFVI** compute, storage and network resources.
- **NFV Orchestrator (NFVO)**: manages the VNF lifecycle and **NFVI** resources (supported by the **VIM**) to ensure an optimised allocation of the necessary resources and connectivity.
