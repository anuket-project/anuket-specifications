[<< Back](../../ref_model)
# 4	Catalogue
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

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
* [4.5 One stop shop.](#4.5)
  * [4.5.1 Naming convention.](#4.5.1)

Infrastructure exposes sets of capabilities, metrics, compute flavours, interface options, storage extensions, and acceleration capabilities to VNFs. Those sets are offered to VNFs in form of instance types with their corresponding options and extensions.

The idea of the infrastructure profiles catalogue is to have a predefined set of instance types with a predefined set of compute flavours (sometimes referred to as T-shirt sizes) which VNF vendors use to build their VNFs. Each VNF uses one or more of those compute flavours (with one or more of offered instance types) to build its overall functionality as illustrated in **Figure 4-1**.

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
n10, n10D, n10T, n10Q, n10P, n10H	|1x 10, 2x 10, 3x 10, 4x 10, 5x 10, 6x 10 Gbps
n25, n25D, n25T, n25Q, n25P, n25H	|1x 25, 2x 25, 3x 25, 4x 25, 5x 25, 6x 25 Gbps
n50, n50D, n50T, n50Q, n50P, n50H	|1x 50, 2x 50, 36x 50, 4x 50, 5x 50, 6x 50 Gbps

<p align="center"><b>Table 4-3:</b> Virtual Network Interface Specification Examples.</p>

<a name="4.3"></a>
##  4.3 Storage Extensions
Multiplee non-ephemeral storage volumes can be attached to virtual computes (*replace with decided term*) for persistent data storage. Each of those volumes can be configured with the required performance catagories (*storage performance prfiles*).

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
## 4.4.1	B Instances (Basic)
This is the basic type of infrastructure profiles and is intended to be used for both IT workloads as well as NFV workloads. It has limited IO capabilities (up to 10Gbps Network interface) with a wide range of compute flavours. This instance type is intended to be available in any data centre within any Operator’s network.

B instance comes with various Interfaces options, Table **Table 4-6** below shows the various Interfaces options available for B instance type (Up to 6 interfaces are possible). 


| Virtual interface option* | Type | Description |
|---------------------------|------------|---------------------------------|
| 1 | virtio-net | 1x 1Gbps network interface |
| 1D | virtio-net | 2x 1Gbps network interface |
| 1T* | virtio-net | 3x 1Gbps network interface |
| 1Q, 1P, 1H* | virtio-net | 4x 1Gbps, 5x 1Gbps, 6x 1Gbps |
| 10 | virtio-net | 1x 10Gbps network |
| 10D | virtio-net | 2x 10Gbps network |
| 10T* | virtio-net | 3x 10Gbps network |
| 10Q, 10P, 10H* | virtio-net | 4x 10Gbps, 5x 10Gbps, 6x 10Gbps |

<p align="center"><b>Table 4-6:</b> Virtual NIC interfaces options for B instance type.</p>

> _*These options are intended to be used for transitional purposes. VNFs are expected to use minimum number of interfaces and adopt micro-servers design principles._

<a name="4.4.2"></a>
#### 4.4.2	N Instances (Network Intensive)
This instance type is intended to be used for those applications that has high network throughput requirements (up to 50Gbps). This instance type is more intended for VNFs and is expected to be available in regional (distributed) data centres and more towards the access networks.

N instance comes with various interfaces options, the Table below shows the various Interfaces options available for N instance types (Up to 6 interfaces are possible).

| Virtual interface option* | Type | Description |
|---------------------------|------------|---------------------------------|
| 10 | virtio-net | 1x 10Gbps network |
| 10D | virtio-net | 2x 10Gbps network |
| 10T* | virtio-net | 3x 10Gbps network |
| 10Q, 10P, 10H* | virtio-net | 4x 10Gbps, 5x 10Gbps, 6x 10Gbps |
| 25 | virtio-net | 1x 25Gbps network |
| 25D | virtio-net | 2x 25Gbps network |
| 25T* | virtio-net | 3x 25Gbps network |
| 25Q, 25P, 25H* | virtio-net | 4x 25Gbps, 5x 25Gbps, 6x 25Gbps |
| 40 | virtio-net | 1x 40Gbps network |
| 40D | virtio-net | 2x 40Gbps network |
| 40T* | virtio-net | 3x 40Gbps network |
| 40Q, 40P, 40H* | virtio-net | 4x 40Gbps, 5x 40Gbps, 6x 40Gbps |
| 50 | virtio-net | 1x 50Gbps network |
| 50D | virtio-net | 2x 50Gbps network |
| 50T* | virtio-net | 3x 50Gbps network |
| 50Q, 50P, 50H* | virtio-net | 4x 50Gbps, 5x 50Gbps, 6x 50Gbps |
| 100 | virtio-net | 1x 100Gbps network |
| 100D | virtio-net | 2x 100Gbps network |
| 100T* | virtio-net | 3x 100Gbps network |
| 100Q, 100P, 100H* | virtio-net | 4x 100Gbps, 5x 100Gbps, 6x 100Gbps |

<p align="center"><b>Table 4-7:</b> Virtual NIC interfaces options for N instance type.</p>

> _*These options are intended to be used for transitional purposes. VNFs are expected to use minimum number of interfaces and adopt micro-servers design principles._

#### 4.4.2.1	Network Acceleration Extensions
N instance types can come with Network Acceleration extensions to assist VNFs offloading some of their network intensive operations to hardware. The list below is preliminary and is expected to grow as more network acceleration resources are developed and standardized. Those interfaces are aligned with ETSI NFV IFA 002 [4].

| .conf | Interface type | Description |
|------------|----------------|-----------------------------------------|
| .il-ipsec | virtio-ipsec* | In-line IPSec acceleration |
| .la-crypto | virtio-crypto | Look-Aside encryption/decryption engine |

<p align="center"><b>Table 4-8:</b> Acceleration extensions for N instance type.</p>

> _*Need to work with relevant open source communities to create missing interfaces._

<a name="4.4.3"></a>
### 4.4.3	C Instances (Compute Intensive)
This instance type is intended to be used for those applications that has high compute requirements and can take advantage of acceleration technologies such as GPU, FPGA, etc. This instance type is intended to be available in local data centers and more towards the Edge of the network.
H instance comes with various Interfaces options, the table below shows the various interfaces options available for C instance type (Up to 6 interfaces are possible). 

| Virtual interface option* | Type | Description |
|---------------------------|------------|---------------------------------|
| 10 | virtio-net | 1x 10Gbps network |
| 10D | virtio-net | 2x 10Gbps network |
| 10T* | virtio-net | 3x 10Gbps network |
| 10Q, 10P, 10H* | virtio-net | 4x 10Gbps, 5x 10Gbps, 6x 10Gbps |
| 25 | virtio-net | 1x 25Gbps network |
| 25D | virtio-net | 2x 25Gbps network |
| 25T* | virtio-net | 3x 25Gbps network |
| 25Q, 25P, 25H* | virtio-net | 4x 25Gbps, 5x 25Gbps, 6x 25Gbps |
| 40 | virtio-net | 1x 40Gbps network |
| 40D | virtio-net | 2x 40Gbps network |
| 40T* | virtio-net | 3x 40Gbps network |
| 40Q, 40P, 40H* | virtio-net | 4x 40Gbps, 5x 40Gbps, 6x 40Gbps |
| 50 | virtio-net | 1x 50Gbps network |
| 50D | virtio-net | 2x 50Gbps network |
| 50T* | virtio-net | 3x 50Gbps network |
| 50Q, 50P, 50H* | virtio-net | 4x 50Gbps, 5x 50Gbps, 6x 50Gbps |

<p align="center"><b>Table 4-9:</b> Virtual NIC interfaces options for C instance type.</p>

> _*These options are intended to be used for transitional purposes. VNFs are expected to use minimum number of interfaces and adopt micro-servers design principles._

### 4.4.3.1	Compute acceleration extensions
C instance types can come with compute acceleration extensions to assist VNF/applications offloading some of their compute intensive operations to hardware. The list below is preliminary and is expected to grow as more compute acceleration resources are developed and standardized.

| .conf | Interface type | Description |
|------------|----------------|-----------------------------------------|
| .la-trans | virtio-trans* | Look-Aside Transcoding acceleration |
| .la-programmable | virtio-programmable | Look-Aside programmable acceleration |

<p align="center"><b>Table 4-10:</b> Acceleration extensions for C instance type.</p>

> _*Need to work with relevant open source communities to create missing interfaces._

<a name="4.5"></a>
## 4.5	One stop shop

<a name="4.5.1"></a>
### 4.5.1	Naming convention
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

