[<< Back](../../ref_model)
# 5 Feature set and Requirements from Infrastructure

## Table of Contents
* [5.1 Cloud Infrastructure Software Profile description.](#5.1)
  * [5.1.1 Virtual Compute.](#5.1.1)
  * [5.1.2 Virtual Storage.](#5.1.2)
  * [5.1.3 Virtual Networking.](#5.1.3)
  * [5.1.4 Security.](#5.1.4)
  * [5.1.5 Platform Services](#5.1.5)
* [5.2 Cloud Infrastructure Software Profiles features and requirements.](#5.2)
  * [5.2.1 Virtual Compute.](#5.2.1)
  * [5.2.2 Virtual Storage.](#5.2.2)
  * [5.2.3 Virtual Networking.](#5.2.3)
* [5.3 Cloud Infrastructure Hardware Profile description.](#5.3)
* [5.4 Cloud Infrastructure Hardware Profiles features and requirements.](#5.4)
  * [5.4.1 Compute Resources.](#5.4.1)
  * [5.4.2 Storage Resources.](#5.4.2)
  * [5.4.3 Network Resources.](#5.4.3)


A profile [RM Section 2.4](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter02.md#24-profiles--flavours) specifies the configuration of a cloud infrastructure node (host or server); [profile extensions](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter02.md#242-profile-extensions-specialisations) may specify additional configuration. Workloads utilise profiles to describe the configuration of nodes on which they can be hosted to execute on. Workload Flavours provide a mechanism to specify the VM or Pod sizing information to host the workload.  Depending on the requirements of the workloads, a VM or a Pod will be deployed as per the specified Flavour information on a node configured as per the specified Profile. Not only do the nodes (the hardware) have to be configured but some of the capabilities also need to be configured in the software layers (such as Operating System and Virtualisation Software). Thus, a Profile can be defined in terms of configuration needed in the software layers, the Cloud Infrastructure Software Profile, and the hardware, the Cloud Infrastructure Hardware Profile.

<a name="5.1"></a>
## 5.1 Cloud Infrastructure Software profile description

Cloud Infrastructure Software layer is composed of 2 layers, **Figure 5-1**:
- The virtualisation Infrastructure layer, which is based on hypervisor virtualisation technology or container-based virtualisation technology. Container virtualisation can be nested in hypervisor-based virtualisation
- The host OS layer

<p align="center"><img src="../figures/ch05-cloud-infrastructure-sw-profile-layers.png" alt="ref_profiles" title="Layers of Software Profile" width="40%"/></p>
<p align="center"><b>Figure 5-1:</b> Cloud Infrastructure software layers</p>

| Ref | Cloud Infratsructure Software | Type | Definition/Notes | Capabilities Reference<sup1</sup> |
|-----|-------------------------------|------|------------------|-----------------------------------|
| infra.sw.001 | Host Operating System |	<value> |	Values such as Ubuntu20.04, Windows 10 Release #, etc. | `e.cap.021` |
| infra.sw.001 | Virtualisation Infrastructure Layer |	<value> |	Values such as KVM, Hyper-V, Kubernetes, etc. | `e.cap.022` |
><sup>1</sup> Reference to the capabilities defined in [Chapter 4](./chapter04.md).

For a host (compute node or physical server), the virtualisation layer is an abstraction layer between hardware components (compute, storage, and network resources) and virtual resources allocated to a VM or a Pod. **Figure 5-2** represents the virtual resources (virtual compute, virtual network, and virtual storage) allocated to a VM or a Pod and managed by the Cloud Infrastructure Manager.

<p align="center"><img src="../figures/ch05_b_ref_profile.png" alt="b_ref_profile" title="Reference Profile" width="70%"/></p>
<p align="center"><b>Figure 5-2:</b> Cloud Infrastructure Virtual resources</p>

A Cloud Infrastructure Software Profile is a set of features, capabilities, and metrics offered by a Cloud Infrastructure software layer and configured in the software layers (the Operating System (OS) and the visrtualisation software (such as hypervisor)). **Figure 5-3** depicts a high level view of the Basic and High Performance Cloud Infrastructure Profiles.

<p align="center"><img src="../figures/RM-ch05-sw-profile.png" alt="ref_sw_profiles" title="Reference Software Profiles" width="60%"/></p>
<p align="center"><b>Figure 5-3:</b> Cloud Infrastructure Software Profiles</p>


The following sections detail the Cloud Infrastructure Software Profile capabilities per type of virtual resource.

<a name="5.1.1"></a>
### 5.1.1 Virtual Compute

**Table 5-1** and **Table 5-2** depict the features related to virtual compute.

| Reference         | Feature                | Type   | Description | Capabilities Reference |
|-------------------|--------------|--------|--------------------|---------|
| infra.com.cfg.001 | CPU allocation ratio | Value  | Number of virtual cores per physical core. | `i.cap.016` |
| infra.com.cfg.002 | NUMA alignment | Yes/No | Support of NUMA at the Host OS and virtualisation layers, in addition to hardware. | `e.cap.007` |
| infra.com.cfg.003 | CPU pinning | Yes/No | Binds a vCPU to a physical core or SMT thread. Configured in OS and virtualisation layers.| `e.cap.006` |
| infra.com.cfg.004 | Huge Pages | Yes/No | Ability to manage huge pages of memory. Configured in OS and virtualisation layers. | `i.cap.018` |
| infra.com.cfg.004 | Simultaneous Multithreading (SMT) | Yes/No | Allows multiple execution threads to be executed on a single physical CPU core. Configured in OS, in addition ot the hardware. | `e.cap.018` |


<p align="center"><b>Table 5-1:</b> Virtual Compute features.</p>

| Reference        | Feature | Type  | Description | Capabilities Reference |
|-------------|----------------|----------------|-----------------------|---------
| infra.com.acc.cfg.001 |	IPSec Acceleration |	Yes/No |	IPSec Acceleration | `e.cap.008` |
| infra.com.acc.cfg.002 |	Transcoding Acceleration |	Yes/No |	Transcoding Acceleration | `e.cap.010 	` |
| infra.com.acc.cfg.003 |	Programmable Acceleration |	Yes/No |	Programmable Acceleration | `e.cap.011` |
| infra.com.acc.cfg.004 |	GPU |	Yes/No |	Hardware coprocessor. | `e.cap.014` |
| infra.com.acc.cfg.005 |	FPGA/other Acceleration H/W |	Yes/No |	Non-specific hardware. These Capabilities generally require hardware-dependent drivers be injected into workloads. | `e.cap.016` |
  
<p align="center"><b>Table 5-2:</b> Virtual Compute Acceleration features.</p>

<a name="5.1.2"></a>
### 5.1.2 Virtual Storage

**Table 5-3** and **Table 5-4** depict the features related to virtual storage.

| Reference        | Feature | Type  | Description |
|------------------|----------------|----------------|---------------|
| infra.stg.cfg.001 | Catalogue Storage Types  | Yes/No   | Support of Storage types described in the catalogue |
| infra.stg.cfg.002 | Storage Block            | Yes/No   | |
| infra.stg.cfg.003 | Storage with replication | Yes/No   | |
| infra.stg.cfg.004 | Storage with encryption  | Yes/No   | |

<p align="center"><b>Table 5-3:</b> Virtual Storage features.</p>

| Reference             | Feature                   | Type   | Description |
|-----------------------|---------------------------|--------|-------------|
| infra.stg.acc.cfg.001 | Storage IOPS oriented     | Yes/No |             |
| infra.stg.acc.cfg.002 | Storage capacity oriented | Yes/No |             |

<p align="center"><b>Table 5-4:</b> Virtual Storage Acceleration features.</p>

<a name="5.1.3"></a>
### 5.1.3 Virtual Networking

**Table 5-5** and **Table 5-6** depict the features related to virtual networking.

| Reference        | Feature                   | Type              | Description  |
|------------------|---------------------------|-------------------|--------------|
| infra.net.cfg.001 | Connection Point interface | IO virtualisation | e.g. virtio1.1 |
| infra.net.cfg.002 | Overlay protocol          | Protocols         | The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric. |
| infra.net.cfg.003 | NAT                       | Yes/No            | Support of Network Address Translation |
| infra.net.cfg.004 | Security Groups           | Yes/No            | Set of rules managing incoming and outgoing network traffic |
| infra.net.cfg.005 | Service Function Chaining | Yes/No            | Support of Service Function Chaining (SFC) |
| infra.net.cfg.006 | Traffic patterns symmetry | Yes/No            | Traffic patterns should be optimal, in terms of packet flow. North-south traffic shall not be concentrated in specific elements in the architecture, making those critical choke-points, unless strictly necessary (i.e. when NAT 1:many is required). |

<p align="center"><b>Table 5-5:</b> Virtual Networking features.</p>

| Reference             | Feature                       | Type                       | Description    | Capabilities Reference |
|-----------------------|-------------------------------|----------------------------|----------------|------------------------|
| infra.net.acc.cfg.001 | vSwitch optimisation          | Yes/No and SW Optimisation | e.g. DPDK.     | `e.cap.019` |
| infra.net.acc.cfg.002 | SmartNIC (for HW Offload)     | Yes/No                     | HW Offload     | `e.cap.015` |
| infra.net.acc.cfg.003 | Crypto acceleration           | Yes/No                     |                | `e.cap.009` |
| infra.net.acc.cfg.004 | Crypto Acceleration Interface | Yes/No                     |                |             |

<p align="center"><b>Table 5-6:</b> Virtual Networking Acceleration features.</p>

<a name="5.1.4"></a>
### 5.1.4 Security
See Chapter 7 Security.

<a name="5.1.5"></a>
### 5.1.5 Platform Services

This section details the services that may be made available to workloads by the Cloud Infrastructure.  

| Reference         | Feature        | Type   | Description                                |
|-------------------|----------------|--------|--------------------------------------------|
| infra.svc.stg.001 | Object Storage | Yes/No | Object Storage Service (e.g S3-compatible) |

<p align="center"><b>Table 5-7:</b> Cloud Infrastructure Platform services.</p>

| Minimum requirements  | Example       |
|-----------------------|---------------|
| Database as a service | Cassandra     |
| Queue                 | Rabbit MQ     |
| LB and HA Proxy       | NGINX, Istio  |
| Security & Compliance | Calico        |
| Monitoring            | Prometheus    |
| Logging and Analysis  | ELK<sup*></sup> Stack |
> <sup*></sup> ELK: Elasticsearch, Logstash, and Kibana

<p align="center"><b>Table 5-7a:</b> Service examples.</p>

<a name="5.2"></a>
## 5.2 Cloud Infrastructure Software Profiles features and requirements

This section will detail Cloud Infrastructure Software Profiles and associated configurations for the 2 types of Cloud Infrastructure Profiles: Basic and Network intensive.

<a name="5.2.1"></a>
### 5.2.1 Virtual Compute

**Table 5-8** depicts the features and configurations related to virtual compute for the two (2) Cloud Infrastructure Profiles.

| Reference         | Feature                | Type   | Basic | High Performance  | Notes |
|-------------------|------------------------|--------|-------|-------------------|-------|
| infra.com.cfg.001 | CPU allocation ratio   | value  | N:1   | 1:1               |       |
| infra.com.cfg.002 | NUMA alignment         | Yes/No | N     | Y                 |       |
| infra.com.cfg.003 | CPU pinning            | Yes/No | N     | Y                 |       |
| infra.com.cfg.004 | Huge Pages             | Yes/No | N     | Y                 |       |
| infra.com.cfg.004 | Simultaneous Multithreading (SMT) | Yes/No | N  | Y         |       |

<p align="center"><b>Table 5-8:</b> Virtual Compute features and configuration for the 2 types of Cloud Infrastructure Profiles.</p>


**Table 5-9** lists the features related to compute acceleration for the High Performance profile. The table also lists the applicable [Profile-Extensions](./chapter04.md#423-profile-extensions) and Extra Specs that may need to be specified.

| Reference             | Feature                            | Type | Profile-Extensions | Profile Extra Specs |
|-----------------------|------------------------------------|------|-------|-------------------|
| infra.com.acc.cfg.001 | IPSec Acceleration | Yes/No | Compute Intensive GPU | |
| infra.com.acc.cfg.002 | Transcoding Acceleration | Yes/No | Compute Intensive GPU | Video Transcoding |
| infra.com.acc.cfg.003 | Programmable Acceleration | Yes/No |	Firmware-programmable adapter | Accelerator |
| infra.com.acc.cfg.004 | GPU | Yes/No | Compute Intensive GPU | |
| infra.com.acc.cfg.005 | FPGA/other Acceleration H/W | Yes/No | Firmware-programmable adapter | |

<p align="center"><b>Table 5-9:</b> Virtual Compute Acceleration features.</p>

<a name="5.2.2"></a>
### 5.2.2 Virtual Storage

**Table 5-10** and **Table 5-11** depict the features and configurations related to virtual storage for the two (2) Cloud Infrastructure Profiles.

| Reference         | Feature                  | Type   | Basic | High Performance  |
|-------------------|--------------------------|--------|-------|-------------------|
| infra.stg.cfg.001 | Catalogue storage Types  | Yes/No | Y     | Y                 |
| infra.stg.cfg.002 | Storage Block            | Yes/No | Y     | Y                 |
| infra.stg.cfg.003 | Storage with replication | Yes/No | N     | Y                 |
| infra.stg.cfg.004 | Storage with encryption  | Yes/No | Y     | Y                 |

<p align="center"><b>Table 5-10:</b> Virtual Storage features and configuration for the two (2) profiles.</p>

**Table 5-11** depicts the features related to Virtual storage Acceleration

| Reference             | Feature                   | Type   | Basic | High Performance  |
|-----------------------|---------------------------|--------|-------|-------------------|
| infra.stg.acc.cfg.001 | Storage IOPS oriented     | Yes/No | N     | Y                 |
| infra.stg.acc.cfg.002 | Storage capacity oriented | Yes/No | N     | N                 |

<p align="center"><b>Table 5-11:</b> Virtual Storage Acceleration features.</p>

<a name="5.2.3"></a>
### 5.2.3 Virtual Networking

**Table 5-12** and **Table 5-13** depict the features and configurations related to virtual networking for the 2 types of Cloud Infrastructure Profiles.

| Reference         | Feature                   | Type              | Basic                           | High Performance |
|-------------------|-----------------------------|-------------------|-------------------------------|-------------------|
| infra.net.cfg.001 | Connection Point interface | IO virtualisation | virtio1.1                     | virtio1.1*        |
| infra.net.cfg.002 | Overlay protocol          | Protocols         | VXLAN, MPLSoUDP, GENEVE, other | VXLAN, MPLSoUDP, GENEVE, other |
| infra.net.cfg.003 | NAT                       | Yes/No            | Y                              | Y                 |
| infra.net.cfg.004 | Security Group            | Yes/No            | Y                              | Y                 |
| infra.net.cfg.005 | Service Function Chaining | Yes/No            | N                              | Y                 |
| infra.net.cfg.006 | Traffic patterns symmetry | Yes/No            | Y                              | Y                 |

<p align="center"><b>Table 5-12:</b> Virtual Networking features and configuration for the 2 types of SW profiles.</p>

> **Note:** * might have other interfaces (such as SR-IOV VFs to be directly passed to a VM or a Pod) or NIC-specific drivers on guest machines transiently allowed until mature enough solutions are available with a similar efficiency level (for example regarding CPU and energy consumption).

| Reference             | Feature                       | Type                       | Basic | High Performance       |
|-----------------------|-------------------------------|----------------------------|-------|------------------------|
| infra.net.acc.cfg.001 | vSwitch optimisation          | Yes/No and SW Optimisation | N     | Y, DPDK                |
| infra.net.acc.cfg.002 | SmartNIC (for HW Offload)     | Yes/No                     | N     | Optional               |
| infra.net.acc.cfg.003 | Crypto acceleration           | Yes/No                     | N     | Optional               |
| infra.net.acc.cfg.004 | Crypto Acceleration Interface | Yes/No                     | N     | Optional               |

<p align="center"><b>Table 5-13:</b> Virtual Networking Acceleration features.</p>

<a name="5.3"></a>
## 5.3 Cloud Infrastructure Hardware Profile description

The support of a variety of different workload types, each with different (sometimes conflicting) compute, storage, and network characteristics, including accelerations and optimizations, drives the need to aggregate these characteristics as a hardware (host) profile and capabilities. A host profile is essentially a “personality” assigned to a compute host (also known as physical server, compute host, host, node, or pServer). The host profiles and related capabilities consist of the intrinsic compute host capabilities (such as number of CPU sockets, number of cores per CPU, RAM, local disks and their capacity, etc.), and capabilities enabled in hardware/BIOS, specialised hardware (such as accelerators), the underlay networking, and storage.

This chapter defines a simplified host, profile and related capabilities model associated with each of the different Cloud Infrastructure Hardware Profile and related capabilities; the [two profiles](./chapter02.md#241-node-profiles-top-level-partitions) (aka host profiles, node profiles, hardware profiles) and some of their associated capabilities are shown in **Figure 5-4**.

<p align="center"><img src="../figures/RM-ch05-hw-profile.png" alt="ref_hw_profiles" title="Reference HW Profiles" width="60%"/></p>
<p align="center"><b>Figure 5-4:</b> Cloud Infrastructure Hardware Profiles and host associated capabilities.</p>

The profiles can be considered to be the set of EPA-related (Enhanced Performance Awareness) configurations on Cloud Infrastructure resources.

> **Note:** In this chapter we shall not list all of the EPA-related configuration parameters.

A given host can only be assigned a single host profile; a host profile can be assigned to multiple hosts. In addition to the host profile, [profile-extensions](./chapter04.md#4.2.3) and additional capability specifications for the configuration of the host can be specified. Different Cloud Service Providers (CSP) may use different naming standards for their host profiles. For the profiles to be configured, the architecture of the underlying resource needs to be known.

| Ref | Cloud Infratsructure Resource | Type | Definition/Notes | Capabilities Reference  |
|-----|-------------------------------|------|------------------|-------------------------|
| infra.hw.001 | CPU Architecture |	<value> |	Values such as x64, ARM, etc. | `e.cap.020` |

The host profile properties are specified in the following sub-sections. The following diagram (**Figure 5-5**) pictorially represents a high-level abstraction of a physical server (host).

<p align="center"><img src="../figures/ch06_ref_hw_profile.PNG" alt="reference_hw_profile" title="Reference HW Profile" width="65%"/></p>
<p align="center"><b>Figure 5-5:</b> Generic model of a compute host for use in Host Profile configurations.</p>

<a name="5.4"></a>
## 5.4 Cloud Infrastructure Hardware Profiles features and requirements.

The configurations specified in here will be used in specifying the actual hardware profile configurations for each of the Cloud Infrastructure Hardware Profiles depicted in **Figure 5-4**.

<a name="5.4.1"></a>
### 5.4.1 Compute Resources

| Reference | Feature | Description | Basic  | High Performance |
|---------------------|----------------------|------------|------------|------------|
| infra.hw.cpu.cfg.001 | Minimum number of CPU sockets  | Specifies the minimum number of populated CPU sockets within each host<sup>*</sup> | 2 | 2 |
| infra.hw.cpu.cfg.002 | Minimum number of cores per CPU  | Specifies the number of cores needed per CPU<sup>*</sup> | 20 | 20 |
| infra.hw.cpu.cfg.003 | NUMA alignment | NUMA alignment enabled and BIOS configured to enable NUMA | N | Y |
| infra.hw.cpu.cfg.004 | Simultaneous Multithreading (SMT) | SMT enabled that allows each core to work multiple streams of data simultaneously  | Y | Y |
> <sup>*</sup> PLease note that these specifications are for general purpose servers normally located in large data centers. Servers for specialised use with the data centers or other locations, such as at edge sites, are likely to have different specifications.
<p align="center"><b>Table 5-14:</b> Minimum sizing and capability configurations for general purpose servers.</p>

<a name="5.4.1.1"></a>
#### 5.4.1.1 Compute Acceleration Hardware Specifications

| Reference            | Feature                    | Description     | Basic  | High Performance | Capabilities Reference  |
|----------------------|----------------------------|-----------------|--------|------------------|-------------------------|
| infra.hw.cac.cfg.001 | GPU                        | GPU             | N      | Optional         | `e.cap.014` |
| infra.hw.cac.cfg.002 |FPGA/other Acceleration H/W | HW Accelerators | N      | Optional         | `e.cap.016` |

<p align="center"><b>Table 5-15:</b> Compute acceleration configuration specifications.</p>


<a name="5.4.2"></a>
### 5.4.2 Storage Configurations

| Reference                | Feature           | Description       | Basic   | High Performance |
|--------------------------|-------------------|-------------------|-------------|-------------------|
| infra.hw.stg.hdd.cfg.001* | Local Storage HDD | Hard Disk Drive   |             |                   |
| infra.hw.stg.ssd.cfg.002* | Local Storage SSD | Solid State Drive | Recommended | Recommended       |

<p align="center"><b>Table 5-16:</b> Storage configuration specification.</p>

> **Note:** *This specified local storage configurations including # and capacity of storage drives.

<a name="5.4.3"></a>
### 5.4.3 Network Resources

<a name="5.4.3.1"></a>
#### 5.4.3.1 NIC configurations

| Reference           | Feature    | Description                                     | Basic | High Performance |
|---------------------|------------|-------------------------------------------------|------------|-------------------|
| infra.hw.nic.cfg.001 | NIC Ports  | Total number of NIC Ports available in the host | 4          | 4                 |
| infra.hw.nic.cfg.002 | Port Speed | Port speed specified in Gbps (minimum values)   | 10         | 25                |

<p align="center"><b>Table 5-17:</b> Minimum NIC configuration specification.</p>

<a name="5.4.3.2"></a>
#### 5.4.3.2 PCIe Configurations

| Reference           | Feature    | Description                                | Basic | High Performance |
|---------------------|------------|--------------------------------------------|------------|-------------------|
| infra.hw.pci.cfg.001 | PCIe slots | Number of PCIe slots available in the host | 8          | 8                 |
| infra.hw.pci.cfg.002 | PCIe speed |                                            | Gen 3      | Gen 3             |
| infra.hw.pci.cfg.003 | PCIe Lanes |                                            | 8          | 8                 |

<p align="center"><b>Table 5-18:</b> PCIe configuration specification.</p>

<a name="5.4.3.3"></a>
#### 5.4.3.3 Network Acceleration Configurations

| Reference            | Feature             | Description                    | Basic    | High Performance |Capabilities Reference |
|----------------------|---------------------|--------------------------------|----------|------------------|-----------------------|
| infra.hw.nac.cfg.001 | Crypto Acceleration | IPSec, Crypto                  | N        | Optional         | `e.cap.009`           |
| infra.hw.nac.cfg.002 | SmartNIC            | offload network functionality  | N        | Optional         | `e.cap.015`           |
| infra.hw.nac.cfg.003 | Compression         |                                | Optional | Optional         |                       |

<p align="center"><b>Table 5-19:</b> Network acceleration configuration specification.</p>
