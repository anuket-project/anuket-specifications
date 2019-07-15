[<< Back](../../ref_model)
# 4	Catalogue
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Compute flavours.](#4.1)
  * [4.1.1 Predefined Compute flavours.](#4.1.1)
* [4.2 Network Interface Specifications.](#4.2)
* [4.3 Storage Extensions.](#4.3)
  * [4.3.1 Available storage extensions.](#4.3.1)
* [4.4 Instance types.](#4.4)
  * [4.4.1 B Instances (Basic).](#4.4.1)
  * [4.4.2 N Instances (Network Intensive).](#4.4.2)
  * [4.4.3 C Instances (Compute Intensive).](#4.4.3)
  * [4.4.4 Network Interface Options.](#4.4.4)
* [4.5 Instance capabilities and metrics.](#4.5)
  * [4.5.1 Instance capabilities.](#4.5.1)
  * [4.5.2 Instance metrics.](#4.5.2)
* [4.6 One stop shop.](#4.6)
  * [4.6.1 Naming convention.](#4.6.1)

Infrastructure exposes sets of capabilities, metrics, compute flavours, interface options, storage extensions, and acceleration capabilities to VNFs. Those sets are offered to VNFs in form of instance types with their corresponding options and extensions.

The idea of the infrastructure instances catalogue is to have a predefined set of instance types with a predefined set of compute flavours (sometimes referred to as T-shirt sizes) which VNF vendors use to build their VNFs. Each VNF uses one or more of those compute flavours (with one or more of offered instance types) to build its overall functionality as illustrated in **Figure 4-1**.

<p align="center"><img src="../figures/ch04_vnf_design.PNG" alt="vnf_design" title="VNF Design" width="65%"/></p>
<p align="center"><b>Figure 4-1:</b> VNFs built against standard instance types and compute flavours.</p>

<a name="4.1"></a>
## 4.1 Compute flavours

Flavours represent the compute, memory, storage capacity, and management network resource templates that are used to create the VMs on the compute hosts. Each VM instance is given a flavour (resource template), which determines the instance’s core, memory and storage characteristics. 

Flavours can also specify secondary ephemeral storage, swap disk, etc. A compute flavour geometry consists of the following elements:

Element |Description 
--------|----------
Name	|A descriptive name
Virtual compute resources (aka vCPUs) |Number of virtual compute resources (vCPUs) presented to the instance.
Memory MB	|Instance memory in megabytes. 
Ephemeral/Local Disk |Specifies the size of an ephemeral data disk that exists only for the life of the instance. Default value is 0.<br />The ephemeral disk may be partitioned into boot (base image) and swap space disks. 
Is Public	|Boolean value, whether flavor is available to all users or private to the project it was created in. Defaults to True.

<p align="center"><b>Table 4-1:</b> Flavour Geometry Specification.</p>

<a name="4.1.1"></a>
###  4.1.1	Predefined Compute flavours
The intent of the following flavours list is to be comprehensive and yet effective to cover both IT and NFV workloads. The compute flavours are specified relative to the standardised “large” flavour. The standard “large” flavour configuration consists of 4 vCPUs, 8 GB of RAM and 80 GB of local disk, and the resulting instance will have a management interface of 1 Gbps. The “medium” flavour is half the size of a large and small is half the size of medium. The tiny flavour is a special sized flavour.

>_*Note:*_ Customised (Parameterized) flavours can be used in concession by operators and , if needed, are  created using TOSCA, HEAT templates and/or VIM APIs.

.conf |vCPU ("c") |RAM ("r") |Local Disk ("d") | Managmenet Interface
-----|------------|----------|-----|-----
.tiny	|1	|512 MB	|1 GB	|1 Gbps
.small	|1	|2 GB	|20 GB 	|1 Gbps
.medium	|2	|4 GB	|40 GB	|1 Gbps
.large	|4	|8 GB	|80 GB	|1 Gbps
.2xlarge*	|8	|16 GB	|160 GB	|1 Gbps
.4xlarge*	|16	|32 GB	|320 GB	|1 Gbps

<p align="center"><b>Table 4-2:</b> Predefined Compute flavours.</p>

> _*These compute flavours are intended to be used for transitional purposes and VNF vendors are expected to consume smaller flavours and adopt micro server’s designs for their VNFs_

<a name="4.2"></a>
## 4.2 Network Interface Specifications

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

<p align="center"><b>Table 4-3:</b> Virtual Network Interface Specification Examples.</p>

<a name="4.3"></a>
##  4.3 Storage Extensions
Multiple non-ephemeral storage volumes can be attached to virtual computes (*replace with decided term*) for persistent data storage. Each of those volumes can be configured with the required performance catagories (*storage performance prfiles*).

.conf	|Read IO/s	|Write IO/s	Read |Throughput (MB/s)	|Write Throughput (MB/s)
---|---|---|---|---
.bronze	|Up to 3K	|Up to 15K	|Up to 180	|Up to 120
.silver	|Up to 60K	|Up to 30K	|Up to 1200	|Up to 400
.gold	|Up to 680K	|Up to 360K	|Up to 2650	|Up to 1400

<p align="center"><b>Table 4-4:</b> Storage Performance Profiles.</p>

<a name="4.3.1"></a>
### 4.3.1 Available storage extensions
These are non-ephemeral storage extensions that can be provided to VNFs for persistent data storage. More than one storage extension can be provided to a single VNF-C. Add comment about CEPH distributed storage. (Potentially create new profile for it).

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

<p align="center"><b>Table 4-5:</b> Storage extensions for compute flavours.</p>

<a name="4.4"></a>
## 4.4 Instance types

<a name="4.4.1"></a>
### 4.4.1	B Instances (Basic)
This is the basic type of infrastructure profiles and is intended to be used for both IT workloads as well as NFV workloads. It has limited IO capabilities (up to 10Gbps Network interface) with a wide range of compute flavours. This instance type is intended to be available in any data centre within any Operator’s network.

<a name="4.4.2"></a>
### 4.4.2	N Instances (Network Intensive)
This instance type is intended to be used for those applications that has high network throughput requirements (up to 50Gbps). This instance type is more intended for VNFs and is expected to be available in regional (distributed) data centres and more towards the access networks.

#### 4.4.2.1	Network Acceleration Extensions
N instance types can come with Network Acceleration extensions to assist VNFs offloading some of their network intensive operations to hardware. The list below is preliminary and is expected to grow as more network acceleration resources are developed and standardized. Those interfaces are aligned with ETSI NFV IFA 002 [4].

| .conf | Interface type | Description |
|------------|----------------|-----------------------------------------|
| .il-ipsec | virtio-ipsec* | In-line IPSec acceleration |
| .la-crypto | virtio-crypto | Look-Aside encryption/decryption engine |

<p align="center"><b>Table 4-7:</b> Acceleration extensions for N instance type.</p>

> _*Need to work with relevant open source communities to create missing interfaces._

<a name="4.4.3"></a>
### 4.4.3	C Instances (Compute Intensive)
This instance type is intended to be used for those applications that has high compute requirements and can take advantage of acceleration technologies such as GPU, FPGA, etc. This instance type is intended to be available in local data centers and more towards the Edge of the network.

#### 4.4.3.1	Compute acceleration extensions
C instance types can come with compute acceleration extensions to assist VNF/applications offloading some of their compute intensive operations to hardware. The list below is preliminary and is expected to grow as more compute acceleration resources are developed and standardized.

| .conf | Interface type | Description |
|------------|----------------|-----------------------------------------|
| .la-trans | virtio-trans* | Look-Aside Transcoding acceleration |
| .la-programmable | virtio-programmable | Look-Aside programmable acceleration |

<p align="center"><b>Table 4-8:</b> Acceleration extensions for C instance type.</p>

> _*Need to work with relevant open source communities to create missing interfaces._

<a name="4.4.4"></a>
### 4.4.4 Network Interface Options
**Table 4-6** below shows the various network interfaces options (from Table 4-4) are available for which profile type (Up to 6 interfaces are possible).

| Virtual interface option* | Basic Type | Network Intensive Type | Compute Intensive Type
|---------------------------|-----|-----|-----
n1, n10, n1T*, n1Q*, n1P*, n1H*	| Y | N |N
n10, n10D, n10T*, n10Q*, n10P*, n10H*	| Y | Y | Y
n25, n25D, n25T*, n25Q*, n25P*, n25H*	| N | Y | Y
n50, n50D, n50T*, n50Q*, n50P*, n50H*	| N | Y | Y
n100, n100D, n100T*, n100Q*, n100P*, n100H* | N | Y | N

<p align="center"><b>Table 4-6:</b> Virtual NIC interfaces options</p>

> _*These options are intended to be used for transitional purposes. VNFs are expected to use minimum number of interfaces and adopt micro-servers design principles._

<a name="4.5"></a>

## 4.5 Instance capabilities and metrics.

<a name="4.5.1"></a>

### 4.5.1 Instance capabilities.
| Ref | B Instance | N Instance | C Instance | Notes |
|----------------------|----------------------------|----------------------------|----------------------------|-------|
| `e.nfvi.res.cap.001` | As per selected  \<flavour> | As per selected  \<flavour> | As per selected  \<flavour> | Exposed resource capabilities as per [**Table 3-5**.](chapter03.md/#Table3-5)|
| `e.nfvi.res.cap.002` | As per selected  \<flavour> | As per selected  \<flavour> | As per selected  \<flavour> |  |
| `e.nfvi.res.cap.003` | As per selected  \<flavour> | As per selected  \<flavour> | As per selected  \<flavour> |  |
| `e.nfvi.res.cap.004` | As per selected  <I Opt> | As per selected  <I Opt> | As per selected  <I Opt> |  |
| `e.nfvi.res.cap.005` | As per selected  <S Ext> | As per selected  <S Ext> | As per selected  <S Ext> |  |
| `e.nfvi.per.cap.001` | No | Yes | Yes | Exposed performance capabilities as per [**Table 3-6**.](chapter03.md/#Table3-6) |
| `e.nfvi.per.cap.002` | No | Yes | No | |
| `e.nfvi.per.cap.003` | No | Yes (if offered) | No | |
| `e.nfvi.per.cap.004` | No | Yes (if offered) | No | |
| `e.nfvi.per.cap.005` | No | No | Yes (if offered) | |
| `e.nfvi.per.cap.006` | No | No | Yes (if offered) | |
| `e.nfvi.mon.cap.001` | No | Yes | No | Exposed monitoring capabilities as per [**Table 3-7**.](chapter03.md/#Table3-7) |
| `i.nfvi.sla.cap.001` | 1:4 | 1:1 | 1:1 | Internal SLA capabilities as per [**Table 3-10**.](chapter03.md/#Table3-10) |
| `i.nfvi.sla.cap.002` | No | Yes | Yes | |
| `i.nfvi.per.cap.001` | No | Yes | No | Internal performance capabilities as per [**Table 3-11**.](chapter03.md/#Table3-11) |
| `i.nfvi.mon.cap.001` | Yes | Yes | Yes | Internal monitoring capabilities as per [**Table 3-12**.](chapter03.md/#Table3-12) |
| `i.nfvi.mon.cap.002` | Yes | Yes | Yes | |
| `i.nfvi.mon.cap.003` | Yes | Yes | Yes | |
| `i.nfvi.mon.cap.004` | Yes | Yes | Yes | |
| `i.nfvi.mon.cap.005` | Yes | No | Yes | |
| `i.nfvi.mon.cap.006` | Yes | No | Yes | |
| `i.nfvi.mon.cap.007` | Yes | No | Yes | |
| `i.nfvi.sec.cap.001` | Yes | Yes | Yes | Internal security capabilities as per [**Table 3-13**.](chapter03.md/#Table3-13) |
| `i.nfvi.sec.cap.002` | No | No | No | |
| `i.nfvi.sec.cap.003` | Yes | No | No | |
| `i.nfvi.sec.cap.004` | Yes | Yes | Yes | |

<p align="center"><b>Table 3-6:</b> Mapping of NFVI capabilities to instance types.</p>
<a name="4.5.2"></a>

### 4.5.2 Instance metrics.

_**Comment:** To be worked on._

<a name="4.6"></a>
## 4.6	One stop shop

<a name="4.6.1"></a>
### 4.6.1	Naming convention
An entry in the infrastructure profile catalogue can be referenced using the following naming convention.

`B/N/C <I opt> . <flavour> . <S ext> . <A ext>`

Whereas:
- **B/N/C**: specifies the instance type (Basic, Network Intensive, and Compute Intensive)
- **\<I opt>**: specifies the interface option of the instant.
- **\<flavour>**: specifies the compute flavour.
- **\<S ext>**: specifies an optional storage extension.
- **\<A ext>**: specifies an optional acceleration extension for either N or H instance types.

<p align="center"><img src="../figures/ch04_one_stop_shop.PNG" alt="one_stop_shop" title="One Stop Shop" width="100%"/></p>
<p align="center"><b>Figure 4-2:</b> Infrastructure Instances catalogue.</p>

