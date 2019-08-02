[<< Back](../../openstack)

# 4. Component Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction.](#4.1)
* [4.2 Open Stack Components (VIM).](#4.2)
* [4.3 NFVI Components](#4.3)
  * [4.3.1 Basic Profile](#4.3.1)
  * [4.3.2 Network Intensive Profile](#4.3.2)
  * [4.3.3 Compute Intensive Profile](#4.3.3)

<a name="4.1"></a>
## 4.1 Introduction.

<a name="4.2"></a>
## 4.2 Open Stack Components (VIM).

Components here will not change amongst different profiles

<a name="4.3"></a>
## 4.3 NFVI Components.

> L2 level of artefacts 

<a name="4.3.1"></a>
### 4.3.1 Basic Profile

#### 4.3.1.1 Software Components
> for example: vSwitch.
#### 4.3.1.2 Hardware Platform
> for example: single socket platform. 2x10G NIC, etc.

<a name="4.3.2"></a>
### 4.3.2 Network Intensive Profile
#### 4.3.2.1 Software Components
> for example: vSwitch DPDK + Contrail
#### 4.3.2.2 Hardware Platform
> for example: dual socket platform. 2x25G NIC, CryptoAcc, etc. 

<a name="4.3.3"></a>
### 4.3.3 Compute Intensive Profile 
#### 4.3.2.1 Software Components
> for example: vSwitch DPDK + Contrail 
#### 4.3.2.2 Hardware Platform
> for example: dual socket platform. 2x25G NIC, GPU, etc.