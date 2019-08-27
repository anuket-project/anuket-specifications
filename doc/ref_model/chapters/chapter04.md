[<< Back](../../ref_model)
# 4	Infrastructure Capabilities, Metrics, and Catalogue
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>


 ______________________________________________________________
## Table of Contents

* [4.1 Capabilities and Metrics.](#4.1)
  * [4.1.1 Exposed vs Internal.](#4.1.1)
  * [4.1.2 Exposed Infrastructure capabilities.](#4.1.2)
  * [4.1.3 Exposed Infrastructure metrics.](#4.1.3)
  * [4.1.4 Internal Infrastructure capabilities.](#4.1.4)
  * [4.1.5 Internal Infrastructure metrics.](#4.1.5)
  * [4.1.6 VIM capabilities.](#4.1.6)
  * [4.1.7 VIM metrics.](#4.1.7)
* [4.2 Catalogue.](#4.2)
  * [4.2.1 Compute flavours.](#4.2.1)
  * [4.2.2 Network Interface Specifications.](#4.2.2)
  * [4.2.3 Storage Extensions.](#4.2.3)
  * [4.2.4 Instance types.](#4.2.4)
  * [4.2.5 Instance capabilities mapping.](#4.2.5)
  * [4.2.6 Instance metrics mapping.](#4.2.6)
  * [4.2.7 One stop shop.](#4.2.7)

<a name="4.1"></a>
## 4.1 Capabilities and Metrics

<a name="4.1.1"></a>
### 4.1.1 Exposed vs Internal

The following pertains to the context of NFVI Capabilities, Metrics and Constraints, as discussed within this chapter.

<b>Exposed:</b> Refers to any mechanism (e.g., discovery, configuration, consumption, telemetry, some object, API, Interface, etc.) that exists in or pertains to, the domain of the NFVI and is made visible (aka “Exposed”) to a tenant and/or VNF in the workload domain. When an object is exposed to a given tenant or VNF, the scope of visibility within a given VNF is at the discretion of the specific VNF’s designer. From an Infra perspective, the Infra-resident object is simply being exposed to one or more virtual environments (i.e. VMs). It is then the responsibility of the kernel or supervisor/executive within the VM to control how, when and where the object is further exposed within the VM, with regard to permissions, security, etc. As the object(s) originate with the NFVI or Control Plane, they are by definition visible within those domains.

<b>Internal:</b> Effectively the opposite of Exposed; objects Internal to the NFVI, which are exclusively available for use by the NFVI and components within the NFVI control plane.

<p align="center"><img src="../figures/Sect_3-2_Exposed_vs_Internal_Diagram_v2.jpg" alt="Exposed vs. Internal Scope" title="Exposed vs. Internal Scope" width="65%"/></p>
<p align="center"><b>Figure 4-1:</b> Exposed vs. Internal Scope</p>

As illustrated in the figure above, objects designated as "Internal" are only visible within the area inside the blue oval (the NFVI), and only when the entity accessing the object has the appropriate permissions. Whereas objects designated as "Exposed" are potentially visible from both the area within the green oval (the Workload), as well as from within the NFVI, again provided the entity accessing the object has appropriate permissions.

Note: The figure above indicates the areas from where the objects are <i>visible</i>. It is not intended to indicate where the objects are <i>instantiated</i>. For example, the virtual resources are instantiated within the NFVI (the blue area), but are Exposed, and therefore are <i>visible</i> to the Workload, within the green area.

<a name="4.1.2"></a>
### 4.1.2 Exposed Infrastructure capabilities
This section describes a set of explicit NFVI capabilities and metrics that define an NFVI. These capabilities and metrics are well known to VNFs as they provide capabilities which VNFs rely on.

> _**Note**: 	It is expected that NFVI capabilities and metrics will evolve with time as more capabilities are added as technology enhances and matures._

<a name="4.1.2.1"></a>
#### 4.1.2.1 Exposed resource capabilities

**Table 4-1** below shows resource capabilities of NFVI. Those indicate resources offered to VNFs by NFVI.

<a name="Table4-1"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|----------------------------------------------------|--------|-------------------------------------------------------------------------------|
| e.nfvi.res.cap.001 | #vCPU cores | number | Min, Max number of vCPU cores that can be assigned to a single VNF-C |
| e.nfvi.res.cap.002 | Amount of RAM (MB) | MB | Min, Max memory in MB that can be assigned to a single VNF-C by NFVI. |
| e.nfvi.res.cap.003 | Total amount of instance (ephemeral) storage (GB) | GB | Min, Max storage in GB that can be assigned to a single VNF-C by NFVI |
| e.nfvi.res.cap.004 | # vNICs | number | Max number of vNIC interfaces that can be assigned to a single VNF-C by NFVI. |
| e.nfvi.res.cap.005 | Total amount of external (persistent) storage (GB) | GB | Min, Max storage in GB that can be attached / mounted to VNF-C by NFVI. |

<p align="center"><b>Table 4-1:</b> Exposed resource capabilities of NFVI.</p>

<a name="4.1.2.2"></a>
#### 4.1.2.2 Exposed performance optimisation capabilities

**Table 4-2** shows possible performance optimisation capabilities that can be provided by NFVI. These indicate capabilities exposed to VNFs. Those capabilities need to be consumed by VNFs in a standard way.

<a name="Table4-2"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|---------------------------|--------|--------------------------------------------|
| e.nfvi.per.cap.001 | CPU pinning support | Yes/No | Determining if NFVI support CPU pinning |
| e.nfvi.per.cap.002 | NUMA support | Yes/No | Determining if NFVI support NUMA awareness |
| e.nfvi.per.cap.003 | IPSec Acceleration | Yes/No | IPSec Acceleration |
| e.nfvi.per.cap.004 | Crypto Acceleration | Yes/No | Crypto Acceleration |
| e.nfvi.per.cap.005 | Transcoding Acceleration | Yes/No | Transcoding Acceleration |
| e.nfvi.per.cap.006 | Programmable Acceleration | Yes/No | Programmable Acceleration |

<p align="center"><b>Table 4-2:</b> Exposed performance optimisation capabilities of NFVI.</p>

<a name="4.1.2.3"></a>
#### 4.1.2.3 Exposed monitoring capabilities

**Table 4-3** shows possible monitoring capabilities available by NFVI for VNFs.

<a name="Table4-3"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|---------------------------|--------|----------------------------------------------------|
| e.nfvi.mon.cap.001 | Monitoring of L2-7 data | Yes/No | Ability for VNF-C to monitor their own L2-L7 data. |

<p align="center"><b>Table 4-3:</b> Exposed monitoring capabilities of NFVI.</p>

<a name="4.1.3"></a>
### 4.1.3 Exposed Infrastructure metrics
The intent of those metrics is to be well known to VNFs.

<a name="4.1.3.1"></a>
#### 4.1.3.1 Exposed performance metrics

The following shows performance metrics per VNF-C, vNIC or vCPU.

<a name="Table4-4"></a>

| Ref                | NFVI metric               | Unit                | Definition/Notes                                             |
| ------------------ | ------------------------- | ------------------- | ------------------------------------------------------------ |
| e.nfvi.per.met.001 | Network throughput        | bits/s or packets/s | Max throughput per vNIC (as aligned with ETSI GS NFV-TST 009 [2]) |
| e.nfvi.per.met.002 | Network latency           | second              | Max round trip time to vNIC (as aligned with ETSI GS NFV-TST 009 [2]) |
| e.nfvi.per.met.003 | Network Delay Variation   | second              | Max packet delay variation (a.k.a., jitter) of round trip time to vNIC (as aligned with ETSI GS NFV-TST 009 [2]) |
| e.nfvi.per.met.004 | Simultaneous active flows | number              | Max simultaneous active L4 flows per vNIC before a new flow is dropped |
| e.nfvi.per.met.005 | New flows rate            | flows/s             | Max new L4 flow rate per vNIC                                |
| e.nfvi.per.met.006 | Storage throughput        | bytes/s or IO/s     | Max throughput per virtual block storage unit assigned to VNF-C |
| e.nfvi.per.met.007 | Processing capacity       | test-specific       | Processing capacity test-specific score per vCPU             |

<p align="center"><b>Table 4-4:</b> Exposed performance metrics of NFVI.</p>


<a name="4.1.4"></a>
### 4.1.4 Internal Infrastructure capabilities

This section covers a list of implicit NFVI capabilities and metrics that define the interior of   NFVI. These capabilities and metrics determine how the NFVI behaves internally. They are hidden from VNFs (i.e. VNFs may not know about them) but they will have a big impact on the overall performance and capabilities of a given NFVI solution.

>_**Note**: 	It is expected that implicit NFVI capabilities and metrics will evolve with time as more capabilities are added as technology enhances and matures._

<a name="4.1.4.1"></a>
#### 4.1.4.1 Internal resource capabilities
**Table 4-5** shows resource capabilities of NFVI. These include capabilities offered to VNFs and resources consumed internally by NFVI.

<a name="Table4-5"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|---------------------------------------------------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------|
| i.nfvi.res.cap.001 | Percentage of vCPU cores consumed by NFVI overhead in a compute node. | % (of total available) | Indicates the percentage of vCPU cores consumed (wasted) by NFVI components (including host OS) in a compute node. |
| i.nfvi.res.cap.002 | Percentage of memory consumed by NFVI overhead in a compute node. | % (of total available) | Indicates the percentage of memory consumed (wasted) by NFVI components (including host OS) in a compute node. |

<p align="center"><b>Table 4-5:</b> Internal resource capabilities of NFVI.</p>

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
<a name="4.1.4.2"></a>
#### 4.1.4.2 Internal SLA capabilities

**Table 4-6** below shows SLA (Service Level Agreement) capabilities available by NFVI. These include capabilities required by VNFs as well as internal capabilities to NFVI. Application of these capabilities to a given workload is determined by its instance type (e.g. T-Shirt size).

<a name="Table4-6"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------|
| i.nfvi.sla.cap.001 | CPU overbooking | 1:N | This indicates the number of vCPU cores consumed (wasted) by NFVI components (including host OS) in a compute node. |
| i.nfvi.sla.cap.002 | vNIC QoS | Yes/No | QoS enablement |

<p align="center"><b>Table 4-6:</b> Internal SLA capabilities to NFVI.</p>

<a name="4.1.4.3"></a>
#### 4.1.4.3 Internal performance optimisation capabilities
**Table 4-7** below shows possible performance optimisation capabilities that can be provided by NFVI. These include capabilities exposed to VNFs as well as internal capabilities to NFVI. These capabilities will be determined by the standard instance type used by VNF-C (VNF Component)

<a name="Table4-7"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|------------------------------------------|--------|----------------------------------------|
| i.nfvi.per.cap.001 | Huge page support | Yes/No | Determining if NFVI support huge pages |

<p align="center"><b>Table 4-7:</b> Internal performance optimisation capabilities of NFVI.</p>

<a name="4.1.4.4"></a>
#### 4.1.4.4 Internal monitoring capabilities

**Table 4-8** shows possible monitoring capabilities available by NFVI. The availability of these capabilities will be determined by the instance type used by the workloads.

<a name="Table4-8"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|-------------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| i.nfvi.mon.cap.001 | Host CPU usage |  | Per Compute node. It needs to Maps to ETSI NFV-TST 008[1] clause 6, processor usage metric (NFVI exposed to VIM) and ETSI NFV-IFA 027 Mean Virtual CPU usage and Peak Virtual CPU usage (VIM exposed to VNFM). |
| i.nfvi.mon.cap.002 | Virtual compute resource CPU usage |  | QoS enablement |
| i.nfvi.mon.cap.003 | Host CPU utilization |  | Per Compute node. It needs to map to ETSI NFV-IFA 027 Mean Virtual CPU usage and Peak Virtual CPU usage (VIM, exposed to VNFM). |
| i.nfvi.mon.cap.004 | Virtual compute resource CPU utilization |  | Range (min, max) per VNF-C |
| i.nfvi.mon.cap.005 | Monitoring of external storage IOPS | Yes/No | Transcoding Acceleration |
| i.nfvi.mon.cap.006 | Monitoring of external storage throughput | Yes/No | Programmable Acceleration |
| i.nfvi.mon.cap.007 | Monitoring of external storage capacity | Yes/No |  |

<p align="center"><b>Table 4-8:</b> Internal monitoring capabilities of NFVI.</p>

<a name="4.1.4.5"></a>
#### 4.1.4.5 Internal security capabilities

<a name="Table4-9"></a>

| Ref | NFVI capability | Unit | Definition/Notes |
|--------------------|-------------------------------------|--------|------------------------------------------------------------------|
| i.nfvi.sec.cap.001 | VNF-C<->VNF-C  memory isolation | Yes/No | Are VNF-C memories isolated from each other by hardware support? |
| i.nfvi.sec.cap.002 | VNF-C -> Host | Yes/No | Can VNF-C access host memory? |
| i.nfvi.sec.cap.003 | Host -> VNF-C | Yes/No | Can Host access VNF-C memory? |
| i.nfvi.sec.cap.004 | External storage at-rest encryption | Yes/No | Is external storage encrypted at-rest? |


<p align="center"><b>Table 4-9:</b> Internal security capabilities of NFVI.</p>

<a name="4.1.5"></a>
### 4.1.5 Internal Infrastructure metrics
<!-- 
[COMMENT - Xavier Grall, Orange: section "3.4.2.3 Internal SLA metrics" is removed since it is redundant with network performance metrics]
//
[COMMENT - Xavier Grall, Orange: section "3.4.2.4 Internal scalability metrics" is removed since it is redundant with resource management metrics]
--> 
<a name="4.1.5.1"></a>
#### 4.1.5.1 Internal performance metrics 
<!-- 
[COMMENT - Xavier Grall, Orange: the mapping table is removed since those reference values will depend on architecture and implementation, and/or may be derived for different cases (eg w/ or w/o filtering rules for network throughput) ]
--> 

The following table shows performance metrics per NFVI node.

<a name="Table4-10"></a>

| Ref | NFVI metrics | Unit | Definition/Notes |
|--------------------|------------------------------------------------------|----------------|----------------------------------------------------------------------|
| i.nfvi.per.met.001 | Network throughput | bits/s or packets/s | Max throughput per node (aligned with ETSI GS NFV-TST 009 [2]) |
| i.nfvi.per.met.002 | Simultaneous active flows | number | Max simultaneous active L4 flows per node before a new flow is dropped |
| i.nfvi.per.met.003 | New flows rate               | flows/s  | Max new L4 flow rate per node                                |
| i.nfvi.per.met.004 | Processing capacity | test-specific | Processing capacity test-specific score per node |
| i.nfvi.per.met.005 | Energy consumption           | W                   | Maximum energy consumption of the node without hosting any VNF-C (but fully ready for it) |
| i.nfvi.per.met.006 | Network energy efficiency    | W/bits/s            | Energy consumption for the node max network throughput, normalized to the bit rate |
| i.nfvi.per.met.007 | Processing energy efficiency | W/core | Energy consumption during the node processing capacity measurement (i.nfvi.per.met.004), normalized to physical cores usable by VNF-C |

<p align="center"><b>Table 4-10:</b> Internal performance metrics of NFVI.</p>

It should be noted that energy-related metrics must only be considered for NFVI software implementations benchmarking on a same NFVI hardware implementation (since energy consumption may be very different for a same processor model due to foundry process spread).

<a name="4.1.5.2"></a>
#### 4.1.5.2 Internal availability/reliability metrics

<!-- Xavier Grall, Orange -->
_**Editor Note:** the following table should be reviewed to only consider and probably detail the recovery-related metrics ; indeed, availability and MTBF metrics do not seem consistent with expected testbed measurement duration]_

<!--
[COMMENT - Xavier Grall, Orange: the mapping table is removed since those reference values will depend on reference architecture and implementation]
-->

<!-- MXS - 13/7/2019 To-do -->
_**Editor Note:** This table needs to be reworked and clarified w/ clear explanations and assumptions stated._

<a name="Table4-11"></a>

| Ref | NFVI metric | Unit | Definition/Notes |
|--------------------|------------------|---------|-------------------------------------------|
| i.nfvi.arl.met.001 | Availability | % |  |
| i.nfvi.arl.met.002 | MTBF single node | days | Mean Time between Failure for single node |
| i.nfvi.arl.met.003 | MTBF AZ | days | Mean Time between Failure for an   AZ |
| i.nfvi.arl.met.004 | Recovery time | seconds |  |

<p align="center"><b>Table 4-11:</b> Internal availability/reliability metrics of NFVI.</p>

<a name="4.1.6"></a>
### 4.1.6 VIM capabilities.

VIM is responsible for controlling and managing the NFVI compute, storage and network resources. Resources allocation is dynamically set up upon VNFs requirements. This section covers the list of capabilities offered by the VIM to VNFs or service orchestrator.

Table 4-12 shows capabilities related to resources allocation

<a name="Table4-12"></a>

| Ref | VIM capability | Unit | Definition/Notes |
|--------------------|------------------|---------|-------------------------------------------|
| e.vim.res.cap.001 | Virtual Compute allocation | Yes/No | Capability to allocate virtual compute resources  to VNFC |
| e.vim.res.cap.002 | Virtual Storage allocation | Yes/No | Capability to allocate virtual storage resources  to VNFC |
| e.vim.res.cap.003 | Virtual Networking resources  allocation | Yes/No | Capability to allocate virtual networking resources  to VNFC |
| e.vim.res.cap.004 | Multi-tenant isolation | Yes/No | Capability to isolate resources between tenants |
| e.vim.res.cap.005 | Images management | Yes/No | Capability to manage VNFC software images |

<p align="center"><b>Table 4-12:</b> VIM capabilities related to resources allocation .</p>


Table 4-13 shows monitoring capabiltities

<a name="Table4-13"></a>

| Ref | VIM capability | Unit | Definition/Notes |
|--------------------|------------------|---------|-------------------------------------------|
| e.vim.mon.cap.001 | Virtual resources inventory per tenant | Yes/No | Capability to provide information related to allocated virtualised resources per tenant |
| e.vim.mon.cap.002 | Resources Monitoring | Yes/No | Capability to notify state changes of allocated resources |
| e.vim.mon.cap.003 | Virtual resources Performance  | Yes/No | Capability to collect and expose performance information on virtualised resources allocated |
| e.vim.mon.cap.004 |Virtual resources Fault information | Yes/No | Capability to collect and notify fault information on virtualised resources |

<p align="center"><b>Table 4-13:</b> VIM capabilities related to resources monitoring .</p>

Table 4-14 shows security capabilities

<a name="Table4-14"></a>

| Ref | VIM capability | Unit | Definition/Notes |
|--------------------|------------------|---------|-------------------------------------------|
| e.vim.sec.cap.001 | Resources management requests verification | Yes/No | Capability to validate and verify the integrity of a resources management requests coming from NFVO or VNFM|

<p align="center"><b>Table 4-14:</b> VIM capabilities related to security .</p>

<!-- Rabi A -->
_**Editor Note:** This Section is still to be worked on._

<a name="4.1.7"></a>
### 4.1.7 VIM metrics.

<a name="4.1.7.1"></a>
#### 4.1.7.1 Resources management metrics 
**Table 4-12** shows resource management metrics of VIM as aligned with ETSI GS NFV TST-012 [3].

<a name="Table4-12"></a>

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

<p align="center"><b>Table 4-12:</b> Resource management metrics of VIM.</p>

<a name="4.1"></a>
## 4.2 Catalogue

Infrastructure exposes sets of capabilities, metrics, compute flavours, interface options, storage extensions, and acceleration capabilities to VNFs. Those sets are offered to VNFs in form of instance types with their corresponding options and extensions.

The idea of the infrastructure instances catalogue is to have a predefined set of instance types with a predefined set of compute flavours (sometimes referred to as T-shirt sizes) which VNF vendors use to build their VNFs. Each VNF uses one or more of those compute flavours (with one or more of offered instance types) to build its overall functionality as illustrated in **Figure 4-2**.

<p align="center"><img src="../figures/ch04_vnf_design.PNG" alt="vnf_design" title="VNF Design" width="65%"/></p>
<p align="center"><b>Figure 4-2:</b> VNFs built against standard instance types and compute flavours.</p>

<a name="4.2.1"></a>
### 4.2.1 Compute flavours

Flavours represent the compute, memory, storage capacity, and management network resource templates that are used to create the VMs on the compute hosts. Each VM instance is given a flavour (resource template), which determines the instance's core, memory and storage characteristics. 

Flavours can also specify secondary ephemeral storage, swap disk, etc. A compute flavour geometry consists of the following elements:

Element |Description 
--------|----------
Name	|A descriptive name
Virtual compute resources (aka vCPUs) |Number of virtual compute resources (vCPUs) presented to the instance.
Memory MB	|Instance memory in megabytes. 
Ephemeral/Local Disk |Specifies the size of an ephemeral data disk that exists only for the life of the instance. Default value is 0.<br />The ephemeral disk may be partitioned into boot (base image) and swap space disks. 
Is Public	|Boolean value, whether flavor is available to all users or private to the project it was created in. Defaults to True.

<p align="center"><b>Table 4-13:</b> Flavour Geometry Specification.</p>

<a name="4.2.1.1"></a>
#### 4.2.1.1 Predefined Compute flavours
The intent of the following flavours list is to be comprehensive and yet effective to cover both IT and NFV workloads. The compute flavours are specified relative to the standardised “large” flavour. The standard “large” flavour configuration consists of 4 vCPUs, 8 GB of RAM and 80 GB of local disk, and the resulting instance will have a management interface of 1 Gbps. The “medium” flavour is half the size of a large and small is half the size of medium. The tiny flavour is a special sized flavour.

>_*Note:*_ Customised (Parameterized) flavours can be used in concession by operators and , if needed, are  created using TOSCA, HEAT templates and/or VIM APIs.

.conf |vCPU ("c") |RAM ("r") |Local Disk ("d") | Management Interface
-----|------------|----------|-----|-----
.tiny	|1	|512 MB	|1 GB	|1 Gbps
.small	|1	|2 GB	|20 GB 	|1 Gbps
.medium	|2	|4 GB	|40 GB	|1 Gbps
.large	|4	|8 GB	|80 GB	|1 Gbps
.2xlarge*	|8	|16 GB	|160 GB	|1 Gbps
.4xlarge*	|16	|32 GB	|320 GB	|1 Gbps

<p align="center"><b>Table 4-14:</b> Predefined Compute flavours.</p>

> _*These compute flavours are intended to be used for transitional purposes and VNF vendors are expected to consume smaller flavours and adopt micro server's designs for their VNFs_

<a name="4.2.2"></a>
### 4.2.2 Network Interface Specifications

The network interface specifications extend the flavour customization to specify the network interface “n” followed by the interface bandwidth (in Gbps) and an alphabetic character defining the number of interfaces with that bandwidth; multiple network interface bandwidths, where network interfaces of different bandwidths exist, can be specified by repeating the “n” option.
```
<network interface bandwidth option> :: <”n”><number (bandwidth in Gbps)>< # of interfaces of that bandwidth>
<number of interfaces> :: <”” | “D” | “T” | “Q” | “P” | “H”> 
where “” represents 1x, “D” 2x, “T” 3x, “Q” 4x, “p” 5x and “H” 6x interfaces of the given bandwidth.
```

Virtual network interface option	|Description (Bandwidth in Gbps)
---|---
n1, n10, n1T, n1Q, n1P, n1H	|1x 1, 2x 1, 3x 1, 4x 1, 5x 1, 6x 1 Gbps
n10, n10D, n10T, n10Q, n10P, n10H	|1x 10, 2x 10, 3x 10, 4x 10, 5x 10, 6x 10 Gbps
n25, n25D, n25T, n25Q, n25P, n25H	|1x 25, 2x 25, 3x 25, 4x 25, 5x 25, 6x 25 Gbps
n50, n50D, n50T, n50Q, n50P, n50H	|1x 50, 2x 50, 36x 50, 4x 50, 5x 50, 6x 50 Gbps
n100, n100D, n100T, n100Q, n100P, n100H	|1x 100, 2x 100, 3x 100, 4x 100, 5x 100, 6x 100 Gbps

<p align="center"><b>Table 4-15:</b> Virtual Network Interface Specification Examples.</p>

<a name="4.2.3"></a>
###  4.2.3 Storage Extensions
Multiple non-ephemeral storage volumes can be attached to virtual computes  for persistent data storage. Each of those volumes can be configured with the required performance category.

.conf	|Read IO/s	|Write IO/s	Read |Throughput (MB/s)	|Write Throughput (MB/s)
---|---|---|---|---
.bronze	|Up to 3K	|Up to 15K	|Up to 180	|Up to 120
.silver	|Up to 60K	|Up to 30K	|Up to 1200	|Up to 400
.gold	|Up to 680K	|Up to 360K	|Up to 2650	|Up to 1400

<p align="center"><b>Table 4-16:</b> Storage Performance Profiles.</p>

<a name="4.2.3.1"></a>
#### 4.2.3.1 Available storage extensions
These are non-ephemeral storage extensions that can be provided to VNFs for persistent data storage. More than one storage extension can be provided to a single VNF-C.

| .conf | capacity | Read IOPS | Write IOPS | Read Throughput (MB/s) | Write Throughput (MB/s) |
|----------|----------|------------|------------|------------------------|-------------------------|
| .bronze1 | 100GB | Up to 3K | Up to 15K | Up to 180 | Up to 120 |
| .bronze2 | 200GB | Up to 3K | Up to 15K | Up to 180 | Up to 120 |
| .bronze3 | 300GB | Up to 3K | Up to 15K | Up to 180 | Up to 120 |
| .silver1 | 100GB | Up to 60K | Up to 30K | Up to 1200 | Up to 400 |
| .silver2 | 200GB | Up to 60K | Up to 30K | Up to 1200 | Up to 400 |
| .silver3 | 300GB | Up to 60K | Up to 30K | Up to 1200 | Up to 400 |
| .gold1 | 100GB | Up to 680K | Up to 360K | Up to 2650 | Up to 1400 |
| .gold2 | 200GB | Up to 680K | Up to 360K | Up to 2650 | Up to 1400 |
| .gold3 | 300GB | Up to 680K | Up to 360K | Up to 2650 | Up to 1400 |

<p align="center"><b>Table 4-17:</b> Storage extensions for compute flavours.</p>

<a name="4.2.4"></a>
### 4.2.4 Instance types

<a name="4.2.4.1"></a>
#### 4.2.4.1 B Instances (Basic)
This instance type is intended to be used for both IT workloads as well as NFV workloads. It has limited IO capabilities (up to 10Gbps Network interface) with a wide range of compute flavours. This instance type is intended to be available in any data centre within any operator's network.

<a name="4.2.4.2"></a>
#### 4.2.4.2 N Instances (Network Intensive)
This instance type is intended to be used for those applications that has high network throughput requirements (up to 50Gbps). This instance type is more intended for VNFs and is expected to be available in regional (distributed) data centres and more towards the access networks.

##### 4.2.4.2.1 Network Acceleration Extensions
N instance types can come with Network Acceleration extensions to assist VNFs offloading some of their network intensive operations to hardware. The list below is preliminary and is expected to grow as more network acceleration resources are developed and standardized. 
>_Interface types are aligned with ETSI NFV IFA 002 [4]._

| .conf | Interface type | Description |
|------------|----------------|-----------------------------------------|
| .il-ipsec | virtio-ipsec* | In-line IPSec acceleration |
| .la-crypto | virtio-crypto | Look-Aside encryption/decryption engine |

<p align="center"><b>Table 4-18:</b> Acceleration extensions for N instance type.</p>

> _*Need to work with relevant open source communities to create missing interfaces._

<a name="4.2.4.3"></a>
#### 4.2.4.3 C Instances (Compute Intensive)
This instance type is intended to be used for those applications that has high compute requirements and can take advantage of acceleration technologies such as GPU, FPGA, etc. This instance type is intended to be available in local data centers and more towards the Edge of the network.

##### 4.2.4.3.1 Compute acceleration extensions
C instance types can come with compute acceleration extensions to assist VNFs/VAs offloading some of their compute intensive operations to hardware. The list below is preliminary and is expected to grow as more compute acceleration resources are developed and standardized.

| .conf | Interface type | Description |
|------------|----------------|-----------------------------------------|
| .la-trans | virtio-trans* | Look-Aside Transcoding acceleration |
| .la-programmable | virtio-programmable | Look-Aside programmable acceleration |

<p align="center"><b>Table 4-19:</b> Acceleration extensions for C instance type.</p>

> _*Need to work with relevant open source communities to create missing interfaces._

<a name="4.2.4.4"></a>
#### 4.2.4.4 Network Interface Options
**Table 4-8** below shows the various network interfaces options (from **Table 4-3**) are available for which profile type (Up to 6 interfaces are possible).

| Virtual interface option* | Basic Type | Network Intensive Type | Compute Intensive Type
|---------------------------|-----|-----|-----
n1, n10, n1T*, n1Q*, n1P*, n1H*	| Y | N |N
n10, n10D, n10T*, n10Q*, n10P*, n10H*	| Y | Y | Y
n25, n25D, n25T*, n25Q*, n25P*, n25H*	| N | Y | Y
n50, n50D, n50T*, n50Q*, n50P*, n50H*	| N | Y | Y
n100, n100D, n100T*, n100Q*, n100P*, n100H* | N | Y | N

<p align="center"><b>Table 4-20:</b> Virtual NIC interfaces options</p>

> _*These options are intended to be used for transitional purposes. VNFs are expected to use minimum number of interfaces and adopt micro-servers design principles._

<a name="4.2.5"></a>
### 4.2.5 Instance capabilities mapping.

| Ref | B Instance | N Instance | C Instance | Notes |
|----------------------|----------------------------|----------------------------|----------------------------|-------|
| `e.nfvi.res.cap.001` | As per selected  \<flavour> | As per selected  \<flavour> | As per selected  \<flavour> | Exposed resource capabilities as per [**Table 4-1**.](#Table4-1)|
| `e.nfvi.res.cap.002` | As per selected  \<flavour> | As per selected  \<flavour> | As per selected  \<flavour> |  |
| `e.nfvi.res.cap.003` | As per selected  \<flavour> | As per selected  \<flavour> | As per selected  \<flavour> |  |
| `e.nfvi.res.cap.004` | As per selected  <I Opt> | As per selected  <I Opt> | As per selected  <I Opt> |  |
| `e.nfvi.res.cap.005` | As per selected  <S Ext> | As per selected  <S Ext> | As per selected  <S Ext> |  |
| `e.nfvi.per.cap.001` | No | Yes | Yes | Exposed performance capabilities as per [**Table 4-2**.](#Table4-2) |
| `e.nfvi.per.cap.002` | No | Yes | No | |
| `e.nfvi.per.cap.003` | No | Yes (if offered) | No | |
| `e.nfvi.per.cap.004` | No | Yes (if offered) | No | |
| `e.nfvi.per.cap.005` | No | No | Yes (if offered) | |
| `e.nfvi.per.cap.006` | No | No | Yes (if offered) | |
| `e.nfvi.mon.cap.001` | No | Yes | No | Exposed monitoring capabilities as per [**Table 4-3**.](#Table4-3) |
| `i.nfvi.sla.cap.001` | 1:4 | 1:1 | 1:1 | Internal SLA capabilities as per [**Table 4-6**.](#Table4-6) |
| `i.nfvi.sla.cap.002` | No | Yes | Yes | |
| `i.nfvi.per.cap.001` | No | Yes | No | Internal performance capabilities as per [**Table 4-7**.](#Table4-7) |
| `i.nfvi.mon.cap.001` | Yes | Yes | Yes | Internal monitoring capabilities as per [**Table 4-8**.](#Table4-8) |
| `i.nfvi.mon.cap.002` | Yes | Yes | Yes | |
| `i.nfvi.mon.cap.003` | Yes | Yes | Yes | |
| `i.nfvi.mon.cap.004` | Yes | Yes | Yes | |
| `i.nfvi.mon.cap.005` | Yes | No | Yes | |
| `i.nfvi.mon.cap.006` | Yes | No | Yes | |
| `i.nfvi.mon.cap.007` | Yes | No | Yes | |
| `i.nfvi.sec.cap.001` | Yes | Yes | Yes | Internal security capabilities as per [**Table 4-9**.](#Table4-9) |
| `i.nfvi.sec.cap.002` | No | No | No | |
| `i.nfvi.sec.cap.003` | Yes | Yes | Yes | |
| `i.nfvi.sec.cap.004` | Yes | Yes | Yes | |

<p align="center"><b>Table 4-21:</b> Mapping of NFVI capabilities to instance types.</p>

<a name="4.2.6"></a>
### 4.2.6 Instance metrics mapping.

_**Comment:** To be worked on._

<a name="4.2.7"></a>
### 4.2.7 One stop shop

<a name="4.2.7.1"></a>
#### 4.2.7.1 Naming convention
An entry in the infrastructure profile catalogue can be referenced using the following naming convention.

`B/N/C <I opt> . <flavour> . <S ext> . <A ext>`

Whereas:
- **B/N/C**: specifies the instance type (Basic, Network Intensive, and Compute Intensive)
- **\<I opt>**: specifies the interface option of the instant.
- **\<flavour>**: specifies the compute flavour.
- **\<S ext>**: specifies an optional storage extension.
- **\<A ext>**: specifies an optional acceleration extension for either N or H instance types.

<p align="center"><img src="../figures/ch04_one_stop_shop.PNG" alt="one_stop_shop" title="One Stop Shop" width="100%"/></p>
<p align="center"><b>Figure 4-3:</b> Infrastructure Instances catalogue.</p>
