[<< Back](../../ref_model)
# Glossary - Terminology
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [11.1 Terminology](#11.1)
  * [11.1.1 Software layers terminology](#11.1.1)
  * [11.1.2 Hardware layers terminology](#11.1.2)
  * [11.1.3 Operational and administrative terminology](#11.1.3)
  * [11.1.4 Container Related Terminology](#11.1.4)
  * [11.1.4 Other terminology](#11.1.5)

<a name="11.1"></a>
## 11.1 Terminology

To help guide the reader, this glossary provides an introduction to the terminology used within this document. These definitions are, with a few exceptions, based on the ETSI GS NFV 003 V1.4.1 (2018-08) definitions.  In a few cases, they have been modified to avoid deployment technology dependencies only when it seems necessary to avoid confusion.

<a name="11.1.1"></a>
### 11.1.1 Software Layer Terminology

- **Network Function Virtualisation (NFV)**: The concept of separating network functions from the hardware they run on by using a virtual hardware abstraction layer.
- **Network Function Virtualisation Infrastructure (NFVI)**: The totality of all hardware and software components used to build the environment in which a set of VAs are deployed.
 >_*Note:*_ The NFV-Infrastructure can span across many locations, e.g. places where data centres or edge nodes are operated. The network providing connectivity between these locations is regarded to be part of the NFVI. NFVI and VNF are the top-level conceptual entities in the scope of Network Function Virtualisation. All other components are sub-entities of these two main entities.

- **Network Function (NF)**:  functional block or application within a network infrastructure that has well-defined external interfaces and well-defined functional behaviour.
  - Within **NFV**, A **Network Function** is implemented in a form of **Virtualised NF** or a **Containerised NF**.
- **Network Service (NS)**: composition of **Network Function**(s) and/or **Network Service**(s), defined by its functional and behavioural specification, including the service lifecycle.
- **Virtual Network Function (VNF)**: a software implementation of a **Network Function**, capable of running on the **NFVi**.
  - **VNF**s are built from one or more VNF Components (**VNFC**) and, in most cases,  the VNFC is hosted on a single VM or Container.
- **Cloud native Network Function (CNF)**: An implementation of a Virtual Network Function (**VNF**, as defined by ETSI GS NFV 003) that adheres to the CNCF Cloud Native Definition or a **VNF** that is transitioning to cloud native.
  >_*Note:*_ This definition is derived from [CNCF TUG White Paper](https://docs.google.com/document/d/1-zqxz5bdCLTuOEvi2ybADR3PcmzbBhNt6YkNnvx-KoA/edit#heading=h.5x0d5h95i329). A cloud native **VNF** is microservices-oriented, to increase agility and maintainability, and can be dynamically orchestrated and managed to optimize resource utilization. The containers run on an application orchestration layer, not directly on the underlaying infrastructure itself. the containers themselves may be Linux, Docker or other similar container technology.
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

- **Cloud service user**: Natural person, or entity acting on their behalf, associated with a cloud service customer that uses cloud services.
>_*Note*_ Examples of such entities include devices and applications.
- **Tenant**: One or more cloud service users sharing access to a set of physical and virtual resources ([ITU](https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-Y.3500-201408-I!!PDF-E&type=items)).
>_*Note*_ Tenants represent an independently manageable logical pool of compute, storage and network resources abstracted from physical hardware.
- **Tenant (Internal) Networks**: Virtual networks that are internal to tenant instances.
- **Multi-tenancy**: feature where physical, virtual or service resources are allocated in such a way that multiple tenants and their computations and data are isolated from and inaccessible by each another. ([ETSI](https://www.etsi.org/deliver/etsi_gs/NFV/001_099/003/01.04.01_60/gs_nfv003v010401p.pdf))
- **External Network**: External networks provide network connectivity for an NFVI tenant to resources outside of the tenant space.
- **Quota**: An imposed upper limit on specific types of resources, usually used to prevent excessive resource consumption in the **VIM** by a given consumer (tenant).
- **Resource pool**: A logical grouping of NFVI hardware and software resources. A resource pool can be based on a certain resource type (for example, compute, storage, network) or a combination of resource types. An **NFVI** resource can be part of none, one or more resource pools.
- **Compute Node**: An abstract definition of a server.
>_*Note:*_ A compute node can refer to a set of hardware and software that support the VMs or Containers running on it. 
- **Service Assurance (SA)**: collects alarm and monitoring data. Applications within SA or interfacing with SA can then use this data for fault correlation, root cause analysis, service impact analysis, SLA management, security, monitoring and analytic, etc.

<a name="11.1.4"></a>
### 11.1.4 Container Related Terminology

>_*Note:*_ Relevant terms are added here from RA2. Most of these term definitions are taken from [Kubernetes glossary](https://kubernetes.io/docs/reference/glossary) but in some cases should be made independent from Kubernetes as a specific container orchestration engine.

- **Container Image**:	Stored instance of a container that holds a set of software needed to run an application.
- **Container**:	A lightweight and portable executable image that contains software and all of its dependencies.
- **Pod**:	The smallest and simplest Kubernetes object. A Pod represents a set of running containers on your cluster. A Pod is typically set up to run a single primary container. It can also run optional sidecar containers that add supplementary features like logging.
- **Kubernetes Cluster**: A set of machines, called nodes, that run containerised applications managed by Kubernetes. A cluster has at least one worker node and at least one master node.
- **Kubernetes Master**:	The master node(s) manages the worker nodes and the pods in the cluster. Multiple master nodes are used to provide a cluster with failover and high availability.
- **Kubernetes Control Plane**:	The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.
- **Kubernetes Node**:	A node is a worker machine in Kubernetes. A worker node may be a VM or physical machine, depending on the cluster. It has local daemons or services necessary to run Pods and is managed by the control plane.
- **CaaS**:	Container-as-a-Service. A complete set of technologies to enable the management of containerised software, including a Kubernetes cluster, container networking, storage, routing, service mesh, etc.
- **CaaS Manager**:	A management plane function that manages the lifecycle (instantiation, scaling, healing, etc.) of one or more CaaS instances, including communication with VIM for master/node lifecycle management.
- **Kubernetes Service**: An abstract way to expose an application running on a set of Pods as a network service.

<a name="11.1.5"></a>
### 11.1.5 Other Referenced Terminology

- **Virtualised Infrastructure Manager (VIM)**: responsible for controlling and managing the **NFVI** compute, storage and network resources.
- **NFV Orchestrator (NFVO)**: manages the VNF lifecycle and **NFVI** resources (supported by the **VIM**) to ensure an optimised allocation of the necessary resources and connectivity.
