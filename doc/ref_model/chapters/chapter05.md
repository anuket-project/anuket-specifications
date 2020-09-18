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

<a name="5.1"></a>
## 5.1 Cloud Infrastructure Software profile description

Cloud Infrastructure Software layer is composed of 2 layers, **Figure 5-1**:
- The virtualisation Infrastructure layer, which is based on hypervisor virtualisation technology or container-based virtualisation technology. Container virtualisation can be nested in hypervisor-based virtualisation
- The host OS layer

<p align="center"><img src="../figures/ch05-cloud-infrastructure-sw-profile-layers.png" alt="ref_profiles" title="Layers of Software Profile" width="50%"/></p>
<p align="center"><b>Figure 5-1:</b> Cloud Infrastructure software layers</p>

For a host (compute node or physical server), the virtualisation layer is an abstraction layer between hardware components (compute, storage, and network resources) and virtual resources allocated to a VM or a Pod. **Figure 5-2** represents the virtual resources (virtual compute, virtual network, and virtual storage) allocated to a VM or a Pod and managed by the Cloud Infrastructure Manager.

<p align="center"><img src="../figures/ch05_b_ref_profile.png" alt="b_ref_profile" title="Reference Profile" width="70%"/></p>
<p align="center"><b>Figure 5-2:</b> Cloud Infrastructure Virtual resources</p>

Depending on the requirements of the workloads, a VM or a Pod will be deployed with a Cloud Infrastructure Profile and an appropriate compute flavour. A Cloud Infrastructure Profile is defined by a Cloud Infrastructure Software Profile and a Cloud Infrastructure Hardware Profile. A Cloud Infrastructure Software Profile is a set of features, capabilities, and metrics offered by a Cloud Infrastructure software layer. **Figure 5-3** depicts a high level view of the Basic and Network Intensive Cloud Infrastructure Profiles.

<p align="center"><img src="../figures/RM_chap5_fig_5_3_SW_profile.png" alt="ref_profiles" title="Reference Profiles" width="80%"/></p>
<p align="center"><b>Figure 5-3:</b> Cloud Infrastructure Profiles</p>



The following sections detail the Cloud Infrastructure Software Profile features per type of virtual resource. The list of these features will evolve over time.

<a name="5.1.1"></a>
### 5.1.1 Virtual Compute

**Table 5-1** and **Table 5-2** depict the features related to virtual compute.

| Reference        | Feature                | Type   | Description                                           |
|------------------|------------------------|--------|-------------------------------------------------------|
| infra.com.cfg.001 | CPU allocation ratio   | Value  | Number of virtual cores per physical core             |
| infra.com.cfg.002 | NUMA alignment         | Yes/No | Support of NUMA at the virtualization layer           |
| infra.com.cfg.003 | CPU pinning            | Yes/No | Binds a process/vCPU to a physical core or SMT thread |
| infra.com.cfg.004 | Huge Pages             | Yes/No | Ability to manage huge pages of memory                |

<p align="center"><b>Table 5-1:</b> Virtual Compute features.</p>

| Reference        | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| infra.com.acc.cfg.001 | Left for RA specifications |  | |

<p align="center"><b>Table 5-2:</b> Virtual Compute Acceleration features.</p>

<a name="5.1.2"></a>
### 5.1.2 Virtual Storage

**Table 5-3** and **Table 5-4** depict the features related to virtual storage.

| Reference        | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
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

| Reference        | Feature                   | Type              | Description                                                                                                                                                                                                                                            |
|------------------|---------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| infra.net.cfg.001 | Connection Point interface | IO virtualisation | e.g. virtio1.1                                                                                                                                                                                                                                         |
| infra.net.cfg.002 | Overlay protocol          | Protocols         | The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric.                                                                                                     |
| infra.net.cfg.003 | NAT                       | Yes/No            | Support of Network Address Translation                                                                                                                                                                                                                 |
| infra.net.cfg.004 | Security Groups           | Yes/No            | Set of rules managing incoming and outgoing network traffic                                                                                                                                                                                            |
| infra.net.cfg.005 | Service Function Chaining | Yes/No            | Support of Service Function Chaining (SFC)                                                                                                                                                                                                                  |
| infra.net.cfg.006 | Traffic patterns symmetry | Yes/No            | Traffic patterns should be optimal, in terms of packet flow. North-south traffic shall not be concentrated in specific elements in the architecture, making those critical choke-points, unless strictly necessary (i.e. when NAT 1:many is required). |

