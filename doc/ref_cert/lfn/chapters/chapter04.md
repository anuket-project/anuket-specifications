[<< Back](../)

# 4. NFVI Test Case Traceability to Architecture Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Selection Criteria](#4.2)
* [4.3 Traceability Matrix](#4.3)
  * [4.3.1 Architecture and OpenStack Based](#4.3.1)
  * [4.3.2 Infrastructure](#4.3.2)
  * [4.3.3 VIM](#4.3.3)
  * [4.3.4 Interfaces & APIs](#4.3.4)
  * [4.3.5 Tenants](#4.3.5)
  * [4.3.6 LCM](#4.3.6)
  * [4.3.7 Assurance](#4.3.7)
  * [4.3.8 Security](#4.3.8)

<a name="4.1"></a>
## 4.1 Introduction

The scope of this chapter is to identify and list down test cases based on requirements defined in [Reference Architecture-1 (RA-1)](../../../ref_arch/openstack/README.md). This will serve as traceability between test cases and requirements.

Note that each requirement may have one or more test cases associated with it. 

**must**: Test Cases that are marked as must are considered mandatory and must pass succesfully.

**should**: Test Cases that are marked as should are expected to be fulfilled by NFVI but it is up to each service provider to accept an NFVI tagetting reference architecture that is not reflecting on any of those requirements. The same applies to should not.

**may**: Test cases that are marked as may are considered optional. The same applies to may not.

<a name="4.2"></a>
## 4.2 Selection Criteria
> Test cases below are selected based on available test cases in open-source tools like OPNFV FuncTest, YardStick, DoveTail etc.

<a name="4.3"></a>
## 4.3 Traceability Matrix

- Write content that explains this section defines the mapping, or traceability of RM/RA-1 requirements to test cases.

<a name="4.3.1"></a>
### 4.3.1 Architecture and OpenStack Requirements

- Describe and define in detail, RM/RA-1 OpenStack requirements.

<a name="4.3.2"></a>
### 4.3.2 Infrastructure


| Test case # | sub-category | Description | Requirement # |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `cert.test.inf.01` | Compute | Create a virtual machine with CPU pinning and 2 NUMA nodes. | `req.inf.com.05` |
| `cert.test.inf.02` | Compute | Create a virtual machine with CPU pinning enabled. | `req.inf.com.06` |
| `cert.test.inf.03` | Compute | Create 2 virtual machines and associate block storage to it. | `req.inf.stg.01	` |
| `cert.test.inf.04` | Compute | Create 2 virtual machines which are booted from block storage. | `req.inf.stg.01	` |

<a name="4.3.3"></a>
### 4.3.3 VIM


| Test case # | sub-category | Description | Requirement # |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `cert.test.vim.01` | VIM | Create a virtual machine with CPU pinning, HugePages and 2 NUMA nodes. | `req.vim.04` |
| `cert.test.vim.02` | VIM | Upload an image to image repository and download it back. | `req.vim.05` |
| `cert.test.vim.03` | VIM | Deploy a heat stack having 2 virtual machines with associated network. | `req.vim.06` |
| `cert.test.vim.04` | VIM | Create 2 tenants and then create virtual machine in each tenant. | `req.vim.07` |

<a name="4.3.4"></a>
### 4.3.4 Interfaces & APIs
This defines the test cases around the functionality that are exposed by OpenStack APIs. All the defined OpenStack 
service APIs in RA-1's [chapter 05](../../../ref_arch/openstack/chapters/chapter05.md) will be the scope here. 

Note: It will only target the functionality that are exposed by standard OpenStack APIs.  

#### 4.3.4.1 Identity - Keystone

It covers the test cases against identity management operations like user management, project management, multi-tenancy etc. 

| Test case # | sub-category | Description | Requirement # |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `cert.test.vim.01` | API | Show API endpoint catalog. It *must* have endpoint for each Core service. | `req.int.api.01` |

#### 4.3.4.2 Image - Glance
It covers the test cases against image management operations. 


#### 4.3.4.3 Block Storage - Cinder
It covers the test cases against volume management operations.

#### 4.3.4.4 Object Storage - Swift
It covers the test cases against object management operations.


#### 4.3.4.5 Networking - Neutron
It covers the test cases against networking management operations.


#### 4.3.4.6 Compute - Nova
It covers the test cases against compute management operations.

#### 4.3.4.7 Orchestration - Heat
It covers the test cases against orchestration operations.

<a name="4.3.5"></a>
### 4.3.5 Tenants

<a name="4.3.6"></a>
### 4.3.6 LCM

<a name="4.3.7"></a>
### 4.3.7 Assurance

<a name="4.3.8"></a>
### 4.3.8 Security
