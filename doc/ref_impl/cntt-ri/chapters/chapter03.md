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

Three types of profiles are mentioned in CNTT Reference Model: VNF profile is used to describe in all workloads running on top of NFVI. NFVI SW profile is used to describe the feature provoided by the unified layer of hypervisor and host OS. Finally the NFVI HW profile is used to depict the characteristics of all actual servers on the bottom.

Lots of contents of this chapter is referenced to the CNTT Reference Model, **RM1** will be used to avoid long and duplication title.

<a name="3.2"></a>
## 3.2 VNF profile

Any virtual network functions and/or cloud-native network functions must choose to run on one of the pre-defined of entries in NFVI Infrastructure Profiles Catalogue. As states in [RM1: 4 Infrastructure Capabilities, Measurements and Catalogue: 4.2 Catalogue](https://cntt-n.github.io/CNTT/doc/ref_model/chapters/chapter04.html#4.2), the entry uses the following naming convention.

  B/N/C <I opt> . <Flavour> . <S ext> . <A ext>

B/N/C is used to specify the instance type (Basic, Network Intensive, and Compute Intensive), different instance types are associated with different acceleartion extensions, network characteristics ([RM1: 4.2.4 Instance Types](https://cntt-n.github.io/CNTT/doc/ref_model/chapters/chapter04.html#4.2.4)) and instance capabilities([RM1: 4.2.5 Instance Capabilities Mapping](https://cntt-n.github.io/CNTT/doc/ref_model/chapters/chapter04.html#4.2.5)).

Whereas:

  - <I opt> stands for network interface options, e.g., the range of vNIC Bandwidth of B instance shall be selected from n1 to n60, for C instance is from n10 to n300, for N instance is from n10 to n600. (RM1: 4.2.2 Virtual Network Interface Specifications and Table 4-23: Virtual NIC Interfaces Options)
  - Instance capabilities do not explicitly appear on the naming convention, because some are common to all instance types so they are covered in the <Flavour> (RM1: 4.2.1 Compute Flavours), additionally there are a few capabilities which are bind to certain types, e.g., CPU pinning or NUMA support are only available for N/C instances, while CPU overbooking can only happens B instance but not for N/C. (See RM1: Table 4-24 Mapping of NFVI Capabilities to Instance Types for full mapping details)
  - <S ext> stands for persistent storage extensions, contains the size and the performance settings (RM1: Table 4-20: Storage Extension Options), note the storage extension is common to all instance types as <Flavours>
  - <A ext> stands for accelaration extensions, features like Transcoding and Programmable are associated with C instances (RM1: 4.2.4.3.1 Compute Accleration Extensions), while IPSec and Crypto features only make scene with N instance (RM1: 4.2.4.2.1 Network Acceleration Extensions),

Every VNF instance must declare its profiles explicitly, which can be used by VIM to allocate resources duration instantiation, also it would be useful to evaluate portability of workload.

> OP: an example snippet:

```yaml
vnfname: foo
instancetype: basic
```

<a name="3.3"></a>
## 3.3 NFVI SW profile

[Reference Model: 5.2 NFVI SW profile features and requirements] defines the NFVI software layer. The profile depicts the feature status of the virtual Compute (nfvi.com.cfg.xxx in RM1 Table 5-7: Virtual Compute features and configuration for the 3 types of SW profiles and nfvi.com.acc.cfg.xxx in Table 5-8: Virtual Compute Acceleration features), storage(see nfvi.stg.cfg.xxx in RM1: Table 5-9: Virtual Storage features and configuration for the 3 types of SW profiles and nfvi.stg.acc.cfg.xxx in Table 5-10: Virtual Storage Acceleration features), networking configuration(see nfvi.net.cfg.xxx in Table 5-11 Virtual Networking features and configuration for the 3 types of SW profiles and nfvi.net.acc.cfg.xxx in Table 5-12 Virtual Networking Acceleration features)

This profile is the global settings for the whole NFVI, which means there should be only one node per NFVI resource pool (Basic/Netowrk/Compute)

```yaml
vnfname: foo
instancetype: basic
```

> OP: include RM1: 4.1.6 VIM Resource Allocation and Performance Measurement Capabilities or not

<a name="3.4"></a>
## 3.3 NFVI HW profile

NFVI HW profile (see [RM1: 5.4 NFVI HW profiles features and requirements]) contains all the compute, storage, network specification of the actual servers, which are used to build basic, network, compute resource pools.

- Compuate resources refers to the number of CPU, the number of cores per CPU, NUMA, SMT/HT, GPU etc(RM1: Table 5-13: Minimum Compute resources configuration parameters and Table 5-14 Compute acceleration configuration specifications for details reference name and details)
- Storage Configurations refers to HDD and SSD detail specification, i.e., total number of hard disk drivers and each capacity (RM1: Table 5-15 Storage configuration specification for details)
- Network resources referes to total number of NIC Ports, Port Speed, total number of PCIe slots available, the PCIe speed, lanes and network accleration configurations (RM1: Table 5-16: Minimum NIC configuration specification, Table 5-17 PCIe configuration specification and Table 5-18: Network acceleration configuration specification)

Every servers used in the NFVI must be contain in a machine readable format file, in case the same configuration is applied to many server, a template can be defined and referenced by all of them to aovid content duplication. This input file can be used and consumed by other tools to calculate statistics overview and make NFVI comparsion eaiser.

```yaml
host: host1
pool: basic
compute:
storage:
network:
```
