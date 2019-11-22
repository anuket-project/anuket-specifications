[<< Back](../../openstack)

# 3. High Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [3.1 Introduction](#3.1)
* [3.2 Infrastructure Services](#3.2)
    * [3.2.1 Container Runtime Services](#3.2.1)
    * [3.2.2 Container Networking Services](#3.2.2)
    * [3.2.3 Container Storage Services](#3.2.3)
    * [3.2.4 Container Package Managers](#3.2.4)
* [3.3 Heading](#3.3)

<a name="3.1"></a>
## 3.1 Introduction

The CNTT Kubernetes Reference Architecture (RA) aims to provide an industry standard reference architecture independent of the many Kubernetes offerings and distributions. It does not seek to change any vendor implementation assuming CNTT compliance out of the box without vendor specific enhancements that are not up-streamed. This would allow operators to provide a common Kubernetes-based architecture allowing any compliant VNF or CNF to be deployed and operate as expected. The purpose of this chapter is to outline all the components required to provide Kubernetes in a consistent and reliable way.

Kubernetes is already very well documented at [https://kubernetes.io/docs/home/](https://kubernetes.io/docs/home/) so rather than repeat content from there this and following chapters will describe the specific features used and how we expect them to be implemented.

This reference architecture provides optionality in terms of pluggable components such as service mesh and other plugins that might be used, however the focus of the reference architecture is on the abstracted interfaces and features that are required for workload management and execution.

<a name="3.2"></a>
## 3.2 Infrastructure Services

> This chapter shall list the services provided by the infrastructure. Some example of these services can be: log collection, monitoring, health check, load balancer. For the shake of clarity CaaS services should be also listed, like container lifecycle management or networking services.

<a name="3.2.1"></a>
### 3.2.1 Container Runtime Services

The Container Runtime is the component that runs within a Host Operating System (OS) and manages the underlying OS functionality such as cgroups and namespaces (in Linux) in order to provide a service within which container images can be launched.  For the purposes of this document the Container Runtime is not just the true 'runtime' but also the container 'engine' that manages the container-related infrastructure such as networking, security, storage and distributed state.  Essentially the component that pulls an image from a registry, unpacks it and runs it.

There are a number of different container runtimes. The simplest form, low-level container runtimes, just manage the OS capabilities such as cgroups and namespaces, and then run commands within those cgroups and namesapces. An example of this type of runtime is runc, which underpins many of the high-level runtimes and is considered a reference implementation of the [Open Container Initiative (OCI) runtime spec](https://github.com/opencontainers/runtime-spec).

Where low-level runtimes are focussed on the execution of a container within an OS, the more complex/complete high-level container runtimes focus on the general management of container images - getting them from somewhere, unpacking them, and then passing them to the low-level runtime, which then executes the container. These high-level runtimes also include a comprehensive API that other applications (e.g. Kubernetes) can use to interact and manage containers. An example of this type of runtime is containerd, which provides the features described above, before passing off the unpacked container image to runc for execution.

When it comes to Kubernetes, the important interface that we need to consider for container management is the [Kubernetes Container Runtime Interface (CRI)](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md), which is an interface specification for any container runtime to be able to integrate with the kubelet on a Kubernetes Node. The CRI decouples the kubelet from the runtime that is running in the Host OS, meaning that the code required to integrate kubelet with a container runtime is not part of the kubelet itself (i.e. if a new container runtime comes along, and it uses CRI, it will work with kubelet). Examples of this type of runtime include containerd (with cri plugin) and cri-o, which was built specifically for Kubernetes.

<a name="3.2.2"></a>
### 3.2.2 Container Networking Services

> This chapter should discuss networking related considerations of container network services, like:
> * Ingress and any limitations on protocol or raw interface support
> * Dependencies on external loadbalancers
> * Regular service mesh related considerations
> * Network Service Mesh related considerations
> * Number of interfaces and IP addresses to be supported by a pod
> * IPv6 single and dual stack needs

<a name="3.2.3"></a>
### 3.2.3 Container Storage Services

Containers, when running, will require ephemeral storage on which to run themselves (i.e. storage on which the unpacked container image is stored and executed from). This ephemeral storage lives and dies with the container and is a directory on the worker node on which the container is running.  Note, this means that the ephemeral storage is mounted locally in the worker node filesystem. The filesystem can also be physically external to the worker node (e.g. iSCSI, NFS, FC) but the container will still reference it as part of the local filesystem.

Additional ephemeral storage can also be attached to a container through the use of Kubernetes Volumes - this can be storage from the worker node filesystem, or it can be external storage that is accessed through the use of a Volume Plugin. Volume Plugins allow the use of a storage protocol (e.g. iSCSI, NFS) or management API (e.g. Cinder) for the attaching and mounting of storage into a Pod. This additional ephemeral storage, that is attached to a container using a Kubernetes Volume, does not live and die with the container but instead follows the lifecycle of the Pod that the container is a part of. This means the ephemeral Volume persists across container restarts, whilst the Pod is still running.

In Kubernetes, Persistent Volumes (PV) are used when data persistence is required. PVs are resources in a Kubernetes Cluster that are consumed by Persistent Volume Claims (PVCs) and have a lifecycle that is independent of any Pod that uses the PV. A Pod will use a PVC as the volume in the Pod spec; a PVC is a request for persistent storage (a PV) by a Pod. By default, PVs and PVCs are manually created and deleted.

Kubernetes also provides an object called Storage Class, which is created by cluster administrators and maps to storage attributes such as quality-of-service, encryption, data resilience, etc. Storage Classes also enable the dynamic provisioning of Persistent Volumes (as opposed to the default manual creation). This can be beneficial for organisations where the administration of storage is performed separately from the administration of Kubernetes-based workloads.

<a name="3.2.4"></a>
### 3.2.4 Kubernetes Application package manager

To manage complex applications consisting from several Pods the reference architecture may provide support for a Kubernetes Application package manager. The package manager may be able to manage the lifecycle a set of Pods and provide a framework to customise a set of parameters for the deployment.

<a name="3.3"></a>
## 3.3 Heading
