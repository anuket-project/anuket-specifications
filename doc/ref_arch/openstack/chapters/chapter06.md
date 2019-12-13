[<< Back](../../openstack)

# 6. Security
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 Security Requirements](#6.2)
* [6.3 NFVI and VIM Security](#6.3)
  * [6.3.1 Hardware Hardening](#6.3.1)
  * [6.3.2 Hypervisor Hardening](#6.3.2)
  * [6.3.3 OpenStack Hardening ](#6.3.3)
  * [6.3.4 Identity and Access Control](#6.3.4)
  * [6.3.5 Network Security ](#6.3.5)
* [6.4 Workload Security](#6.4)
  * [6.4.1 Tenant Credentials](#6.4.1)
  * [6.4.2 Tenant Isolation](#6.4.2)
  * [6.4.3 VNFs Security](#6.4.3)
  * [6.4.4 Storage Security](#6.4.4)
* [6.5 Operations and Management (OAM) Networks Security](#6.5)
* [6.6 External Networks Security](#6.6)

<a name="6.1"></a>
## 6.1 Introduction

Context and scope

<a name="6.2"></a>
## 6.2 Security Requirements

Based on chapter 2 requirements

<a name="6.3"></a>
## 6.3 NFVI and VIM Security

OpenStack security guide:
https://docs.openstack.org/security-guide/introduction/introduction-to-openstack.html

<a name="6.3.1"></a>
### 6.3.1 Hardware Hardening

Server boot hardening: BIOS, password policies, TPM
  
<a name="6.3.2"></a>  
### 6.3.2 Hypervisor Hardening

<a name="6.3.3"></a>  
### 6.3.3 OpenStack Hardening

Configurations files, APIs security (TLS), Dashboard access, Identity

<a name="6.3.4"></a>  
### 6.3.4 Identity and Access Control

Identification, authentication, authorization

RBAC

Secrets management (Barbican)

<a name="6.3.5"></a>  
### 6.3.5 Network Security 

Security between management and execution zones

IP filtering

<a name="6.4"></a>
## 6.4 Workload Security

<a name="6.4.1"></a>
### 6.4.1 Tenant Credentials

<a name="6.4.2"></a>
### 6.4.2 Tenant Isolation

<a name="6.4.3"></a>
### 6.4.3 VNFs Security

<a name="6.4.4"></a>
### 6.4.4 Storage Security

<a name="6.5"></a>
## 6.5 Operations and Management (OAM) Networks Security

IP filtering

SSH jumphost 

<a name="6.6"></a>
## 6.6 External Networks Security
