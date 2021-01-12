[<< Back](../../kubernetes)

# 3. High Level Architecture
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [3.1 Introduction](#3.1)
* [3.2 Infrastructure Services](#3.2)
    * [3.2.1 Container Compute Services](#3.2.1)
        * [3.2.1.1 Container Runtime Services](#3.2.1.1)
        * [3.2.1.2 CPU Management](#3.2.1.2)
        * [3.2.1.3 Memory and Huge Pages Resources Management](#3.2.1.3)
        * [3.2.1.4 Hardware Topology Management](#3.2.1.4)
        * [3.2.1.5 Node Feature Discovery](#3.2.1.5)
        * [3.2.1.6 Device Plugin Framework](#3.2.1.6)
        * [3.2.1.7 Hardware Acceleration](#3.2.1.7)
        * [3.2.1.8 Scheduling Pods with Non-resilient Applications](#3.2.1.8)
    * [3.2.2 Container Networking Services](#3.2.2)
    * [3.2.3 Container Storage Services](#3.2.3)
    * [3.2.4 Container Package Managers](#3.2.4)

<a name="3.1"></a>
## 3.1 Introduction

The CNTT Kubernetes Reference Architecture (RA) is intended to be an industry
standard independent Kubernetes reference architecture that is not tied to any
specific offering or distribution. No vendor-specific enhancements are required
in order to achieve conformance to CNTT principles; conformance is achieved by
using upstream components or features that are developed by the open source
community. This allows operators to have a common Kubernetes-based architecture
that supports any conformant VNF or CNF deployed on it to operate as expected.
The purpose of this chapter is to outline all the components required to provide
Kubernetes in a consistent and reliable way.  The specification of how to use
these components is detailed in [Chapter 04](chapter04.md).

Kubernetes is already a well documented and widely deployed Open Source project
managed by the Cloud Native Computing Foundation (CNCF). Full documentation of
the Kubernetes code and project can be found at
[https://kubernetes.io/docs/home/](https://kubernetes.io/docs/home/). The
following chapters will only describe the specific features required by the CNTT
Reference Architecture, and how they would be expected to be implemented. For
any information related to standard Kubernetes features and capabilities, refer
back to the standard Kubernetes documentation.

While this reference architecture provides options for pluggable components such
as service mesh and other plugins that might be used,  the focus of the
reference architecture is on the abstracted interfaces and features that are
required for telco type workload management and execution.

Chapter 5 of the Reference Model (RM) describes the
[hardware](../../../ref_model/chapters/chapter05.md#5.3) and
[software](../../../ref_model/chapters/chapter05.md#5.1) profiles that are
descriptions of the capabilities and features that the Cloud Infrastructure
provide to the workloads. As of v2.0, Figure 5-3 in the RM (also shown below)
depicts a high level view of the software profile features that apply to each
instance profile (Basic and Network Intensive). For more information on the
instance profiles please refer to [RM Chapter 4, section
4.2.4](../../../ref_model/chapters/chapter04.md#4.2.4).

<p align="center"><img
src="../../../ref_model/figures/RM_chap5_fig_5_3_SW_profile.png"
width="80%"/></p> <p align="center"><b>Figure 5-3 (from RM):</b> NFVI software
profiles</p>

In addition, the RM Figure 5-4 (shown below) depicts the hardware profile features
that apply to each instance profile.

<p align="center"><img
src="../../../ref_model/figures/RM_chap5_fig_5_4_HW_profile.png"
width="80%"/></p> <p align="center"><b>Figure 5-4 (from RM):</b> NFVI hardware
profiles and host associated capabilities</p>

The features and capabilities described in the software and hardware profiles
are considered throughout this RA, with the RA requirements traceability to the
RM requirements formally documented in [chapter 2, section
2.2](./chapter02.md#2.2) of this RA.

<a name="3.2"></a>
## 3.2 Infrastructure Services

> This chapter shall list the services provided by the infrastructure. Some example of these services are: log collection, monitoring, health check, load balancer. For the sake of clarity CaaS services should be also listed, like container lifecycle management or networking services.

<a name="3.2.1"></a>
### 3.2.1 Container Compute Services

The primary interface between the Physical / Virtual Infrastructure and any
container-relevant components is the Kubernetes Node Operating System.  This is
the OS within which the container runtime exists, and within which the
containers run (and therefore, the OS whose kernel is shared by the referenced
containers).  This is shown in Figure 3-1 below.

<p align="center"><img src="../figures/ch03_hostOS.png" alt="Kubernetes Host
Operating System" Title="Kubernetes Node Operating System" width="65%"/></p>
<p align="center"><b>Figure 3-1:</b> Kubernetes Node Operating System</p>

The Kubernetes Node OS (as with any OS) consists of two main  components:
- Kernel space
- User space

The Kernel is the tightly controlled space that provides an API to applications
running in the user space (which usually have their own southbound interface in
an interpreter or libraries). Key containerisation capabilities such as Control
Groups (cgroups) and namespaces are kernel features, and are used and managed by
the container runtime in order to provide isolation between the user space
processes, which would also include the container itself as well as any
processes running within it. The security of the Kubernetes Node OS and its
relationship to the container and the applications running within the container
or containers is essential to the overall security posture of the entire system,
and must be appropriately secured to ensure processes running in one container
cannot escalate their privileges or otherwise affect processes running in an
adjacent container.  An example and more details of this concept can be found in
[chapter 6](./chapter06.md)).

It is important to note that the container runtime itself is also a set of
processes that run in user space, and therefore also interact with the kernel
via system calls.  Many diagrams will show containers as running on top of the
runtime, or inside the runtime.  More accurately, the containers themselves are
simply processes running within an OS, the container runtime is simply another
set of processes that are used to manage these containers (pull, run, delete,
etc.), and the kernel features required to provide the isolation mechanisms
(cgroups, namespaces, filesystems, etc.) between the components.


<a name="3.2.1.1"></a>
#### 3.2.1.1 Container Runtime Services

The Container Runtime is the component that runs within a Kubernetes Node
Operating System (OS) and manages the underlying OS functionality, such as
cgroups and namespaces (in Linux), in order to provide a service within which
container images can be executed and make use of the infrastructure resources
(compute, storage, networking and other I/O devices) abstracted by the Container
Host OS, based on API instructions from the kubelet.

There are a number of different container runtimes. The simplest form, low-level
container runtimes, just manage the OS capabilities such as cgroups and
namespaces, and then run commands from within those cgroups and namesapces. An
example of this type of runtime is runc, which underpins many of the
higher-level runtimes and is considered a reference implementation of the [Open
Container Initiative (OCI) runtime
spec](https://github.com/opencontainers/runtime-spec). This specification
includes details on how an implementation (i.e. an actual container runtime such
as runc) must, for example, configure resource shares and limits (e.g. CPU,
Memory, IOPS) for the containers that Kubernetes (via the kubelet) schedules on
that host. This is important to ensure that the features and capabilities
described in [chapter 5 of the RM](../../../ref_model/chapters/chapter05.md) are
supported by this RA and delivered by any downstream Reference Implementations
(RIs) to the instance types defined in the RM.

Where low-level runtimes are used for the execution of a container within an OS,
the more complex/complete high-level container runtimes are used for the general
management of container images - moving them to where they need to be executed,
unpacking them, and then passing them to the low-level runtime, which then
executes the container. These high-level runtimes also include a comprehensive
API that other applications (e.g. Kubernetes) can use to interact and manage the
containers. An example of this type of runtime is containerd, which provides the
features described above, before passing off the unpacked container image to
runc for execution.

For Kubernetes the important interface to consider for container management is
the [Kubernetes Container Runtime Interface
(CRI)](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/).
This is an interface specification for any container runtime so that it is able
to integrate with the kubelet on a Kubernetes Node. The CRI decouples the
kubelet from the runtime that is running in the Host OS, meaning that the code
required to integrate kubelet with a container runtime is not part of the
kubelet itself (i.e. if a new container runtime is needed and it uses CRI, it
will work with kubelet). Examples of this type of runtime include containerd
(with CRI plugin) and cri-o, which is built specifically to work with
Kubernetes.

To fullfill `req.inf.vir.01` the architecture should support a container runtime
which provides the isolation of Operating System kernels.

The architecture must support a way to isolate the compute resources of the
infrastructure itself from the workloads compute resources.


<a name="3.2.1.2"></a>
#### 3.2.1.2 CPU Management

CPU management has policies to determine placement preferences to use for workloads that are sensitive to cache affinity or latency, and so the workloads must not be moved by OS scheduler or throttled by kubelet. Additionally, some workloads are sensitive to differences between physical cores and SMT, while others (like DPDK-based workloads) are designed to run on isolated CPUs (like on Linux with cpuset-based selection of CPUs and isolcpus kernel parameter specifying cores isolated from general SMP balancing and scheduler algorithms).

Kubernetes [CPU Manager](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/) works with Topology Manager. Special care needs to be taken of:

•	Supporting isolated CPUs: Using kubelet [Reserved CPUs](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#explicitly-reserved-cpu-list) and Linux isolcpus allows configuration where only isolcpus are allocatable to pods. Scheduling pods to such nodes can be influenced with taints, tolerations and node affinity.

•	Differentiating between physical cores and SMT: When requesting even number of CPU cores for pods, scheduling can be influenced with taints, tolerations, and node affinity.
Kubernetes supports Topology policy per node as beta feature ([documentation](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/)) and not per pod. The Topology Manager receives Topology information from Hint Providers which identify NUMA nodes (defined as server system architecture divisions of CPU sockets) and preferred scheduling. In the case of the pod with Guaranteed QoS class having integer CPU requests, the static CPU Manager policy would return topology hints relating to the exclusive CPU and the Device Manager would provide hints for the requested device.

Memory or Huge Pages are not considered by the Topology Manager. This can be done by the operating system providing best-effort local page allocation for containers as long as there is sufficient free local memory on the node, or with Control Groups (cgroups) cpuset subsystem that can isolate memory to single NUMA node.


<a name="3.2.1.3"></a>
#### 3.2.1.3 Memory and Huge Pages Resources Management

The Reference Model requires the support of Huge Pages in i.cap.018 which is supported by upstream Kubernetes ([documentation](https://kubernetes.io/docs/tasks/manage-hugepages/scheduling-hugepages/)).

For proper mapping of Huge Pages to scheduled pods, both need to have Huge Pages enabled in the operating system (configured in kernel and mounted with correct permissions) and kubelet configuration. Multiple sizes of Huge Pages can be enabled like 2 MiB and 1 GiB.

For some applications, Huge Pages
should be allocated to account for consideration of the underlying HW topology.
This newer feature is missing from Kubernetes, therefore a gap has been
identified and added to [Chapter 6.2.8](./chapter06.md#628-hw-topology-aware-hugepages).


<a name="3.2.1.4"></a>
#### 3.2.1.4 Hardware Topology Management

Scheduling pods across NUMA boundaries can result in lower performance and higher latencies. This would be an issue for applications that require optimizations of CPU isolation, memory and device locality.


<a name="3.2.1.5"></a>
#### 3.2.1.5 Node Feature Discovery

[Node Feature Discovery](https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/index.html) (NFD) can run on every node as a daemon or as a job. NFD detects detailed hardware and software capabilities of each node and then advertises those capabilities as node labels. Those node labels can be used in scheduling pods by using Node Selector or Node Affinity for pods that require such capabilities.


<a name="3.2.1.6"></a>
#### 3.2.1.6 Device Plugin Framework

[Device Plugin Framework](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) advertises device hardware resources to kubelet with which vendors can implement plugins for devices that may require vendor-specific activation and life cycle management, and securely maps these devices to containers.


<a name="3.2.1.7"></a>
#### 3.2.1.7 Hardware Acceleration

Hardware Acceleration Abstraction in RM [3.8 Hardware Acceleration Abstraction](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter03.md#3.8) describes types of hardware acceleration (CPU instructions, Fixed function accelerators, Firmware-programmable adapters, SmartNICs and SmartSwitches), and usage for Infrastructure Level Acceleration and Application Level Acceleration.

Scheduling pods that require or prefer to run on nodes with hardware accelerators will depend on type of accelerator used:

•	CPU instructions can be found with Node Feature Discovery

•	Fixed function accelerators, Firmware-programmable network adapters and SmartNICs can be found and mapped to pods by using Device Plugin.


<a name="3.2.1.8"></a>
#### 3.2.1.8 Scheduling Pods with Non-resilient Applications

Non-resilient applications are sensitive to platform impairments on Compute like pausing CPU cycles (for example because of OS scheduler) or Networking like packet drops, reordering or latencies. Such applications need to be carefully scheduled on nodes and preferably still decoupled from infrastructure details of those nodes.

| # | Intensive on  | Not intensive on | Using hardware acceleration | Requirements for optimized pod scheduling |
|---|---|---|---|---|
| 1 | Compute | Networking (dataplane) | No | CPU Manager |
| 2 | Compute | Networking (dataplane) | CPU instructions | CPU Manager, NFD |
| 3 | Compute | Networking (dataplane) | Fixed function acceleration, Firmware-programmable network adapters or SmartNICs | CPU Manager, Device Plugin |
| 4 | Networking (dataplane) | | No, or Fixed function acceleration, Firmware-programmable network adapters or SmartNICs  | Huge Pages (for DPDK-based applications); CPU Manager with configuration for isolcpus and SMT; Multiple interfaces; NUMA topology; Device Plugin |
| 5 | Networking (dataplane) | | CPU instructions | Huge Pages (for DPDK-based applications); CPU Manager with configuration for isolcpus and SMT; Multiple interfaces; NUMA topology; Device Plugin; NFD |

<p align="center"><b>Table 3-1:</b> Categories of applications, requirements for scheduling pods and Kubernetes features</p>


<a name="3.2.2"></a>
### 3.2.2 Container Networking Services

As all production networking solutions for Kubernetes are based on CNI plugins
and the implicit requirement in [4.2.2 Virtual Network Interface
Specifications](../../../ref_model/chapters/chapter04.md#422-virtual-network-interface-specifications)
that documents the requirement to have the capability to attach several network
interfaces to the pods, the CNTT architecture must support a CNI metaplugin/CNI
multiplexer.

A CNI metaplugin/CNI multiplexer has the capability to attach several
interfaces, using different other CNI plugins, to a pod. Note that the different
network characteristics of the interfaces might require different networking
technologies, which would potentially require different CNI plugins.

To comply with `req.inf.ntw.08`, inter node communication must be served by a
CNI plugin which complies with the default [Kubernetes networking assumptions](https://kubernetes.io/docs/concepts/cluster-administration/networking/#the-kubernetes-network-model).

There are two types of low latency and high throughput networks required by
telco workloads: signalling traffic workloads and user plane traffic workloads.
Networks used for signalling traffic are more demanding than what a standard
overlay network can handle, but still do not need the use of user space
networking. Due to the nature of the signalling protocols used, these type of
networks require NAT-less communication documented in infra.net.cfg.003 and will
need to be served by a CNI plugin with IPVLAN or MACVLAN support. On the other
hand, the low latency, high throughput networks used for handling the user plane
traffic require the capability to use a user space networking technology.

> Note: An infrastructure can provide the possibility to use SR-IOV with DPDK as
an additional feature and still be conformant with CNTT.

> Editors note: The possibility to SR-IOV for DPDK is under discussion.

The integration of SDN solutions required by `req.inf.ntw.05` should be enabled
via their respective CNI integration.

> Note: An SDN solution can manage the pod networks via the Kubernetes API or
can have a CNI integration.

The container based architecture must support telecom equipment networking where
the CNF networks are set up by the operator's network administrators. This is
why, as `req.gen.cnt.05` requires, the architecture must provide a set of
abstract management APIs to manage the network connectivity of the CNF pods
themselves.

The API must support multiple tenants and must require elevated access rights to
manipulate infrastructure related API objects as these operations generally
require reconfiguration of the physical network infrastructure.

To fulfill the requirements of `e.cap.016` the architecture should optionally
support the use of device plugins via the Device Plugin API and the alignment of
the devices, CPU topology and Huge Pages must be supported using the [Topology
Manager](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/).

The architecture must support IPv4, IPv6 and dual stack interfaces of the
workloads as required by `req.inf.ntw.04`.

As Kubernetes Ingress, Egress and Services have no support for all the protocols
needed in telecommunication environments (Diameter, SIP, LDAP, etc) and their
capacity is limited, the architecture must enable the use of alternative load
balancers, including external or ones built into the application. Management of
external load balancers must be possible via Kubernetes API objects.

The well known service meshes are "application service meshes" that address and
interact with the application layer 7 protocols (eg.: HTTP) only. Therefore,
their support is not required in this architecture, as these service meshes are
outside the scope of the infrastructure layer of the CNTT stack.

> Refer to software profile features
[here](../../../ref_model/chapters/chapter05.md#5.1) and hardware profile
features [here](../../../ref_model/chapters/chapter05.md#5.4).

<a name="3.2.3"></a>
### 3.2.3 Container Storage Services

Since its 1.13 version Kubernetes supports Container Storage Interface (CSI) in
production and in-tree volume plugins are moved out from the Kubernetes
repository (see a list of CSI drivers
[here](https://kubernetes-csi.github.io/docs/drivers.html)).

Running containers will require ephemeral storage on which to run themselves
(i.e. storage on which the unpacked container image is stored and executed
from). This ephemeral storage lives and dies with the container and is a
directory on the worker node on which the container is running.  Note, this
means that the ephemeral storage is mounted locally in the worker node
filesystem. The filesystem can be physically external to the worker node
(e.g. iSCSI, NFS, FC) but the container will still reference it as part of the
local filesystem.

Additional storage might also be attached to a container through the use of
Kubernetes Volumes - this can be storage from the worker node filesystem
(through hostPaths - not recommended), or it can be external storage that is
accessed through the use of a Volume Plugin. Volume Plugins allow the use of a
storage protocol (e.g. iSCSI, NFS) or management API (e.g. Cinder, EBS) for the
attaching and mounting of storage into a Pod. This additional storage, that is
attached to a container using a Kubernetes Volume, does not live and die with
the container but instead follows the lifecycle of the Pod that the container is
a part of. This means the Volume persists across container restarts, as long as
the Pod itself is still running. However it does not necessarily persist when a
Pod is destroyed, and therefore cannot be considered suitable for any scenario
requiring persistent data. The lifecycle of the actual data depends on the
Volume Plugin used, and sometimes the configuration of the Volume Plugin as
well.

For those scenarios where data persistence is required, Persistent Volumes (PV)
are used in Kubernetes. PVs are resources in a Kubernetes Cluster that are
consumed by Persistent Volume Claims (PVCs) and have a lifecycle that is
independent of any Pod that uses the PV. A Pod will use a PVC as the volume in
the Pod spec; a PVC is a request for persistent storage (a PV) by a Pod. By
default, PVs and PVCs are manually created and deleted.

Kubernetes also provides an object called Storage Class, which is created by
cluster administrators and maps to storage attributes such as
quality-of-service, encryption, data resilience, etc. Storage Classes also
enable the dynamic provisioning of Persistent Volumes (as opposed to the default
manual creation). This can be beneficial for organisations where the
administration of storage is performed separately from the administration of
Kubernetes-based workloads.

There are no restrictions or constraints that Kubernetes places on the storage
that can be consumed by a workload, in terms of the requirements that are
defined in RM sections
[5.2.2](../../../ref_model/chapters/chapter05.md#522-virtual-storage) (software)
and [5.4.2](../../../ref_model/chapters/chapter05.md#542-storage-configurations)
(hardware). The only point of difference is that Kubernetes does not have a
native object storage offering, and addressing this capability gap directly is
outside of the scope of this RA.

<a name="3.2.4"></a>
### 3.2.4 Kubernetes Application package manager

To manage complex applications consisting of several Pods the Reference
Architecture must provide support for a Kubernetes Application  package manager.
The Package Manager would be able to manage the lifecycle of a set of Pods and
provide a framework to customise a set of parameters for their deployment. The
requirement for this Reference Architecture is to provide a Kubernetes API that
complies with the CNCF Conformance test for the package managers to use in the
lifecycle management of the applications they manage. The Reference Architecture
does not recommend the usage of a Kubernetes Application package manager with a
server side component installed to the Kubernetes cluster (e.g.: Tiller).