<p align="center"><b>Table 5-5:</b> Virtual Networking features.</p>

| Reference             | Feature                       | Type                       | Description               |
|-----------------------|-------------------------------|----------------------------|---------------------------|
| infra.net.acc.cfg.001 | vSwitch optimisation          | Yes/No and SW Optimisation | e.g. DPDK.                |
| infra.net.acc.cfg.002 | Support of HW offload         | Yes/No                     | e.g. support of SmartNic. |
| infra.net.acc.cfg.003 | Crypto acceleration           | Yes/No                     |                           |
| infra.net.acc.cfg.004 | Crypto Acceleration Interface | Yes/No                     |                           |

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

| Minimum requirements | Example                                    |
|----------------------|--------------------------------------------|
|Database as a service | Cassandra                                  |
|Queue                 | Rabbit MQ                                  |
|LB and HA Proxy       |                                            |
<p align="center"><b>Table 5-7a:</b> Service examples.</p>

<a name="5.2"></a>
## 5.2 Cloud Infrastructure Software Profiles features and requirements

This section will detail Cloud Infrastructure Software Profiles and associated configurations for the 2 types of Cloud Infrastructure Profiles: Basic and Network intensive. <!-- and Compute intensive. -->

<a name="5.2.1"></a>
### 5.2.1 Virtual Compute

**Table 5-8** depicts the features and configurations related to virtual compute for the 2 types of Cloud Infrastructure Profiles.

| Reference         | Feature                | Type   | Basic | Network Intensive | Notes |
|-------------------|------------------------|--------|-------|-------------------|-------|
| infra.com.cfg.001 | CPU allocation ratio   | value  | 1:1   | 1:1               |This is set to 1:1 for the Basic profile to enable predictable and consistent performance during benchmarking and certification.  Operators may choose to modify this for actual deployments if they are willing to accept the risk of performance impact to workloads using the basic profile._ |
| infra.com.cfg.002 | NUMA alignment         | Yes/No | N     | Y                 |       |
| infra.com.cfg.003 | CPU pinning            | Yes/No | N     | Y                 |       |
| infra.com.cfg.004 | Huge Pages             | Yes/No | N     | Y                 |       |

<!--
| .conf             | Feature                | Type   | Basic | Network Intensive | Compute Intensive | Notes |
|-------------------|------------------------|--------|-------|-------------------|-------------------|-------|
| infra.com.cfg.001 | CPU allocation ratio   | value  | 1:1   | 1:1               | 1:1               |_**Note**: This is set to 1:1 for the Basic profile to enable predictable and consistent performance during benchmarking and certification.  Operators may choose to modify this for actual deployments if they are willing to accept the risk of performance impact to workloads using the basic profile._ |
| infra.com.cfg.002 | NUMA awareness         | Yes/No | N     | Y                 | Y                 |       |
| infra.com.cfg.003 | CPU pinning capability | Yes/No | N     | Y                 | Y                 |       |
| infra.com.cfg.004 | Huge Pages             | Yes/No | N     | Y                 | Y                 |       |
-->
<p align="center"><b>Table 5-8:</b> Virtual Compute features and configuration for the 2 types of Cloud Infrastructure Profiles.</p>

> **Note:** Capability nfvi.com.cfg.001 is set to 1:1 for the Basic profile to enable predictable and consistent performance during benchmarking, certification, and deployment.  Operators may choose to modify this for actual deployments if they are willing to accept the risk of performance impact to these workloads.

**Table 5-9** will gather virtual compute acceleration features. It will be filled over time.

