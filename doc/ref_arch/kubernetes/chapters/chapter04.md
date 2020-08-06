[<< Back](../../kubernetes)

# 4. Component Level Architecture
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Container Host](#4.2)
* [4.3 Kubernetes](#4.3)
* [4.4 Container runtimes](#4.4)
* [4.5 Networking solutions](#4.5)
* [4.6 Storage components](#4.6)
* [4.7 Service meshes](#4.7)
* [4.8 Container package managers](#4.8)
* [4.9 Kubernetes workloads](#4.9)
* [4.10 Supplementary components](#4.10)

<a name="4.1"></a>
## 4.1 Introduction

This chapter describes in detail the Kubernetes Reference Architecture in terms of the functional capabilities and how they relate to the Reference Model requirements, i.e. how the infrastructure profiles are determined, documented and delivered.

The specifications defined in this chapter will be detailed with unique identifiers, which will follow the pattern: `ra2.<section>.<index>`, e.g. `ra2.ch.001` for the first requirement in the Container Host section.  These specifications will then be used as requirements input for the Kubernetes Reference Implementation and any Vendor or Community Implementations.

Figure 4-1 below shows the architectural components that are described in the subsequent sections of this chapter.

<p align="center"><img src="../figures/ch04_k8s_architecture.png" alt="Kubernetes Reference Architecture" Title="Kubernetes Reference Architecture" width="65%"/></p>
<p align="center"><b>Figure 4-1:</b> Kubernetes Reference Architecture</p>

<a name="4.2"></a>
## 4.2 Container Host

This section describes the configuration that will be applied to the physical or virtual machine and an installed Operating System.
In order for a Container Host to be conformant with the Reference Architecture it must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.ch.001`||||
|`ra2.ch.002`||||
|`ra2.ch.003`||||

<p align="center"><b>Table 4-1:</b> Host OS Specifications</p>

<!--
> THE BELOW TEXT HAS BEEN COMMENTED AS NEEDS REPLACING WITH SPECS IN THE ABOVE TABLE AS PER:
#991
#920
#1184
#1634

- A version of the Linux kernel that is [compatible with kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/implementation-details/#kubeadm-init-workflow-internal-design) - this has been chosen as the baseline because kubeadm is concerned with nothing other than installing and managing the lifecycle of Kubernetes, hence it is easily integrated into higher-level and more complete tooling for the full lifecycle management of the infrastructure, cluster add-ons, and other tools and applications required for the full system.
- Windows Server 2019 (this can be used for worker nodes, but be aware of the [limitations](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#limitations)).
- Support `req.gen.cnt.02` (immutable infrastructure), which means that the Host OS must be easily reproduced, consistent, disposable, with a repeatable deployment process, and will not have configuration or artifacts that are modifiable in place (i.e. once it is in a  running state).
- The selection of Host OS shall not restrict the selection of the OS used to build container images (container base image).

Table 4-1 lists the Linux kernel versions that comply with this Reference Architecture specification.

|OS Family|Version(s)|Notes|
|---|---|---|
|Linux|3.10+||
|Windows|1809 (10.0.17763)|For worker nodes only|

<p align="center"><b>Table 4-1:</b> Conformant OS Kernels</p>
-->


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
|`ra2.k8s.004`|Highly available worker nodes|An implementation must consist of at least one worker node per availability zone or fault domain to ensure the high availability and resilience of workloads managed by Kubernetes|[req.gen.rsl.01 req.gen.avl.01 req.kcm.gen.02](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.005`|Kubernetes API Version|In alignment with the [Kubernetes version support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions), an implementation must use one of three latest minor versions (`n-2`). e.g. if the latest version is 1.17 then the RI must use either 1.17, 1.16 or 1.15.|TBC|
|`ra2.k8s.006`||||
|`ra2.k8s.007`||||

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

In order for the Container runtime(s) to be conformant with the Reference Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.crt.001`||||
|`ra2.crt.002`||||
|`ra2.crt.003`||||
|`ra2.crt.004`||||

<p align="center"><b>Table 4-3:</b> Container Runtime Specifications</p>

<!--
> THE BELOW TEXT HAS BEEN COMMENTED AS NEEDS REVIEWING AND REPLACED WITH SPECS IN THE ABOVE TABLE AS PER:
#1636

The chosen runtime must be conformant with the [Kubernetes Container Runtime Interface (CRI)](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/) and the [Open Container Initiative (OCI) runtime spec](https://github.com/opencontainers/runtime-spec). Examples of container runtimes that are conformant with these specification in no particular order are:
- container-d (with CRI plugin enabled, which it is by default)
- Docker CE (via the dockershim, which is currently built in to the kubelet)
- CRI-O
- Frakti
The above list is by no means intended to be a complete listing of all the possible options for container runtimes.

To support `req.inf.vir.01` the architecture specifies the use of a container runtime with the capability for Kernel isolation:
- kata-containers

These specifications cover the [full lifecycle of a container](https://github.com/opencontainers/runtime-spec/blob/master/runtime.md#lifecycle) `creating > created > running > stopped` which includes the use of any storage required during the lifecycle of the container, including the management of the Host OS filesystem by the container runtime. This lifecycle management by the container runtime (when conformant with the above specifications) supports ephemeral storage for Pods.

To support the isolation of the resources used by the infrastructure from the resources used by the workloads the architecture specifies the use of the Kubernetes CPU Manager and [CPU Pooler](https://github.com/nokia/CPU-Pooler/).

-->

<a name="4.5"></a>
## 4.5 Networking solutions

In order for the networking solution(s) to be conformant with the Reference Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.ntw.001`|CNI multiplexer/metaplugin|As the selected CNI multiplexer/metapulgin MUST support other CNI plugins (`req.inf.ntw.06`) and SHOULD provide an API based solution to administer the networks from a central point (`req.inf.ntw.03`) the selected CNI multiplexer/metapulgin must be [DANM](https://github.com/nokia/danm).| [req.inf.ntw.06](./chapter02.md#23-kubernetes-architecture-requirements), [req.inf.ntw.03](./chapter02.md#23-kubernetes-architecture-requirements) |
|`ra2.ntw.002`|CNI to implement a default network which implements the Kubernetes network model|[Calico](https://github.com/projectcalico/cni-plugin) must be used based on the requirement `req.inf.ntw.08` due to it's capability to handle `NetworkPolicies`|[req.inf.ntw.08](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.003`|NAT less connectivity|IPVLAN CNI component of DANM or the [MACVLAN CNI](https://github.com/containernetworking/plugins/tree/master/plugins/main/macvlan) must be used||
|`ra2.ntw.004`|User plane networks|[User Space CNI](https://github.com/intel/userspace-cni-network-plugin) must be used. The User Space CNI may use VPP or OVS-DPDK as a backend.||
|`ra2.ntw.005`|SR-IOV|[SR-IOV CNI plugin](https://github.com/intel/sriov-cni) must be used||
|`ra2.ntw.006`|SR-IOV|[SR-IOV Device Plugin](https://github.com/intel/sriov-network-device-plugin) must be used||


<p align="center"><b>Table 4-4:</b> Networking Solution Specifications</p>

<a name="4.6"></a>
## 4.6 Storage components

In order for the storage solution(s) to be conformant with the Reference Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.stg.001`||||
|`ra2.stg.002`||||
|`ra2.stg.003`||||
|`ra2.stg.004`||||

<p align="center"><b>Table 4-5:</b> Storage Solution Specifications</p>

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
- This Reference Architecture does not include any specifications for object storage, as this is neither a native Kubernetes object, nor something that is required by CSI drivers.  Object storage is an application-level requirement that would ordinarily be provided by a highly scalable service offering rather than being something an individual Kubernetes cluster could offer.

> Todo: specifications/commentary to support req.inf.stg.04 (SDS) and req.inf.stg.05 (high performance and horizontally scalable storage). Also req.sec.gen.06 (storage resource isolation), req.sec.gen.10 (CIS - if applicable) and req.sec.zon.03 (data encryption at rest).


<a name="4.7"></a>
## 4.7 Service meshes

Application service meshes are not in scope for the architecture.  Network service mesh specifications are handled in section [4.5 Networking solutions](#4.5).

<a name="4.8"></a>
## 4.8 Kubernetes Application package manager

In order for the storage solution(s) to be conformant with the Reference Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.pkg.001`|API-based package management|A package manager must use the Kubernetes APIs to manage application artefacts. Cluster-side components such as Tiller are not supported.|[req.int.api.02](./chapter02.md#23-kubernetes-architecture-requirements)|

<p align="center"><b>Table 4-6:</b> Kubernetes Application Package Management Specifications</p>

<a name="4.9"></a>
## 4.9 Kubernetes workloads

In order for the Kubernetes workloads to be conformant with the Reference Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|
|---|---|---|---|
|`ra2.app.001`||||
|`ra2.app.002`||||
|`ra2.app.003`||||
|`ra2.app.004`||||

<p align="center"><b>Table 4-7:</b> Kubernetes Workload Specifications</p>

<a name="4.10"></a>
## 4.10 Additional required components

> This chapter should list any additional components needed to provide the services defined in Chapter 3.2 (e.g: Prometheus)
