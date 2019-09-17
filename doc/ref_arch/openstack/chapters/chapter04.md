[<< Back](../../openstack)

# 4. Component Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction.](#4.1)
* [4.2 Network Topology.](#4.2)
* [4.3 Cloud Topology.](#4.3)
* [4.4 Cloud Controller Services.](#4.4)
* [4.5 Cloud Workload Services.](#4.5)
* [4.6 Integration / Interfaces.](#4.6)
* [4.7 Logging / Monitoring / Alerting of Control Plane.](#4.7)
* [4.8 Telemetry.](#4.8)
* [4.9 General Hardware requirements.](#4.9)

<a name="4.1"></a>
## 4.1 Introduction.

This should focus on IaaS elements.

<a name="4.2"></a>
## 4.2 Network Topology (control plane, storage, tenant, external)
- Physical Network = Spine / Leaf with dual homing to ToR
- Proposed logical network layout – VLANs, overlay, FIPs, IPv6   – we will follow common vendor recommendations however we can agree on our minimum expectations
- LBaaS v2 compliant Load Balancing
- Neutron ML2 integration to any external SDN controller


<a name="4.3"></a>
## 4.3 Cloud Topology
- Host aggregates / AZs / pools /  scheduler hints
- Default tenant configuration and topologies


<a name="4.4"></a>
## 4.4 Cloud Controller Services
- Core Components (keystone, heat, nova, neutron, glance)
- Identity Management


<a name="4.5"></a>
## 4.5 Cloud Workload Services.

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
    - > for example: vSwitch DPDK + Open Contrail
  - Hardware Platform
  - > for example: dual socket platform. 2x25G NIC, GPU, etc.


<a name="4.6"></a>
## 4.6 Integration / Interfaces
- Detail integration to other supporting services (enablers) – LDAP, DNS, etc.
- Enterprise systems for Identity Management, IP Address Management, …


<a name="4.7"></a>
## 4.7 Logging / Monitoring / Alerting of Control Plane
- Prometheus


<a name="4.8"></a>
## 4.8 Telemetry


<a name="4.9"></a>
## 4.9 General Hardware requirements (for control, compute, storage)
- Scaling options for extra compute, storage, throughput
- Shared Storage (Optional)
