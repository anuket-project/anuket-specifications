[<< Back](../../ref_arch)

# 4. Component Level Architecture

## Table of Contents
* [4.1 Open Stack Components (VIM).](#4.1)
* [4.2 NFVI Components](#4.2)

<a name="4.1"></a>
## 4.1 Open Stack Components (VIM).

Components here will not change amongst different profiles

<a name="4.2"></a>
## 4.2 NFVI Components.

> L2 level of artefacts 

### 4.2.1 Basic Profile

#### 4.2.1.1 Software Components
> for example: vSwitch.
#### 4.2.1.2 Hardware Platform
> for example: single socket platform. 2x10G NIC, etc.


### 4.2.2 Network Intensive Profile
#### 4.2.2.1 Software Components
> for example: vSwitch DPDK + Contrail
#### 4.2.2.2 Hardware Platform
> for example: dual socket platform. 2x25G NIC, CryptoAcc, etc. 

### 4.2.3 Compute Intensive Profile 
#### 4.2.2.1 Software Components
> for example: vSwitch DPDK + Contrail 
#### 4.2.2.2 Hardware Platform
> for example: dual socket platform. 2x25G NIC, GPU, etc.