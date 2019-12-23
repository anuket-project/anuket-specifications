[<< Back](../../openstack)

# 8. Gaps, Innovation, and Development
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction](#8.1)
* [8.2 The Gaps](#8.2)
* [8.3 Heading](#8.3)

<a name="8.1"></a>
## 8.1 Introduction
The purpose of this chapter is to identify the gaps between what is required for automated deployment of VNFs on NFVI frameworks and framework offered by OpenStack. 
Once gaps are identified, the next step will be to propose a plan to address these gaps. 
The most obvious way to address the gaps will be to propose a set of APIs in the upstream OpenStack community

<a name="8.2"></a>
## 8.2 The Gaps
* Discovery  - The VNFs and NFVI frameworks should be able to discover each other and exchange their capabilities required or offered. CNTT reference model specifies a model, but OpenStack does not provide APIs to support such capabilities. Following should be supported: 
NFVI should be able to publish the capabilities it offers to VNFs/CNFs
VNFs/CNFs should be able to query the NFVI for specific capabilities - such as number of cores, performance parameters.
Negotiation/Hand Shake API - VNFs and NFVIs should be able to negotiate on certain capabilities. For instance, VNF desires HW acceleration for high throughput, but, should be able to fall back to high throughput offered by NFVI via DPDK offering, and vice-a-versa

* Support Load Balance of VNF/CNFs - Ability to load balance workflows through multiple instances of same VNF or CNF - e.g. using ECMP to distribute workloads through the multiple instances of Firewall. As an example imagine a distributed finance application with multiple instances of Web-tier and DB-tier. The traffic needs to flow through multiple instances of Firewall (for HA as well load balancing). There is no simple way to accomplish this in OpenStack. 

* Service Function Chain - Reference model  makes a reference to SFC support from NFVI. Moreover to support network services, a way is needed to chain the services. Service Function Chain was developed in OpenStack and went dormant. It is not supported and well tested. This requires to be revamped to be useful for CNTT reference architecture

* Packet Acceleration Request (e.g Hardware Acceleration) - Reference model states packet acceleration should be supported. OpenStack does not have such support that could be easily used or automated for deployments of VNFs/NFVIs. 

* Public and Multi-Cloud  - The framework offered by OpenStack does not support multi-cloud of public deployments, along with the core deployments



<a name="8.3"></a>
## 8.3 Heading
