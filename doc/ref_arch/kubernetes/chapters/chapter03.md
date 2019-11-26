[<< Back](../../openstack)

# 3. High Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [3.1 Introduction](#3.1)
* [3.2 Infrastructure Services](#3.2)
    * [3.2.1 Container Compute Services](#3.2.1)
        * [3.2.1.1 Memory management](#3.2.1.1)
        * [3.2.1.2 HW Topology management](#3.2.1.2)
        * [3.2.1.3 HW Acceleration](#3.2.1.3)
        * [3.2.1.4 CPU management](#3.2.1.4)
        * [3.2.1.5 Container Runtime Services](#3.2.1.5)
    * [3.2.2 Container Networking Services](#3.2.2)
    * [3.2.3 Container Storage Services](#3.2.3)
    * [3.2.4 Container Package Managers](#3.2.4)
* [3.3 Heading](#3.3)

<a name="3.1"></a>
## 3.1 Introduction

<a name="3.2"></a>
## 3.2 Infrastructure Services

> This chapter shall list the services provided by the infrastructure. Some example of these services can be: log collection, monitoring, health check, load balancer. For the shake of clarity CaaS services should be also listed, like container lifecycle management or networking services.

<a name="3.2.1"></a>
### 3.2.1 Container Compute Services

> This chapter should describe considerations about container compute services.

<a name="3.2.1.1."></a>
#### 3.2.1.1 Memory management

> This chapter should describe considerations about memory management, like huge pages.

<a name="3.2.1.2"></a>
#### 3.2.1.2 HW Topology management

> This chapter should describe considerations about hardware topology management.

<a name="3.2.1.3"></a>
#### 3.2.1.3 HW Acceleration

> This chapter should describe considerations about hardware acceleration, like device management.

<a name="3.2.1.4"></a>
#### 3.2.1.4 CPU management

> This chapter should describe considerations about CPU management.

<a name="3.2.1.5"></a>
#### 3.2.1.5 Container Runtime Services

> This chapter should describe considerations about the services of container runtimes.

<a name="3.2.2"></a>
### 3.2.2 Container Networking Services

Becouse `req.inf.ntw.01` requires the architecture to support CNI and `req.inf.ntw.16` requires the capability to attach several network interfaces to the pods the architecture must suport a CNI metaplugin/CNI multiplexer.

A CNI metaplugin/CNI multiplexer is capable to attach several interfaces, using different other CNI plugins to a pod. The different network charastheristics of the interfaces, which require different networking technologies require different CNI plugins.

Inter node communication required by `req.inf.ntw.02` must be served by a simple CNI using overlay technology, like Flannel.

There are two types of low latency and high throughput networks required by `req.inf.ntw.04`. Network used for signalling traffic are more demanding than what an overlay network can handle, but still does not need the usage of user space networking. Due to the nature of signalling protocols used this type of netorks require the NAT-less communication stated by `req.inf.ntw.03`. Due to the combination of these two requirements networks with this charactheristics must be served by a CNI plugin with IPVLAN or MACVLAN suport.

The low latency, high throughput networks for handling the user plane traffic require the capability to use an user space networking technology, like VPP or DPDK. In case of DPDK the usage of SR-IOV VF-s is recommended.

As `req.inf.ntw.14` mandates the architecture must enable the integration of different SDN solutions via their respective CNI integration.

The architecture must support networking for telecom equipments in an environment where the networks of the CNF-s are set up by the network adminisrators of the telecom operator. This is why, as `req.inf.ntw.10` requires, the architecture must provide a set of abstract management API-s to manage the network connectivity of the CNF pods.
The API must support multiple tennants and must require elevated acces rights to manipulate infrastructure related API objects as these operations require reconfiguration of the physical network infrastructure.

To fullfill the requirements of `req.inf.acc.02` the architecture must support the usage of device plugins via the Device Plugin API, also the alignement of the devices and the CPU topology must be supported using the Topology Manager.

The architecture must support both IPv4, IPv6 and dual stack interfaces of the workloads.
 > How about IPv6 support of the control plane?

As Kubernetes Ingress and Services have no support for all the protocols needed in telecommunication environments and their capacity is limited the architecture must enable the usage alternative load balancers, like external or built into the application.

Well known service meshes have no support for protocols required by telecom applications therefore their suport is not required in the architecture.

As the most recent version of Network Service Mesh is v0.1.0 at the time of specifying RA2 in Snezka release it is not required in the architecture.

<a name="3.2.3"></a>
### 3.2.3 Container Storage Services

> This shapter should discuss storage services provided by the reference architecture. 

<a name="3.2.4"></a>
### 3.2.4 Kubernetes Application package manager

To manage complex applications consisting from several pods the reference architecture may provide support for a Kubernetes Application package manager. The package manager may be able to manage the lifecycle a set of pods and provide a framework to customize a set of parameters for the deployment.
