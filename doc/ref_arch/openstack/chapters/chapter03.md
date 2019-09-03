[<< Back](../../openstack)

# 3. High Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.x xxx.](#3.x)


<a name="3.1"></a>

## 3.1 Introduction
- Architectural drivers (from requirements)
- Core NFVI Software services to meet requirements (minimum set of commonly utilized services)

<a name="3.2"></a>

## 3.2 NFVI Software Services Topology
- Distribution options for control, storage, compute nodes etc. e.g.  >=3 control nodes 
  – also include options for Edge – cater for multiple sized clouds / edge?
  - Baseline versions

<a name="3.3"></a>

## 3.3 Foundation
- Baremetal cloud creation

<a name="3.4"></a>

## 3.4 Control Plane
- Highly available OpenStack Services 
<!-- - Core APIs (keystone, heat, nova, neutron, cinder, glance)
- Logging / Monitoring / Alerting (should this be a separate section on its own?)
- Identity Management
-->

<a name="3.5"></a>

## 3.5 User Plane
- Abstraction of Compute, Storage, Network resources (this is covered in RM Chapter 3)
- Tenant separation (this is covered in RM Chapter 3)

<a name="3.6"></a>

## 3.6 Interfaces

<a name="3.7"></a>

## 3.7 APIs 
