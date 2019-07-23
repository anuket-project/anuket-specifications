[<< Back](../../ref_model)
# 3	Infrastructure Abstraction
<p align="right"><img src="../figures/bogo_lsf.png" alt="bogo" title="Bogo Meter" width="35%"/></p>
 
## Table of Contents
* [3.1 Model.](#3.1)
* [3.2 Exposed vs Internal.](#3.2)
* [3.3 Exposed NFVI capabilities, metrics.](#3.3)
  * [3.3.1 Exposed NFVI capabilities.](#3.3.1)
  * [3.3.2 Exposed NFVI metrics.](#3.3.2)
* [3.4 Internal NFVI capabilities and metrics.](#3.4)
  * [3.4.1 Internal NFVI capabilities.](#3.4.1)
  * [3.4.2 Internal NFVI metrics.](#3.4.2)
* [3.5 VIM capabilities and metrics.](#3.5)
  * [3.5.1 VIM capabilities.](#3.5.1)
  * [3.5.2 VIM metrics.](#3.5.2)

There is the necessity to clearly define which kind of infrastructure resources a shared network function virtualisation infrastructure (NFVI) will provide for hosting workloads including virtual network functions (VNFs) and/or cloud-native network functions (CNF), so that the requirements of the workloads match the capabilities of the NFVI.

The lack of a common understanding of which resources and corresponding capabilities a suitable NFVI should provide may lead to several issues which could negatively impact the time and the cost for on-boarding and maintaining these solutions on top of a virtualised infrastructure. For Example:

- Supporting any kind of workload specific requirements (e.g. regarding network acceleration or API access) might result in having to establish different silo of NFVIs for each workload type.
- Synchronising the release cycles of a large set of different technologies will sooner or later lead to situations in which required upgrades cannot be applied easily due to incompatibilities.

The abstraction model presented in this chapter specifies a common set of virtual infrastructure resources which NFVI will need to provide to be able to host most of the typical VNF/CNF workloads required by the operator community.

Although a couple of explicit and implicit abstraction models (e.g. in the context of ETSI NFV) are already available, they fall short when addressing the following design principles:
-	**Scope:** the model should describe the most relevant virtualised infrastructure resources (incl. acceleration technologies) an NFVI needs to provide for hosting Telco workloads
-	**Separation of Concern:** the model should support a clear distinction between the responsibilities related to maintaining the network function virtualisation infrastructure and the responsibilities related to managing the various VNF workloads
-	**Simplicity:** the amount of different types of resources (including their attributes and relationships amongst one another) should be kept to a minimum to reduce the configuration spectrum which needs to be considered
-	**Declarative:** the model should allow for a declarative description of the required NFVI capabilities for on-boarding and maintaining workloads
-	**Explicit:** the model needs to be rich enough to allow for a direct mapping towards the APIs of NFVIs for the instantiation of virtual infrastructure elements without requiring any additional parameters
-	**Lifecycle:** the model must distinguish between resources which have independent lifecycles but should group together those resources which share a common lifecycle
-	**Aligned:** the model should clearly highlight the dependencies between the elements to allow for a well-defined and simplified synchronisation of independent automation tasks.

_**To summarise:** the abstraction model presented in this document will build upon existing modelling concepts and simplify and streamline them to the needs of telco operators who intend to distinguish between infrastructure related and workload related responsibilities._

<a name="3.1"></a>
## 3.1	Model

The abstraction model for the NFVI makes use of the following layers (only the virtual infrastructure layer will be directly exposed to workloads (VNFs/CNFs)):

<p align="center"><img src="../figures/figure_3.1_NFVI-Model.png" alt="NFVI model_layers" Title="NFVI Model Layers" width="65%"/></p>
<p align="center"><b>Figure 3-1:</b> NFVI Model Layers.</p>
  
The functionalities of each layer are as follows:
- **Physical Infrastructure Resources:** This layer consists of physical hardware components such as servers, (including random access memory, local storage, network ports, and hardware acceleration devices), storage devices, network devices, etc. and the basic input output system (BIOS).
- **NFVI Software:** This layer consists of both the host Operating System (OS) responsible for managing the physical infrastructure resources as well as the virtualization/containerization technology which, on request, dynamically allocates hardware components and exposes them as virtual resources.
- **Virtual Infrastructure Resources:** This layer represents all the infrastructure resources (compute, storage and networks) which the NFVI provides to the workloads such as VNFs/CNFs. These virtual resources can be managed by the tenants and tenant workloads directly or indirectly via an application programming interface (API).
- **Workloads (VNFs/CNFs):** This layer consists of workloads such as virtualized and/or containerized network functions that run on top of a VM or as a Container. The virtual infrastructure resources provided by the NFVI can be grouped into four categories as shown in the diagram in **Figure 3-2**.

The virtual infrastructure resources provided by the NFVI can be grouped into four categories as shown in the diagram below:

<p align="center"><img src="../figures/figure_3.2_Virtual_Infra_Resources.png" alt="virtual_resources" Title="Virtual Infrastructure Resources" width="65%"/></p>
<p align="center"><b>Figure 3-2:</b> Virtual Infrastructure Resources provides virtual compute, storage and networks in a tenant context.</p>

- **Tenants:** represent an independently manageable logical pool of compute, storage and network resources
- **Compute resources:** represent virtualised computes for workloads and Operating and other Systems as necessary
- **Storage resources:** represent virtualised resources for persisting data
- **Network resources:** represent virtual resources providing layer 2 and layer 3 connectivity

The virtualised infrastructure resources related to these categories are listed below:

### Tenant

A network function virtualisation infrastructure (NFVI) needs to be capable of supporting multiple tenants and has to isolate sets of infrastructure resources dedicated to specific workloads (VNF/CNF) from one another. Tenants represent an independently manageable logical pool of compute, storage and network resources abstracted from physical hardware. _**Example**: a tenant within an OpenStack environment or a Kubernetes cluster._

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

### Compute
A virtual machine or a container/pod belonging to a tenant capable of hosting the application components of workloads (VNFs). A virtual compute therefore requires a tenant context and since it will need to communicate with other communication partners it is assumed that the networks have been provisioned in advance. _**Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV._

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
A block device of a certain size for persisting information which can be created and dynamically attached to/detached from a virtual compute. A storage device resides in a tenant context and exists independently from any compute host. _**Example**: an OpenStack cinder volume._

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
A layer 2 / layer 3 communication domain within a tenant. A network requires a tenant context. _**Example**: a virtual compute descriptor as defined in TOSCA Simple Profile for NFV._

| Attribute | Description |
| --- | --- |
| `name` | name of the network resource |
| `subnet` | network address of the subnet |
| `acceleration` | key/value pairs for selection of the appropriate acceleration technology |

<p align="center"><b>Table 3-4:</b> Attributes of network resources.</p>

<a name="3.2"></a>
## 3.2	Exposed vs Internal

The following pertains to the context of NFVI Capabilities, Metrics and Constraints, as discussed within this chapter.

<b>Exposed:</b> Refers to any mechanism (e.g., discovery, configuration, consumption, telemetry, some object, API, Interface, etc.) that exists in or pertains to, the domain of the NFVI and is made visible (aka “Exposed”) to a tenant and/or VNF in the workload domain. When an object is exposed to a given tenant or VNF, the scope of visibility within a given VNF is at the discretion of the specific VNF’s designer. From an Infra perspective, the Infra-resident object is simply being exposed to one or more virtual environments (i.e. VMs). It is then the responsibility of the kernel or supervisor/executive within the VM to control how, when and where the object is further exposed within the VM, with regard to permissions, security, etc. As the object(s) originate with the NFVI or Control Plane, they are by definition visible within those domains.

<b>Internal:</b> Effectively the opposite of Exposed; objects Internal to the NFVI, which are exclusively available for use by the NFVI and components within the NFVI control plane.

<p align="center"><img src="../figures/Sect_3-2_Exposed_vs_Internal_Diagram_v2.jpg" alt="Exposed vs. Internal Scope" title="Exposed vs. Internal Scope" width="65%"/></p>
<p align="center"><b>Figure 3-3:</b> Exposed vs. Internal Scope</p>

As illustrated in the figure above, objects designated as "Internal" are only visible within the area inside the blue oval (the NFVI), and only when the entity accessing the object has the appropriate permissions. Whereas objects designated as "Exposed" are potentially visible from both the area within the green oval (the Workload), as well as from within the NFVI, again provided the entity accessing the object has appropriate permissions.

Note: The figure above indicates the areas from where the objects are <i>visible</i>. It is not intended to indicate where the objects are <i>instantiated</i>. For example, the virtual resources are instantiated within the NFVI (the blue area), but are Exposed, and therefore are <i>visible</i> to the Workload, within the green area.

<a name="3.3"></a>
## 3.3	Exposed NFVI capabilities and metrics

<a name="3.3.1"></a>
### 3.3.1	Exposed NFVI capabilities
This section describes a set of explicit NFVI capabilities and metrics that define an NFVI. These capabilities and metrics are well known to VNFs as they provide capabilities which VNFs rely on.

> _**Note**: 	It is expected that NFVI capabilities and metrics will evolve with time as more capabilities are added as technology enhances and matures._

#### 3.3.1.1	Exposed resource capabilities
**Table 3-5** below shows resource capabilities of NFVI. Those indicate resources offered to VNFs by NFVI.

<a name="Table3-5"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|----------------------------------------------------|--------|-------------------------------------------------------------------------------|
| e.nfvi.res.cap.001 | #vCPU cores | number | Min, Max number of vCPU cores that can be assigned to a single VNF-C |
| e.nfvi.res.cap.002 | Amount of RAM (MB) | MB | Min, Max memory in MB that can be assigned to a single VNF-C by NFVI. |
| e.nfvi.res.cap.003 | Total amount of instance (ephemeral) storage (GB) | GB | Min, Max storage in GB that can be assigned to a single VNF-C by NFVI |
| e.nfvi.res.cap.004 | # vNICs | number | Max number of vNIC interfaces that can be assigned to a single VNF-C by NFVI. |
| e.nfvi.res.cap.005 | Total amount of external (persistent) storage (GB) | GB | Min, Max storage in GB that can be attached / mounted to VNF-C by NFVI. |

<p align="center"><b>Table 3-5:</b> Exposed resource capabilities of NFVI.</p>

#### 3.3.1.2 Exposed performance optimisation capabilities
**Table 3-6** shows possible performance optimisation capabilities that can be provided by NFVI. These indicate capabilities exposed to VNFs. Those capabilities need to be consumed by VNFs in a standard way.

<a name="Table3-6"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|---------------------------|--------|--------------------------------------------|
| e.nfvi.per.cap.001 | CPU pinning support | Yes/No | Determining if NFVI support CPU pinning |
| e.nfvi.per.cap.002 | NUMA support | Yes/No | Determining if NFVI support NUMA awareness |
| e.nfvi.per.cap.003 | IPSec Acceleration | Yes/No | IPSec Acceleration |
| e.nfvi.per.cap.004 | Crypto Acceleration | Yes/No | Crypto Acceleration |
| e.nfvi.per.cap.005 | Transcoding Acceleration | Yes/No | Transcoding Acceleration |
| e.nfvi.per.cap.006 | Programmable Acceleration | Yes/No | Programmable Acceleration |

<p align="center"><b>Table 3-6:</b> Exposed performance optimisation capabilities of NFVI.</p>

#### 3.3.1.3	Exposed monitoring capabilities
**Table 3-9** shows possible monitoring capabilities available by NFVI for VNFs.

<a name="Table3-7"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|---------------------------|--------|----------------------------------------------------|
| e.nfvi.mon.cap.001 | Monitoring of L2-7 data | Yes/No | Ability for VNF-C to monitor their own L2-L7 data. |

<p align="center"><b>Table 3-7:</b> Exposed monitoring capabilities of NFVI.</p>

<a name="3.3.2"></a>
### 3.3.2	Exposed NFVI metrics
The intent of those metrics is to be well known to VNFs.

#### 3.3.2.1	Exposed performance metrics

The following shows performance metrics per VNF-C, vNIC or vCPU.

<a name="Table3-8"></a>

| Ref                | NFVI metric               | Unit                | Definition/Notes                                             |
| ------------------ | ------------------------- | ------------------- | ------------------------------------------------------------ |
| e.nfvi.per.met.001 | Network throughput        | bits/s or packets/s | Max throughput per vNIC (as aligned with ETSI GS NFV-TST 009 [2]) |
| e.nfvi.per.met.002 | Network latency           | second              | Max round trip time to vNIC (as aligned with ETSI GS NFV-TST 009 [2]) |
| e.nfvi.per.met.003 | Network Delay Variation   | second              | Max packet delay variation (a.k.a., jitter) of round trip time to vNIC (as aligned with ETSI GS NFV-TST 009 [2]) |
| e.nfvi.per.met.004 | Simultaneous active flows | number              | Max simultaneous active L4 flows per vNIC before a new flow is dropped |
| e.nfvi.per.met.005 | New flows rate            | flows/s             | Max new L4 flow rate per vNIC                                |
| e.nfvi.per.met.006 | Storage throughput        | bytes/s or IO/s     | Max throughput per virtual block storage unit assigned to VNF-C |
| e.nfvi.per.met.007 | Processing capacity       | test-specific       | Processing capacity test-specific score per vCPU             |

<p align="center"><b>Table 3-8:</b> Exposed performance metrics of NFVI.</p>

<a name="3.4"></a>
## 3.4	Internal NFVI capabilities metrics, and constraints
This section covers a list of implicit NFVI capabilities and metrics that define the interior of   NFVI. These capabilities and metrics determine how the NFVI behaves internally. They are hidden from VNFs (i.e. VNFs may not know about them) but they will have a big impact on the overall performance and capabilities of a given NFVI solution.

>_**Note**: 	It is expected that implicit NFVI capabilities and metrics will evolve with time as more capabilities are added as technology enhances and matures._

<a name="3.4.1"></a>
### 3.4.1	Internal NFVI capabilities
#### 3.4.1.1	Internal resource capabilities
**Table 3-13** shows resource capabilities of NFVI. These include capabilities offered to VNFs and resources consumed internally by NFVI.

<a name="Table3-9"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|---------------------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------|
| i.nfvi.res.cap.001 | Percentage of vCPU cores consumed by NFVI overhead in a compute node. | % (of total available) | Indicates the percentage of vCPU cores consumed (wasted) by NFVI components (including host OS) in a compute node. |
| i.nfvi.res.cap.002 | Percentage of memory consumed by NFVI overhead in a compute node. | % (of total available) | Indicates the percentage of memory consumed (wasted) by NFVI components (including host OS) in a compute node. |

<p align="center"><b>Table 3-9:</b> Internal resource capabilities of NFVI.</p>

<!--
/* MXS 13/7/2019 - Mapping table 3-14 is being commented out. If someone can provide supporting details,
   we can put it back. Details should include assumptions (e.g., is it SRIOV, OvS or what?), 
   citable references, an explanation of what we're mapping and why (#s represent min? max? anticipated?, etc.),
   and a detailed basis for the values, including an explanation for how come the numbers are identical for both
   cores and ram. Thanks, -Mark */
//
| Ref | B Instance | N Instance | C Instance |
|--------------------|--------------------------|--------------------------|--------------------------|
| `i.nfvi.res.cap.001` | 5-10% | 10-20% | 15-25% |
| `i.nfvi.res.cap.002` | 5-10% | 10-20% | 15-25% |
<p align="center"><b>Table 3-14:</b> Mapping of Internal resource capabilities to NFVI instance types.</p>
//
-->

#### 3.4.1.2	Internal SLA capabilities
**Table 3-10** below shows SLA (Service Level Agreement) capabilities available by NFVI. These include capabilities required by VNFs as well as internal capabilities to NFVI. Application of these capabilities to a given workload is determined by its instance type (e.g. T-Shirt size).

<a name="Table3-10"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------|
| i.nfvi.sla.cap.001 | CPU overbooking | 1:N | This indicates the number of vCPU cores consumed (wasted) by NFVI components (including host OS) in a compute node. |
| i.nfvi.sla.cap.002 | vNIC QoS | Yes/No | QoS enablement |

<p align="center"><b>Table 3-10:</b> Internal SLA capabilities to NFVI.</p>

#### 3.4.1.3	Internal performance optimisation capabilities
**Table 3-11** below shows possible performance optimisation capabilities that can be provided by NFVI. These include capabilities exposed to VNFs as well as internal capabilities to NFVI. These capabilities will be determined by the standard instance type used by VNF-C (VNF Component)

<a name="Table3-11"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|------------------------------------------|--------|----------------------------------------|
| i.nfvi.per.cap.001 | Huge page support | Yes/No | Determining if NFVI support huge pages |

<p align="center"><b>Table 3-11:</b> Internal performance optimisation capabilities of NFVI.</p>

#### 3.4.1.4	Internal monitoring capabilities
**Table 3-12** shows possible monitoring capabilities available by NFVI. The availability of these capabilities will be determined by the instance type used by the workloads.

<a name="Table3-12"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|-------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| i.nfvi.mon.cap.001 | Host CPU usage |  | Per Compute node. It needs to Maps to ETSI NFV-TST 008[1] clause 6, processor usage metric (NFVI exposed to VIM) and ETSI NFV-IFA 027 Mean Virtual CPU usage and Peak Virtual CPU usage (VIM exposed to VNFM). |
| i.nfvi.mon.cap.002 | Virtual compute resource CPU usage |  | QoS enablement |
| i.nfvi.mon.cap.003 | Host CPU utilization |  | Per Compute node. It needs to map to ETSI NFV-IFA 027 Mean Virtual CPU usage and Peak Virtual CPU usage (VIM, exposed to VNFM). |
| i.nfvi.mon.cap.004 | Virtual compute resource CPU utilization |  | Range (min, max) per VNF-C |
| i.nfvi.mon.cap.005 | Monitoring of external storage IOPS | Yes/No | Transcoding Acceleration |
| i.nfvi.mon.cap.006 | Monitoring of external storage throughput | Yes/No | Programmable Acceleration |
| i.nfvi.mon.cap.007 | Monitoring of external storage capacity | Yes/No |  |

<p align="center"><b>Table 3-12:</b> Internal monitoring capabilities of NFVI.</p>

#### 3.4.1.5	Internal security capabilities

<a name="Table3-13"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|-------------------------------------|--------|------------------------------------------------------------------|
| i.nfvi.sec.cap.001 | VNF-C<->VNF-C  memory isolation | Yes/No | Are VNF-C memories isolated from each other by hardware support? |
| i.nfvi.sec.cap.002 | VNF-C -> Host | Yes/No | Can VNF-C access host memory? |
| i.nfvi.sec.cap.003 | Host -> VNF-C | Yes/No | Can Host access VNF-C memory? |
| i.nfvi.sec.cap.004 | External storage at-rest encryption | Yes/No | Is external storage encrypted at-rest? |


<p align="center"><b>Table 3-13:</b> Internal security capabilities of NFVI.</p>

<a name="3.4.2"></a>

### 3.4.2	Internal NFVI metrics

<!-- 
[COMMENT - Xavier Grall, Orange: section "3.4.2.3 Internal SLA metrics" is removed since it is redundant with network performance metrics]
//
[COMMENT - Xavier Grall, Orange: section "3.4.2.4 Internal scalability metrics" is removed since it is redundant with resource management metrics]
--> 

#### 3.4.2.1	Internal performance metrics 
<!-- 
[COMMENT - Xavier Grall, Orange: the mapping table is removed since those reference values will depend on architecture and implementation, and/or may be derived for different cases (eg w/ or w/o filtering rules for network throughput) ]
--> 

The following table shows performance metrics per NFVI node.

<a name="Table3-14"></a>

| Ref | NFVI metrics | Unit | Definition/Notes |
|--------------------|------------------------------------------------------|----------------|----------------------------------------------------------------------|
| i.nfvi.per.met.001 | Network throughput | bits/s or packets/s | Max throughput per node (aligned with ETSI GS NFV-TST 009 [2]) |
| i.nfvi.per.met.002 | Simultaneous active flows | number | Max simultaneous active L4 flows per node before a new flow is dropped |
| i.nfvi.per.met.003 | New flows rate               | flows/s  | Max new L4 flow rate per node                                |
| i.nfvi.per.met.004 | Processing capacity | test-specific | Processing capacity test-specific score per node |
| i.nfvi.per.met.005 | Energy consumption           | W                   | Maximum energy consumption of the node without hosting any VNF-C (but fully ready for it) |
| i.nfvi.per.met.006 | Network energy efficiency    | W/bits/s            | Energy consumption for the node max network throughput, normalized to the bit rate |
| i.nfvi.per.met.007 | Processing energy efficiency | W/core | Energy consumption during the node processing capacity measurement (i.nfvi.per.met.004), normalized to physical cores usable by VNF-C |

<p align="center"><b>Table 3-14:</b> Internal performance metrics of NFVI.</p>

It should be noted that energy-related metrics must only be considered for NFVI software implementations benchmarking on a same NFVI hardware implementation (since energy consumption may be very different for a same processor model due to foundry process spread).

#### 3.4.2.2	Internal availability/reliability metrics

<!-- Xavier Grall, Orange -->
_**Editor Note:** the following table should be reviewed to only consider and probably detail the recovery-related metrics ; indeed, availability and MTBF metrics do not seem consistent with expected testbed measurement duration]_

<!--
[COMMENT - Xavier Grall, Orange: the mapping table is removed since those reference values will depend on reference architecture and implementation]
-->

<!-- MXS - 13/7/2019 To-do -->
_**Editor Note:** This table needs to be reworked and clarified w/ clear explanations and assumptions stated._

<a name="Table3-15"></a>

| Ref | NFVI metric | Unit | Definition/Notes |
|--------------------|------------------|---------|-------------------------------------------|
| i.nfvi.arl.met.001 | Availability | % |  |
| i.nfvi.arl.met.002 | MTBF single node | days | Mean Time between Failure for single node |
| i.nfvi.arl.met.003 | MTBF AZ | days | Mean Time between Failure for an   AZ |
| i.nfvi.arl.met.004 | Recovery time | seconds |  |

<p align="center"><b>Table 3-15:</b> Internal availability/reliability metrics of NFVI.</p>

<a name="3.5"></a>

## 3.5 VIM capabilities, metrics, and constraints.

Editor Note: This Section is still to be worked on.

<a name="3.5.1"></a>

### 3.5.1 VIM capabilities.

<!-- Rabi A -->
_**Editor Note:** This Section is still to be worked on._

<a name="3.5.2"></a>

### 3.5.2 VIM metrics.

#### 3.5.2.1	 Resources management metrics 
**Table 3-16** shows resource management metrics of VIM as aligned with ETSI GS NFV TST-012 [3].

<a name="Table3-16"></a>

| Ref | VIM metrics | Unit | Definition/Notes |
|--------------------|------------------------------------------------------|--------|------------------------------------------------------------------|
| vim.rmt.met.001 | Time to create Virtual Compute for a given VNF | Max ms |  |
| vim.rmt.met.002 | Time to delete Virtual Compute of a given VNF | Max ms |  |
| vim.rmt.met.003 | Time to start Virtual Compute of a given VNF | Max ms |  |
| vim.rmt.met.004 | Time to stop Virtual Compute of a given VNF | Max ms |  |
| vim.rmt.met.005 | Time to pause Virtual Compute of a given VNF | Max ms |  |
| vim.rmt.met.006 | Time to create internal virtual network | Max ms |  |
| vim.rmt.met.007 | Time to delete internal virtual network | Max ms |  |
| vim.rmt.met.008 | Time to update internal virtual network | Max ms |  |
| vim.rmt.met.009 | Time to create external virtual network | Max ms |  |
| vim.rmt.met.010 | Time to delete external virtual network | Max ms |  |
| vim.rmt.met.011 | Time to update external virtual   network | Max ms |  |
| vim.rmt.met.014 | Time to create external storage ready for use by VNF | Max ms |  |

<p align="center"><b>Table 3-16:</b> Resource management metrics of VIM.</p>
