[<< Back](../)

# 3. NFVI + VNF Target State & Specification
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Introduction](#3.1)
* [3.2 VNF profile](#3.2)
* [3.3 NFVI SW profile](#3.3)
* [3.4 NFVI HW profile](#3.4)

<a name="3.1"></a>
## 3.1 Introduction

Three types of profiles are mentioned in CNTT Reference Model: VNF profile is used to describe every workload running on top of NFVI. NFVI SW profile is used to describe the list of features provided by the hypervisor and host OS. Finally the NFVI HW profile is used to depict the details characteristics of every actual servers on the bottom.

The CNTT Reference Model will be referenced as **RM1** to avoid long and duplicated reference titles.

<a name="3.2"></a>
## 3.2 VNF profile

Any virtual network functions and/or cloud-native network functions must choose to run on one of the pre-defined of entries in NFVI Infrastructure Profiles Catalogue. As states in [RM1: 4 Infrastructure Capabilities, Measurements and Catalogue: 4.2 Catalogue](../../../ref_model/chapters/chapter04.html#4.2), the entry uses the following naming convention.

`B/N/C <I opt> . <Flavour> . <S ext> . <A ext>`

B/N/C is used to specify the instance type (Basic, Network Intensive, and Compute Intensive), different instance types are associated with different acceleartion extensions, network characteristics ([RM1: 4.2.4 Instance Types](../../../ref_model/chapters/chapter04.html#4.2.4)) and instance capabilities([RM1: 4.2.5 Instance Capabilities Mapping](../../../ref_model/chapters/chapter04.html#4.2.5)).

Whereas:

  - `<I opt>` stands for network interface options, e.g., the range of vNIC Bandwidth of B instance shall be selected from n1 to n60, for C instance is from n10 to n300, for N instance is from n10 to n600. (RM1: 4.2.2 Virtual Network Interface Specifications and Table 4-23: Virtual NIC Interfaces Options)
  - Instance capabilities do not explicitly appear on the naming convention, because some are common to all instance types so they are covered in the `<Flavour>` (RM1: 4.2.1 Compute Flavours), additionally there are a few capabilities which are bind to certain types, e.g., CPU pinning or NUMA support are only available for N/C instances, while CPU overbooking can only happens B instance but not for N/C. (See RM1: Table 4-24 Mapping of NFVI Capabilities to Instance Types for full mapping details)
  - `<S ext>` stands for persistent storage extensions, contains the size and the performance settings (RM1: Table 4-20: Storage Extension Options), note the storage extension is common to all instance types as <Flavours>
  - `<A ext>` stands for accelaration extensions, features like Transcoding and Programmable are associated with C instances (RM1: 4.2.4.3.1 Compute Accleration Extensions), while IPSec and Crypto features only make scene with N instance (RM1: 4.2.4.2.1 Network Acceleration Extensions),

Every VNF instance must declare its profiles explicitly, which can be used by VIM to allocate resources duration instantiation, also it would be useful to evaluate portability of workload.

|.conf | Basic | Network Intensive | Compute Intensive |
|------|-------|-------------------|-------------------|
|n1, n2, n3, n4, n5, n6 | Y | N | N |
|n10, n20, n30, n40, n50, n60 | Y | Y | Y |
|n25, n50, n75, n100, n125, n150 | N | Y | Y |
|n50, n100, n150, n200, n250, n300 | N | Y | Y |
|n100, n200, n300, n400, n500, n600 | N | Y | N |
|CPU pinning support | N | Y | Y |
|NUMA support | N | Y | Y |
|IPSec Acceleration) | N | Y | N |
|Crypto Acceleration | N | Y | N |
|Transcoding Acceleration | N | N | Y |
|Programmable Acceleration | N | N | Y |
|Enhanced Cache Management | E | E | X |
|Monitoring of L2-7 data | N | Y | N |
|CPU overbooking | 1:4 | 1:1 | 1:1 |
|vNIC QoS | N | Y | Y |
|Huge page support | N | Y | Y |
|Host CPU usage | Y | Y | Y |
|Virtual compute CPU usage | Y | Y | Y |
|Host CPU utilization | Y | Y | Y |
|Virtual compute CPU utilization | Y | Y | Y |
|External storage capacity | N | N | Y |

> Open Point 1: Does ONAP have some relevant spec or VNF declaration schema so that CNTT can re-use/revise to cover what we need ? Or define a new one ?

> Open Point 2: What principles should be followed if some the pre-define VNF profile items does not match what actual requires ? How to adjust, "ceiling", "floor", "customerize" ?

> Open Point 3: Is it relevant/necessary to include NFVI SW/HW profile description file as following sections ?

<a name="3.3"></a>
## 3.3 NFVI SW profile

[RM1: 5.2 NFVI SW profile features and requirements](../../../ref_model/chapters/chapter05.html#5.2) defines the NFVI software layer. The profile depicts the feature status of the
  - virtual Compute (**nfvi.com.cfg.xxx** in RM1 Table 5-7: Virtual Compute features and configuration for the 3 types of SW profiles and **nfvi.com.acc.cfg.xxx** in Table 5-8: Virtual Compute Acceleration features),
  - storage (**nfvi.stg.cfg.xxx** in RM1: Table 5-9: Virtual Storage features and configuration for the 3 types of SW profiles and **nfvi.stg.acc.cfg.xxx** in Table 5-10: Virtual Storage Acceleration features)
  - networking configuration(see **nfvi.net.cfg.xxx** in Table 5-11 Virtual Networking features and configuration for the 3 types of SW profiles and **nfvi.net.acc.cfg.xxx** in Table 5-12 Virtual Networking Acceleration features)

This profile is the global settings for the whole NFVI, which means there should be only one entry per NFVI resource pool, i.e., Basic/Network/Compute

| .conf | Basic | Network Intensive | Compute Intensive |
|-------|----------------|----------------|----------------|
| CPU allocation ratio  | 4:1 | 1:1  | 1:1 |
| NUMA awareness | N | Y | Y |
| CPU pinning capability | N | Y | Y |
| Huge Pages | N | Y | Y |
| Catalogue storage Types | Y  | Y  | Y |
| Storage Block | Y | Y |Y  |
| Storage Object | Y | Y | Y |
| Storage with replication | N | Y | Y |
| Storage with encryption | Y | Y | Y |
| Storage IOPS oriented | N | Y | Y |
| Storage capacity oriented | N | N | Y |
| vNIC interface | virtio1.1 |  virtio1.1, i40evf (Intel driver for VF SR-IOV) |  virtio1.1, i40evf (Intel driver for VF SR-IOV) |
| Overlay protocol | VXLAN, MPLSoUDP, GENEVE, other |  VXLAN, MPLSoUDP, GENEVE, other |VXLAN, MPLSoUDP, GENEVE, other |
| NAT | Y | Y | Y |
| Security Group | Y | Y | Y |
| SFC support | N | Y | Y |
| Traffic patterns symmetry | Y | Y | Y |
| vSwitch optimisation | N | Y, DPDK | Y, DPDK |
| Support of HW offload | N | Y, support of SR-IOV and  SmartNic |Y, support of SR-IOV and  SmartNic |
| Crypto acceleration | N  | Y | Y |
| Crypto Acceleration Interface | N  | Y | Y |

<a name="3.4"></a>
## 3.3 NFVI HW profile

NFVI HW profile (see [RM1: 5.4 NFVI HW profiles features and requirements](../../../ref_model/chapters/chapter05.html#5.4)) contains all the compute, storage, network specification of the actual servers, which are used to build basic, network, compute resource pools.

  - Compute resources refers to the number of CPU, the number of cores per CPU, NUMA, SMT/HT, GPU etc(RM1: Table 5-13: Minimum Compute resources configuration parameters and Table 5-14 Compute acceleration configuration specifications for details reference name and details)
  - Storage Configurations refers to HDD and SSD detail specification, i.e., total number of hard disk drivers and each capacity (RM1: Table 5-15 Storage configuration specification for details)
  - Network resources referes to total number of NIC Ports, Port Speed, total number of PCIe slots available, the PCIe speed, lanes and network accleration configurations (RM1: Table 5-16: Minimum NIC configuration specification, Table 5-17 PCIe configuration specification and Table 5-18: Network acceleration configuration specification)

| .conf | Basic | Network Intensive | Compute Intensive |
|-------|-------|-------------------|-------------------|
| Number of CPU (Sockets) | 2| 2| 2 |
| Number of Cores per CPU | 20 | 20 | 20 |
| NUMA | N | Y | Y |
| Simultaneous Multithreading/Hyperthreading (SMT/HT) | Y | Y| Y |
| GPU | N | N | Y |
| Local Storage HDD |  |  |  |
| Local Storage SSD | Recommended | Recommended |Recommended |
| NIC Ports | 4 | 4 | 4 |
| Port Speed | 10 | 25 | 25 |
| PCIe slots | 8 | 8 | 8 |
| PCIe speed | Gen 3 | Gen 3 | Gen 3 |
| Bonded VLAN ports | Y | Y | Y |
| IPSec, Crypto |  N | Optional | Optional |
| SmartNIC | N | Optional  | Optional |
| Compression |  |  |  |
