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



