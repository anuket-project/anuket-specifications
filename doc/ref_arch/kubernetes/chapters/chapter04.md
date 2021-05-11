[<< Back](../../kubernetes)

# 4. Component Level Architecture
<p align="right"><img src="../figures/bogo_lsf.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents <!-- omit in toc -->
- [4. Component Level Architecture](#4-component-level-architecture)
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

## 4.2 Kubernetes Node

This section describes the configuration that will be applied to the physical or
virtual machine and an installed Operating System. In order for a Kubernetes Node
to be conformant with the Reference Architecture it must be implemented as per
the following specifications:

|Ref|Specification|Details|Requirement Trace|Reference Implementation Trace|
|---|---|---|---|---|
|`ra2.ch.001`|Huge Pages|When hosting workloads matching the Network Intensive profile, it must be possible to enable Huge Pages (2048KiB and 1048576KiB) within the Kubernetes Node OS, exposing schedulable resources `hugepages-2Mi` and `hugepages-1Gi`.|[infra.com.cfg.004](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)|[sw_config/bmra/kube-node.yml](../../../ref_impl/cntt-ri2/chapters/chapter04.md#431-installation-on-bare-metal-infratructure)|
|`ra2.ch.002`|SR-IOV capable NICs|When hosting workloads matching the Network Intensive profile, the physical machines on which the Kubernetes Nodes run must be equipped with NICs that are SR-IOV capable.|[e.cap.013](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)||
|`ra2.ch.003`|SR-IOV Virtual Functions|When hosting workloads matching the Network Intensive profile, SR-IOV virtual functions (VFs) must be configured within the Kubernetes Node OS, as the SR-IOV Device Plugin does not manage the creation of these VFs.|[e.cap.013](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)|[sw_config/bmra/kube-node.yml](../../../ref_impl/cntt-ri2/chapters/chapter04.md#431-installation-on-bare-metal-infratructure)|
|`ra2.ch.004`|CPU Simultaneous Multi-Threading (SMT)|SMT must be enabled in the BIOS on the physical machine on which the Kubernetes Node runs.|[infra.hw.cpu.cfg.004](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)||
|`ra2.ch.005`|CPU Allocation Ratio - VMs|For Kubernetes nodes running as Virtual Machines, ensure the CPU allocation ratio between vCPU and physical CPU core is 1:1.|[infra.com.cfg.001](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)||
|`ra2.ch.006`|CPU Allocation Ratio - Pods|To ensure the CPU allocation ratio between vCPU and physical CPU core is 1:1, the sum of CPU requests and limits by containers in Pod specifications must remain less than the allocatable quantity of CPU resources (i.e. `requests.cpu < allocatable.cpu` and `limits.cpu < allocatable.cpu`).|[infra.com.cfg.001](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)||
|`ra2.ch.007`|IPv6DualStack|To support IPv4/IPv6 dual stack networking, the Kubernetes Node OS must support and be allocated routable IPv4 and IPv6 addresses.|[req.inf.ntw.04](./chapter02.md#23-kubernetes-architecture-requirements)||
|`ra2.ch.008`|Physical CPU Quantity|The physical machines on which the Kubernetes Nodes run must be equipped with at least 2 physical sockets, each of at least 20 CPU cores.|[infra.hw.cpu.cfg.001](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)<br>[infra.hw.cpu.cfg.002](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)||
|`ra2.ch.009`|Physical Storage|The physical machines on which the Kubernetes Nodes run should be equipped with Sold State Drives (SSDs).|[infra.hw.stg.ssd.cfg.002](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)||
|`ra2.ch.010`|Local Filesystem Storage Quantity|The Kubernetes Nodes must be equipped with local filesystem capacity of at least 320GB for unpacking and executing containers. Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.|[e.cap.003](./chapter02.md#221-cloud-infrastructure-software-profile-capabilities)||
|`ra2.ch.011`|Virtual Node CPU Quantity|If using VMs, the Kubernetes Nodes must be equipped with at least 16 vCPUs.  Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.|[e.cap.001](./chapter02.md#221-cloud-infrastructure-software-profile-capabilities)||
|`ra2.ch.012`|Kubernetes Node RAM Quantity|The Kubernetes Nodes must be equipped with at least 32GB of RAM. Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.|[e.cap.002](./chapter02.md#221-cloud-infrastructure-software-profile-capabilities)||
|`ra2.ch.013`|Physical NIC Quantity|The physical machines on which the Kubernetes Nodes run must be equipped with at least four (4) Network Interface Card (NIC) ports.|[infra.hw.nic.cfg.001](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.ch.014`|Physical NIC Speed - Basic Profile|The NIC ports housed in the physical machines on which the Kubernetes Nodes run for workloads matching the Basic Profile must be at least 10Gbps.|[infra.hw.nic.cfg.002](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.ch.015`|Physical NIC Speed - Network Intensive Profile|The NIC ports housed in the physical machines on which the Kubernetes Nodes run for workloads matching the Network Intensive profile must be at least 25Gbps.|[infra.hw.nic.cfg.002](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.ch.016`|Physical PCIe slots|The physical machines on which the Kubernetes Nodes run must be equipped with at least eight (8) Gen3.0 PCIe slots, each with at least eight (8) lanes.|
|`ra2.ch.017`|Immutable infrastructure|Whether physical or virtual machines are used, the Kubernetes Node is not changed after it is made ready for use. New changes to the Kubernetes Node are rolled out as new instances. This covers any changes from BIOS through Operating System to running processes and all associated configurations.|[req.gen.cnt.02](./chapter02.md#23-kubernetes-architecture-requirements)|[Use of Ansible](../../../ref_impl/cntt-ri2/chapters/chapter04.md#431-installation-on-bare-metal-infratructure)|
|`ra2.ch.018`|NFD|[Node Feature Discovery](https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/index.html) must be used to advertise the detailed software and hardware capabilities of each node in the Kubernetes Cluster.|TBD|TBD|

<p align="center"><b>Table 4-1:</b> Node Specifications</p>

## 4.3 Kubernetes

In order for the Kubernetes components to be conformant with the Reference Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|Reference Implementation Trace|
|---|---|---|---|---|
|`ra2.k8s.001`|Kubernetes Conformance|The Kubernetes distribution, product, or installer used in the implementation must be listed in the [Kubernetes Distributions and Platforms document](https://docs.google.com/spreadsheets/d/1LxSqBzjOxfGx3cmtZ4EbB_BGCxT_wlxW_xgHVVa23es/edit#gid=0) and marked (X) as conformant for the Kubernetes version that is being used.|[req.gen.cnt.03](./chapter02.md#23-kubernetes-architecture-requirements)||
|`ra2.k8s.002`|Highly available etcd|An implementation must consist of either three, five or seven nodes running the etcd service (can be colocated on the master nodes, or can run on separate nodes, but not on worker nodes).|[req.gen.rsl.02 req.gen.avl.01](./chapter02.md#23-kubernetes-architecture-requirements)|["For the high availability requirement"](../../../ref_impl/cntt-ri2/chapters/chapter04.md#431-installation-on-bare-metal-infratructure)|
|`ra2.k8s.003`|Highly available control plane|An implementation must consist of at least one master node per availability zone or fault domain to ensure the high availability and resilience of the Kubernetes control plane services.|[req.gen.rsl.02](./chapter02.md#23-kubernetes-architecture-requirements)<br>[req.gen.avl.01](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.012`|Control plane services|A master node must run at least the following Kubernetes control plane services: `kube-apiserver`, `kube-scheduler` and `kube-controller-manager`.|[req.gen.rsl.02](./chapter02.md#23-kubernetes-architecture-requirements)<br>[req.gen.avl.01](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.004`|Highly available worker nodes|An implementation must consist of at least one worker node per availability zone or fault domain to ensure the high availability and resilience of workloads managed by Kubernetes|[req.gen.rsl.01](./chapter02.md#23-kubernetes-architecture-requirements)<br>[req.gen.avl.01](./chapter02.md#23-kubernetes-architecture-requirements)<br>[req.kcm.gen.02](./chapter02.md#23-kubernetes-architecture-requirements)<br>[req.inf.com.01](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.005`|Kubernetes API Version|In alignment with the [Kubernetes version support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions), an implementation must use one of three latest minor versions (`n-2`). e.g. if the latest version is 1.17 then the RI must use either 1.17, 1.16 or 1.15.|TBC|
|`ra2.k8s.006`|NUMA Support|When hosting workloads matching the Network Intensive profile, the `TopologyManager` and `CPUManager` feature gates must be enabled and configured on the kubelet (note, TopologyManager is enabled by default in Kubernetes v1.18 and later, with CPUManager enabled by default in Kubernetes v1.10 and later). `--feature-gates="...,TopologyManager=true,CPUManager=true" --topology-manager-policy=single-numa-node --cpu-manager-policy=static`|[e.cap.007](chapter02.md#221-cloud-infrastructure-software-profile-capabilities) [infra.com.cfg.002](./chapter02.md#223-cloud-infrastructure-software-profile-requirements) [infra.hw.cpu.cfg.003](./chapter02.md#224-cloud-infrastructure-hardware-profile-requirements)|
|`ra2.k8s.007`|DevicePlugins Feature Gate|When hosting workloads matching the Network Intensive profile, the DevicePlugins feature gate must be enabled (note, this is enabled by default in Kubernetes v1.10 or later). `--feature-gates="...,DevicePlugins=true,..."`|Various, e.g. [e.cap.013](chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|[Implied by `sriov_net_dp_enabled`](../../../ref_impl/cntt-ri2/chapters/chapter04.md#431-installation-on-bare-metal-infratructure)|
|`ra2.k8s.008`|System Resource Reservations|To avoid resource starvation issues on nodes, reserve compute resources for system daemons and Kubernetes system daemons such as kubelet, container runtime, etc. (requires Kubernetes version 1.17 or later). Use the following kubelet flags: `--reserved-cpus=[a-z]`, using two of `a-z` to reserve 2 SMT threads.|[i.cap.014](chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|[Implied by `isolcpus_enabled`](../../../ref_impl/cntt-ri2/chapters/chapter04.md#431-installation-on-bare-metal-infratructure)|
|`ra2.k8s.009`|CPU Pinning|When hosting workloads matching the Network Intensive profile, in order to support CPU Pinning, the kubelet must be started with the `--cpu-manager-policy=static` option. (Note, only containers in `Guaranteed` pods - where CPU resource `requests` and `limits` are identical - and configured with positive-integer CPU `requests` will take advantage of this. All other Pods will run on CPUs in the remaining shared pool.)|[infra.com.cfg.003](./chapter02.md#223-cloud-infrastructure-software-profile-requirements)|
|`ra2.k8s.010`|IPv6DualStack|To support IPv6 and IPv4, the `IPv6DualStack` feature gate must be enabled on various components (requires Kubernetes v1.16 or later). kube-apiserver: `--feature-gates="IPv6DualStack=true"`. kube-controller-manager: `--feature-gates="IPv6DualStack=true" --cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR> --service-cluster-ip-range=<IPv4 CIDR>,<IPv6 CIDR> --node-cidr-mask-size-ipv4 ¦ --node-cidr-mask-size-ipv6` defaults to /24 for IPv4 and /64 for IPv6. kubelet: `--feature-gates="IPv6DualStack=true"`. kube-proxy: `--cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR> --feature-gates="IPv6DualStack=true"`|[req.inf.ntw.04](./chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.k8s.011`|Anuket profile labels|To clearly identify which worker nodes are compliant with the different profiles defined by Anuket the worker nodes must be labelled according to the following pattern: an `anuket.io/profile/basic` label must be set to `true` on the worker node if it can fulfil the requirements of the basic profile and an `anuket.io/profile/network-intensive` label must be set to `true` on the worker node if it can fulfil the requirements of the network intensive profile. The requirements for both profiles can be found in [chapter 2](./chapter02.md#22-reference-model-requirements)|||


<p align="center"><b>Table 4-2:</b> Kubernetes Specifications</p>

## 4.4 Container runtimes

|Ref|Specification|Details|Requirement Trace|Reference Implementation Trace|
|---|---|---|---|---|
|`ra2.crt.001`|Conformance with OCI 1.0 runtime spec|The container runtime must be implemented as per the [OCI 1.0](https://github.com/opencontainers/runtime-spec/blob/master/spec.md) (Open Container Initiative 1.0) specification.|[req.gen.ost.01](chapter02.md#23-kubernetes-architecture-requirements)||
|`ra2.crt.002`|Kubernetes Container Runtime Interface (CRI)|The Kubernetes container runtime must be implemented as per the [Kubernetes Container Runtime Interface (CRI)](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/)|[req.gen.ost.01](chapter02.md#23-kubernetes-architecture-requirements)||

<p align="center"><b>Table 4-3:</b> Container Runtime Specifications</p>

## 4.5 Networking solutions

In order for the networking solution(s) to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|Reference Implementation Trace|
|---|---|---|---|---|
|`ra2.ntw.001`|Centralised network administration|The networking solution deployed within the implementation must be administered through the Kubernetes API using native Kubernetes API resources and objects, or Custom Resources.|[req.inf.ntw.03](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.002`|Default Pod Network - CNI|The networking solution deployed within the implementation must use a CNI-conformant Network Plugin for the Default Pod Network, as the alternative (kubenet) does not support cross-node networking or Network Policies.|[req.gen.ost.01](chapter02.md#23-kubernetes-architecture-requirements)<br>[req.inf.ntw.08](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.003`|Multiple connection points|The networking solution deployed within the implementation must support the capability to connect at least FIVE connection points to each Pod, which are additional to the default connection point managed by the default Pod network CNI plugin.|[e.cap.004](chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|
|`ra2.ntw.004`|Multiple connection points presentation|The networking solution deployed within the implementation must ensure that all additional non-default connection points are requested by Pods using standard Kubernetes resource scheduling mechanisms such as annotations or container resource requests and limits.|[req.inf.ntw.03](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.005`|Multiplexer/meta-plugin|The networking solution deployed within the implementation may use a multiplexer/meta-plugin.|[req.inf.ntw.06](chapter02.md#23-kubernetes-architecture-requirements)<br>[req.inf.ntw.07](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.006`|Multiplexer/meta-plugin CNI Conformance|If used, the selected multiplexer/meta-plugin must integrate with the Kubernetes control plane via CNI.|[req.gen.ost.01](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.007`|Multiplexer/meta-plugin CNI Plugins|If used, the selected multiplexer/meta-plugin must support the use of multiple CNI-conformant Network Plugins.|[req.gen.ost.01](chapter02.md#23-kubernetes-architecture-requirements)<br>[req.inf.ntw.06](chapter02.md#23-kubernetes-architecture-requirements)|[`sriov`, `userspace` and `bond` CNIs all listed](../../../ref_impl/cntt-ri2/chapters/chapter04.md#431-installation-on-bare-metal-infratructure)|
|`ra2.ntw.008`|SR-IOV Device Plugin for Network Intensive|When hosting workloads that match the Network Intensive profile and require SR-IOV acceleration, a Device Plugin for SR-IOV must be used to configure the SR-IOV devices and advertise them to the `kubelet`.|[e.cap.013](chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|[`sriov_net_dp_enabled: true`](../../../ref_impl/cntt-ri2/chapters/chapter04.md#431-installation-on-bare-metal-infratructure)|
|`ra2.ntw.009`|Multiple connection points with multiplexer/meta-plugin|When a multiplexer/meta-plugin is used, the additional non-default connection points must be managed by a CNI-conformant Network Plugin.|[req.gen.ost.01](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.010`|User plane networking|When hosting workloads matching the Network Intensive profile, CNI network plugins that support the use of DPDK, VPP, or SR-IOV must be deployed as part of the networking solution.|[infra.net.acc.cfg.001](chapter02.md#223-cloud-infrastructure-software-profile-requirements)|[All are available under `example_net_attach_defs:`](../../../ref_impl/cntt-ri2/chapters/chapter04.md#431-installation-on-bare-metal-infratructure)|
|`ra2.ntw.011`|NATless connectivity|When hosting workloads that require source and destination IP addresses to be preserved in the traffic headers, a CNI plugin that exposes the pod IP directly to the external networks (e.g. Calico, MACVLAN or IPVLAN CNI plugins) is required.|[req.inf.ntw.14](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.ntw.012`|Device Plugins|When hosting workloads matching the Network Intensive profile that require the use of FPGA, SR-IOV or other Acceleration Hardware, a Device Plugin for that FPGA or Acceleration Hardware must be used.|[e.cap.016](chapter02.md#221-cloud-infrastructure-software-profile-capabilities), [e.cap.013](chapter02.md#221-cloud-infrastructure-software-profile-capabilities)|
|`ra2.ntw.013`|Dual stack CNI|The networking solution deployed within the implementation must use a CNI-conformant Network Plugin that is able to support dual-stack IPv4/IPv6 networking.|[req.inf.ntw.04](chapter02.md#23-kubernetes-architecture-requirements)|

<p align="center"><b>Table 4-4:</b> Networking Solution Specifications</p>

## 4.6 Storage components

In order for the storage solution(s) to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|Reference Implementation Trace|
|---|---|---|---|---|
|`ra2.stg.001`| Ephemeral Storage | An implementation must support ephemeral storage, for the unpacked container images to be stored and executed from, as a directory in the filesystem on the worker node on which the container is running. <br>See the [Container runtimes](#4.4) section above for more information on how this meets the requirement for ephemeral storage for containers. ||
|`ra2.stg.002`| Kubernetes Volumes | An implementation may attach additional storage to containers using Kubernetes Volumes. ||
|`ra2.stg.003`| Kubernetes Volumes | An implementation may use Volume Plugins (see `ra2.stg.005` below) to allow the use of a storage protocol (e.g. iSCSI, NFS) or management API (e.g. Cinder, EBS) for the attaching and mounting of storage into a Pod. ||
|`ra2.stg.004`| Persistent Volumes | An implementation may support Kubernetes Persistent Volumes (PV) to provide persistent storage for Pods.<br>Persistent Volumes exist independent of the lifecycle of containers and/or pods. |[req.inf.stg.01](chapter02.md#23-kubernetes-architecture-requirements)|
|`ra2.stg.005`| Storage Extension | Volume plugins must allow for the use of a range of backend storage systems. ||
|`ra2.stg.006`| Container Storage Interface (CSI) | An implementation may support the Container Storage Interface (CSI), an Out-of-tree plugin.<br>In order to support CSI, the  feature gates `CSIDriverRegistry` and `CSINodeInfo` must be enabled.<br>The implementation must use a CSI driver (a full list of CSI drivers can be found [here](https://kubernetes-csi.github.io/docs/drivers.html)). <br>An implementation may support ephemeral storage through a CSI-compatible volume plugin in which case the `CSIInlineVolume` feature gate must be enabled.<br>An implementation may support Persistent Volumes through a CSI-compatible volume plugin in which case  the `CSIPersistentVolume` feature gate must be enabled. | |
|`ra2.stg.007`|  | An implementation should use Kubernetes Storage Classes to support automation and the separation of concerns between providers of a service and consumers of the service. | |

<p align="center"><b>Table 4-6:</b> Storage Solution Specifications</p>

A note on object storage:
- This Reference Architecture does not include any specifications for object
storage, as this is neither a native Kubernetes object, nor something that is
required by CSI drivers.  Object storage is an application-level requirement
that would ordinarily be provided by a highly scalable service offering rather
than being something an individual Kubernetes Cluster could offer.  

> Todo: specifications/commentary to support req.inf.stg.04 (SDS) and req.inf.stg.05 (high performance and horizontally scalable storage). Also req.sec.gen.06 (storage resource isolation), req.sec.gen.10 (CIS - if applicable) and req.sec.zon.03 (data encryption at rest).


## 4.7 Service meshes

Application service meshes are not in scope for the architecture.  Network
service mesh specifications are handled in section [4.5 Networking
solutions](#45-networking-solutions).

## 4.8 Kubernetes Application package manager

In order for the storage solution(s) to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|Reference Implementation Trace|
|---|---|---|---|---|
|`ra2.pkg.001`|API-based package management|A package manager must use the Kubernetes APIs to manage application artefacts. Cluster-side components such as Tiller are not supported.|[req.int.api.02](./chapter02.md#23-kubernetes-architecture-requirements)||

<p align="center"><b>Table 4-7:</b> Kubernetes Application Package Management Specifications</p>

## 4.9 Kubernetes workloads

In order for the Kubernetes workloads to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

|Ref|Specification|Details|Requirement Trace|Reference Implementation Trace|
|---|---|---|---|---|
|`ra2.app.001`|[Root](https://github.com/opencontainers/runtime-spec/blob/master/config.md) Parameter Group (OCI Spec)|Specifies the container's root filesystem.|TBD|N/A|
|`ra2.app.002`|[Mounts](https://github.com/opencontainers/runtime-spec/blob/master/config.md#mounts) Parameter Group (OCI Spec)|Specifies additional mounts beyond root|TBD|N/A|
|`ra2.app.003`|[Process](https://github.com/opencontainers/runtime-spec/blob/master/config.md#process) Parameter Group (OCI Spec)|Specifies the container process|TBD|N/A|
|`ra2.app.004`|[Hostname](https://github.com/opencontainers/runtime-spec/blob/master/config.md#hostname) Parameter Group (OCI Spec)|Specifies the container's hostname as seen by processes running inside the container|TBD|N/A|
|`ra2.app.005`|[User](https://github.com/opencontainers/runtime-spec/blob/master/config.md#user) Parameter Group (OCI Spec)|User for the process is a platform-specific structure that allows specific control over which user the process runs as|TBD|N/A|
|`ra2.app.006`|Consumption of additional, non-default connection points|The workload must request additional non-default connection points through the use of workload annotations or resource requests and limits within the container spec passed to the Kubernetes API Server.|[req.int.api.01](chapter02.md#23-kubernetes-architecture-requirements)|N/A|
|`ra2.app.007`|Host Volumes|Workloads should not use `hostPath` volumes, as [Pods with identical configuration (such as created from a PodTemplate) may behave differently on different nodes due to different files on the nodes.](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath)|[req.kcm.gen.02](chapter02.md#23-kubernetes-architecture-requirements)|N/A|
|`ra2.app.008`|Infrastructure dependency|Workloads must not rely on the availability of the master nodes for the successful execution of their functionality (i.e. loss of the master nodes may affect non-functional behaviours such as healing and scaling, but components that are already running will continue to do so without issue). |TBD|N/A|
|`ra2.app.009`|Device plugins|Workload descriptors must use the resources advertised by the device plugins to indicate their need for an FPGA, SR-IOV or other acceleration device.|TBD|N/A|
|`ra2.app.010`|Node Feature Discovery (NFD)|Workload descriptors must use the labels advertised by [Node Feature Discovery](https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/index.html) to indicate which node software of hardware features they need.|TBD|N/A|


<p align="center"><b>Table 4-8:</b> Kubernetes Workload Specifications</p>

## 4.10 Additional required components

> This chapter should list any additional components needed to provide the services defined in Chapter 3.2 (e.g: Prometheus)
