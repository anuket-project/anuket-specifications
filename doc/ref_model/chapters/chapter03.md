[<< Back](../../ref_model)
# 3	Infrastructure Abstraction
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Model.](#model)
* [3.2 Exposed vs Internal.](#expint)
* [3.3 Exposed NFVI capabilities, metrics, and constraints.](#expcap)

There is the necessity to clearly define which kind of infrastructure resources a shared network function virtualisation infrastructure (NFVI) will provide for hosting virtual network functions (VNFs) and/or cloud-native network functions (CNF), so that the requirements of each of the VNFs and CNFs match the capabilities of the NFVI.

<< Figure 3 >>

The lack of a common understanding of which resources and corresponding capabilities a suitable NFVI should provide may lead to several issues which could negatively impact the time and cost for onboarding and maintaining these solutions on top of a virtualised infrastructure e.g.:
- supporting any kind of VNF specific requirements (e.g. regarding network acceleration or API access) might result in having to establish different silo NFVIs for each VNF
- synchronising the release cycles of a large set of different technologies will sooner or later lead to situations in which required upgrades cannot be applied easily due to incompatibilities.

The abstraction model presented in this chapter specifies a common set of virtual infrastructure resources which a NFVI will need to provide to be able to host most of the typical VNF workloads required by the operator community.
Although a couple of explicit and implicit abstraction models (e.g. in the context of ETSI/NFV) are already available they fall short when address following design principles:
-	**Scope**: the model should describe the most relevant virtualised infrastructure resources (incl. acceleration technologies) an NFVI needs to provide for hosting Telco VNF workloads
-	**Separation of Concern**: the model should support a clear distinction between the responsibilities related to maintaining the network function virtualisation infrastructure and the responsibilities related to managing the various VNF workloads
-	**Simplicity**: the amount of different types of resources (including their attributes and relationships amongst one another) should be kept to a minimum to reduce the configuration spectrum which needs to be considered
-	**Declarative**: the model should allow for a declarative description of the required NFVI capabilities for onboarding and maintaining VNFs
-	**Explicit**: the model needs to be rich enough to allow for a direct mapping towards the APIs of NFVIs for the instantiation of virtual infrastructure elements without requiring any additional parameters
-	**Lifecycle**: the model must distinguish between resources which have independent lifecycles but should group together those resources which share a common lifecycle
-	**Aligned**: the model should clearly highlight the dependencies between the elements to allow for a well-defined and simplified synchronisation of independent automation tasks.

To summarise: the abstraction model presented in this paper will build upon existing modelling concepts and simplify and streamline them to the needs of telco operators who intend to distinguish between infrastructure related and VNF related responsibilities.

<a name="model"></a>
## 3.1	Model
The abstraction model for the NFVI makes use of following layers (only the virtual infrastructure layer will be directly exposed to the VNFs/CNFs):

<<Figure 4 >>
  
The functionalities of each layer are as follows:
- NFVI hardware profile: This layer consists of physical hardware components such as servers, random access memory, storage devices, network ports, hardware acceleration devices, etc. and their corresponding basic operating systems (BIOS).
- NFVI software profile: This layer consists of both the host Operating System (OS) responsible for managing the hardware resources of the layer below as well as the virtualization/containerization technology which turns hardware components into a pool of logical resources and dynamically allocates them to the layer above.
- Virtual infrastructure resources: This layer represents all the infrastructure resources which the NFVI provides to the VNFs/CNFs such as tenants, compute hosts, storage and networks These resources can be managed by the layer above directly or indirectly via an application programming interface or graphical user interface.
- VNFs/CNFs: This layer consists of virtualized and/or containerized network functions that run on top of a VM or as a Container.
The virtual infrastructure resources provided by the NFVI can be grouped into four categories as shown in the diagram below:

<<Figure 5>>

- tenant: tenants represent an independently manageable logical pool of compute, storage and network resources
- compute resources: represent virtualised hosts for operating systems and applications
- storage resources: represent virtualised resources for persisting data
- network resources: represent virtual resources providing layer 2 and layer 3 connectivity

The virtualised infrastructure resources related to these categories are listed below:

### Tenant

A network function virtualisation infrastructure needs to be capable of supporting multiple tenants and has to isolate sets of infrastructure resources dedicated to specific VNF/CNF workloads from one another. Tenants represent an independently manageable logical pool of compute, storage and network resources abstracted from physical hardware. **Example**: a tenant within an OpenStack environment or a Kubernetes cluster.

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

### Compute Host
A virtual machine or a container/pod belonging to a tenant capable of hosting the application components of VNFs. A compute host therefore requires a tenant context and since it will need to communicate with other communication partners it is assumed that the networks have been provisioned in advance. **Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV.

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

### Storage
A block device of a certain size for persisting information which can be created and dynamically attached to/detached from a compute host. A storage device resides in a tenant context and exists independently from any compute host. **Example**: an OpenStack cinder volume.

| Attribute | Description |
| --- | --- |
| `name` | name of storage resources |
| `size` | size of disc in GB |
| `attachments` | list of compute hosts to which the device is currently attached |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |
| `metadata` | key/value pairs for selection of the appropriate redundancy domain |

<p align="center"><b>Table 3-3:</b> Attributes of storage resources.</p>

_**Comments**: we need to be more specific regarding acceleration and metadata._

### Network
A layer 2 / layer 3 communication domain within a tenant. A network requires a tenant context. **Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV.

| Attribute | Description |
| --- | --- |
| `name` | name of the network resource |
| `subnet` | classless inter-domain routing of the subnet |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |

<p align="center"><b>Table 3-4:</b> Attributes of network resources.</p>

<a name="expint"></a>
## 3.2	Exposed vs Internal
Mark S./Tom investigating.
1.	(Explanation)
2.	E.g. this is how I expose my NFVi storage to the VNF = External

<a name="expcap"></a>
## 3.3	Exposed NFVI capabilities, metrics, and constraints

### 3.3.1	Exposed NFVI capabilities
This section covers a list of explicit NFVI capabilities and metrics that defines an NFVI. These capabilities and metrics are well known to VNFs as they provide capabilities which VNFs rely on.

> _**Note**: 	It is expected that NFVI capabilities and metrics will evolve with time as more capabilities are added as technology enhances and matures._

#### 3.3.1.1	Exposed resource capabilities
**Table 3-5** below shows resource capabilities of NFVI. Those indicate resources offered to VNFs by NFVI.

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|----------------------------------------------------|--------|-------------------------------------------------------------------------------|
| e.nfvi.res.cap.001 | #vCPU cores | number | Min, Max number of vCPU cores that can be assigned to a single VNF-C |
| e.nfvi.res.cap.002 | Amount of RAM (MB) | MB | Min, Max memory in MB  that can be assigned to a single VNF-C by NFVI. |
| e.nfvi.res.cap.003 | Total amount of instance (ephemeral) storage (GB) | GB | Min, Max storage in GB  that can be assigned to a single VNF-C by NFVI |
| e.nfvi.res.cap.004 | # vNICs | number | Max number of vNIC interfaces that can be assigned to a single VNF-C by NFVI. |
| e.nfvi.res.cap.005 | Total amount of external (persistent) storage (GB) | GB | Min, Max storage in GB that can be attached / mounted to VNF-C by NFVI. |

<p align="center"><b>Table 3-5:</b> Exposed resource capabilities of NFVI.</p>

**Table 3-6** is how they map to different NFVI instances:

| Ref | B Instance | N Instance | C Instance |
|--------------------|----------------------------|----------------------------|----------------------------|
| `e.nfvi.res.cap.001` | As per selected  <flavour> | As per selected  <flavour> | As per selected  <flavour> |
| `e.nfvi.res.cap.002` | As per selected  <flavour> | As per selected  <flavour> | As per selected  <flavour> |
| `e.nfvi.res.cap.003` | As per selected  <flavour> | As per selected  <flavour> | As per selected  <flavour> |
| `e.nfvi.res.cap.004` | As per selected  <I Opt> | As per selected  <I Opt> | As per selected  <I Opt> |
| `e.nfvi.res.cap.005` | As per selected  <S Ext> | As per selected  <S Ext> | As per selected  <S Ext> |

<p align="center"><b>Table 3-6:</b> Mapping of exposed resource capabilities to different NFVI instances.</p>

#### 3.3.1.2 Exposed performance optimisation capabilities
**Table 3-7** shows possible performance optimisation capabilities that can be provided by NFVI. These indicate capabilities exposed to VNFs. Those capabilities need to be consumed by VNFs in a standard way.

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|---------------------------|--------|--------------------------------------------|
| e.nfvi.per.cap.001 | CPU pinning support | Yes/No | Determining if NFVI support CPU pinning |
| e.nfvi.per.cap.002 | NUMA support | Yes/No | Determining if NFVI support NUMA awareness |
| e.nfvi.per.cap.003 | IPSec Acceleration | Yes/No | IPSec Acceleration |
| e.nfvi.per.cap.004 | Crypto Acceleration | Yes/No | Crypto Acceleration |
| e.nfvi.per.cap.005 | Transcoding Acceleration | Yes/No | Transcoding Acceleration |
| e.nfvi.per.cap.006 | Programmable Acceleration | Yes/No | Programmable Acceleration |

<p align="center"><b>Table 3-7:</b> Exposed performance optimisation capabilities of NFVI.</p>

| Ref | B Instance | N Instance | C Instance |
|--------------------|------------|------------------|------------------|
| `e.nfvi.per.cap.001` | No | Yes | Yes |
| `e.nfvi.per.cap.002` | No | Yes | No |
| `e.nfvi.per.cap.003` | No | Yes (if offered) | No |
| `e.nfvi.per.cap.004` | No | Yes (if offered) | No |
| `e.nfvi.per.cap.005` | No | No | Yes (if offered) |
| `e.nfvi.per.cap.006` | No | No | Yes (if offered) |

<p align="center"><b>Table 3-8:</b> Mapping of Exposed performance optimisation capabilities with different NFVI instance types.</p>

#### 3.3.1.3	Exposed monitoring capabilities
**Table 3-9** shows possible monitoring capabilities available by NFVI for VNFs.

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|---------------------------|--------|----------------------------------------------------|
| e.nfvi.mon.cap.001 | Monitoring of L2-7 data | Yes/No | Ability for VNF-C to monitor their own L2-L7 data. |

<p align="center"><b>Table 3-9:</b> Exposed monitoring capabilities of NFVI.</p>

| Ref | B Instance | N Instance | C Instance |
|--------------------|------------|------------------|------------------|
| `e.nfvi.mon.cap.001` | No | Yes | No |

<p align="center"><b>Table 3-10:</b> Mapping of Exposed monitoring capabilities with different NFVI instance types.</p>

### 3.3.2	Exposed NFVI metrics
#### 3.3.2.1	Exposed performance metrics 
**Table 3-11** below shows performance metrics of NFVI. The intent of those metrics is to be well known to VNFs. These metrics are aligned with ETSI GS NFV TST-009 [2].

| Ref | NFVI metric | Unit | Definition/Notes |
|--------------------|------------------------------------------|--------|-----------------------------------------------------------------------|
| e.nfvi.per.met.001 | Network Throughput | bps | Max thougput per vNIC assigned to VNF-C @256 Bytes |
| e.nfvi.per.met.002 | Network Latency | ms | Range (min, max) on each vNIC assigned to VNF-C. ETSI NFV-TST 009[2]. |
| e.nfvi.per.met.003 | External (persistent) storage IO | iops | Range (min, max) per VNF-C |
| e.nfvi.per.met.004 | External (persistent) storage throughput | MB/s | Range (min, max) per VNF-C |

<p align="center"><b>Table 3-11:</b> Exposed performance metrics of NFVI.</p>

| Ref | B Instance | N Instance | C Instance |
|--------------------|--------------------------|---------------------------|---------------------------|
| `e.nfvi.per.met.001` | Up to speed of   <I Opt> | Up to speed of    <I Opt> | Up to speed of    <I Opt> |
| `e.nfvi.per.met.002` | <30ms | <0.5ms | <5ms |
| `e.nfvi.per.met.003` | As per selected  <S Ext> | As per selected  <S Ext> | As per selected  <S Ext> |
| `e.nfvi.per.met.004` | As per selected  <S Ext> | As per selected  <S Ext> | As per selected  <S Ext> |

<p align="center"><b>Table 3-12:</b> Mapping of Exposed performance metrics to NFVI instance types.</p>

## 3.4	Internal NFVI capabilities metrics, and constraints
This section covers a list of implicit NFVI capabilities and metrics that defines the interior of   NFVI. These capabilities and metrics determines how NFVI behaves internally. They are hidden from VNFs (i.e. VNFs may not know about them) but they will have a big impact on the overall performance and capabilities of a given NFVI solution.
>_Note: 	It is expected that implicit NFVI capabilities and metrics will evolve with time as more capabilities are added as technology enhances and matures._
### 3.4.1	Internal NFVI capabilities
#### 3.4.1.1	Internal resource capabilities