| Reference             | Feature                            | Type | Basic | Network Intensive |
|-----------------------|------------------------------------|------|-------|-------------------|
| infra.com.acc.cfg.001 | _**Note:** for further study_ |      |       |                   |

<p align="center"><b>Table 5-9:</b> Virtual Compute Acceleration features.</p>

<a name="5.2.2"></a>
### 5.2.2 Virtual Storage

**Table 5-10** and **Table 5-11** depict the features and configurations related to virtual storage for the 2 types of Cloud Infrastructure Profiles.
<!--
| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| infra.stg.cfg.001 | Catalogue storage Types | Yes/No | Y  | Y  | Y |
| infra.stg.cfg.002 | Storage Block | Yes/No | Y | Y |Y  |
| infra.stg.cfg.003 | Storage with replication | Yes/No | N | Y | Y |
| infra.stg.cfg.004 | Storage with encryption |Yes/No | Y | Y | Y |
-->

| Reference         | Feature                  | Type   | Basic | Network Intensive |
|-------------------|--------------------------|--------|-------|-------------------|
| infra.stg.cfg.001 | Catalogue storage Types  | Yes/No | Y     | Y                 |
| infra.stg.cfg.002 | Storage Block            | Yes/No | Y     | Y                 |
| infra.stg.cfg.003 | Storage with replication | Yes/No | N     | Y                 |
| infra.stg.cfg.004 | Storage with encryption  | Yes/No | Y     | Y                 |

<p align="center"><b>Table 5-10:</b> Virtual Storage features and configuration for the 2 types of SW profiles.</p>

**Table 5-11** depicts the features related to Virtual storage Acceleration
<!--
| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| infra.stg.acc.cfg.001 | Storage IOPS oriented | Yes/No | N | Y | Y |
| infra.stg.acc.cfg.002 | Storage capacity oriented |  Yes/No| N | N | Y |
-->

| Reference             | Feature                   | Type   | Basic | Network Intensive |
|-----------------------|---------------------------|--------|-------|-------------------|
| infra.stg.acc.cfg.001 | Storage IOPS oriented     | Yes/No | N     | Y                 |
| infra.stg.acc.cfg.002 | Storage capacity oriented | Yes/No | N     | N                 |

<p align="center"><b>Table 5-11:</b> Virtual Storage Acceleration features.</p>

<a name="5.2.3"></a>
### 5.2.3 Virtual Networking

**Table 5-12** and **Table 5-13** depict the features and configurations related to virtual networking for the 2 types of Cloud Infrastructure Profiles.
<!--
| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| infra.net.cfg.001 | vNIC interface | IO virtualisation | virtio1.1 |  virtio1.1* |  virtio1.1 |
| infra.net.cfg.002 | Overlay protocol | Protocols  | VXLAN, MPLSoUDP, GENEVE, other |  VXLAN, MPLSoUDP, GENEVE, other |VXLAN, MPLSoUDP, GENEVE, other |
| infra.net.cfg.003 | NAT | Yes/No  | Y | Y | Y |
| infra.net.cfg.004 | Security Group | Yes/No  | Y | Y | Y |
| infra.net.cfg.005 | SFC support | Yes/No  | N | Y | Y |
| infra.net.cfg.006 | Traffic patterns symmetry | Yes/No  | Y | Y | Y |
-->

| Reference         | Feature                   | Type              | Basic                           | Network Intensive |
|-------------------|-----------------------------|-------------------|-------------------------------|-------------------|
| infra.net.cfg.001 | Connection Point interface | IO virtualisation | virtio1.1                     | virtio1.1*        |
| infra.net.cfg.002 | Overlay protocol          | Protocols         | VXLAN, MPLSoUDP, GENEVE, other |                   |
| infra.net.cfg.003 | NAT                       | Yes/No            | Y                              | Y                 |
| infra.net.cfg.004 | Security Group            | Yes/No            | Y                              | Y                 |
| infra.net.cfg.005 | Service Function Chaining | Yes/No            | N                              | Y                 |
| infra.net.cfg.006 | Traffic patterns symmetry | Yes/No            | Y                              | Y                 |

