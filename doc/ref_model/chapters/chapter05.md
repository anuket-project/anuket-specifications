[<< Back](../../ref_model)
# 5	Reference NFVI SW profiles and configurations
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [5.1 NFVI SW profile description.](#5.1)
  * [5.1.1 Virtual Compute.](#5.1.1)
  * [5.1.2 Virtual Storage.](#5.1.2)
  * [5.1.3 Virtual Networking.](#5.1.3) 
  * [5.1.4 Security.](#5.1.4) 
* [5.2 NFVI reference SW profiles and configurations.](#5.2)
  * [5.2.1 Virtual Compute features and configurations.](#5.2.1)
  * [5.2.2 Virtual Storage features and configurations.](#5.2.2)
  * [5.2.3 Virtual Networking features and configurations.](#5.2.3)

<a name="5.1"></a>
## 5.1 NFVI SW profile description

NFVI Software layer is composed of 2 layers, **Figure 5-1**:
- the virtualization Infrastructure layer, which is based on hypervisor virtualization technology or container-based virtualization technology. Container virtualization can be nested in hypervisor-based virtualization
- the host OS layer

<p align="center"><img src="../figures/ch05_nfvi_layers_sw_profile.PNG" alt="ref_profiles" title="Layers of Software Profile" width="50%"/></p>
<p align="center"><b>Figure 5-1:</b> NFVI software layers.</p>

For a host (compute node or physical server), the virtualization layer is an abstraction layer between hardware components (compute, storage and network resources) and virtual resources allocated to VNF-C, each VNF-C generally maps 1:1 against a single VM or a single container/pod. **Figure 5-2** represents the virtual resources (virtual compute, virtual network and virtual storage) allocated to VNF-C and managed by the VIM.

<p align="center"><img src="../figures/ch05_b_ref_profile.PNG" alt="b_ref_profile" title="Reference Profile" width="70%"/></p>
<p align="center"><b>Figure 5-2:</b> NFVI- Virtual resources.</p>

Depending on the requirements of VNFs, a VNFC will be deployed with a NFVI instance type and an appropriate compute flavour. A NFVI instance type is defined by a NFVI SW profile and a NFVI HW profile. A NFVI SW profile is a set of virtual resources with specific behaviour, capabilities and metrics. **Figure 5-3** depicts a high level view of software profiles for Basic, Network Intensive and Compute intensive instances types.

<p align="center"><img src="../figures/ch05_ref_nfvi_sw_profiles_v2.png" alt="ref_profiles" title="Reference Profiles" width="80%"/></p>
<p align="center"><b>Figure 5-3:</b> Reference NFVI software profiles.</p>

The following sections detail the NFVI SW profile features per type of virtual resource. The list of these features will evolve over time.

### 5.1.1	Virtual Compute

**Table 5-1** and **Table 5-2**	depict the features related to virtual compute.

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.com.cfg.001 | Support of flavours | Flavours | Support of compute Flavours defined in Compute Flavour's catalogue.|
| nfvi.com.cfg.002 | CPU partionning  | Value | CPU dedicated to the host and CPU dedicated to VNFs  |
| nfvi.com.cfg.003 | CPU allocation ratio  | Value |  |
| nfvi.com.cfg.004 | NUMA awareness | Yes/No  | Support of NUMA at the virtualization layer  |
| nfvi.com.cfg.005 | CPU pinning capability  | Yes/No |  |
| nfvi.com.cfg.006 | Huge Pages  | Yes/No |  |

<p align="center"><b>Table 5-1:</b> Virtual Compute features.</p>


| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.com.acc.cfg.001 | |  | |

<p align="center"><b>Table 5-2:</b> Virtual Compute Acceleration features.</p>

<a name="5.2"></a>
### 5.1.2	Virtual Storage

**Table 5-3** and **Table 5-4** depict the features related to virtual storage.

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.stg.cfg.001 | Storage Types |   | Supported Storage types. |
| nfvi.stg.cfg.002 | Storage Block | Yes/No  |  |  
| nfvi.stg.cfg.003 | Storage Object | Yes/No |  |  
| nfvi.stg.cfg.004 | Storage with replication |  Yes/No |  |  
| nfvi.stg.cfg.005 | Storage with encryption | Yes/No |  |  

<p align="center"><b>Table 5-3:</b> Virtual Storage features.</p>

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.stg.acc.cfg.001 | Storage IOPS oriented | Yes/No   |   |
| nfvi.stg.acc.cfg.002 | Storage capacity oriented | Yes/No   |   |

<p align="center"><b>Table 5-4:</b> Virtual Storage Acceleration features.</p>

### 5.1.3 Virtual Networking

**Table 5-5** and **Table 5-6** depict the features related to virtual networking.

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.net.cfg.001 | vNIC interface | IO virtualisation | e.g. virtio1.1, i40evf (Intel driver for VF SR-IOV). |
| nfvi.net.cfg.002 | Overlay protocol | Protocols | The overlay network encapsulation protocol needs to enable ECMP in the underlay to take advantage of the scale-out features of the network fabric. |
| nfvi.net.cfg.003 | NAT |  Yes/No |  |
| nfvi.net.cfg.004 | Security Group | Yes/No  |  |
| nfvi.net.cfg.005 | SFC support |Yes/No   |  |  
| nfvi.net.cfg.006 | Traffic patterns symmetry | Yes/No  | Traffic patterns should be optimal, in terms of packet flow. North-south traffic shall not be concentrated in specific elements in the architecture, making those critical choke-points, unless strictly necessary (i.e. when NAT 1:many is required). |
| nfvi.net.cfg.007 | Horizontal scaling | Yes/No  | The VNF cluster must be able to scale horizontally and to leverage technologies such as ECMP to enable scale-outs/scale-ins, privileging Active-Active HA models, even though this may require some level of application re-design to cope with the need of sharing state between VNF instances |

<p align="center"><b>Table 5-5:</b> Virtual Networking features.</p>

| .conf | Feature | Type  | Description |
|------------------|----------------|----------------|------------------------------------------------------------------------------------------------|
| nfvi.net.acc.cfg.001 | vSwitch optimization | Yes/No and SW Optimization | e.g. DPDK. |
| nfvi.net.acc.cfg.002 | Support of HW offload | Yes/No | e.g. support of SR-IOV, SmartNic. |
| nfvi.net.acc.cfg.003 | Crypto acceleration | Yes/No |  |
| nfvi.net.acc.cfg.004 | Crypto Acceleration Interface |Yes/No | |

<p align="center"><b>Table 5-6:</b> Virtual Networking Acceleration features.</p>

### 5.1.4	Security


<a name="5.2"></a>
## 5.2	NFVI reference SW profiles and configurations

This section will detail NFVI SW profiles and associated configurations for the 3 types of NFVI instances: Basic, Network intensive and Compute intensive.

### 5.2.1	Virtual Compute features and configurations

**Table 5-7** depicts the features and configurations related to virtual compute for the 3 types of reference NFVI instances.

| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| nfvi.com.cfg.001 | Support of flavours | Yes/No | Y | Y |Y|
| nfvi.com.cfg.002 | CPU partionning  | value |  |  |  |
| nfvi.com.cfg.003 | CPU allocation ratio  | value | 1:4 | 1:1  | 1:1 |
| nfvi.com.cfg.004 | NUMA awareness | Yes/No  | N | Y | Y |
| nfvi.com.cfg.005 | CPU pinning capability | Yes/No  | N | Y | Y |
| nfvi.com.cfg.006 | Huge Pages  | Yes/No  | N | Y | Y |

<p align="center"><b>Table 5-7:</b> Virtual Compute features and configuration for the 3 types of SW profiles.</p>

**Table 5-8** will gather virtual compute acceleration features. It will be filled over time.

| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| nfvi.com.acc.cfg.001 | |  | | |

<p align="center"><b>Table 5-8:</b> Virtual Compute Acceleration features.</p>


### 5.2.2	Virtual Storage features and configuration

**Table 5-9** and **Table 5-10** depict the features and configurations related to virtual storage for the 3 types of reference NFVI instances.

| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| nfvi.stg.cfg.001 | Catalogue storage Types | Yes/No | Y  | Y  | Y |  
| nfvi.stg.cfg.002 | Storage Block | Yes/No | Y | Y |Y  | 
| nfvi.stg.cfg.003 | Storage Object |Yes/No  | Y | Y | Y | 
| nfvi.stg.cfg.004 | Storage with replication | Yes/No | N | Y | Y | 
| nfvi.stg.cfg.005 | Storage with encryption |Yes/No | N | N | Y | 

<p align="center"><b>Table 5-9:</b> Virtual Storage features and configuration for the 3 types of SW profiles.</p>

**Table 5-10** depicts the features related to Virtual storage Acceleration

| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| nfvi.stg.acc.cfg.001 | Storage IOPS oriented | Yes/No | N | Y | Y |  
| nfvi.stg.acc.cfg.002 | Storage capacity oriented |  Yes/No| N | N | Y |  

<p align="center"><b>Table 5-10:</b> Virtual Storage Acceleration features.</p>


### 5.2.3 Virtual Networking features and configurations

**Table 5-11** and **Table 5-12** depict the features and configurations related to virtual networking for the 3 types of reference NFVI instances.

| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| nfvi.net.cfg.001 | vNIC interface | IO virtualisation | virtio1.1 |  virtio1.1, i40evf (Intel driver for VF SR-IOV) |  virtio1.1, i40evf (Intel driver for VF SR-IOV) |
| nfvi.net.cfg.002 | Overlay protocol | Protocols  | VXLAN, MPLSoUDP, GENEVE, other |  VXLAN, MPLSoUDP, GENEVE, other |VXLAN, MPLSoUDP, GENEVE, other |
| nfvi.net.cfg.003 | NAT | Yes/No  | Y | Y | Y |
| nfvi.net.cfg.004 | Security Group | Yes/No  | Y | Y | Y |
| nfvi.net.cfg.005 | SFC support | Yes/No  | N | Y | Y |
| nfvi.net.cfg.006 | Traffic patterns symmetry | Yes/No  | Y | Y | Y |
| nfvi.net.cfg.007 | Horizontal scaling | Yes/No  | Y | Y | Y |

<p align="center"><b>Table 5-11:</b> Virtual Networking features and configuration for the 3 types of SW profiles.</p>

| .conf | Feature | Type  | Basic | Network Intensive | Compute Intensive |
|------------------|----------------|----------------|----------------|----------------|----------------|
| nfvi.net.acc.cfg.001 | vSwitch optimization | YeS/No and SW Optimization | N | Y, DPDK | Y, DPDK |
| nfvi.net.acc.cfg.002 | Support of HW offload | YeS/No | N | Y, support of SR-IOV and  SmartNic |Y, support of SR-IOV and  SmartNic |
| nfvi.net.acc.cfg.003 | Crypto acceleration | Yes/No | N  | Y | Y |
| nfvi.net.acc.cfg.004 | Crypto Acceleration Interface | Yes/No | N  | Y | Y |

<p align="center"><b>Table 5-12:</b> Virtual Networking Acceleration features.</p>

