[<< Back](../../kubernetes)

# 4. Component Level Architecture
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
- [4. Component Level Architecture](#4-component-level-architecture)
  - [Table of Contents](#table-of-contents)
  - [4.1 Introduction](#41-introduction)
  - [4.2 Kubernetes Node](#42-kubernetes-node)
  - [4.3 Kubernetes](#43-kubernetes)
  - [4.4 Container runtimes](#44-container-runtimes)
  - [4.5 Networking solutions](#45-networking-solutions)
  - [4.6 Storage components](#46-storage-components)
  - [4.7 Service meshes](#47-service-meshes)
  - [4.8 Kubernetes Application package manager](#48-kubernetes-application-package-manager)
  - [4.9 Kubernetes workloads](#49-kubernetes-workloads)
  - [4.10 Additional required components](#410-additional-required-components)

<a name="4.1"></a>
## 4.1 Introduction

This chapter describes in detail the Kubernetes Reference Architecture in terms
of the functional capabilities and how they relate to the Reference Model
requirements, i.e. how the infrastructure profiles are determined, documented
and delivered.

The specifications defined in this chapter will be detailed with unique
identifiers, which will follow the pattern: `ra2.<section>.<index>`, e.g.
`ra2.ch.001` for the first requirement in the Kubernetes Node section.  These
specifications will then be used as requirements input for the Kubernetes
Reference Implementation and any Vendor or Community Implementations.

Figure 4-1 below shows the architectural components that are described in the
subsequent sections of this chapter.

<p align="center"><img src="../figures/ch04_k8s_architecture.png"
alt="Kubernetes Reference Architecture" Title="Kubernetes Reference
Architecture" width="65%"/></p>
<p align="center"><b>Figure 4-1:</b> Kubernetes Reference Architecture</p>

<a name="4.2"></a>
## 4.2 Kubernetes Node

This section describes the configuration that will be applied to the physical or
virtual machine and an installed Operating System. In order for a Kubernetes Node
to be conformant with the Reference Architecture it must be implemented as per
the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.ch.001`|Huge Pages|When hosting workloads matching the Network Intensive profile, it must be possible to enable Huge Pages (2048KiB and 1048576KiB) within the Kubernetes Node OS, exposing schedulable resources `hugepages-2Mi` and `hugepages-1Gi`.|[infra.com.cfg.004](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.ch.002`|SR-IOV capable NICs|When hosting workloads matching the Network Intensive profile, the physical machines on which the Kubernetes Nodes run must be equipped with NICs that are SR-IOV capable.|[e.cap.013](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.ch.003`|SR-IOV Virtual Functions|When hosting workloads matching the Network Intensive profile, SR-IOV virtual functions (VFs) must be configured within the Kubernetes Node OS, as the SR-IOV Device Plugin does not manage the creation of these VFs.|[e.cap.013](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.ch.004`|CPU Simultaneous Multi-Threading (SMT)|SMT must be enabled in the BIOS on the physical machine on which the Kubernetes Node runs.|[infra.hw.cpu.cfg.004](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.ch.005`|CPU Allocation Ratio - VMs|For Kubernetes nodes running as Virtual Machines, ensure the CPU allocation ratio between vCPU and physical CPU core is 1:1.|[infra.com.cfg.001](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.ch.006`|CPU Allocation Ratio - Pods|To ensure the CPU allocation ratio between vCPU and physical CPU core is 1:1, the sum of CPU requests and limits by containers in Pod specifications must remain less than the allocatable quantity of CPU resources (i.e. `requests.cpu < allocatable.cpu` and `limits.cpu < allocatable.cpu`).|[infra.com.cfg.001](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.ch.007`|IPv6DualStack|To support IPv4/IPv6 dual stack networking, the Kubernetes Node OS must support and be allocated routable IPv4 and IPv6 addresses.|[req.inf.ntw.04](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ch.008`|Physical CPU Quantity|The physical machines on which the Kubernetes Nodes run must be equipped with at least 2 physical sockets, each of at least 20 CPU cores.|[infra.hw.cpu.cfg.001](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)<br>[infra.hw.cpu.cfg.002](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.ch.009`|Physical Storage|The physical machines on which the Kubernetes Nodes run should be equipped with Sold State Drives (SSDs).|[infra.hw.stg.ssd.cfg.002](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.ch.010`|Local Filesystem Storage Quantity|The Kubernetes Nodes must be equipped with local filesystem capacity of at least 320GB for unpacking and executing containers. Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.|[e.cap.003](./chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|
|`ra2.ch.011`|Virtual Node CPU Quantity|If using VMs, the Kubernetes Nodes must be equipped with at least 16 vCPUs.  Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.|[e.cap.001](./chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|
|`ra2.ch.012`|Kubernetes Node RAM Quantity|The Kubernetes Nodes must be equipped with at least 32GB of RAM. Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.|[e.cap.002](./chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|
|`ra2.ch.013`|Physical NIC Quantity|The physical machines on which the Kubernetes Nodes run must be equipped with at least four (4) Network Interface Card (NIC) ports.|[infra.hw.nic.cfg.001](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.ch.014`|Physical NIC Speed - Basic Profile|The NIC ports housed in the physical machines on which the Kubernetes Nodes run for workloads matching the Basic Profile must be at least 10Gbps.|[infra.hw.nic.cfg.002](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.ch.015`|Physical NIC Speed - Network Intensive Profile|The NIC ports housed in the physical machines on which the Kubernetes Nodes run for workloads matching the Network Intensive profile must be at least 25Gbps.|[infra.hw.nic.cfg.002](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.ch.015`|Physical PCIe slots|The physical machines on which the Kubernetes Nodes run must be equipped with at least eight (8) Gen3.0 PCIe slots, each with at least eight (8) lanes.|
|`ra2.ch.016`|Immutable infrastructure|Whether physical or virtual machines are used, the Kubernetes Node is not changed after it is made ready for use. New changes to the Kubernetes Node are rolled out as new instances. This covers any changes from BIOS through Operating System to running processes and all associated configurations.|[`req.gen.cnt.02`](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ch.017`||||
|`ra2.ch.018`||||
|`ra2.ch.019`||||
|`ra2.ch.020`||||
|`ra2.ch.021`||||

<p align="center"><b>Table 4-1:</b> Host OS Specifications</p>

<a name="4.3"></a>
## 4.3 Kubernetes
> * The version of version range of Kubernetes and the mandatory components needed for Kubernetes (e.g.: etcd, cadvisor)
> * Which optional features are used and which optional API-s are available
> * Which [alpha or beta features](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) are used

In order for the Kubernetes components to be conformant with the Reference Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.k8s.001`|Kubernetes Conformance|The Kubernetes distribution, product, or installer used in the implementation must be listed in the [Kubernetes Distributions and Platforms document](https://docs.google.com/spreadsheets/d/1LxSqBzjOxfGx3cmtZ4EbB_BGCxT_wlxW_xgHVVa23es/edit#gid=0) and marked (X) as conformant for the Kubernetes version that is being used.|[req.gen.cnt.03](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.002`|Highly available etcd|An implementation must consist of either three, five or seven nodes running the etcd service (can be colocated on the master nodes, or can run on separate nodes, but not on worker nodes).|[req.gen.rsl.02 req.gen.avl.01](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.003`|Highly available control plane|An implementation must consist of at least one master node per availability zone or fault domain to ensure the high availability and resilience of the Kubernetes control plane services|[req.gen.rsl.02 req.gen.avl.01](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.004`|Highly available worker nodes|An implementation must consist of at least one worker node per availability zone or fault domain to ensure the high availability and resilience of workloads managed by Kubernetes|[req.gen.rsl.01 req.gen.avl.01 req.kcm.gen.02 req.inf.com.01](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.005`|Kubernetes API Version|In alignment with the [Kubernetes version support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions), an implementation must use one of three latest minor versions (`n-2`). e.g. if the latest version is 1.17 then the RI must use either 1.17, 1.16 or 1.15.|TBC|
|`ra2.k8s.006`|NUMA Support|When hosting workloads matching the Network Intensive profile, the `TopologyManager` and `CPUManager` feature gates must be enabled and configured on the kubelet (note, TopologyManager is enabled by default in Kubernetes v1.18 and later, with CPUManager enabled by default in Kubernetes v1.10 and later). `--feature-gates="...,TopologyManager=true,CPUManager=true" --topology-manager-policy=single-numa-node --cpu-manager-policy=static`|[e.cap.007](./chapter02.md#221-cloud-infrastructure-software-profile-capabilities) [infra.com.cfg.002](./chapter02.md#223-cloud-infrastructure-software-profile-requirements) [infra.hw.cpu.cfg.004](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.k8s.007`|DevicePlugins Feature Gate|When hosting workloads matching the Network Intensive profile, the DevicePlugins feature gate must be enabled (note, this is enabled by default in Kubernetes v1.10 or later). `--feature-gates="...,DevicePlugins=true,..."`|Various, e.g. [e.cap.013, e.cap.014](./chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|
|`ra2.k8s.008`|System Resource Reservations|To avoid resource starvation issues on nodes, reserve compute resources for system daemons and Kubernetes system daemons such as kubelet, container runtime, etc. (requires Kubernetes version 1.17 or later). Use the following kubelet flags: `--reserved-cpus=[a-z]`|TBC|
|`ra2.k8s.009`|CPU Pinning|When hosting workloads matching the Network Intensive profile, in order to support CPU Pinning, the kubelet must be started with the `--cpu-manager-policy=static` option. (Note, only containers in `Guaranteed` pods - where CPU resource `requests` and `limits` are identical - and configured with positive-integer CPU `requests` will take advantage of this. All other Pods will run on CPUs in the remaining shared pool.)|[infra.com.cfg.003](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.k8s.010`|IPv6DualStack|To support IPv6 and IPv4, the `IPv6DualStack` feature gate must be enabled on various components (requires Kubernetes v1.16 or later). kube-apiserver: `--feature-gates="IPv6DualStack=true"`. kube-controller-manager: `--feature-gates="IPv6DualStack=true" --cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR> --service-cluster-ip-range=<IPv4 CIDR>,<IPv6 CIDR> --node-cidr-mask-size-ipv4 ¦ --node-cidr-mask-size-ipv6` defaults to /24 for IPv4 and /64 for IPv6. kubelet: `--feature-gates="IPv6DualStack=true"`. kube-proxy: `--cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR> --feature-gates="IPv6DualStack=true"`|[req.inf.ntw.04](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.011`||||
|`ra2.k8s.012`||||
|`ra2.k8s.013`||||
|`ra2.k8s.014`||||
|`ra2.k8s.015`||||

<p align="center"><b>Table 4-2:</b> Kubernetes Specifications</p>

<!--
> THE BELOW TEXT HAS BEEN COMMENTED AS NEEDS REVIEWING AND REPLACED WITH SPECS IN THE ABOVE TABLE AS PER:
#1635



This Reference Architecture also specifies:

- Master nodes must run the following Kubernetes control plane services:
    - kube-apiserver
    - kube-scheduler
    - kube-controller-manager
- Master nodes can also run the etcd service and host the etcd database, however etcd can also be hosted on separate nodes if desired
- Master node services, including etcd, and worker node services (e.g. consumer workloads) must be kept separate - i.e. there must be at least one master node, and at least one worker node
- Workloads must ***not*** rely on the availability of the master nodes for the successful execution of their functionality (i.e. loss of the master nodes may affect non-functional behaviours such as healing and scaling, but components that are already running will continue to do so without issue). This function is essential for support of Edge type architectures.
- The following kubelet features must be enabled
    - CPU Manager
    - Device Plugin
    - Topology Manager

All kubelet features can be enabled/disabled by using the `feature-gates:` section in the kubelet config file.  e.g.
```
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
feature-gates:
  CPUManager: true|false (BETA - default=true)
  DevicePlugins: true|false (BETA - default=true)
  TopologyManager: true|false (ALPHA - default=false)
```
-->

<a name="4.4"></a>
## 4.4 Container runtimes

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.crt.001`|Conformance with OCI 1.0 runtime spec|The container runtime must be implemented as per the [OCI 1.0](https://github.com/opencontainers/runtime-spec/blob/master/spec.md) (Open Container Initiative 1.0) specification.|TBC|
|`ra2.crt.002`|Kubernetes Container Runtime Interface (CRI)|The kubernetes container runtime must be implemented as per the [Kubernetes Container Runtime Interface (CRI)](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/)|TBC|
<p align="center"><b>Table 4-3:</b> Container Runtime Specifications</p>

<a name="4.5"></a>
## 4.5 Networking solutions

In order for the networking solution(s) to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.ntw.001`|Centralised network administration|The networking solution deployed within the implementation must be administered through the Kubernetes API using native Kubernetes API resources and objects, or Custom Resources.|[`req.inf.ntw.03`](chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.ntw.002`|Container Network Interface|The networking solution deployed within the implementation must use a CNI-conformant Network Plugin for the Default Pod Network, as the alternative (kubenet) does not support cross-node networking or Network Policies.|[`req.inf.ntw.08`](chapter02.md#23-kubernetes-architecture-requirements)<br><br>[`infra.net.cfg.004`](chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.ntw.003`|Multiplexer/meta-plugin CNI Conformance|The networking solution deployed within the implementation must support the use a multiplexer/meta-plugin that conforms with the CNI specification.|[`req.inf.ntw.06`](chapter02.md#23-kubernetes-architecture-requirements)<br><br>[`req.inf.ntw.07`](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.004`|Multiplexer/meta-plugin CNI Plugins|The selected multiplexer/meta-plugin must support the use of multiple CNI-conformant Network Plugins.|[`req.inf.ntw.06`](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.005`|SR-IOV Device Plugin for Network Intensive|When hosting workloads matching the Network Intensive profile, a Device Plugin for SR-IOV must be used.|[`e.cap.013`](chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|
|`ra2.ntw.006`|SR-IOV Network Plugin for Network Intensive|When hosting workloads matching the Network Intensive profile, a CNI-conformant Network Plugin for SR-IOV must be used.|[`e.cap.013`](chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|
|`ra2.ntw.007`|User plane overlay networking|When hosting workloads matching the Network Intensive profile, a CNI network plugin that supports the use of OVS-DPDK or VPP vSwitches should be deployed as part of the networking solution.|[`infra.net.acc.cfg.001`](chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.ntw.008`|NATless connectivity|When hosting workloads that require source and destination IP addresses to be preserved in the traffic headers, a CNI plugin that exposes the pod IP directly to the external networks (e.g. MACVLAN or IPVLAN) is required.|[`req.inf.ntw.14`](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.009`|Optional Device Plugins|When hosting workloads matching the Network Intensive profile that require the use of FPGA or other Acceleration Hardware, a Device Plugin for that FPGA or Acceleration Hardware may be used.|[`e.cap.016`](chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|
|`ra2.ntw.010`|Dual stack CNI|The networking solution deployed within the implementation must use a CNI-conformant Network Plugin that is able to support dual-stack IPv4/IPv6 networking.|[`req.inf.ntw.04`](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.011`||||
|`ra2.ntw.012`||||
|`ra2.ntw.013`||||
|`ra2.ntw.014`||||
|`ra2.ntw.015`||||
|`ra2.ntw.016`||||
|`ra2.ntw.017`||||
|`ra2.ntw.018`||||

<p align="center"><b>Table 4-4:</b> Networking Solution Specifications</p>


<a name="4.6"></a>
## 4.6 Storage components

In order for the storage solution(s) to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.stg.001`| Ephemeral Storage | An implementation must support ephemeral storage, for the unpacked container images to be stored and executed from, as a directory in the filesystem on the worker node on which the container is running. <br>See the [Container runtimes](#4.4) section above for more information on how this meets the requirement for ephemeral storage for containers. ||
|`ra2.stg.002`| Kubernetes Volumes | An implementation may attach additional storage to containers using Kubernetes Volumes. ||
|`ra2.stg.003`| Kubernetes Volumes | An implementation may use Volume Plugins (see `ra2.stg.005` below) to allow the use of a storage protocol (e.g. iSCSI, NFS) or management API (e.g. Cinder, EBS) for the attaching and mounting of storage into a Pod. ||
|`ra2.stg.004`| Persistent Volumes | An implementation may support Kubernetes Persistent Volumes (PV) to provide persistent storage for Pods (requirement 'req.inf.stg.01'.<br>Persistent Volumes exist independent of the lifecycle of containers and/or pods. |[req.inf.stg.01](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/kubernetes/chapters/chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.stg.005`| Storage Extension | Volume plugins must allow for the use of a range of backend storage systems. ||
|`ra2.stg.006`| Container Storage Interface (CSI) | An implementation may support the Container Storage Interface (CSI), an Out-of-tree plugin.<br>In order to support CSI, the  feature gates `CSIDriverRegistry` and `CSINodeInfo` must be enabled.<br>The implementation must use a CSI driver (a full list of CSI drivers can be found [here](https://kubernetes-csi.github.io/docs/drivers.html)). <br>An implementation may support ephemeral storage through a CSI-compatible volume plugin in which case the `CSIInlineVolume` feature gate must be enabled.<br>An implementation may support Persistent Volumes through a CSI-compatible volume plugin in which case  the `CSIPersistentVolume` feature gate must be enabled. | |
 |`ra2.stg.007`|  | An implementation should use Kubernetes Storage Classes to support automation and the separation of concerns between providers of a service and consumers of the service. | |

<p align="center"><b>Table 4-6:</b> Storage Solution Specifications</p>

<!--
> THE BELOW TEXT HAS BEEN COMMENTED AS NEEDS REVIEWING AND REPLACED WITH SPECS IN THE ABOVE TABLE AS PER:
#1638

As described in [chapter 3](./chapter03.md), storage in Kubernetes consists of three types of storage:
1. Ephemeral storage that is used to execute the containers
    - **Ephemeral storage follows the lifecycle of a container**
    - See the [Container runtimes](#4.4) section above for more information how this meets the requirement for ephemeral storage for Pods
1. Kubernetes Volumes, which are used to present additional storage to containers
    - **A Volume follow the lifecycle of a Pod**
    - This is a native Kubernetes capability and therefore `req.inf.stg.01` is supported by default
    - This capability also delivers support for ephemeral storage although depending on the Volume Plugin used there may be additional steps required in order to remove data from disk (not all plugins manage the full lifecycle of the storage mounted using Volumes)
1. Kubernetes Persistent Volumes, which are a subset of the above whose lifecycle persists beyond the lifetime of a Pod to allow for data persistence
    - **Persistent Volumes have a lifecycle that is independent of Containers and/or Pods**
    - This supports the requirement `req.inf.stg.01` for persistent storage for Pods

Volume plugins are used in Kubernetes to allow for the use of a range of backend storage systems. There are two types of Volume plugin:
1. In-tree
    - These plugins are built, linked, compiled and shipped with the core Kubernetes binaries
    - Therefore if a new backend storage system needs adding this is a change to the core Kubernetes code
1. Out-of-tree
    - These plugins allow new storage plugins to be created without any changes to the core Kubernetes code
    - The Container Storage Interface (CSI) is such an out-of-tree plugin and many in-tree drivers are being migrated to use the CSI plugin instead (e.g. the [Cinder CSI plugin](https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/using-cinder-csi-plugin.md))
    - In order to support CSI, the following feature gates must be enabled:
      - `CSIDriverRegistry`
      - `CSINodeInfo`
    - In addition to these feature gates, a CSI driver must be used (as opposed to an in-tree volume plugin) - a full list of CSI drivers can be found [here](https://kubernetes-csi.github.io/docs/drivers.html)
    - In order to support ephemeral storage use through a CSI-compatible volume plugin, the `CSIInlineVolume` feature gate must be enabled
    - In order to support Persistent Volumes through a CSI-compatible volume plugin, the `CSIPersistentVolume` feature gate must be enabled

> In order to support automation and the separation of concerns between providers of a service and consumers of the service, Kubernetes Storage Classes should be used. Storage Classes allow a consumer of the Kubernetes platform to request Persistent Storage using a Persistent Volume Claim and for a Persistent Volume to be dynamically created based on the "class" that has been requested. This avoids having to grant `create`/`update`/`delete` permissions in RBAC to PersistentVolume resources, which are cluster-scoped rather than namespace-scoped (meaning an identity can manage all PVs or none).
-->
A note on object storage:
- This Reference Architecture does not include any specifications for object
storage, as this is neither a native Kubernetes object, nor something that is
required by CSI drivers.  Object storage is an application-level requirement
that would ordinarily be provided by a highly scalable service offering rather
than being something an individual Kubernetes cluster could offer.  

> Todo: specifications/commentary to support req.inf.stg.04 (SDS) and req.inf.stg.05 (high performance and horizontally scalable storage). Also req.sec.gen.06 (storage resource isolation), req.sec.gen.10 (CIS - if applicable) and req.sec.zon.03 (data encryption at rest).


<a name="4.7"></a>
## 4.7 Service meshes

Application service meshes are not in scope for the architecture.  Network
service mesh specifications are handled in section [4.5 Networking
solutions](#4.5).

<a name="4.8"></a>
## 4.8 Kubernetes Application package manager

In order for the storage solution(s) to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.pkg.001`|API-based package management|A package manager must use the Kubernetes APIs to manage application artefacts. Cluster-side components such as Tiller are not supported.|[req.int.api.02](./chapter02.md#23-kubernetes-architecture-requirements)|

<p align="center"><b>Table 4-7:</b> Kubernetes Application Package Management Specifications</p>

<a name="4.9"></a>
## 4.9 Kubernetes workloads

In order for the Kubernetes workloads to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.app.001`|[Root](https://github.com/opencontainers/runtime-spec/blob/master/config.md) Parameter Group (OCI Spec)|Specifies the container's root filesystem.|TBD|
|`ra2.app.002`|[Mounts](https://github.com/opencontainers/runtime-spec/blob/master/config.md#mounts) Parameter Group (OCI Spec)|Specifies additional mounts beyond root|TBD|
|`ra2.app.003`|[Process](https://github.com/opencontainers/runtime-spec/blob/master/config.md#process) Parameter Group (OCI Spec)|Specifies the container process|TBD|
|`ra2.app.004`|[Hostname](https://github.com/opencontainers/runtime-spec/blob/master/config.md#hostname) Parameter Group (OCI Spec)|Specifies the container's hostname as seen by processes running inside the container|TBD|
|`ra2.app.005`|[User](https://github.com/opencontainers/runtime-spec/blob/master/config.md#user) Parameter Group (OCI Spec)|User for the process is a platform-specific structure that allows specific control over which user the process runs as|TBD|
<p align="center"><b>Table 4-8:</b> Kubernetes Workload Specifications</p>

<a name="4.10"></a>
## 4.10 Additional required components

> This chapter should list any additional components needed to provide the services defined in Chapter 3.2 (e.g: Prometheus)
