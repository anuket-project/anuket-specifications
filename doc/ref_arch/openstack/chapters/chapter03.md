[<< Back](../../openstack)

# 3. Core NFVI and OpenStack Services for an IaaS Cloud
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Introduction.](#3.1)
  * [3.1.1. Architectural Drivers – Requirements Traceability.](#3.1.1)
  * [3.1.2. Core NFVI Software Services.](#3.1.2)
* [3.2 NFVI Software Services Topology.](#3.2)
  * [3.2.1. Architectural Drivers – Requirements Traceability.](#3.2.1)
  * [3.2.2. Topology.](#3.2.2)
* [3.3 Foundation.](#3.3)
  * [3.3.1. Architectural Drivers – Requirements Traceability.](#3.3.1)
  * [3.3.2. Foundation Node.](#3.3.2)
* [3.4 Cloud Controller Services.](#3.4)
  * [3.4.1. Architectural Drivers – Requirements Traceability.](#3.4.1)
  * [3.4.2. Overview.](#3.4.2)
* [3.5 Cloud Workload Services.](#3.5)



<a name="3.1"></a>
## 3.1 Introduction

<a name="3.1.1"></a>
### 3.1.1. Architectural Drivers – Requirements Traceability

| Ref #| sub-category| Description| 
|--------|--------------------|--------------------------------------------|
| req.gen.cnt.01| Cloud nativeness | The Architecture should consist of stateless service components. However, where state is required it must be kept external to the component. | 
| req.gen.rsl.01| Resiliency| The Architecture must support resilient OpenStack components that are required for the continued availability of running workloads. | 
| req.gen.rsl.02| Resiliency| The Architecture should support resilient OpenStack service components that are not subject to req.gen.rsl.01. | 
| req.gen.avl.01| Availability| The Architecture must provide High Availability for OpenStack components. | 

<a name="3.1.2"></a>
### 3.1.2. Core NFVI Software Services

The Common Telco NFVI OpenStack Reference Architecture aims to provide an industry standard reference architecture independent of the many distributions of OpenStack.  It does not seek to change any vendor implementation assuming Common Telco NFVI compliance out of the box without vendor specific enhancements that are not up-streamed.

This document assumes a good understanding of OpenStack core services and will not repeat details found at <a href="https://openstack.org">OpenStack website</a>.  Its primary aim is to highlight the important considerations needed by all operators to deploy NFVI in a consistent, cost effective and predictable way and allowing vendors to work on a level technical playing field. 

Since OpenStack is a complex, multi-project framework, we initially will focus on the core services required to provide Infrastructure-as-a-Service (IaaS) as this is generally all that is required for NFVi/VIM use cases.   Other components are optional and provide functionality above and beyond NFVi/VIM requirements.

The architecture consists of the services shown in the Figure 3-1.   The rest of this document will address the specific Common Telco NFVI implementation requirements and recommendations.

<p align="center"><img src=”../figures/Figure_3_1_Core_NFVI_Services.png” alt=” Core NFVI Software Services”></br>
Figure 3-1. Core NFVI Software Services</p>

We will refer to the functions above as falling into the following categories to avoid any confusion with other terminology that may be used:
-	Control nodes
-	Foundation node
-	Compute nodes 
-	Other supporting service nodes e.g. network, shared storage, logging, monitoring and alerting.

Each deployment of OpenStack should be a unique cloud with its own API endpoint.  Sharing underlying cloud resources across OpenStack clouds is not recommended.


<a name="3.2"></a>
## 3.2 NFVI Software Services Topology

<a name="3.2.1"></a>
### 3.2.1. Architectural Drivers – Requirements Traceability

| Ref #	sub-category	Description |
|-----------------|----------------------|------------------------------|
| req.gen.rsl.01 \ Resiliency | The Architecture must support resilient OpenStack components that are required for the continued availability of running workloads. |
| req.vim.02 | General | The Architecture should support deployment of OpenStack components in containers. |

<a name="3.2.2"></a>
### 3.2.2. Topology

NFVI software services are distributed over 2 planes: 
-	Control Plane that hosts all Control and Management services 
-	Data Plane (a.k.a. User plane) that provides physical and virtual resources (compute, storage and networking) for the actual virtual workloads to run.

The architecture based on OpenStack technology relies on different types of nodes associated with specific roles:
- Controller node types with control and management services, which include VIM functionalities
- Compute node types running workloads
- Network node types offering L3 connectivity
- Storage node types offering external attached storage (block, object, flat files)

The data plane consists of the compute nodes. It is typical to consider the other node types to be part of the control plane.
Figure 3-2 depicts the 4 types of nodes constitutive of the Infrastructure: control, compute, network and storage nodes.

<p align="center"><img src=”../figures/Figure_3_2_ NFVI_Software_Services_Topology.png” alt=” NFVI Software Services Topology”></br>
Figure 3-2. NFVI Software Services Topology</p>

Deployments can be structured using the distribution of services amongst the 4 node types as depicted in Figure 3-2, but depending on workloads requirements, OpenStack services can also be hosted on the same nodes. For instance, services related to Controller, network and storage roles can be hosted on controller nodes.

<a name="3.3"></a>
## 3.3 Foundation/Deployment Node

<a name="3.3.1"></a>
### 3.3.1 Architectural Drivers – Requirements Traceability

Ref #|sub-category|Description |
|--------|-------------|---------------------------|
| req.lcm.adp.04 | Automated deployment | The Architecture should support declarative specifications of hardware and software assets for automated deployment, configuration, maintenance and management. |
| req.lcm.adp.05 | Automated deployment | The Architecture should support automated process for Deployment and life-cycle management of VIM Instances. |

<a name="3.3.2"></a>
### 3.3.2. Foundation Node
To build and lifecycle manage an OpenStack cloud it is typically necessary to deploy a server or virtual machine as a deployment node.  

This function must be able to manage the bare-metal provisioning of the hardware resources but since this does not affect cloud execution it can be detached from the OpenStack cloud and an operator can select their own tooling as they wish.   
Functional requirements of this node include:
-	Build the cloud (control, compute, storage, network hardware resources)
-	Patch management / upgrades / change management
-	Grow / Shrink resources


<a name="3.4"></a>
## 3.4 Cloud Controller Services

<a name="3.4.1"></a>
### 3.4.1. Architectural Drivers – Requirements Traceability

| Ref # | sub-category | Description  |
|--------|-------------|---------------------------|
| req.gen.ost.01 | Open source | The Architecture must use OpenStack APIs.  |
| req.gen.ost.02 | Open source | The Architecture must support dynamic request and configuration of virtual resources (compute, network, storage) through OpenStack APIs.  |
| req.gen.cnt.01 | Cloud nativeness | The Architecture should consist of stateless service components. However, where state is required it must be kept external to the component.  |
| req.gen.cnt.02 | Cloud nativeness | The Architecture should consist of service components implemented as microservices that are individually dynamically scalable.  |
| req.gen.rsl.01 | Resiliency | The Architecture must support resilient OpenStack components that are required for the continued availability of running workloads.  |
| req.gen.rsl.02 | Resiliency | The Architecture should support resilient OpenStack service components that are not subject to req.gen.rsl.01.  |
| req.gen.avl.01 | Availability | The Architecture must provide High Availability for OpenStack components.  |
| req.vim.02 | General | The Architecture should support deployment of OpenStack components in containers.  |
| req.vim.05 | General | The Architecture must include image repository management.  |
| req.vim.06 | General | The Architecture must allow orchestration solutions to be integrated with VIM.  |
| req.sec.gen.03 | General | The Architecture must support a centralised authentication and authorisation mechanism.  |
| req.sec.zon.01 | Zoning | The Architecture must support identity management (specific roles and permissions assigned to a domain or tenant).  |
| req.inf.stg.06 | Storage | The Architecture should make the immutable images available via location independent means.  |
| req.inf.ntw.01 | Network | The Architecture must provide virtual network interfaces to VM instances.  |
| req.inf.ntw.02 | Network | The Architecture must include capabilities for integrating SDN controllers to support provisioning of network services, from the OpenStack Neutron service, such as networking of VTEPs to the Border Edge based VRFs.  |
| req.inf.ntw.05 | Network | The Architecture must allow for East/West tenant traffic within the cloud (via tunnelled encapsulation overlay such as VXLAN or Geneve).  |
| req.inf.com.01 | Compute | The Architecture must provide compute resources for VM instances.  |
| req.inf.stg.01 | Storage | The Architecture must provide shared Block storage for VM Instances.  |
| req.inf.stg.02 | Storage | The Architecture must provide shared Object storage for VM Instances.  |
| req.inf.stg.03 | Storage | The Architecture may provide local file system storage solution for VM Instances.  |
| req.int.api.02 | API | The Architecture must provide GUI access to tenant facing cloud platform core services.  |
| req.tnt.gen.02 | General | The Architecture must support self-service dashboard (GUI) and APIs for users to deploy, configure and manage their workloads.  |


<a name="3.4.2"></a>
### 3.4.2. Overview 
The following OpenStack components are deployed on the Infrastructure. Some of them will be only deployed within control plane and some of them will be deployed within both control and compute nodes:

| Service  |  Description  | Deployed on Controller Nodes | Deployed on Compute Nodes |
|-----------|-------------|-----------|-----------------|
| Keystone  |  the authentication service  | X |  |
| Glance  |  the image management service  | X |  |
| Cinder  |  the block storage management service  | X |  |
| Swift  |  the Object storage management service  | X | X |
| Neutron  |  the network management service  | X | X |
| Nova  |  the compute resources management service  | X | X |
| Ironic  | the Bare Metal Provisioning service  | X | X |
| Heat  |  the orchestration service  | X |  |
| Horizon  |  the WEB UI service  | X |  |

All components must be deployed within a high available architecture that can withstand at least a single node failure and respects the anti-affinity rules for the location of the services (i.e. instances of a same service must run on different nodes). 

The services can be containerized or VM hosted as long as they provide the high availability principles described above.

#### 3.4.2.1. Keystone
Keystone is the authentication service, the foundation of identity management in OpenStack. Keystone needs to be the first deployed service. Keystone has services running on the control nodes and no services running on the compute nodes:
-	Keystone admin API
-	Keystone public API – in Keystone V3 this is the same as the admin API,

| ** OpenStack Service ** | ** Link for API and CLI  ** | ** API/client Baseline Version ** |
|------------------|----------------------------------------------------|-------------------|
|Identity: Keystone | https://docs.openstack.org/api-ref/identity/v3/index.html | Version 3.10 |
|Identity: Keystone | https://docs.openstack.org/python-keystoneclient/latest/using-api-v3.html | Version 3.10 |

#### 3.4.2.2 Glance
Glance is the image management service. Glance has only a dependency on the Keystone service therefore it is the second one deployed. Glance has services running on the control nodes and no services running on the compute nodes:
-	Glance API,
-	Glance Registry.

| ** OpenStack Service ** | ** Link for API and CLI  ** | ** API/Client Baseline Version ** |
|------------------|----------------------------------------------------|-------------------|
| Imaging: Glance | https://docs.openstack.org/api-ref/image/v2/index.html#images | Version 2.0 |
| Imaging: Glance | https://docs.openstack.org/python-glanceclient/latest/ | Version 2.0 |

#### 3.4.2.3. Cinder 
Cinder is the block device management service, Cinder depends on Keystone and possibly Glance to be able to create volumes from images. Cinder has services running on the control nodes and no services running on the compute nodes:
-	Cinder API,
-	Cinder Scheduler,
-	Cinder Volume – the Cinder volume process needs to talk to its backends.

| ** OpenStack Service ** | ** Link for API and CLI ** | ** API/CLI Baseline Version ** |
|------------------|----------------------------------------------------|-------------------|
|Block Storage: Cinder | https://docs.openstack.org/api-ref/block-storage/v3/index.html#api-versions/a> | Version 3.0 |

#### 3.4.2.4. Swift
Swift is the object storage management service, Swift depends on Keystone and possibly Glance to be able to create volumes from images. Swift has services running on the control nodes and the compute nodes:
-	Proxy Services
-	Object Services
-	Container Services
-	Account Services 

| ** OpenStack Service ** | ** Link for API and CLI ** | ** API/CLI Baseline Version ** |
|------------------|----------------------------------------------------|-------------------|
| Object Storage: Swift | https://docs.openstack.org/api-ref/object-store/ | Version 1.0 |
| Object Storage: Swift |https://docs.openstack.org/python-swiftclient/latest/ | Version 1.0 |
When images are stored in block storage service, Cinder, the object storage service, Swift, may not be required. 

#### 3.4.2.5. Neutron
Neutron is the networking service, Neutron depends on Keystone and has services running on the control nodes and the compute nodes:
-	neutron-api
-	neutron-rpc
-	neutron-*-agent agents which runs on Compute and Network nodes

| ** OpenStack Service ** | ** Link for API and CLI ** | ** API/CLI Baseline Version ** |
|------------------|----------------------------------------------------|-------------------|
| Networking: Neutron | https://docs.openstack.org/api-ref/network/ | Version 2.0 |
| Networking: Neutron | https://docs.openstack.org/python-neutronclient/latest/cli/index.html | Version 2.0 |

#### 3.4.2.6. Nova
Nova is the compute management service, Nova depends on all above components and is deployed after. Nova has services running on the control nodes and the compute nodes:
-	nova-metadata-api
-	nova-placement-api
-	nova-compute api
-	nova-consoleauth
-	nova-scheduler
-	nova-conductor
-	nova-novncproxy
-	nova-compute-agent which runs on Compute node

| ** OpenStack Service ** | ** Link for API and CLI ** | ** API/CLI Baseline Version ** |
|--------------|------------------|---------------------------------------|
| Compute: Nova | https://docs.openstack.org/api-ref/compute/ | Version 2.1 |
| Compute: Nova | https://docs.openstack.org/python-novaclient/latest/cli/index.html | Version 2.1 |

#### 3.4.2.7. Ironic
Ironic is the bare metal provisioning service. Ironic depends on all above components and is deployed after. Ironic has services running on the control nodes and the compute nodes:
-	Ironic API
-	ironic-conductor which executes operation on bare metal nodes 

| ** OpenStack Service ** | ** Link for API and CLI ** | ** API/CLI Baseline Version ** |
|------------------|----------------------------------------------------|-------------------|
| Bare Metal: Ironic | https://docs.openstack.org/api-ref/baremetal/ | Version 1.0 |
| Bare Metal: Ironic | https://docs.openstack.org/python-ironicclient/latest/cli/index.html | Version 1.25 |

#### 3.4.2.8. Heat
Heat is the orchestration service using template to provision cloud resources, Heat integrates with all OpenStack services. Heat has services running on the control nodes and no services running on the compute nodes:
-	heat-api
-	heat-cfn-api
-	heat-engine

|** OpenStack Service ** | ** Link for API and CLI ** | ** API/CLI Baseline Version ** |
|------------------|----------------------------------------------------|-------------------|
| Bare Metal: Heat | https://docs.openstack.org/api-ref/orchestration/v1/index.html#api-versions | Version 1.0 |
| Bare Metal: Heat | https://docs.openstack.org/python-heatclient/latest/ | Version 1.25 |

#### 3.4.2.9. Horizon
Horizon is the Web User Interface to all OpenStack services. Horizon has services running on the control nodes and no services running on the compute nodes.


<a name="3.5"></a>
## 3.5 Compute Node Services

This section describes the high-level set of infrastructure components needed to run VMs and provide their compute, network and storage resources. The core set of services and service components needed to run workloads including instances (such as VMs), their networks and storage are referred to as the “Compute Node Services” (a.k.a. user or data plane services).  Contrast this with the Controller nodes which host OpenStack services used for cloud administration and management. The Compute Node Services include virtualisation, hypervisor instance creation/deletion, networking and storage services; some of these activities include RabbitMQ queues in the control plane including the scheduling, networking and cinder volume creation / attachment.
-	Compute, Storage, Network services: Section 3.4 lists the OpenStack service components that are deployed in the data plane (viz., Compute nodes).
  -	Nova Compute service: nova-compute (creating/deleting instances)
  -	Neutron Networking service: neutron-l2-agent (manage local Open vSwitch (OVS) configuration), VXLAN
  -	Local Storage (Ephemeral, Root, etc.)
  -	Attached Storage (using Local drives)
-	Virtualisation Services: The OpenStack nova-compute service supports multiple hypervisors natively or through libvirt. The supported hypervisors include ESXi (primarily through VMware vSphere) and QEMU/KVM through libvirt. Since the hypervisor plays a critical role for virtualized workloads including their isolation from each other, the selection of the hypervisor should be guided by security considerations in addition to other factors such as efficiency and resiliency. 

The number of Compute nodes (for workloads) determines the load on the controller nodes and networking traffic and, hence, the number of controller nodes needed in the OpenStack cloud; the number of controller nodes required is determined on the load placed on these controller nodes and the need for High availability and quorum requires at least 3 instances of many of the services on these controller nodes.

