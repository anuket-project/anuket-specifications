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

The CNTT Kubernetes Reference Architecture (RA) aims to provide an industry standard reference architecture independent of the many Kubernetes offerings and distributions. The RA does not seek to require vendor-specific enhancements in order to achieve CNTT compliance; compliance is achieved using upstream components or features that are developed by the open source community. This would allow operators to provide a common Kubernetes-based architecture that allows any compliant VNF or CNF to be deployed and operated as expected. The purpose of this chapter is to outline all the components required to provide Kubernetes in a consistent and reliable way.

Kubernetes is already very well documented at [https://kubernetes.io/docs/home/](https://kubernetes.io/docs/home/) so rather than repeat content from there this and following chapters will describe the specific features used and how we expect them to be implemented.

This reference architecture provides optionality in terms of pluggable components such as service mesh and other plugins that might be used, however the focus of the reference architecture is on the abstracted interfaces and features that are required for workload management and execution.

Chapter 5 of the Reference Model (RM) describes the [hardware](../../../ref_model/ref_model/chapters/chapter05.md#5.4) and [software](../../../ref_model/ref_model/chapters/chapter05.md#52-nfvi-sw-profiles-features-and-requirements) profiles, which are descriptions of the capabilities and features that the NFVI offer to the workloads. As of v2.0, Figure 5-3 in the RM (also shown below) depicts a high level view of the software profile features that apply to each instance profile (Basic, Network Intensive, Compute Intensive). For more information on the instance profiles please read [RM Chapter 4, section 4.2.4](../../../ref_model/chapters/chapter04.md#4.2.4).

<p align="center"><img src="../../../ref_model/figures/RM_chap5_fig_5_3_SW_profile.png" width="80%"/></p>
<p align="center"><b>Figure 5-3 (from RM):</b> NFVI software profiles</p>

In addition, Figure 5-4 (also shown below) depicts the hardware profile features that apply to each instance profile.

<p align="center"><img src="../../../ref_model/figures/RM_chap5_fig_5_4_HW_profile.png" width="80%"/></p>
<p align="center"><b>Figure 5-4 (from RM):</b> NFVI hardware profiles and host associated capabilities</p>

These features and capabilities that are described in the software and hardware profiles are considered throughout this RA, with traceability of the RA requirements to the RM requirements formally captured in [chapter 2, section 2.2](./chapter02.md#2.2) of this RA.

> As this RA is developed, it is quite possible that modifications to the RM are requested in order to make the RM more technology agnostic (i.e. to cater for VMs and Containers) or to add container-specific specifications to the RM.

<a name="3.2"></a>
## 3.2 Infrastructure Services

> This chapter shall list the services provided by the infrastructure. Some example of these services can be: log collection, monitoring, health check, load balancer. For the shake of clarity CaaS services should be also listed, like container lifecycle management or networking services.

<a name="3.2.1"></a>
### 3.2.1 Container Compute Services

> This chapter should describe considerations about container compute services.

<a name="3.2.1.1."></a>
#### 3.2.1.1 Memory management

> This chapter should describe considerations about memory management, like huge pages.

> Relate back to features described in the RM [here](../../../ref_model/ref_model/chapters/chapter05.md#521-virtual-compute). Note that the RM appears to be missing Memory-based HW profile features [here](../../../ref_model/chapters/chapter05.md#54-nfvi-hw-profiles-features-and-requirements).

<a name="3.2.1.2"></a>
#### 3.2.1.2 HW Topology management

> This chapter should describe considerations about hardware topology management.

<a name="3.2.1.3"></a>
#### 3.2.1.3 HW Acceleration

> This chapter should describe considerations about hardware acceleration, like device management.

<a name="3.2.1.4"></a>
#### 3.2.1.4 CPU management

> This chapter should describe considerations about CPU management.

> Relate back to features described in the RM [here](../../../ref_model/ref_model/chapters/chapter05.md#521-virtual-compute) and [here](../../../ref_model/ref_model/chapters/chapter05.md#54-nfvi-hw-profiles-features-and-requirements).


<a name="3.2.1.5"></a>
#### 3.2.1.5 Container Runtime Services

The Container Runtime is the component that runs within a Host Operating System (OS) and manages the underlying OS functionality, such as cgroups and namespaces (in Linux), in order to provide a service within which container images can be executed and make use of the infrastructure resources (compute, storage, networking and other I/O devices) abstracted by the Host OS, based on API instructions from the kubelet.

There are a number of different container runtimes. The simplest form, low-level container runtimes, just manage the OS capabilities such as cgroups and namespaces, and then run commands within those cgroups and namesapces. An example of this type of runtime is runc, which underpins many of the high-level runtimes and is considered a reference implementation of the [Open Container Initiative (OCI) runtime spec](https://github.com/opencontainers/runtime-spec). This specification includes detail on how an implementation (i.e. an actual container runtime such as runc) must, for example, configure resource shares and limits (e.g. CPU, Memory, IOPS) for the containers that Kubernetes (via the kubelet) schedules on that host. This is important in ensuring the features and capabilities described in [chapter 5 of the RM](../../../ref_model/ref_model/chapters/chapter05.md) are delivered by this RA and any subsequent Reference Implementations (RIs) to the instance types defined in the RM.

Where low-level runtimes are focused on the execution of a container within an OS, the more complex/complete high-level container runtimes focus on the general management of container images - getting them from somewhere, unpacking them, and then passing them to the low-level runtime, which then executes the container. These high-level runtimes also include a comprehensive API that other applications (e.g. Kubernetes) can use to interact and manage containers. An example of this type of runtime is containerd, which provides the features described above, before passing off the unpacked container image to runc for execution.

When it comes to Kubernetes, the important interface that we need to consider for container management is the [Kubernetes Container Runtime Interface (CRI)](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/), which is an interface specification for any container runtime to be able to integrate with the kubelet on a Kubernetes Node. The CRI decouples the kubelet from the runtime that is running in the Host OS, meaning that the code required to integrate kubelet with a container runtime is not part of the kubelet itself (i.e. if a new container runtime comes along, and it uses CRI, it will work with kubelet). Examples of this type of runtime include containerd (with cri plugin) and cri-o, which was built specifically for Kubernetes.

<a name="3.2.2"></a>
### 3.2.2 Container Networking Services

> This chapter should discuss networking related considerations of container network services, like:
> * Ingress and any limitations on protocol or raw interface support
> * Dependencies on external loadbalancers
> * Regular service mesh related considerations
> * Network Service Mesh related considerations
> * Number of interfaces and IP addresses to be supported by a pod
> * IPv6 single and dual stack needs

> Refer to software profile features [here](../../../ref_model/ref_model/chapters/chapter05.md#523-virtual-networking) and hardware profile features [here](../../../ref_model/ref_model/chapters/chapter05.md#543-network-resources).

<a name="3.2.3"></a>
### 3.2.3 Container Storage Services

Containers, when running, will require ephemeral storage on which to run themselves (i.e. storage on which the unpacked container image is stored and executed from). This ephemeral storage lives and dies with the container and is a directory on the worker node on which the container is running.  Note, this means that the ephemeral storage is mounted locally in the worker node filesystem. The filesystem can also be physically external to the worker node (e.g. iSCSI, NFS, FC) but the container will still reference it as part of the local filesystem.

Additional storage can also be attached to a container through the use of Kubernetes Volumes - this can be storage from the worker node filesystem (through hostPaths - not recommended), or it can be external storage that is accessed through the use of a Volume Plugin. Volume Plugins allow the use of a storage protocol (e.g. iSCSI, NFS) or management API (e.g. Cinder, EBS) for the attaching and mounting of storage into a Pod. This additional storage, that is attached to a container using a Kubernetes Volume, does not live and die with the container but instead follows the lifecycle of the Pod that the container is a part of. This means the Volume persists across container restarts, whilst the Pod is still running. However it does not necessarily persist when a Pod is destroyed, and therefore cannot be considered suitable for persistent data scenarios. The lifecycle of the actual data depends on the Volume Plugin used, and sometimes the configuration of the Volume Plugin.

For those scenarios where data persistence is required, Persistent Volumes (PV) are used in Kubernetes. PVs are resources in a Kubernetes Cluster that are consumed by Persistent Volume Claims (PVCs) and have a lifecycle that is independent of any Pod that uses the PV. A Pod will use a PVC as the volume in the Pod spec; a PVC is a request for persistent storage (a PV) by a Pod. By default, PVs and PVCs are manually created and deleted.

Kubernetes also provides an object called Storage Class, which is created by cluster administrators and maps to storage attributes such as quality-of-service, encryption, data resilience, etc. Storage Classes also enable the dynamic provisioning of Persistent Volumes (as opposed to the default manual creation). This can be beneficial for organisations where the administration of storage is performed separately from the administration of Kubernetes-based workloads.

There are no restrictions or constraints that Kubernetes places on the storage that can be consumed by a workload, in terms of the requirements that are defined in RM sections [5.2.2](../../../ref_model/ref_model/chapters/chapter05.md#522-virtual-storage) (software) and [5.4.2](../../../ref_model/ref_model/chapters/chapter05.md#542-storage-configurations) (hardware). The only point of difference is that Kubernetes does not have a native object storage offering, and this RA is not looking to address this capability directly.

<a name="3.2.4"></a>
### 3.2.4 Kubernetes Application package manager

To manage complex applications consisting from several Pods the reference architecture may provide support for a Kubernetes Application package manager. The package manager may be able to manage the lifecycle a set of Pods and provide a framework to customise a set of parameters for the deployment. The requirement on this Reference Architecture is to provide the Kubernetes API in conformance with the CNCF Conformance test, for the package managers to use in the lifecycle management of the applications they manage.
