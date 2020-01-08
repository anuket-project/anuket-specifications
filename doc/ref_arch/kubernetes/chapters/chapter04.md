[<< Back](../../openstack)

# 4. Component Level Architecture
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Host OS](#4.2)
* [4.3 Kubernetes](#4.3)
* [4.4 Container runtimes](#4.4)
* [4.5 CNI plugins](#4.5)
* [4.6 Storage components](#4.6)
* [4.7 Service meshes](#4.7)
* [4.8 Container package managers](#4.8)
* [4.9 Supplementary components](#4.9)

<a name="4.1"></a>
## 4.1 Introduction

This chapter will describe in detail the Kubernetes Reference Architecture in terms of the functional capabilities and how they relate to the Reference Model requirements, i.e. how the infrastructure profiles are delivered and described.

Figure 4-1 below shows the architectural components that are described in the subsequent sections of this chapter.

<p align="center"><img src="../figures/ch04_k8s_architecture.png" alt="Kubernetes Reference Architecture" Title="Kubernetes Reference Architecture" width="65%"/></p>
<p align="center"><b>Figure 4-1:</b> Kubernetes Reference Architecture</p>

<a name="4.2"></a>
## 4.2 Host OS

In order for a Host OS to be compliant with this Reference Architecture it must meet the following requirements:
- A deb/rpm compatible distribution of Linux (this must be used for the master nodes, and can be used for worker nodes).
- A version of Linux that is [compatible with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#before-you-begin) - this has been chosen as the baseline because kubeadm is focussed on installing and managing the lifecycle of Kubernetes and nothing else, hence it is easily integrated into higher-level and more complete tooling for the full lifecycle management of the infrastructure, cluster add-ons, etc.
- Windows Server 2019 (this can be used for worker nodes, but be aware of the [limitations](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#limitations)).
- In order to support `req.gen.cnt.03` and `req.lcm.gen.01` and `req.lcm.adp.04`, the Host OS must be disposable and therefore the configuration of the Host OS (and associated infrastructure such as VM or bare metal server) must be consistent - e.g. the system software and configuration of that software must be identical apart from those areas of configuration that must be different such as IP addresses and hostnames.

Table 4-1 lists the Operating Systems that comply with this Reference Architecture specification.

|OS|Version(s)|Notes|
|---|---|---|
|Ubuntu|16.04+||
|Debian|9+||
|CentOS|7||
|Red Hat Enterprise Linux (RHEL)|7||
|Fedora|25+||
|HypriotOS|1.0.1+||
|Container Linux|1800.6.0||
|Windows Server|2019|For worker nodes only|

<p align="center"><b>Table 4-1:</b> Compliant Host OSs</p>


<a name="4.3"></a>
## 4.3 Kubernetes

> This chapter should discuss:
> * The version of version range of Kubernetes and the mandatory components needed for Kubernetes (e.g.: etcd, cadvisor)
> * Which optional features are used and which optional API-s are available
> * Which [alfa or beta features](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) are used

The distribution and version of Kubernetes used must be listed in the [Kubernetes Distributions and Platforms document](https://docs.google.com/spreadsheets/d/1LxSqBzjOxfGx3cmtZ4EbB_BGCxT_wlxW_xgHVVa23es/edit#gid=0) which lists all those that are Certified as being conformant with the CNCF Kubernetes specification.

This Reference Architecture also specifies:

- Master nodes must run the following Kubernetes control plane services:
    - kube-apiserver
    - kube-scheduler
    - kube-controller-manager
- Master nodes can also run the etcd service and host the etcd database, however etcd can also be hosted on separate nodes
- In order to support `req.gen.rsl.01`, `req.gen.rsl.02` and `req.gen.avl.01` a Reference Implementation must:
    - Consist of either three, five or seven nodes running the etcd service (can be colocated on the master nodes, or can run on separate nodes, but not on worker nodes)
    - At least one master node per availability zone or fault domain to ensure the high availability and resilience of Kubernetes control plane services
    - At least one worker node per availability zone or fault domain to ensure the high availability and resilience of workloads managed by Kubernetes
- Master node services, including etcd, and worker node services (e.g. consumer workloads) must be kept separate - i.e. there must be at least one master node, and at least one worker node
- Workloads must ***not*** rely on the availability of the master nodes for the successful execution of their functionality (i.e. loss of the master nodes may affect non-functional behaviours such as healing and scaling, but components that are already running will continue to do so without issue)
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

<a name="4.4"></a>
## 4.4 Container runtimes

In order to support `req.inf.com.03`, the chosen runtime must be compliant with the [Kubernetes Container Runtime Interface (CRI)](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/) and the [Open Container Initiative (OCI) runtime spec](https://github.com/opencontainers/runtime-spec). Examples of container runtimes that are compliant with these specification are (note this is not a complete list and in no particular order):
- container-d (with CRI plugin enabled, which it is by default)
- Docker CE (via the dockershim, which is currently built in to the kubelet)
- CRI-O
- Frakti

These specifications cover the [full lifecycle of a container](https://github.com/opencontainers/runtime-spec/blob/master/runtime.md#lifecycle) `creating > created > running > stopped` which includes the use of storage that is required during this lifecycle - this is management of the Host OS filesystem by the container runtime. This lifecycle management by the container runtime (when compliant with the above specifications) supports the requirement `req.inf.stg.06` for ephemeral storage for Pods.

If privileged containers are required (not recommended, but required for some features such as the use of CSI drivers) then a container runtime that provides additional security isolation is required in order to support `req.sec.gen.01` and `req.sec.gen.04`.  This could be via the use of lightweight virtual machines (e.g. Kata) or alternative sandbox methods (e.g. gVisor).  For more information on isolation of workloads and underlying Host OS kernel, see the [Security chapter](./chapter06.md).

> Todo: details and RA2 specifications relating to runtimes in order to meet RM features and requirements from RM chapters 4 and 5.

<a name="4.5"></a>
## 4.5 CNI plugins

> This chapter should describe which CNI plugins are part of the Rerefence Architecture.

<a name="4.6"></a>
## 4.5 Storage components

As described in [chapter 3](./chapter03.md), storage in Kubernetes consists of three types of storage:
1. Ephemeral storage that is used to execute the containers
    - **Ephemeral storage follows the lifecycle of a container**
    - See the [Container runtimes](#4.4) section above for more information how this meets the requirement `req.inf.stg.06` for ephemeral storage for Pods
1. Kubernetes Volumes, which are used to present additional storage to containers
    - **A Volume follow the lifecycle of a Pod**
    - This is a native Kubernetes capability and therefore `req.inf.stg.01` is supported by default
    - This capability also delivers support for `req.inf.stg.06` although depending on the Volume Plugin used there may be additional steps required in order to remove data from disk (not all plugins manage the full lifecycle of the storage mounted using Volumes)
1. Kubernetes Persistent Volumes, which are a subset of the above whose lifecycle persists beyond the lifetime of a Pod to allow for data persistence
    - **Persistent Volumes have a lifecycle that is independent of Containers and/or Pods**
    - This supports the requirement `req.inf.stg.07` for persistent storage for Pods

Volume plugins are used in Kubernetes to allow for the use of a range of backend storage systems. There are two types of Volume plugin:
1. In-tree
    - These plugins are built, linked, compiled and shipped with the core Kubernetes binaries
    - Therefore if a new backend storage system needs adding this is a change to the core Kubernetes code
1. Out-of-tree
    - These plugins allow new storage plugins to be created without any changes to the core Kubernetes code
    - The Container Storage Interface (CSI) is such an out-of-tree plugin and many in-tree drivers are being migrated to use the CSI plugin instead (e.g. the [Cinder CSI plugin](https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/using-cinder-csi-plugin.md))
    - In order to support the requirement `req.inf.stg.03` (CSI support), the following feature gates must be enabled:
      - `CSIDriverRegistry`
      - `CSINodeInfo`
    - In addition to these feature gates, a CSI driver must be used (as opposed to an in-tree volume plugin) - a full list of CSI drivers can be found [here](https://kubernetes-csi.github.io/docs/drivers.html)
    - In order to support ephemeral storage use through a CSI-compatible volume plugin, the `CSIInlineVolume` feature gate must be enabled
    - In order to support Persistent Volumes through a CSI-compatible volume plugin, the `CSIPersistentVolume` feature gate must be enabled

> Should the following paragraph be moved to the Security chapter?

> In order to support `req.sec.gen.09` and more generally to support automation and the separation of concerns between providers of a service and consumers of the service, Kubernetes Storage Classes should be used. Storage Classes allow a consumer of the Kubernetes platform to request Persistent Storage using a Persistent Volume Claim and for a Persistent Volume to be dynamically created based on the "class" that has been requested. This avoids having to grant `create`/`update`/`delete` permissions in RBAC to PersistentVolume resources, which are cluster-scoped rather than namespace-scoped (meaning an identity can manage all PVs or none).

A note on object storage:
- This Reference Architecture does not include any specifications for object storage, as this is neither a native Kubernetes object, nor something that is required by CSI drivers.  Object storage is an application-level requirement that would ordinarily be provided by a highly scalable service offering rather than being something an individual Kubernetes cluster could offer.

> Todo: specifications/commentary to support req.inf.stg.04 (SDS) and req.inf.stg.05 (high performance and horizontally scalable storage). Also req.sec.gen.06 (storage resource isolation), req.sec.gen.10 (CIS - if applicable) and req.sec.zon.03 (data encryption at rest).


<a name="4.7"></a>
## 4.7 Service meshes

> This chapter should describe which service meshes are part of the Reference Architecture. For the shake of simplcity this chapter should discuss both the "normal" service meshes and Network Service Mesh.

<a name="4.8"></a>
## 4.8 Kubernetes Application package manager

The reference architecture must support the usage of a Kubernetes Application package manager using the Kubernetes API-s, like [Helm v3](https://v3.helm.sh/).

<a name="4.9"></a>
## 4.9 Supplementary components (okay, this is a bad heading, but I do not have any better)

> This chapter should list all the supplementary components needed to provide the services defined in Chapter 3.2 (e.g: Prometheus)
