[<< Back](../../ref_model)
# 4	Catalogue
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 VNFs collateral (Sample).](#4.1)
* [4.2 Analysis of requirements.](#4.1)
* [4.3 NFVI Profiles.](#4.1)

Infrastructure profiles are collection of capabilities, metrics, compute flavours, interface options, storage extensions, and acceleration capabilities that are offered by the infrastructure to VNFs. Infrastructure profiles are offered to VNFs in form of instance types with their corresponding options and extensions.

The idea of the infrastructure profiles catalogue is to have a predefined set of instance types with a predefined set of compute flavours (sometimes referred to as T-shirt sizes) which VNF vendors use to build their VNFs. Each VNF uses one or more of those compute flavours (with one or more of offered instance types) to build its overall functionality as illustrated in **Figure 4-1**.

<p align="center"><img src="../figures/ch04_vnf_design.PNG" alt="vnf_design" title="VNF Design" width="65%"/></p>
<p align="center"><b>Figure 4-1:</b> VNFs built against standard instance types and compute flavours.</p>

<a name="4.1"></a>
## 4.1 Compute flavours
Compute flavours defines the compute, memory, storage capacity, and management network interface of an instance. The intent of this list is to be comprehensive and yet effective to cover both IT and NFV workloads.

| .conf | vCPU | RAM | Local Disk | Management Interface |
|-----------|------|-------|------------|----------------------|
| .tiny | 1 | 512MB | 1GB | 1Gbps |
| .small | 1 | 2GB | 40GB | 1Gbps |
| .meduim | 2 | 4GB | 40GB | 1Gbps |
| .large | 4 | 8GB | 80GB | 1Gbps |
| .large2* | 4 | 16GB | 80GB | 1Gbps |
| .xlarge* | 8 | 16GB | 160GB | 1Gbps |
| .xlarge2* | 8 | 32GB | 160GB | 1Gbps |
| .xlarge3* | 8 | 64GB | 160GB | 1Gbps |

<p align="center"><b>Table 4-1:</b> Compute flavours.</p>

> _*These compute flavours are intended to be used for transitional purposes and VNF vendors are expected to consume smaller flavours and adopt micro server’s designs for their VNFs_

### 4.1.1 Storage extensions
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

<p align="center"><b>Table 4-2:</b> Storage extensions for compute flavours.</p>

## 4.2 Instance types
## 4.2.1	B Instances (Basic)
This is the basic type of infrastructure profiles and is intended to be used for both IT workloads as well as NFV workloads. It has limited IO capabilities (up to 10Gbps Network interface) with a wide range of compute flavours. This instance type is intended to be available in any data centre within any Operator’s network.

B instance comes with various Interfaces options, Table **Table 4-3** below shows the various Interfaces options available for B instance type (Up to 6 interfaces are possible). 


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

<p align="center"><b>Table 4-3:</b> Virtual NIC interfaces options for B instance type.</p>

> _*These options are intended to be used for transitional purposes. VNFs are expected to use minimum number of interfaces and adopt micro-servers design principles._

#### 4.2.2	N Instances (Network Intensive)
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

<p align="center"><b>Table 4-4:</b> Virtual NIC interfaces options for N instance type.</p>

> _*These options are intended to be used for transitional purposes. VNFs are expected to use minimum number of interfaces and adopt micro-servers design principles._

#### 4.2.2.1	Network Acceleration Extensions
N instance types can come with Network Acceleration extensions to assist VNFs offloading some of their network intensive operations to hardware. The list below is preliminary and is expected to grow as more network acceleration resources are developed and standardized. Those interfaces are aligned with ETSI NFV IFA 002 [4].

| .conf | Interface type | Description |
|------------|----------------|-----------------------------------------|
| .il-ipsec | virtio-ipsec* | In-line IPSec acceleration |
| .la-crypto | virtio-crypto | Look-Aside encryption/decryption engine |

<p align="center"><b>Table 4-5:</b> Acceleration extensions for N instance type.</p>

> _*Need to work with relevant open source communities to create missing interfaces._

### 4.2.3	C Instances (Compute Intensive)
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

<p align="center"><b>Table 4-5:</b> Virtual NIC interfaces options for C instance type.</p>

> _*These options are intended to be used for transitional purposes. VNFs are expected to use minimum number of interfaces and adopt micro-servers design principles._

### 4.2.3.1	Compute acceleration extensions
C instance types can come with compute acceleration extensions to assist VNF/applications offloading some of their compute intensive operations to hardware. The list below is preliminary and is expected to grow as more compute acceleration resources are developed and standardized.

| .conf | Interface type | Description |
|------------|----------------|-----------------------------------------|
| .la-trans | virtio-trans* | Look-Aside Transcoding acceleration |
| .la-programmable | virtio-programmable | Look-Aside programmable acceleration |

<p align="center"><b>Table 4-6:</b> Acceleration extensions for C instance type.</p>

> _*Need to work with relevant open source communities to create missing interfaces._

## 4.3	One stop shop
### 4.3.1	Naming convention
An entry in the infrastructure profile catalogue can be referenced using the following naming convention.



Whereas:
- **B/N/C**: specifies the instance type (Basic, Network Intensive, and Compute Intensive)
- **\<I opt>**: specifies the interface option of the instant.
- **\<flavour>**: specifies the compute flavour.
- **\<S ext>**: specifies an optional storage extension.
- **\<A ext>**: specifies an optional acceleration extension for either N or H instance types.