<p align="center"><b>Table 5-12:</b> Virtual Networking features and configuration for the 2 types of SW profiles.</p>

> **Note:** * might have other interfaces (such as SR-IOV VFs to be directly passed to a VM or a Pod) or NIC-specific drivers on guest machines transiently allowed until mature enough solutions are available with a similar efficiency level (for example regarding CPU and energy consumption).

<!--
| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| infra.net.acc.cfg.001 | vSwitch optimisation | Yes/No and SW Optimisation | N | Y, DPDK | Y, DPDK |
| infra.net.acc.cfg.002 | Support of HW offload | Yes/No | N | Y, support of SmartNic |Y, support of SmartNic |
| infra.net.acc.cfg.003 | Crypto acceleration | Yes/No | N  | Y | Y |
| infra.net.acc.cfg.004 | Crypto Acceleration Interface | Yes/No | N  | Y | Y |
-->

| Reference             | Feature                       | Type                       | Basic | Network Intensive      |
|-----------------------|-------------------------------|----------------------------|-------|------------------------|
| infra.net.acc.cfg.001 | vSwitch optimisation          | Yes/No and SW Optimisation | N     | Y, DPDK                |
| infra.net.acc.cfg.002 | Support of HW offload         | Yes/No                     | N     | Y, support of SmartNic |
| infra.net.acc.cfg.003 | Crypto acceleration           | Yes/No                     | N     | Y                      |
| infra.net.acc.cfg.004 | Crypto Acceleration Interface | Yes/No                     | N     | Y                      |

<p align="center"><b>Table 5-13:</b> Virtual Networking Acceleration features.</p>

<a name="5.3"></a>
## 5.3 Cloud Infrastructure Hardware Profile description

