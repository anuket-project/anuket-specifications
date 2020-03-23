[<< Back](../../ref_model)
# Glossary
<p align="right"><img src="./figures/bogo_lsf.png" alt="scope" title="baldy" width="35%"/></p>

## Table of Contents
* [1. Terminology](#1.0)
  * [1.1 Software layers terminology](#1.1)
  * [1.2 Hardware layers terminology](#1.2)
  * [1.3 Operational and administrative terminology](#1.3)
  * [1.4 Container Related Terminology](#1.4)
  * [1.5 Other terminology](#1.5)

<a name="1.0"></a>
# 1 Terminology

To help guide the reader, this glossary provides an introduction to the terminology used within this document. These definitions are, with a few exceptions, based on the ETSI GS NFV 003 V1.4.1 (2018-08) definitions.  In a few cases, they have been modified to avoid deployment technology dependencies only when it seems necessary to avoid confusion.

<a name="1.1"></a>
## 1.1 Software Layer Terminology

- **Network Function Virtualisation (NFV)**: The concept of separating network functions from the hardware they run on by using a virtual hardware abstraction layer.
- **Network Function Virtualisation Infrastructure (NFVI)**: The totality of all hardware and software components used to build the environment in which a set of VAs are deployed (also referred to as cloud infrastructure).
 >_*Note:*_ The NFVI can span across many locations, e.g. places where data centres or edge nodes are operated. The network providing connectivity between these locations is regarded to be part of the cloud infrastructure. **NFVI** and **VNF** are the top-level conceptual entities in the scope of Network Function Virtualisation. All other components are sub-entities of these two main entities.
- **Cloud Infrastructure**: A generic term covering **NFVI** and **CaaS** capabilities - essentially the infrastructure on which a **Workload** can be executed.
- **Network Function (NF)**:  functional block or application within a network infrastructure that has well-defined external interfaces and well-defined functional behaviour.
  - Within **NFV**, A **Network Function** is implemented in a form of **Virtualised NF** or a **Cloud Native NF**.
- **Network Service (NS)**: composition of **Network Function**(s) and/or **Network Service**(s), defined by its functional and behavioural specification, including the service lifecycle.
- **Virtual Network Function (VNF)**: a software implementation of a **Network Function**, capable of running on the **Cloud Infrastructure**.
  - **VNF**s are built from one or more VNF Components (**VNFC**) and, in most cases,  the VNFC is hosted on a single VM or Container.
- **Cloud Native Network Function (CNF)**: A cloud native network function (CNF) is a cloud native application that implements network functionality. A CNF consists of one or more microservices and has been developed using Cloud Native Principles including immutable infrastructure, declarative APIs, and a “repeatable deployment process”.
  >_*Note:*_ This definition is derived from the [Cloud Native Thinking for Telecommunications Whitepaper](https://github.com/cncf/telecom-user-group/blob/master/whitepaper/cloud_native_thinking_for_telecommunications.md#1.4), which also includes further detail and examples.
- **Virtual Application (VA)**: A general term for software which can be loaded into a Virtual Machine.
  >_*Note:*_ a **VNF** is one type of VA.
- **Workload**: Workload refers to software running on top of compute resources such as **VMs** or **Container**s. Most relevant workload categories in context of cloud infrastructure are:
  - **Data Plane Workloads**: are related to packet handling of the end-to-end communication between applications. These tasks are expected to be very I/O and memory read/write operations intensive.
  - **Control Plane Workloads**: are the task related to any other communication between NFs that is not directly related to the end-to-end data communication between applications. For example, this category includes session management, routing or authentication.
  - **Storage Workloads**: are all tasks related to disk storage (either SSD or HDD or other).  Examples range from non-intensive router logging to more intensive database read/write operations.
- **Virtual Machine (VM)**: virtualised computation environment that behaves like a physical computer/server.
  >_*Note:*_ A **VM** consists of all of the components (processor (CPU), memory, storage, interfaces/ports, etc.) of a physical computer/server. It is created using Instance Type together with sizing information or Compute Flavour.
- **Instance**: is a virtual compute resource, in a known state such as running or suspended, that can be used like a physical server.  >_*Note:*_ Can be used to specify VM Instance or Container Instance.
- **Compute flavour**: defines the sizing of the virtualised resources (compute, memory, and storage) required to run a workload.
     >_*Note:*_ used to define the configuration/capacity limit of a virtualised container.
- **VM instances Catalogue**: Pre-defined instance types and compute flavours.
- **Virtual resources**:
  - **Virtual Compute resource (a.k.a. virtualisation container)**: partition of a compute node that provides an isolated virtualised computation environment.
  - **Virtual Storage resource**: virtualised non-volatile storage allocated to a virtualised computation environment hosting a **VNFC**
  - **Virtual Networking resource**: routes information among the network interfaces of a virtual compute resource and physical network interfaces, providing the necessary connectivity
- **Hypervisor**: A piece of software with management components that allows the user to partition the underlying physical resources and allocate them to Virtual Machines. Typically, the hypervisor is managed by a cloud management software such as OpenStack.
- **Cloud Infrastructure Profile**: The combination of the Cloud Infrastructure Software Profile and the Cloud Infrastructure Hardware Profile that defines the capabilities of the Cloud Infrastructure.
- **Cloud Infrastructure Software Profile**: defines the behaviour, capabilities and metrics provided by a cloud infrastructure Software Layer
- **Cloud Infrastructure Software Configuration**: a set of settings (Key:Value) that are applied/mapped to **cloud infrastructure** SW deployment.

<a name="1.2"></a>
## 1.2 Hardware Layer Terminology

- **Physical Network Function (PNF)**: Implementation of a network function via tightly coupled dedicated hardware and software system.
  >_*Note:*_ This is a physical cloud infrastructure resource with the NF software.
- **Hardware resources**: Compute/Storage/Network hardware resources on which the cloud infrastructure platform software, virtual machines and containers run on.
- **Cloud Infrastructure Hardware Profile**: defines the behaviour, capabilities and metrics provided by an cloud infrastructure Hardware Layer.
  - **Host Profile**: is another term for a **cloud infrastructure hardware profile**.
- **Cloud Infrastructure Hardware Configuration**: a set of settings (Key:Value) that are applied/mapped to **Cloud Infrastructure** HW deployment.
- **Simultaneous Multi-threading**: Simultaneous multithreading (SMT) is a technique for improving the overall efficiency of superscalar CPUs with hardware multithreading. SMT permits multiple independent threads of execution to better utilise the resources provided by modern processor architectures.


<a name="1.3"></a>
## 1.3 Operational and Administrative Terminology

- **Cloud service user**: Natural person, or entity acting on their behalf, associated with a cloud service customer that uses cloud services.
>_*Note*_ Examples of such entities include devices and applications.
- **Tenant**: One or more cloud service users sharing access to a set of physical and virtual resources ([ITU](https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-Y.3500-201408-I!!PDF-E&type=items)).
>_*Note*_ Tenants represent an independently manageable logical pool of compute, storage and network resources abstracted from physical hardware.
- **Tenant (Internal) Networks**: Virtual networks that are internal to tenant instances.
- **Multi-tenancy**: feature where physical, virtual or service resources are allocated in such a way that multiple tenants and their computations and data are isolated from and inaccessible by each another. ([ETSI](https://www.etsi.org/deliver/etsi_gs/NFV/001_099/003/01.04.01_60/gs_nfv003v010401p.pdf))
- **External Network**: External networks provide network connectivity for a cloud infrastructure tenant to resources outside of the tenant space.
- **Quota**: An imposed upper limit on specific types of resources, usually used to prevent excessive resource consumption in the **VIM** by a given consumer (tenant).
- **Resource pool**: A logical grouping of cloud infrastructure hardware and software resources. A resource pool can be based on a certain resource type (for example, compute, storage, network) or a combination of resource types. An **Cloud Infrastructure** resource can be part of none, one or more resource pools.
- **Compute Node**: An abstract definition of a server.
>_*Note:*_ A compute node can refer to a set of hardware and software that support the VMs or Containers running on it.
- **Service Assurance (SA)**: collects alarm and monitoring data. Applications within SA or interfacing with SA can then use this data for fault correlation, root cause analysis, service impact analysis, SLA management, security, monitoring and analytic, etc.

<a name="1.4"></a>
## 1.4 Container Related Terminology

>_*Note:*_ Relevant terms are added here from RA2. Most of these term definitions are taken from [Kubernetes glossary](https://kubernetes.io/docs/reference/glossary) but in some cases should be made independent from Kubernetes as a specific container orchestration engine.

- **Container Image**:	Stored instance of a container that holds a set of software needed to run an application.
- **Container**:	A lightweight and portable executable image that contains software and all of its dependencies.
>_*Note:*_ OCI defines **Container** as "An environment for executing processes with configurable isolation and resource limitations. For example, namespaces, resource limits, and mounts are all part of the container environment."
A **Container** provides operating-system-level virtualisation by abstracting the “user space”. One big difference between **Containers** and **VMs** is that unlike VMs, where each **VM** is self-contained with all the operating systems components are within the **VM** package, containers "share" the host system’s kernel with other containers.

- **Container Runtime**: The software that is responsible for running containers.
>_*Note:*_ as explained in [OCI Glossary](https://github.com/opencontainers/runtime-spec/blob/master/glossary.md) it reads the configuration files for a **Container** from a directory structure, uses that information to create a container, launches a process inside the container, and performs other lifecycle actions.

- **Container Engine**: Software components used to create, destroy, and manage containers on top of an operating system.

- **Pod**:	The smallest and simplest Kubernetes object. A Pod represents a set of running containers on your cluster. A Pod is typically set up to run a single primary container. It can also run optional sidecar containers that add supplementary features like logging.
- **Kubernetes Cluster**: A set of machines, called nodes and master, that run containerised applications managed by Kubernetes. A cluster has at least one worker node and at least one master.
>_*Note:*_ adapted from [Kubernetes Glossary](https://kubernetes.io/docs/reference/glossary/?all=true#term-cluster).
- **Kubernetes Master**:	The master node(s) manage the worker nodes and the pods in the cluster. Multiple masters are used to provide a cluster with failover and high availability.
- **Kubernetes Control Plane**:	The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.
- **Kubernetes Node**:	A node is a worker machine in Kubernetes. A worker node may be a **VM** or physical machine, depending on the cluster. It has local daemons or services necessary to run Pods and is managed by the control plane.
- **Kubernetes Service**: An abstract way to expose an application running on a set of Pods as a network service.
>_*Note:*_ This definition from [Kubernetes Glossary](https://kubernetes.io/docs/reference/glossary/?all=true#term-service) uses the term "network service" differently than in ETSI NFV.

Terms not defined by Kubernetes:
- **CaaS**:	Container-as-a-Service. A complete set of technologies to enable the management of containerised software, including a Kubernetes cluster, container networking, storage, routing, service mesh, etc.
- **CaaS Manager**:	A management plane function that manages the lifecycle (instantiation, scaling, healing, etc.) of one or more CaaS instances, including communication with VIM for master/node lifecycle management.

<a name="1.5"></a>
## 1.5 Other Referenced Terminology

- **Virtualised Infrastructure Manager (VIM)**: responsible for controlling and managing the **Network Function Virtualisation Infrastructure** compute, storage and network resources.
- **NFV Orchestrator (NFVO)**: manages the VNF lifecycle and **Cloud Infrastructure** resources (supported by the **VIM**) to ensure an optimised allocation of the necessary resources and connectivity.
- **Platform**: A cloud capabilities type in which the cloud service user can deploy, manage and run customer-created or customer-acquired applications using one or more programming languages and one or more execution environments supported by the cloud service provider ([ITU](https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-Y.3500-201408-I!!PDF-E&type=items)).
>_*Note:*_ For CNTT,  this includes the physical infrastructure, Operating Systems, virtualisation/containerisation software and other orchestration, security, monitoring/logging and life-cycle management software.

- **PM / Performance Measurement / Measurement:** The procedure or set of operations having the object of determining a Measured Value or Measurement Result. In this context, PMs reflect data generated and collected within the cloud infrastructure, that reflects the performance of the infrastructure. For example, a count of frames or packets traversing an interface, memory usage information, other resource usage and availability, etc. These data may be instantaneous or accumulated, and made available (i.e. exposed) based on permissions and contexts (e.g., workload vs. infra)

- **Monitoring (Capability):** Monitoring capabilities are used for the passive observation of workload-specific traffic traversing the Cloud Infrastructure. Note, as with all capabilities, Monitoring may be unavailable or intentionally disabled for security reasons in a given cloud infrastructure instance.

- PVP: Physical-Virtual-Physical; PVP represents a Workload test topology where a measurement is taken across two physical test points (e.g., physical NICs on a host), with traffic traversing a virtualized Workload that is logically connected between the physical points. PVP is an ETSI term, defined in [ETSI GS NFV-TST 009](https://www.etsi.org/deliver/etsi_gs/NFV-TST/001_099/009/03.01.01_60/gs_NFV-TST009v030101p.pdf)
