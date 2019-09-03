[<< Back](../../openstack)

# 4. Component Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.xx xx.](#4.x)

<a name="4.1"></a>

## 4.1 Introduction.

This should focus on IaaS elements.

<a name="4.2"></a>

## 4.2 Foundational Components.
Components here will not change amongst different profiles

- Enabler services.

## 4.3 Network Topology (control plane, storage, tenant, external)
- Physical Network = Spine / Leaf with dual homing to ToR
- Proposed logical network layout – VLANs, overlay, FIPs, IPv6   – we will follow common vendor recommendations however we can agree on our minimum expectations
- LBaaS v2 compliant Load Balancing 
- Neutron ML2 integration to any external SDN controller


## 4.4 Cloud Topology
- Host aggregates / AZs / pools /  scheduler hints
- Default T-Shirt sizes – predefined Flavors
- Default tenant configuration and topologies
- Host Profile choices for “any workload, any host” (prevent partitioning of the cloud)


## 4.5 Control Plane
- Core Components (keystone, heat, nova, neutron, cinder, glance)
- Logging / Monitoring / Alerting (should this be a separate section on its own?)
- Identity Management


<a name="4.4"></a>

## 4.6 Data Plane Components.

- Basic Profile
  - Software components
    - > for example: vSwitch.
  - Hardware Platform
    - > for example: single socket platform. 2x10G NIC, etc.


- Network Intensive Profile
  - Software Components
    - > for example: vSwitch DPDK + Contrail
  - Hardware Platform
    - > for example: dual socket platform. 2x25G NIC, CryptoAcc, etc. 

- Compute Intensive Profile 
  - Software Components
    - > for example: vSwitch DPDK + Contrail 
  - Hardware Platform
  - > for example: dual socket platform. 2x25G NIC, GPU, etc.

## 4.7 Integration / Interfaces
- Detail integration to other supporting services (enablers) – LDAP, DNS, etc.
- Enterprise systems for Identity Management, IP Address Management, …

## 4.8 Logging / Monitoring / Alerting of Control Plane / Prometheus

## 4.9 Telemetry

## 4.10 General Hardware requirements (for control, compute, storage)
- Scaling options for extra compute, storage, throughput
- Shared Storage (Optional)