The support of a variety of different workload types, each with different (sometimes conflicting) compute, storage, and network characteristics, including accelerations and optimizations, drives the need to aggregate these characteristics as a hardware (host) profile and capabilities. A host profile is essentially a “personality” assigned to a compute host (physical server, also known as compute host, host, node, or pServer). The host profiles and related capabilities consist of the intrinsic compute host capabilities (such as #CPUs (sockets), # of cores/CPU, RAM, local disks and their capacity, etc.), and capabilities enabled in hardware/BIOS, <!--software (VIM, Hypervisor, Operating System),--> specialised hardware (such as accelerators), the underlay networking, and storage.

This chapter defines a simplified host, host profile and related capabilities model associated with each of the different Cloud Infrastructure Hardware Profile and related capabilities; some of these profiles and capability parameters are shown in **Figure 5-4**.

<p align="center"><img src="../figures/RM_chap5_fig_5_4_HW_profile.png" alt="ref_hw_profiles" title="Reference HW Profiles" width="100%"/></p>
<p align="center"><b>Figure 5-4:</b> Cloud Infrastructure Hardware Profiles and host associated capabilities.</p>

The host profile model and configuration parameters (hereafter for simplicity simply "host profile") will be used in the **Reference Architecture** to define different hardware profiles. The host profiles can be considered to be the set of EPA-related (Enhanced Performance Awareness) configurations on Cloud Infrastructure resources.

> **Note:** In this chapter we shall not list all of the EPA-related configuration parameters.

A software profile (see **Chapter 4**, **5.1 and 5.2**) defines the characteristics of Cloud Infrastructure SW of which Virtual Machines or Containers will be deployed on. A many to many relationship exists between software profiles and host profiles. A given host can only be assigned a single host profile; a host profile can be assigned to multiple hosts. Different Cloud Service Providers (CSP) may use different naming standards for their host profiles.

The following naming convention is used in this document:

`<host profile name>:: <”hp”><numeral host profile sequence #>`

When a software profile is associated with a host profile,  a qualified name can be used as specified below.
`<qualified host profile>:: <software profile><”-“><”hp”><numeral host profile sequence #>`
_**For Example:** for software profile “n” (network intensive) the above host profile name would be “n-hp1”_.

<p align="center"><img src="../figures/Chapter-6-HW-SW-Profile-Diagram_v2.png" alt="HW-Profile-SW-Flavour" Title="HW Profile and SW Profile relationship" width="85%"/></p>
<p align="center"><b>Figure 5-5:</b> Generic Hardware Profile, Software Flavour, Physical server relationship.</p>


**Figure 5-5** shows a simplistic depiction of the relationship between Hardware profile, Software Profile, Physical server, and virtual compute. In the diagram the resource pool, a logical construct, depicts all physical hosts that have been configured as per a given host profile; there is one resource pool for each hardware profile.
> **Note:** resource pools are not OpenStack host aggregates.

The host profile and capabilities include:
1. **# of CPUs (sockets)**: is the #of CPUs installed on the physical server.
1. **# of cores/CPU**: is the number of cores on each of the CPUs of the physical server.
1. **RAM (GB)**: is the amount of RAM installed on the physical server.
1. **Local Disk Capacity**: is the # of local disks and the capacity of the disks installed on the physical server.
1. **SMT (Simultaneous Multithreading)**: Enabled on all physical servers. Gets multiple threads per physical core. Always ON. Configured in the host.
1. **NUMA (Non-Uniform Memory Access)**: Indicates that vCPU will be on a Socket that is aligned with the associated NIC card and memory. Important for performance optimized workloads. Configured in the host.
1. **SR-IOV (Single-Root Input/Output Virtualisation)**: Configure PCIe ports to enable SR-IOV.
1. **smartNIC (aka Intelligent Server Adaptors)**: Accelerated virtual switch using smartNIC
1. **Cryptography Accelerators**: such as AES-NI, SIMD/AVX, and QAT.
1. **Security features**: such as Trusted Platform Module (TPM).

<!--1. **CPU Oversubscription Ratio**: is based on the number of threads available. For example, on a 2CPU, 24-core host with SMT, there are 96 vCPUs with 1:1 CPU Ratio and 192 vCPUs with 2:1 CPU Ratio. NOTE: While the oversubscription ratio is specified in the Virtual Infrastructure MAnager (VIM), once assigned it becomes part of the host personality and hence will be treated as part of the host profile and capabilities. -->
<!--1. **DPDK (Data Plane Development Kit)**: Accelerated virtual switch using Data Plan Development Kit (DPDK) -->
<!--1. **CPU Pinning**: vCPU is pinned to a physical core and dedicated to the requesting VM. Configured in VIM and Hypervisor.-->
<!--1. **Huge Pages**: By default, CPUs allocate RAM in 4K chunks. Huge Pages can be enabled to allocate in larger Chunks (such as 2MB, 1GB). This helps improve performance in some cases. Configured in the Operating System. -->

The following model, **Figure 5-6**, depicts the essential characteristics of a host that are of interest in specifying a host profile. The host (physical server) is composed of compute, network, and storage resources. The compute resources are composed of physical CPUs (aka CPU sockets or sockets) and memory (RAM). The network resources and storage resources are similarly modelled.

<p align="center"><img src="../figures/ch06_generic_model.PNG" alt="generic_model" title="Generic Model" width="100%"/></p>
<p align="center"><b>Figure 5-6:</b> Generic model of a compute host for use in Host Profile configurations.</p>

The hardware (host) profile properties are specified in the following sub-sections. The following diagram (**Figure 5-7**) pictorially represents a high-level abstraction of a physical server (host).

<p align="center"><img src="../figures/ch06_ref_hw_profile.PNG" alt="reference_hw_profile" title="Reference HW Profile" width="65%"/></p>
<p align="center"><b>Figure 5-7:</b> Generic model of a compute host for use in Host Profile configurations.</p>

<a name="5.4"></a>
## 5.4 Cloud Infrastructure Hardware Profiles features and requirements.

The configurations specified in here will be used in specifying the actual hardware profile configurations for each of the Cloud Infrastructure Hardware Profiles depicted in **Figure 5-4**.

<a name="5.4.1"></a>
### 5.4.1 Compute Resources

| Reference           | Feature                                             | Description                                                        | Basic Type | Network Intensive |
|---------------------|-----------------------------------------------------|--------------------------------------------------------------------|------------|-------------------|
| infra.hw.cpu.cfg.001 | Minimum Number of CPU sockets  | This determines the minimum number of CPU sockets within each host | 2          | 2                 |
| infra.hw.cpu.cfg.002 | Minimum Number of cores per CPU  | This determines the number of cores needed per CPU.                | 20         | 20                |
| infra.hw.cpu.cfg.003 | NUMA alignment                    | NUMA alignment support and BIOS configured to enable NUMA                    | N          | Y                 |
| infra.hw.cpu.cfg.004 | Simultaneous Multithreading (SMT) | This allows a CPU to work multiple streams of data simultaneously  | Y          | Y                 |

<!--
| Reference | Feature | Description | Basic Type | Network Intensive | Compute Intensive |
|---------------------|-----------|---------------------------|--------|--------|--------|
| infra.hw.cpu.cfg.001 | Number of CPU (Sockets) | This determines the minimum number of CPU sockets within each host | 2| 2| 2 |
| infra.hw.cpu.cfg.002 | Number of Cores per CPU | This determines the number of cores needed per each CPU. | 20 | 20 | 20 |
| infra.hw.cpu.cfg.003 | NUMA | NUMA support and BIOS configured to enable NUMA | N | Y | Y |
| infra.hw.cpu.cfg.004 | Simultaneous Multithreading (SMT) | This allows a CPU to work multiple streams of data simultaneously | Y | Y| Y |
-->

<!--
| infra.hw.cpu.cfg.005 | CPU Pinning |  | N | Y | Y
| infra.hw.cpu.cfg.006 | CPU Oversubscription Ratio* |  | n:1 | 1:1 | 1:1
| infra.hw.cpu.cfg.007 | Hugepages* |  | N | Y | Y
-->

<p align="center"><b>Table 5-14:</b> Minimum Compute resources configuration parameters.</p>

<!--
> _*These features are not set at the physical server BIOS_
-->

<a name="5.4.1.1"></a>
#### 5.4.1.1 Compute Acceleration Hardware Specifications

| Reference           | Feature | Description | Basic Type | Network Intensive |
|---------------------|---------|-------------|------------|-------------------|
| infra.hw.cac.cfg.001 | GPU     | GPU         | N          | N                 |

<!--
| Reference | Feature | Description | Basic Type | Network Intensive | Compute Intensive |
|---------------------|-----------|--------------|--------|--------|--------|
| infra.hw.cac.cfg.001 | GPU | GPU | N | N | Y |
-->

<p align="center"><b>Table 5-15:</b> Compute acceleration configuration specifications.</p>


<a name="5.4.2"></a>
### 5.4.2 Storage Configurations

| Reference                | Feature           | Description       | Basic Type  | Network Intensive |
|--------------------------|-------------------|-------------------|-------------|-------------------|
| infra.hw.stg.hdd.cfg.001* | Local Storage HDD | Hard Disk Drive   |             |                   |
| infra.hw.stg.ssd.cfg.002* | Local Storage SSD | Solid State Drive | Recommended | Recommended       |

<!--
| Reference | Feature | Description | Basic Type | Network Intensive | Compute Intensive |
|---------------------|-----------|---------------------------|--------|--------|--------|
| infra.hw.stg.hdd.cfg.001* | Local Storage HDD | Hard Disk Drive |  |  |  |
| infra.hw.stg.ssd.cfg.002* | Local Storage SSD | Solid State Drive | Recommended | Recommended |Recommended |
-->

<p align="center"><b>Table 5-16:</b> Storage configuration specification.</p>

> **Note:** *This specified local storage configurations including # and capacity of storage drives.

<a name="5.4.3"></a>
### 5.4.3 Network Resources

<a name="5.4.3.1"></a>
#### 5.4.3.1 NIC configurations

| Reference           | Feature    | Description                                     | Basic Type | Network Intensive |
|---------------------|------------|-------------------------------------------------|------------|-------------------|
| infra.hw.nic.cfg.001 | NIC Ports  | Total Number of NIC Ports available in the host | 4          | 4                 |
| infra.hw.nic.cfg.002 | Port Speed | Port speed specified in Gbps (minimum values)   | 10         | 25                |

<!--
| Reference | Feature | Description | Basic Type | Network Intensive | Compute Intensive |
|---------------------|-----------|---------------------------|--------|--------|--------|
| infra.hw.nic.cfg.001 | NIC Ports | Total Number of NIC Ports available in the host | 4 | 4 | 4 |
| infra.hw.nic.cfg.002 | Port Speed | Port speed specified in Gbps (minimum values) | 10 | 25 | 25 |
-->

<p align="center"><b>Table 5-17:</b> Minimum NIC configuration specification.</p>

<a name="5.4.3.2"></a>
#### 5.4.3.2 PCIe Configurations

| Reference           | Feature    | Description                                | Basic Type | Network Intensive |
|---------------------|------------|--------------------------------------------|------------|-------------------|
| infra.hw.pci.cfg.001 | PCIe slots | Number of PCIe slots available in the host | 8          | 8                 |
| infra.hw.pci.cfg.002 | PCIe speed |                                            | Gen 3      | Gen 3             |
| infra.hw.pci.cfg.003 | PCIe Lanes |                                            | 8          | 8                 |

<!--
| Reference | Feature | Description | Basic Type | Network Intensive | Compute Intensive |
|---------------------|-----------|---------------------------|--------|--------|--------|
| infra.hw.pci.cfg.001 | PCIe slots | Number of PCIe slots available in the host | 8 | 8 | 8 |
| infra.hw.pci.cfg.002 | PCIe speed |  | Gen 3 | Gen 3 | Gen 3 |
| infra.hw.pci.cfg.003 | PCIe Lanes |  | 8 | 8 | 8 |
-->

<p align="center"><b>Table 5-18:</b> PCIe configuration specification.</p>

<!--
<a name="5.4.3.3"></a>
#### 5.4.3.3 Network Bond Configurations

| Reference* | Feature | Description | Basic Type | Network Intensive | Compute Intensive |
|---------------------|-----------|---------------------------|--------|--------|--------|
| infra.hw.bdc.cfg.001 | Bonded VLAN ports |  | Y | Y | Y |

<p align="center"><b>Table 6-5:</b> Network bond configuration specifications.</p>

> _*Repeat Configuration for each Bond and specify use._
-->

<a name="5.4.3.3"></a>
#### 5.4.3.3 Network Acceleration Configurations

| Reference           | Feature                    | Description                                                          | Basic Type | Network Intensive |
|---------------------|----------------------------|----------------------------------------------------------------------|------------|-------------------|
| infra.hw.nac.cfg.001 | Crypto Acceleration | IPSec, Crypto                                                        | N          | Optional          |
| infra.hw.nac.cfg.002 | SmartNIC            | A SmartNIC that is used to offload network functionality to hardware | N          | Optional          |
| infra.hw.nac.cfg.003 | Compression         |                                                                      |            | Optional          |

<!--
| Reference | Feature | Description | Basic Type | Network Intensive | Compute Intensive |
|---------------------|-----------|---------------------------|--------|--------|--------|
| infra.hw.nac.cfg.001 | Cryptographic Acceleration | IPSec, Crypto |  N | Optional | Optional |
| infra.hw.nac.cfg.002 | SmartNIC | A SmartNIC that is used to offload network functionality to hardware | N | Optional  | Optional |
| infra.hw.nac.cfg.003 | Compression |  |  |  |
-->

<p align="center"><b>Table 5-19:</b> Network acceleration configuration specification.</p>
