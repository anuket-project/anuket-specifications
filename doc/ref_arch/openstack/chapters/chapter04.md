[<< Back](../../openstack)

# 4. Operationalising the OpenStack IaaS Cloud
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction.](# 4.1)
* [4.2 Network Topology .](#4.2)
  * [4.2.1. Architectural Drivers – Requirements Traceability.](#4.2.1)
  * [4.2.2. Physical Network.](#4.2.2)
  * [4.2.3. High Level Logical Network Layout.](#4.2.3)
  * [4.2.4. LBaaS v2 compliant Load Balancing.](#4.2.4)
  * [4.2.5. Neutron ML2 integration.](#4.2.5)
* [4.3 Cloud Topology.](#4.3)
  * [4.3.1. Host Aggregates, Availability Zones.](#4.3.1)
  * [4.3.2. Cloud Topology Considerations.](#4.3.2)
  * [4.3.3. Containerised OpenStack Services.](#4.3.3)
* [4.4 Compute Node Services.](#4.4)
  * [4.4.1. Hardware Considerations.](#4.4.1)
  * [4.4.2. Minimum Software Versions.](#4.4.2)
* [4.5 Integration Interfaces.](#4.5)
* [4.6 Logging / Monitoring / Alerting of Control Plane.](#4.6)
* [4.7 Telemetry.](#4.7)  **not MVP**
* [4.8 General Hardware requirements (for control, compute, storage) .](#4.8)  **not MVP**
* [4.9. LCM Considerations.](#4.9) **not MVP**
* [4.10. Security Considerations.](#4.10) **not MVP**


<a name="4.1"></a>
## 4.1 Introduction.

Chapter 3 presented the core OpenStack services for creating an IaaS cloud.  The chapter discussed the deployment topology including distribution of the core OpenStack services among Controller and Compute nodes. Chapter 3 also presented security and LCM considerations that play a role in the deployment and management of the services. This Chapter will delve deeper into certain topics that need to be considered in creating and operating an OpenStack based IaaS cloud. The OpenStack IaaS cloud needs the physical (underlay) and the overlay networks needed for intra tenant and external (to the tenant) communications. Cloud topology related to host aggregates and availability zones, and minimal software versions for shared services (kernel, host operating system, common drivers, etc.). To round up the operationalization considerations, the chapter includes a listing of some of the requirements for Security and Life Cycle Management.


<a name="4.2"></a>
## 4.2 Network Topology 

<a name="4.2.1"></a>
### 4.2.1. Architectural Drivers – Requirements Traceability

| Ref # | sub-category | Description |
|--------|---------------|--------------------------------|
| req.inf.ntw.01 | Network | The Architecture must provide virtual network interfaces to VM instances. |
| req.inf.ntw.02 | Network | The Architecture must include capabilities for integrating SDN controllers to support provisioning of network services, from the OpenStack Neutron service, such as networking of VTEPs to the Border Edge based VRFs. |
| req.inf.ntw.03 | Network | The Architecture must support low latency and high throughput traffic needs. |
| req.inf.ntw.04 | Network | The Architecture should support service function chaining. |
| req.inf.ntw.05 | Network | The Architecture must allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay such as VXLAN or Geneve). |
| req.inf.ntw.06 | Network | The Architecture should support Distributed Virtual Routing (DVR) to allow compute nodes to route traffic efficiently. |
| req.inf.ntw.07 | Network | The Architecture must support network resiliency. |
| req.inf.ntw.08 | Network | The NFVI Network Fabric should embrace the concepts of open networking and disaggregation using commodity networking hardware and disaggregated Network Operating Systems. |
| req.inf.ntw.09 | Network | The NFVI Network Fabric should embrace open-based standards and technologies. |
| req.inf.ntw.10 | Network | The NFVI Network Fabric must be capable of supporting highly available (Five 9’s or better) VNF workloads. |
| req.inf.ntw.11 | Network | The NFVI Network Fabric should be architected to provide a standardised, scalable, and repeatable deployment model across all applicable NFVI sites. |
| req.inf.ntw.12 | Network | The SDN solution should be configurable via orchestration or VIM systems in an automated manner using openly published API definitions. |
| req.inf.ntw.13 | Network | The SDN solution should be able to support federated networks. |
| req.inf.ntw.14 | Network | The SDN solution should be able to be centrally administrated and configured. |
| req.inf.ntw.15 | Network | The Architecture must support multiple networking options for NFVI to support various infrastructure profiles (Base, Network Intensive, and Compute Intensive). |
| req.inf.ntw.16 | Network | The Architecture must support dual stack IPv4 and IPv6 for tenant networks and workloads. |
| req.inf.ntw.17 | Network | The Architecture should use dual stack IPv4 and IPv6 for NFVI internal networks. |
| req.inf.acc.01 | Acceleration | The Architecture should support Application Specific Acceleration (exposed to VNFs). |
| req.inf.acc.02 | Acceleration | The Architecture should support NFVI Acceleration (such as SmartNICs). |
| req.sec.ntw.03 | Networking | The Architecture must have the underlay network incorporate encrypted and/or private communications channels to ensure its security. |
| req.sec.ntw.04 | Networking | The Architecture must configure all of the underlay network components to ensure the complete separation from the overlay customer deployments. |

<a name="4.2.2"></a>
### 4.2.2. Physical Network

<p align="center"><img src="../figures/Figure_4_1_Network_Fabric_Physical.png" alt="Network Fabric -- Physical"></br>Figure 4-1. Network Fabric – Physical</p>

Figure 4-1 shows a physical network layout where each physical server is dual homed to TOR (C/Agg-Leaf) switches with redundant (2x) connections.  The Leaf switches are dual homed with redundant connections to spines. 

<a name="4.2.3"></a>
### 4.2.3. High Level Logical Network Layout

A tenant network represents the Layer 2 and Layer 3 network resources that are configured to enable layer-3 routing between networks connecting VMs and the external WAN VPN. Figure 4-2 (<a href="https://docs.openstack.org/newton/install-guide-ubuntu/launch-instance-networks-selfservice.html">OpenStack Self-Srevice (tenant) Networks</a>) shows the connectivity from Tenant VMs through provider networks (and by extension to other Tenant VMs on a different Compute node (server)) and to external networks. The OpenStack Provider networks are shared by all Tenants. Each VNF/VM network interface will be associated with the Tenant network. A tenant network can be local or external; local tenant networks do not have WAN access. External Tenant networks have their VLANs and IP subnets associated with a WAN VPN (Figure 4-2).

<p align="center"><img src="../figures/Figure_4_2_Tenant_Network.png" alt="Tenant Network"></br>Figure 4-2. <a href="https://docs.openstack.org/newton/install-guide-ubuntu/launch-instance-networks-selfservice.html">OpenStack Self-Srevice (tenant) Networks</a></p>

A VNF application network topology is expressed in terms of VMs, vNIC interfaces with vNet access networks, and WAN Networks while the VNF Application VMs require multiple vNICs, VLANs, and host routes configured within the VM’s Kernel.

<a name="4.2.4"></a>
### 4.2.4. LBaaS v2 compliant Load Balancing

<a name="4.2.5"></a>
### 4.2.5. Neutron ML2 integration 

The OpenStack Modular Layer 2 (ML2) plugin simplifies adding networking technologies by utilizing drivers that implement these network types and methods for accessing them.  Each network type is managed by an ML2 type driver and the mechanism driver exposes interfaces to support the actions that can be performed on the network type resources. The <a href="https://wiki.openstack.org/wiki/Neutron/ML2">OpenStack ML2 documentation</a> lists example mechanism drivers.

<a name="4.3"></a>
## 4.3 Cloud Topology

<a name="4.3.1"></a>
### 4.3.1. Host Aggregates, Availability Zones

A host aggregate is a set of hosts with specific properties (multiple software and/or hardware properties); the properties are specified as key-value pairs.  Example would be a host aggregate created for a particular flavour or specific hardware. A host can belong to multiple host aggregates. Host aggregates are not visible to users.

Availability Zones are user visible host aggregates where a host can only be in one availability zone.  Availability zones partition the cloud independent of the infrastructure layout.
Availability zones (AZ) serve a couple of important purposes. Firstly, users can deploy their workloads to create local redundancy for resiliency and high availability.  This permits rolling upgrades – an AZ at a time upgrade with enough time between AZ upgrades to allow recovery of tenant workloads on the upgraded AZ. Secondly, AZs can accommodate hosts with special hardware and software characteristics, for example, hosts with hardware accelerators.

An over use of host aggregates and availability zones can result in a granular partition the cloud and, hence, operational c
omplexities and inefficiencies.

<a name="4.3.2"></a>
### 4.3.2. Cloud Topology Considerations

A Telco cloud will be deployed in multiple locations (“sites”) of varying size and capabilities (HVAC, for example); or stated slightly differently, multiple telco clouds (i.e. OpenStack end points) will be deployed and they all contain isolated resources that do not rely on each other.   The application must span such end points in order to provide the required service SLA Irrespective of the nature of the deployment characteristics (number of racks, number of hosts, etc.), the intent of the architecture would be to allow VNFs to be deployed in these sites as needed without major changes; if not all as many as possible. 
-	Large data center capable of hosting thousands of servers and the networking to support them
-	Mini data center (such as a central office) capable of hosting up to a hundred servers
-	Edge (not customer premise) capable of hosting between ten to fifty servers

Host profiles (SW Host profile + HW host profile) “partition” the cloud into pseudo sub-clouds, for example, hosts targeted for basic instance types, network intensive instance types and compute intensive instance types. This can happen, because of specific hardware adds and/or hardware and software configurations.  Depending upon the workload types and the capacity requirements, cloud providers and operators may choose to support the instance types with targeted hardware (different number of sockets, RAM, clock speeds, etc.) and host profiles or choose common hardware and minimize the number of host profiles (for example, network intensive and compute intensive types using a common host profile).

As we get away from the large data centers to the smaller sites it becomes progressively difficult to be able to create enough capacity for each of these instance types in support of their target VNFs or to have a mix of hardware targeted for each instance type. 

<a name="4.3.3"></a>
### 4.3.3. Containerised OpenStack Services

#### 4.3.3.1. Architectural Drivers – Requirements Traceability

| Ref # | sub-category | Description |
|----|----|-----|
| req.gen.cnt.02 | Cloud nativeness | The Architecture should consist of service components implemented as microservices that are individually dynamically scalable. |
| req.vim.02 | General | The Architecture should support deployment of OpenStack components in containers. |
| req.gen.rsl.01 | Resiliency | The Architecture must support resilient OpenStack components that are required for the continued availability of running workloads. |

#### 4.3.3.2. Justification

ontainers are lightweight compared to Virtual Machines and leads to efficient resource utilization. Kubernetes auto manages scaling, recovery from failures, etc.  Thus, it is recommended that the OpenStack services be containerized for resiliency and resource efficiency.


<a name="4.4"></a>
## 4.4 Compute Node Services

In Section 3.5 the high-level set of infrastructure components needed to run VMs was presented.  This section is primarily about scheduling the VM to be created onto a particular physical server. This section delves into the compute host selection for these VMs, the resource pools, hardware and software considerations.

<p align="center"><img src="../figures/Figure_4_3_Select_host_instance_launch.png" alt="Selection of a compute host to launch an instance"></br>Figure 4-3. Selection of a compute host to launch an instance.</p>

When a request for an instance creation is made, the requested features and capabilities of the instance is used to determine the host on which the instance should be launched (Figure 4-3).  The nova scheduler service matches requested features and capabilities of the instance and the capabilities/configuration of the hosts (hardware and software).  The nova-scheduler can be configured to use the host aggregates (and availability zones) in selecting the hosts when an instance create request with these capabilities/configurations is requested. The Common Telco NFVI has only a handful of standard profiles and hence the number of potential target host servers (Figure 4-3) may be large if only the host-aggregates filter is utilized and, thus, other filters should also be selected; affinity/non-affinity, custom key-value pairs, etc. 

A flavor may, in addition to the base flavor properties, include additional properties specified as key-value pairs in the extra specifications section of the flavour definition.  These additional properties can specify advanced configurations information or desired hardware characteristics. Examples include SSD drives, hardware accelerators, or a key-value pair used as meta data to associate the host with a tenant or host aggregate; both the host aggregate and the hosts that are to be assigned to the host aggregate would be assigned the same key-value pair, for example, <OVS-DPDK, True>. 

<a name="4.4.1"></a>
### 4.4.1. Hardware Considerations

-	Multiple pools of hardware resources where each resource pool caters for workloads of a specific profile (for example, network intensive). Leads to efficient use of the hardware as the server resources are specific to the flavour.  If not properly sized or when demand changes can lead to oversupply/starvation scenarios; reconfiguration may not be possible because of the underlying hardware or inability to vacate servers for reconfiguration to support another flavor type. The specifications for this type of resource pooling is specified in 4.5.2.
-	Single pool of hardware resources including for controllers have the same CPU type. This is operationally efficient as any server can be utilized to support a flavor or controller. The single pool is valuable with unpredictable workloads or when the demand of certain flavours is insufficient to justify individual hardware selection. The specifications for this type of resource pooling is specified in 4.5.3.

<a name="4.4.2"></a>
### 4.4.2. Minimum Software Versions
This section specifies specific software components needed to support the three primary flavor types, Basic, Network Intensive and Compute Intensive, and Controllers. The number of controller nodes and compute nodes is determined by the cloud size and workload needs. For Resiliency and availability, we need at least 3 deployments of each of the Controller node services. The minimum hardware requirements are specified in the Reference Model Chapter 4: Feature set and Requirements from Infrastructure.
Compute Hosts
-	Basic Profile
  -	Software components
     - Virtio 1.1, Open vSwitch (OVS), VXLAN, GENEVE, MPLSoUDP
     - Minimum Linux kernel version:

-	Network Intensive Profile
  -	Software Components
    -	Virtio 1.1, Open vSwitch (OVS), VXLAN, GENEVE, MPLSoUDP, OVS-DPDK (medium throughput), i40evf (Intel driver for SR-IOV (high throughput)
    -	Minimum Linux kernel version: 

- Compute Intensive Profile
  -	Software Components
    - Virtio 1.1, Open vSwitch (OVS), VXLAN, GENEVE, MPLSoUDP, OVS-DPDK (medium throughput), i40evf (Intel driver for SR-IOV (high throughput) 
    - Minimum Linux kernel version:


<a name="4.5"></a>
## 4.5 Integration Interfaces.

**DHCP**
When the Neutron-DHCP agent is hosted in controller nodes, then VMs, on a Tenant network, that need to acquire an IPv4 and/or IPv6 address, the VLAN for the Tenant must be extended to the control plane servers so that the Neutron agent can receive the DHCP requests from the VM and send the response to the VM with the IPv4 and/or IPv6 addresses and the lease time. Please see <a href="https://docs.openstack.org/ocata/networking-guide/deploy-ovs-provider.html">OpenStack provider Network</a>.

**DNS**

**LDAP**

**IPAM**



<a name="4.6"></a>
## 4.6 Logging / Monitoring / Alerting of Control Plane

Enterprises and vendors may have custom monitoring and logging solutions. The intent of the logging and monitoring is to capture events and data of interest to the NFVI and workloads so that appropriate actions can be taken.  Some of the data is to support the metrics collection specified in the <a href="https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter04.md">Reference Model Chapter 4: Infrastructure Capabilities, Metrics and Catalogue</a>.

In this section, a possible framework utilizing Prometheus, Elasticsearch and Kibana is given as an example only. 

<p align="center"><img src="../figures/Figure_4_4_Monitoring_Logging_Framework.png" alt="Monitoring and Logging Framework"></br>
Figure 4-4. Monitoring and Logging Framework </p>

The monitoring and logging framework (Figure 4-4) leverages Prometheus as the monitoring engine and Fluentd for logging. In addition, the framework uses Elasticsearch to store and organize logs for easy access. Prometheus agents pull information from individual components on every host.  Fluentd, an open source data collector, unifies data collection and consumption for better use and understanding of data. Fluentd captures the access, application and system logs.

<a name="4.7"></a>
## 4.7 Telemetry


<a name="4.8"></a>
## 4.8 General Hardware requirements (for control, compute, storage)
- Scaling options for extra compute, storage, throughput
- Shared Storage (Optional)

<a name="4.9"></a>
## 4.9. LCM Considerations
**NOT MVP**

<a name="4.10"></a>
## 4.10. Security Considerations
**NOT MVP**
