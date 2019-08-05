[<< Back](../../openstack)

# 4. Component Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction.](#4.1)
* [4.2 Foundational Components.](#4.2)
  * [4.2 Enabler services.](#4.2.1)
  * [4.2 Networking Fabric.](#4.2.2)
* [4.3 Open Stack Components (Controller nodes).](#4.3)
* [4.4 NFVI Components (Compute nodes)](#4.4)
  * [4.4.1 Basic Profile](#4.3.1)
  * [4.4.2 Network Intensive Profile](#4.4.2)
  * [4.4.3 Compute Intensive Profile](#4.4.3)
* [4.5 Storage nodes](#4.4)

<a name="4.1"></a>
## 4.1 Introduction.

<a name="4.2"></a>
## 4.2 Foundational Components.
Components here will not change amongst different profiles

<a name="4.2.1"></a>
## 4.2.1 Enabler services.

<a name="4.2.2"></a>
## 4.2.2 Networking Fabric.

<a name="4.3"></a>
## 4.3 Open Stack Components (Controller nodes).

Components here will not change amongst different profiles

<a name="4.4"></a>
## 4.4 NFVI Components (Compute nodes).

> L2 level of artefacts 

<a name="4.4.1"></a>
### 4.4.1 Basic Profile

#### 4.4.1.1 Software Components
> for example: vSwitch.
#### 4.4.1.2 Hardware Platform
> for example: single socket platform. 2x10G NIC, etc.

<a name="4.4.2"></a>
### 4.4.2 Network Intensive Profile
#### 4.4.2.1 Software Components
> for example: vSwitch DPDK + Contrail
#### 4.4.2.2 Hardware Platform
> for example: dual socket platform. 2x25G NIC, CryptoAcc, etc. 

<a name="4.4.3"></a>
### 4.4.3 Compute Intensive Profile 
#### 4.4.2.1 Software Components
> for example: vSwitch DPDK + Contrail 
#### 4.4.2.2 Hardware Platform
> for example: dual socket platform. 2x25G NIC, GPU, etc.

<a name="4.5"></a>
## 4.5 Storage nodes.