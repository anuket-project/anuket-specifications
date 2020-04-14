[<< Back](../../kubernetes)

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

In order for a Host OS to be conformant with this Reference Architecture it must meet the following requirements:
- A version of the Linux kernel that is [compatible with kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/implementation-details/#kubeadm-init-workflow-internal-design) - this has been chosen as the baseline because kubeadm is focussed on installing and managing the lifecycle of Kubernetes and nothing else, hence it is easily integrated into higher-level and more complete tooling for the full lifecycle management of the infrastructure, cluster add-ons, etc.
- Windows Server 2019 (this can be used for worker nodes, but be aware of the [limitations](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#limitations)).
- In order to support `req.gen.cnt.03` (immutable infrastructure), the Host OS must be easily reproduced, consistent, disposable, will have a repeatable deployment process, and will not have configuration or artifacts that are modifiable in place (i.e. once it is running).
- The selection of Host OS shall not restrict the selection of the OS used to build container images (container base image).

Table 4-1 lists the Linux kernel versions that comply with this Reference Architecture specification.

|OS Family|Version(s)|Notes|
|---|---|---|
|Linux|3.10+||
|Windows|1809 (10.0.17763)|For worker nodes only|

<p align="center"><b>Table 4-1:</b> Conformant OS Kernels</p>


<a name="4.3"></a>
## 4.3 Kubernetes

> This chapter should discuss:
> * The version of version range of Kubernetes and the mandatory components needed for Kubernetes (e.g.: etcd, cadvisor)
> * Which optional features are used and which optional API-s are available
> * Which [alfa or beta features](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) are used

In alignment with the [Kubernetes version support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions), a Reference Implementation must use one of three latest minor versions (`n-2`) - e.g. if the latest version is 1.17 then the RI must use either 1.17, 1.16 or 1.15. The Kubernetes distribution, product, or installer used in the RI must be listed in the [Kubernetes Distributions and Platforms document](https://docs.google.com/spreadsheets/d/1LxSqBzjOxfGx3cmtZ4EbB_BGCxT_wlxW_xgHVVa23es/edit#gid=0) and marked (X) as conformant for the Kubernetes version that is being used.

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

In order to support `req.inf.com.03`, the chosen runtime must be conformant with the [Kubernetes Container Runtime Interface (CRI)](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/) and the [Open Container Initiative (OCI) runtime spec](https://github.com/opencontainers/runtime-spec). Examples of container runtimes that are conformant with these specification are (note this is not a complete list and in no particular order):
- container-d (with CRI plugin enabled, which it is by default)
- Docker CE (via the dockershim, which is currently built in to the kubelet)
- CRI-O
- Frakti

To support `req.sec.gen.04` the architecture specifies the usage of a container runtime with the capability of Kernel isolation:
- kata-containers

These specifications cover the [full lifecycle of a container](https://github.com/opencontainers/runtime-spec/blob/master/runtime.md#lifecycle) `creating > created > running > stopped` which includes the use of storage that is required during this lifecycle - this is management of the Host OS filesystem by the container runtime. This lifecycle management by the container runtime (when conformant with the above specifications) supports the requirement `req.inf.stg.06` for ephemeral storage for Pods.

To fulfill `req.sec.gen.05` the architecture specifies the usage of the Kubernetes CPU Manager and to support the isolation of workload resources from the infrastructure resources [CPU Pooler](https://github.com/nokia/CPU-Pooler/).

> Todo: details and RA2 specifications relating to runtimes in order to meet RM features and requirements from RM chapters 4 and 5.

<a name="4.5"></a>
## 4.5 CNI plugins

> Editors note: The following chapter lists a set of CNI plugins conformant with the Reference Architecture. In future releases the list of CNI plugins should be refined in a way that there is only one example component selected for each functionality. 

The selected CNI multiplexer/metapulgin may be [DANM](https://github.com/nokia/danm) as it provides the possibility to use several other CNI plugins (`req.inf.ntw.16`) and provides an API based solution to administer the networks (`req.inf.ntw.10`) from a central point (`req.inf.ntw.11`).<br>

The following table contains a comparision of relevant features and requirements in Multus and DANM.

| Requirement | Support in Multus | Support in DANM |
|-------------|-------------------|-----------------|
| `req.inf.ntw.01` | Supported | Supported |
| `req.inf.ntw.02` | Supported via another CNI plugin | Supported via another CNI plugin |
| `req.inf.ntw.03` | Supported via another CNI plugin | Supported |
| `req.inf.ntw.04` | Supported via another CNI plugin | Supported via another CNI plugin |
| `req.inf.ntw.06` | Supported | Supported |
| `req.inf.ntw.07` | Supported | Supported |
| `req.inf.ntw.08` | Supported | Supported |
| `req.inf.ntw.09` | Supported via LCM tools |  Supported via LCM tools |
| `req.inf.ntw.10` | Not supported | Suported |
| `req.inf.ntw.11` | Not supported | Partially supported |
| `req.inf.ntw.14` | Supported via another CNI plugin | Supported via another CNI plugin |
| `req.inf.ntw.15` | Not relevant | Not relevant |
| `req.inf.ntw.16` | Supported | Supported |
| Cluster wide IP address management | Not suported | Supported |
| Service based discovery of all provisioned interfaces |Supported | Supported |

 [Calico](https://github.com/projectcalico/cni-plugin) may be used as the CNI what complies with the basic networking assumptions of Kubernetes based on the requirement `req.inf.ntw.02` due to it's capability to handle `NetworkPolicies`, what is missing from [Flannel](https://github.com/coreos/flannel-cni).
For the network of signalling connections the built in IPVLAN CNI of DANM or the [MACVLAN CNI](https://github.com/containernetworking/plugins/tree/master/plugins/main/macvlan) may be used as these provide NAT-less connectivity (`req.inf.ntw.03`). For the user plane network(s) fullfilling requirement `req.inf.ntw.04` the [User Space CNI](https://github.com/intel/userspace-cni-network-plugin) may be used. The User Space CNI may use VPP or OVS-DPDK as a backend.

> Editors note: The usage SR-IOV in container environments, therefore the inclusion of an SR-IOV CNI plugin and the [SR-IOV Device Plugin](https://github.com/intel/sriov-network-device-plugin) to the architecture are under debate.

<a name="4.6"></a>
## 4.6 Storage components

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

No service meshes are part of the architecture.

<a name="4.8"></a>
## 4.8 Kubernetes Application package manager

The reference architecture specifies the usage of a Kubernetes Application package manager using the Kubernetes API-s, like [Helm v3](https://v3.helm.sh/).

<a name="4.9"></a>
## 4.9 Supplementary components (okay, this is a bad heading, but I do not have any better)

> This chapter should list all the supplementary components needed to provide the services defined in Chapter 3.2 (e.g: Prometheus)
