[<< Back](../../ref_model)
# 5	Reference NFVI SW profiles and configurations
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [5.1 Virtual Compute.](#5.1)
* [5.2 Virtual Storage.](#5.2)
* [5.3 Virtual Networking.](#5.3) 
* [5.4 Security.](#5.4)
* [5.5 Basic NFVI reference SW profile and configuration.](#5.5)
  * [5.5.1 Virtual Compute.](#5.5.1)
  * [5.5.2 Virtual Storage.](#5.5.2)
  * [5.5.3 Virtual Networking and SDN.](#5.5.3)
  * [5.5.4 Security.](#5.5.4)
* [5.6 Network intensive NFVI reference SW profile and configuration.](#5.6)
  * [5.6.1 Virtual Compute.](#5.6.1)
  * [5.6.2 Virtual Storage.](#5.6.2)
  * [5.6.3 Virtual Networking and SDN.](#5.6.3)
  * [5.6.4 Security.](#5.6.4)
* [5.7 Compute intensive NFVI reference SW profile and configuration.](#5.7)
  * [5.7.1 Virtual Compute.](#5.7.1)
  * [5.7.2 Virtual Storage.](#5.7.2)
  * [5.7.3 Virtual Networking and SDN.](#5.7.3)
  * [5.7.4 Security.](#5.7.4)

NFVI Software layer is composed of 2 layers, **Figure 5-1**:
- the virtualization Infrastructure layer, which is based on hypervisor virtualization technology or container-based virtualization technology. Container virtualization can be nested in hypervisor-based virtualization
- the host OS layer

<p align="center"><img src="../figures/ch05_nfvi_layers_sw_profile.PNG" alt="ref_profiles" title="Layers of Software Profile" width="100%"/></p>
<p align="center"><b>Figure 5-1:</b> Layers of NFVI software profile.</p>

For a host (compute node or physical server), the virtualization layer is an abstraction layer between hardware components (compute, storage and network resources) and logical resources allocated to VNF-C, each VNF-C maps 1:1 against a single VM or a single Container. **Figure 5-2** represents the virtual resources (virtual compute, virtual network and virtual storage) allocated to VNF-C and managed by the VIM.

<p align="center"><img src="../figures/ch05_b_ref_profile.PNG" alt="b_ref_profile" title="Reference Profile" width="100%"/></p>
<p align="center"><b>Figure 5-2:</b> NFVI- Virtual resources.</p>

Depending on the requirements of VNFs and the capabilities expected from the infrastructure, a NFVI software profile represents for a host the right configuration needed. It is a set of virtual resources with specific behaviour, capabilities and metrics. **Figure 5-3** depicts a high level view of software profiles for Basic, Network Intensive and Compute intensive requirements.

<p align="center"><img src="../figures/ch05_ref_nfvi_sw_profiles_v2.PNG" alt="ref_profiles" title="Reference Profiles" width="100%"/></p>
<p align="center"><b>Figure 5-3:</b> Reference NFVI software profiles.</p>

The features of these software profiles types are detailed in the following sections. The list of these features will evolved on time.

<a name="5.1"></a>
## 5.1	Virtual Compute

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.com.cfg.001 | Support of flavours |  | Supported compute Flavours need to be the same as those listed in the compute flavours' catalogue. |
| nfvi.com.cfg.002 | CPU partionning  | value | CPU dedicated to the host and CPU dedicated to VNFs  |
| nfvi.com.cfg.003 | CPU allocation ratio  | value |  |
| nfvi.com.cfg.004 | NUMA awareness | true/false  | Support of NUMA at the virtualization layer  |
| nfvi.com.cfg.005 | CPU pinning capability  | true/false |  |
| nfvi.com.cfg.006 | Huge Pages  | value |  |

<p align="center"><b>Table 5-1:</b> Virtual Compute features.</p>

### 5.1.1	Virtual compute Acceleration

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.com.acc.cfg.001 | |  | |

<p align="center"><b>Table 5-2:</b> Virtual Compute Acceleration features.</p>

<a name="5.2"></a>
## 5.2	Virtual Storage

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.stg.cfg.001 | Storage Types |   | Supported Storage types needs to be the same as those listed in the catalogue. |
| nfvi.stg.cfg.002 | Storage Block |  |  |  
| nfvi.stg.cfg.003 | Storage Object |  |  |  
| nfvi.stg.cfg.004 | Storage with replication |  |  |  
| nfvi.stg.cfg.005 | Storage with encryption |  |  |  

<p align="center"><b>Table 5-3:</b> Virtual Storage features.</p>

### 5.2.1 Virtual storage Acceleration

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.stg.acc.cfg.001 | Storage IOPS oriented |   |   |
| nfvi.stg.acc.cfg.002 | Storage capacity oriented |   |   |

<p align="center"><b>Table 5-4:</b> Virtual Storage Acceleration features.</p>

<a name="5.3"></a>
## 5.3 Virtual Networking

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.net.cfg.001 | vNIC interface | | e.g. virtio1.1, i40evf (Intel driver for VF SR-IOV). |
| nfvi.net.cfg.002 | Overlay protocol |  | The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric. |
| nfvi.net.cfg.003 | NAT |  |  |
| nfvi.net.cfg.004 | Security Group |  |  |
| nfvi.net.cfg.005 | SFC support |  |  |  
| nfvi.net.cfg.006 | Traffic patterns symmetry |  | Traffic patterns should be optimal, in terms of packet flow. North-south traffic shall not be concentrated in specific elements in the architecture, making those critical choke-points, unless strictly necessary (i.e. when NAT 1:many is required). |
| nfvi.net.cfg.007 | Horizontal scaling |  | The VNF cluster must be able to scale horizontally and to leverage technologies such as ECMP to enable scale-outs/scale-ins, privileging Active-Active HA models, even though this may require some level of application re-design to cope with the need of sharing state between VNF instances |

<p align="center"><b>Table 5-5:</b> Virtual Networking features.</p>

### 5.3.1	Virtual Network Acceleration

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.net.acc.cfg.001 | vSwitch optimization | | e.g. DPDK. |
| nfvi.net.acc.cfg.002 | Support of HW offload | | e.g. support of SR-IOV, SmartNic. |
| nfvi.net.acc.cfg.003 | Crypto acceleration | |  |
| nfvi.net.acc.cfg.004 | Crypto Acceleration Interface | | |

<p align="center"><b>Table 5-6:</b> Virtual Networking Acceleration features.</p>

<a name="5.4"></a>
## 5.4	Security
Note: can be removed?


Note: 	The following sections should be more relevant for reference architecture document

<a name="5.5"></a>
## 5.5	Basic NFVI reference SW profile and configuration
This NFVI SW Profile and configuration will be suitable for B instance type (Please see Section 3). **Figure 5-2** below shows the reference architecture of the NFVI solution.

<p align="center"><img src="../figures/ch05_b_ref_profile.PNG" alt="b_ref_profile" title="Basic Reference Profile" width="100%"/></p>
<p align="center"><b>Figure 5-2:</b> Reference NFVI software profile and configuration for B instance.</p>

<a name="5.5.1"></a>
### 5.5.1	Virtual Compute

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|----------------|----------------------------------|------------|------------------------------------------------------------------------------------------------|
| nfvi.com.cfg.001 | VM Flavours | All flavours listed in **Chapter 4** | Yes | Supported VM Flavours needs to be the same as those listed in the compute flavours' catalogue. |
| nfvi.com.cfg.002 | Hyperthreading | Enabled | Yes | Hyperthreading needs to be enabled and allowed. |
| nfvi.com.cfg.003 |  |  |  |  |

<p align="center"><b>Table 5-1:</b> Virtual Compute Configuration for B instance.</p>

#### 5.5.1.1	Virtual compute Acceleration

<a name="5.5.2"></a>
### 5.5.2	Virtual Storage

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|---------------|-----------------------------------|------------|--------------------------------------------------------------------------------|
| nfvi.stg.cfg.001 | Storage Types | All types listed in **Chapter 4** | Yes | Supported Storage types needs to be the same as those listed in the catalogue. |
| nfvi.stg.cfg.002 |  |  |  |  |
| nfvi.stg.cfg.003 |  |  |  |  |

<p align="center"><b>Table 5-2:</b> Virtual Storage Configuration for B instance.</p>

#### 5.5.2.1 Virtual storage Acceleration

<a name="5.5.3"></a>
### 5.5.3 Virtual Networking and SDN

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|---------------------------|--------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nfvi.net.cfg.001 | vNIC interface | Virtio1.1 |  | vNIC interface needs to be virtio1.1. |
| nfvi.net.cfg.002 | Overlay protocol | VXLAN, MPLSoUDP, GENEVE, other |  | The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric. |
| nfvi.net.cfg.003 | SFC support |  |  |  |
| nfvi.net.cfg.004 | Traffic patterns symmetry |  |  | Traffic patterns should be optimal, in terms of packet flow. North-south traffic shall not be concentrated in specific elements in the architecture, making those critical choke-points, unless strictly necessary (i.e. when NAT 1:many is required). |
| nfvi.net.cfg.005 | Horizontal scaling |  |  | The VNF cluster must be able to scale horizontally and to leverage technologies such as ECMP to enable scale-outs/scale-ins, privileging Active-Active HA models, even though this may require some level of application re-design to cope with the need of sharing state between VNF instances |

<p align="center"><b>Table 5-3:</b> Virtual Networking & SDN Configuration for B instance.</p>

#### 5.5.3.1	Virtual Network Acceleration

<a name="5.5.4"></a>
### 5.5.4	Security

<a name="5.6"></a>
## 5.6	Network intensive NFVI reference SW profile and configuration
This NFVI SW Profile and configuration will be suitable for both B and N instance types.

<p align="center"><img src="../figures/ch05_n_ref_profile.PNG" alt="n_ref_profile" title="Network Intensive Reference Profile" width="100%"/></p>
<p align="center"><b>Figure 5-3:</b> Reference NFVI software profile and configuration for N instance.</p>

<a name="5.6.1"></a>
### 5.6.1	Virtual Compute

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|----------------|----------------------------------|------------|------------------------------------------------------------------------------------------------|
| nfvi.com.cfg.001 | VM Flavours | All flavours listed in **Chapter 4** | Yes | Supported VM Flavours needs to be the same as those listed in the compute flavours' catalogue. |
| nfvi.com.cfg.002 | Hyperthreading | Enabled | Yes | Hyperthreading needs to be enabled and allowed. |
| nfvi.com.cfg.003 |  |  |  |  |

<p align="center"><b>Table 5-4:</b> Virtual Compute Configuration for N instance.</p>


#### 5.6.1.1	Virtual compute Acceleration

<a name="5.6.2"></a>
### 5.6.2	Virtual Storage

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|---------------|-----------------------------------|------------|--------------------------------------------------------------------------------|
| nfvi.stg.cfg.001 | Storage Types | All types listed in **Chapter 4** | Yes | Supported Storage types needs to be the same as those listed in the catalogue. |
| nfvi.stg.cfg.002 |  |  |  |  |
| nfvi.stg.cfg.003 |  |  |  |  |

<p align="center"><b>Table 5-5:</b> Virtual Storage Configuration for N instance.</p>

#### 5.6.2.1	Virtual storage Acceleration

<a name="5.6.3"></a>
### 5.6.3	Virtual Networking and SDN

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|---------------------------|--------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nfvi.net.cfg.001 | vNIC interface | Virtio1.1 |  | vNIC interface needs to be virtio1.1. |
| nfvi.net.cfg.002 | Overlay protocol | VXLAN, MPLSoUDP, GENEVE, other |  | The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric. |
| nfvi.net.cfg.003 | SFC support |  |  |  |
| nfvi.net.cfg.004 | Traffic patterns symmetry |  |  | Traffic patterns should be optimal, in terms of packet flow. North-south traffic shall not be concentrated in specific elements in the architecture, making those critical choke-points, unless strictly necessary (i.e. when NAT 1:many is required). |
| nfvi.net.cfg.005 | Horizontal scaling |  |  | The VNF cluster must be able to scale horizontally and to leverage technologies such as ECMP to enable scale-outs/scale-ins, privileging Active-Active HA models, even though this may require some level of application re-design to cope with the need of sharing state between VNF instances |
| nfvi.net.cfg.006 | vRouter/vSwitch |  |  | The vRouter/vSwitch elements must be optimised/accelerated and/or HW offloadable. |

<p align="center"><b>Table 5-6:</b> Virtual Networking & SDN Configuration for N instance.</p>

#### 5.6.3.1	Virtual Network Acceleration

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|-------------------------------|-------------------|------------|--------------------------------------------------|
| nfvi.acc.cfg.001 | Crypto Acceleration | Supported | No |  |
| nfvi.acc.cfg.002 | Crypto Acceleration Interface | VDPA/virtio-ipsec | Yes | To be decided what interface it needs to support |

<p align="center"><b>Table 5-7:</b> Virtual Acceleration configuration for N instance.</p>

<a name="5.6.4"></a>
### 5.6.4	Security

<a name="5.7"></a>
## 5.7	Compute intensive NFVI reference SW profile and configuration
This NFVI SW profile and configuration will be suitable for C instance type

<p align="center"><img src="../figures/ch05_c_ref_profile.PNG" alt="c_ref_profile" title="Compute Intensive Reference Profile" width="100%"/></p>
<p align="center"><b>Figure 5-4:</b> Reference NFVI software profile and configuration for C instance.</p>

<a name="5.7.1"></a>
### 5.7.1	Virtual Compute

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|----------------|----------------------------------|------------|------------------------------------------------------------------------------------------------|
| nfvi.com.cfg.001 | VM Flavours | All flavours listed in **Chapter 4** | Yes | Supported VM Flavours needs to be the same as those listed in the compute flavours' catalogue. |
| nfvi.com.cfg.002 | Hyperthreading | Enabled | Yes | Hyperthreading needs to be enabled and allowed. |
| nfvi.com.cfg.003 |  |  |  |  |

<p align="center"><b>Table 5-8:</b> Virtual Compute Configuration for C instance.</p>


#### 5.7.1.1	Virtual compute Acceleration

<a name="5.7.2"></a>
### 5.7.2	Virtual Storage

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|---------------|-----------------------------------|------------|--------------------------------------------------------------------------------|
| nfvi.stg.cfg.001 | Storage Types | All types listed in **Chapter 4** | Yes | Supported Storage types needs to be the same as those listed in the catalogue. |
| nfvi.stg.cfg.002 |  |  |  |  |
| nfvi.stg.cfg.003 |  |  |  |  |

<p align="center"><b>Table 5-9:</b> Virtual Storage Configuration for C instance.</p>

#### 5.7.2.1	Virtual storage Acceleration

<a name="5.7.3"></a>
### 5.7.3	Virtual Networking and SDN

| .conf | Feature | Configuration | Mandatory? | Description |
|------------------|---------------------------|--------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nfvi.net.cfg.001 | vNIC interface | Virtio1.1 |  | vNIC interface needs to be virtio1.1. |
| nfvi.net.cfg.002 | Overlay protocol | VXLAN, MPLSoUDP, GENEVE, other |  | The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric. |
| nfvi.net.cfg.003 | SFC support |  |  |  |
| nfvi.net.cfg.004 | Traffic patterns symmetry |  |  | Traffic patterns should be optimal, in terms of packet flow. North-south traffic shall not be concentrated in specific elements in the architecture, making those critical choke-points, unless strictly necessary (i.e. when NAT 1:many is required). |
| nfvi.net.cfg.005 | Horizontal scaling |  |  | The VNF cluster must be able to scale horizontally and to leverage technologies such as ECMP to enable scale-outs/scale-ins, privileging Active-Active HA models, even though this may require some level of application re-design to cope with the need of sharing state between VNF instances |
| nfvi.net.cfg.006 | vRouter/vSwitch |  |  | The vRouter/vSwitch elements must be optimised/accelerated and/or HW offloadable. |

<p align="center"><b>Table 5-10:</b> Virtual Networking & SDN Configuration for C instance.</p>

#### 5.7.3.1	Virtual Network Acceleration

<a name="5.7.4"></a>
### 5.7.4	Security
