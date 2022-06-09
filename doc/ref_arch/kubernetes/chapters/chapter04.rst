Component Level Architecture
============================

Introduction
------------

This chapter describes in detail the Kubernetes Reference Architecture in terms
of the functional capabilities and how they relate to the Reference Model
requirements, i.e. how the infrastructure profiles are determined, documented
and delivered.

The specifications defined in this chapter will be detailed with unique
identifiers, which will follow the pattern: ``ra2.<section>.<index>``, e.g.
``ra2.ch.001`` for the first requirement in the Kubernetes Node section. These
specifications will then be used as requirements input for the Kubernetes
Reference Implementation and any vendor or community implementations.

Figure 4-1 below shows the architectural components that are described in the
subsequent sections of this chapter.

.. image:: ../figures/ch04_k8s_architecture.png
   :alt: "Figure 4-1: Kubernetes Reference Architecture"


**Figure 4-1:** Kubernetes Reference Architecture

Kubernetes Node
---------------

This section describes the configuration that will be applied to the physical or
virtual machine and an installed Operating System. In order for a Kubernetes Node
to be conformant with the Reference Architecture it must be implemented as per
the following specifications:

.. list-table:: Node Specifications
   :widths: 10 10 40 20 20
   :header-rows: 1

   * - Ref
     - Specification
     - Details
     - Requirement Trace
     - Reference Implementation Trace
   * - ra2.ch.001
     - Huge pages
     - When hosting workloads matching the High Performance profile, it must be possible to enable Huge pages (2048KiB and 1048576KiB) within the Kubernetes Node OS, exposing schedu lable resources hugepages-2Mi and hugepages-1Gi.
     - infra.com.cfg.004
     - RI2 4.3.1
   * - ra2.ch.002
     - SR-IOV capable NICs
     - When hosting workloads matching the High Performance profile, the physical machines on which the Kubernetes Nodes run must be equipped with NICs that are SR-IOV capable.
     - e.cap.013
     - RI2 3.3
   * - ra2.ch.003
     - SR-IOV Virtual Functions Functions
     - When hosting workloads matching the High Performance profile, SR-IOV virtual functions (VFs) must be configured within the Kubernetes Node OS, as the SR-IOV Device Plugin does not manage the creation of these VFs.
     - e.cap.013
     - RI2 4.3.1
   * - ra2.ch.004
     - CPU Simultaneo us Multi-Threa ding (SMT)
     - SMT must be enabled in the BIOS on the physical machine on which the Kubernetes Node runs.
     - infra.hw.cpu.cfg.004
     - RI2 3.3
   * - ra2.ch.005
     - CPU Allocation Ratio - VMs
     - For Kubernetes nodes running as Virtual Machines, the CPU allocation ratio between vCPU and physical CPU core must be 1:1.
     -
     -
   * - ra2.ch.006
     - CPU Allocation Ratio - Pods
     - To ensure the CPU allocation ratio between vCPU and physical CPU core is 1:1, the sum of CPU requests and limits by containers in Pod specifications must remain less than the allocatable quantity of CPU resources (i.e. requests.cpu < allocatable.cpu and limits.cpu < allocatable.cpu).
     - infra.com.cfg.001
     - RI2 3.3
   * - ra2.ch.007
     - IPv6DualStack
     - To support IPv4/IPv6 dual stack networking, the Kubernetes Node OS must support and be allocated routable IPv4 and IPv6 addresses.
     -
     -
   * - ra2.ch.008
     - Physical CPU Quantity
     - The physical machines on which the Kubernetes Nodes run must be equipped with at least 2 physical sockets, each with at least 20 CPU cores.
     - infra.hw.cpu.cfg.001 infra.hw.cpu.cfg.002
     - RI2 3.3
   * - ra2.ch.009
     - Physical Storage
     - The physical machines on which the Kubernetes Nodes run should be equipped with Sold State Drives (SSDs).
     - infra.hw.stg.ssd.cfg.002
     - RI2 3.3
   * - ra2.ch.010
     - Local Filesystem Storage Quantity
     - The Kubernetes Nodes must be equipped with local filesystem capacity of at least 320GB for unpacking and executing containers. Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.
     - e.cap.003
     - RI2 3.3
   * - ra2.ch.011
     - Virtual Node CPU Quantity
     - If using VMs, the Kubernetes Nodes must be equipped with at least 16 vCPUs. Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.
     - e.cap.001
     -
   * - ra2.ch.012
     - Kubernetes Node RAM Quantity
     - The Kubernetes Nodes must be equipped with at least 32GB of RAM. Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.
     - e.cap.002
     - RI2 3.3
   * - ra2.ch.013
     - Physical NIC Quantity
     - The physical machines on which the Kubernetes Nodes run must be equipped with at least four (4) Network Interface Card (NIC) ports.
     - infra.hw.nic.cfg.001
     - RI2 3.3
   * - ra2.ch.014
     - Physical NIC Speed - Basic Profile
     - The speed of NIC ports housed in the physical machines on which the Kubernetes Nodes run for workloads matching the Basic Profile must be at least 10Gbps.
     - infra.hw.nic.cfg.002
     - RI2 3.3
   * - ra2.ch.015
     - Physical NIC Speed - High Performance Profile
     - The speed of NIC ports housed in the physical machines on which the Kubernetes Nodes run for workloads matching the High Performance profile must be at least 25Gbps.
     - infra.hw.nic.cfg.002
     - RI2 3.3
   * - ra2.ch.016
     - Physical PCIe slots
     - The physical machines on which the Kubernetes Nodes run must be equipped with at least eight (8) Gen3.0 PCIe slots, each with at least eight (8) lanes.
     -
     -
   * - ra2.ch.017
     - Immutable infrastructure
     - Whether physical or virtual machines are used, the Kubernetes Node must not be changed after it is instantiated. New changes to the Kubernetes Node must be implemented as new Node instances. This covers any changes from BIOS through Operating System to running processes and all associated configurations.
     - req.gen.cnt.02
     - RI2 4.3.1
   * - ra2.ch.018
     - NFD
     - `Node Feature Discovery <https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/index.html>`__ must be used to ad vertise the detailed software and hardware capabilities of each node in the Kubernetes Cluster.
     - tbd
     - RI2 4.3.1

Node Operating System
---------------------

In order for a Host OS to be compliant with this Reference Architecture it must meet the following requirements:

.. list-table:: Operating System Requirements
   :widths: 10 10 40 20 20
   :header-rows: 1

   * - Ref
     - Specification
     - Details
     - Requirement Trace
     - Reference Implementation Trace
   * - ra2.os.001
     - Linux Distribution
     - A deb/rpm compatible distribution of Linux (this must be used for the master nodes, and can be used for worker nodes).
     - tbd
     - tbd
   * - ra2.os.002
     - Linux Kernel Version
     - A version of the Linux kernel that is compatible with kubeadm - this has been chosen as the baseline because kubeadm is focussed on installing and managing the lifecycle of Kubernetes and nothing else, hence it is easily integrated into higher-level and more complete tooling for the full lifecycle management of the infrastructure, cluster add-ons, etc.
     - tbd
     - tbd
   * - ra2.os.003
     - Windows Server
     - Windows Server (this can be used for worker nodes, but be aware of the limitations).
     - tbd
     - tbd
   * - ra2.os.004
     - Disposable OS
     - In order to support req.gen.cnt.03 (immutable infrastructure), the Host OS must be disposable, meaning the configuration of the Host OS (and associated infrastructure such as VM or bare metal server) must be consistent - e.g. the system software and configuration of that software must be identical apart from those areas of configuration that must be different such as IP addresses and hostnames.
     - tbd
     - tbd
   * - ra2.os.005
     - Automated Deployment
     - This approach to configuration management supports req.lcm.gen.01 (automated deployments)
     - tbd
     - tbd

The following lists the kernel versions that comply with this Reference Architecture specification.

.. list-table:: Operating System Versions
   :widths: 20 20 20
   :header-rows: 1

   * - OS Family
     - Kernel Version(s)
     - Notes
   * - Linux
     - 3.10+
     -
   * - Windows
     - 1809 (10.0.17763)
     - For worker nodes only

Kubernetes
----------

In order for the Kubernetes components to be conformant with the Reference Architecture they must be implemented as per
the following specifications:

.. list-table:: Kubernetes Specifications
   :widths: 10 10 40 20 20
   :header-rows: 1

   * - Ref
     - Specification
     - Details
     - Requirement Trace
     - Reference Implementation Trace
   * - ra2.k8s.001
     - Kubernetes Conformance
     - The Kubernetes distribution, product, or installer used in the implementation must be listed in the `Kubernetes Distributions and Platforms document <https://docs.google.com/spreadsheets/d/1uF9BoDzzisHSQemXHIKegMhuythuq_GL3N1mlUUK2h0/edit#gid=0>`__ and marked (X) as conformantfor the Kubernetes version defined in :ref:`ref_arch/kubernetes/README:required versions of most important components`.
     - req.gen.cnt.03
     - RI2 4.3.1
   * - ra2.k8s.002
     - Highly available etcd
     - An implementation must consist of either three, five or seven nodes running the etcd service (can be colocated on the master nodes, or can run on separate nodes, but not on worker nodes).
     - req.gen.rsl.02, req.gen.avl.01
     - RI2 4.3.1
   * - ra2.k8s.003
     - Highly available control plane
     - An implementation must consist of at least one master node per availability zone or fault domain to ensure the high availability and resilience of the Kubernetes control plane services.
     -
     -
   * - ra2.k8s.012
     - Control plane services
     - A master node must run at least the following Kubernetes control plane services: kube-apiserver, kube-scheduler and kube-controller-manager.
     - req.gen.rsl.02, req.gen.avl.01
     - RI2 4.3.1
   * - ra2.k8s.004
     - Highly available worker nodes
     - An implementation must consist of at least one worker node per availability zone or fault domain to ensure the high availability and resilience of workloads managed by Kubernetes
     - req.gen.rsl.01, req.gen.avl.01, req.kcm.gen.02, req.inf.com.02
     -
   * - ra2.k8s.005
     - Kubernetes API Version
     - In alignment with the `Kubernetes version support policy <https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions>`__, an implementation must use a Kubernetes version as per the subcomponent versions table in :ref:`ref_arch/kubernetes/README:required versions of most important components`.
     -
     -
   * - ra2.k8s.006
     - NUMA Support
     - When hosting workloads matching the High Performance profile, the TopologyManager and CPUManager feature gates must be enabled and configured on the kubelet (note, TopologyManager is enabled by default in Kubernetes v1.18 and later, with CPUManager enabled by default in Kubernetes v1.10 and later). --feature-gates="..., TopologyManager=true,CPUManager=true" --topology-manager-policy=single-numa-node --cpu-manager-policy=static
     - e.cap.007, infra.com.cfg .002, infra.hw.cpu. cfg.003
     -
   * - ra2.k8s.007
     - DevicePlugins Feature Gate
     - When hosting workloads matching the High Performance profile, the DevicePlugins feature gate must be enabled (note, this is enabled by default in Kubernetes v1.10 or later). --feature-gates="...,DevicePlugins=true,..."
     - Various, e.g. e.cap.013
     - RI2 4.3.1
   * - ra2.k8s.008
     - System Resource Reservations
     - To avoid resource starvation issues on nodes, the implementation of the architecture must reserve compute resources for system daemons and Kubernetes system daemons such as kubelet, container runtime, etc. Use the following kubelet flags: --reserved-cpus=[a-z], using two of a-z to reserve 2 SMT threads.
     - i.cap.014
     -
   * - ra2.k8s.009
     - CPU Pinning
     - When hosting workloads matching the High Performance profile, in order to support CPU Pinning, the kubelet must be started with the --cpu-manager-policy=static option. (Note, only containers in Guaranteed pods - where CPU resource requests and limits are identical - and configured with positive-integer CPU requests will take advantage of this. All other Pods will run on CPUs in the remaining shared pool.)
     - infra.com.cfg .003
     -
   * - ra2.k8s.010
     - IPv6DualStack
     - To support IPv6 and IPv4, the IPv6DualStack feature gate must be enabled on various components (requires Kubernetes v1.16 or later). kube-apiserver: --feature-gates="IPv6DualStack=true". kube-controller-manager: --feature-gates="IPv6DualStack=true" --cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR> --service-cluster-ip-range=<IPv4 CIDR>, <IPv6 CIDR> --node-cidr-mask-size-ipv4 ¦ --node-cidr-mask-size-ipv6 defaults to /24 for IPv4 and /64 for IPv6. kubelet: --feature-gates="IPv6DualStack=true". kube-proxy: --cluster-cidr=<IPv4 CIDR>, <IPv6 CIDR> --feature-gates="IPv6DualStack=true"
     - req.inf.ntw. 04
     -
   * - ra2.k8s.011
     - Anuket profile labels
     - To clearly identify which worker nodes are compliant with the different profiles defined by Anuket the worker nodes must be labelled according to the following pattern: an anuket.io/profile/basic label must be set to true on the worker node if it can fulfil the requirements of the basic profile and an anuket.io/profile/network-intensive label must be set to true on the worker node if it can fulfil the requirements of the High Performance profile. The requirements for both profiles can be found in :doc:`ref_arch/kubernetes/chapters/chapter02`.
     -
     -
   * - ra2.k8s.012
     - Kubernetes APIs
     - Kubernetes `Alpha API <https://kubernetes.io/docs/reference/using-api/#api-versioning>`__ are recommended only for testing, therefore all Alpha APIs must be disabled.
     -
     -
   * - ra2.k8s.013
     - Kubernetes APIs
     - Backward compatibility of all supported GA APIs of Kubernetes must be supported.
     -
     -
   * - ra2.k8s.014
     - Security Groups
     - Kubernetes must support NetworkPolicy feature.
     -
     -
   * - ra2.k8s.015
     - Publishing Services (ServiceTypes)
     - Kubernetes must support LoadBalancer `Service (ServiceTypes) <https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types>`__.
     -
     -
   * - ra2.k8s.016
     - Publishing Services (ServiceTypes)
     - Kubernetes must support `Ingress <https://kubernetes.io/docs/concepts/services-networking/ingress/>`__.
     -
     -
   * - ra2.k8s.017
     - Publishing Services (ServiceTypes)
     - Kubernetes should support NodePort `Service (ServiceTypes) <https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types>`__.
     - req.inf.ntw. 17
     -
   * - ra2.k8s.018
     - Publishing Services (ServiceTypes)
     - Kubernetes should support ExternalName `Service (ServiceTypes) <https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types>`__.
     -
     -
   * - ra2.k8s.019
     - Kubernetes APIs
     - Kubernetes Beta APIs must be supported only when a stable GA of the same version doesn't exist.
     - req.int.api. 04
     -

Container runtimes
------------------

.. list-table:: Container Runtime Specifications
   :widths: 10 10 40 20 20
   :header-rows: 1

   * - Ref
     - Specification
     - Details
     - Requirement Trace
     - Reference Implementation Trace
   * - ra2.crt.001
     - Conformance with OCI 1.0 runtime spec
     - The container runtime must be implemented as per the `OCI 1.0 <https://github.com/opencontainers/runtime-spec/blob/master/spec.md>`__ (Open Container Initiative 1.0) specification.
     - req.gen.ost. 01
     - RI2 4.3.1
   * - ra2.crt.002
     - Kubernetes Container Runtime Interface (CRI)
     - The Kubernetes container runtime must be implemented as per the `Kubernetes Container Runtime Interface (CRI) <https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/>`__
     - req.gen.ost. 01
     - RI2 4.3.1

Networking solutions
--------------------

In order for the networking solution(s) to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

.. list-table:: Networking Solution Specifications
   :widths: 10 10 40 20 20
   :header-rows: 1

   * - Ref
     - Specification
     - Details
     - Requirement Trace
     - Reference Implementation Trace
   * - ra2.ntw.001
     - Centralised network administration
     - The networking solution deployed within the implementation must be administered through the Kubernetes API using native Kubernetes API resources and objects, or Custom Resources.
     - req.inf.ntw. 03
     - RI2 4.3.1
   * - ra2.ntw.002
     - Default Pod Network - CNI
     - The networking solution deployed within the implementation must use a CNI-conformant Network Plugin for the Default Pod Network, as the alternative (kubenet) does not support cross-node networking or Network Policies.
     - req.gen.ost. 01, req.inf.ntw. 08
     - RI2 4.3.1
   * - ra2.ntw.003
     - Multiple connection points
     - The networking solution deployed within the implementation must support the capability to connect at least FIVE connection points to each Pod, which are additional to the default connection point managed by the default Pod network CNI plugin.
     - e.cap.004
     - RI2 4.3.1
   * - ra2.ntw.004
     - Multiple connection points presentation
     - The networking solution deployed within the implementation must ensure that all additional non-default connection points are requested by Pods using standard Kubernetes resource scheduling mechanisms such as annotations or container resource requests and limits.
     - req.inf.ntw. 03
     - RI2 4.3.1
   * - ra2.ntw.005
     - Multiplexer / meta-plugin
     - The networking solution deployed within the implementation may use a multiplexer/meta-plugin.
     - req.inf.ntw. 06, req.inf.ntw. 07
     - RI2 4.3.1
   * - ra2.ntw.006
     - Multiplexer / meta-plugin CNI Conformance
     - If used, the selected multiplexer/meta-plugin must integrate with the Kubernetes control plane via CNI.
     - req.gen.ost. 01
     - RI2 4.3.1
   * - ra2.ntw.007
     - Multiplexer / meta-plugin CNI Plugins
     - If used, the selected multiplexer/meta-plugin must support the use of multiple CNI-conformant Network Plugins.
     - req.gen.ost. 01, req.inf.ntw. 06
     - RI2 4.3.1
   * - ra2.ntw.008
     - SR-IOV Device Plugin for High Performance
     - When hosting workloads that match the High Performance profile and require SR-IOV acceleration, a Device Plugin for SR-IOV must be used to configure the SR-IOV devices and advertise them to the kubelet.
     - e.cap.013
     - RI2 4.3.1
   * - ra2.ntw.009
     - Multiple connection points with multiplexer / meta-plugin
     - When a multiplexer/meta-plugin is used, the additional non-default connection points must be managed by a CNI-conformant Network Plugin.
     - req.gen.ost. 01
     - RI2 4.3.1
   * - ra2.ntw.010
     - User plane networking
     - When hosting workloads matching the High Performance profile, CNI network plugins that support the use of DPDK, VPP, and/or SR-IOV must be deployed as part of the networking solution.
     - infra.net.acc .cfg.001
     - RI2 4.3.1
   * - ra2.ntw.011
     - NATless connectivity
     - When hosting workloads that require source and destination IP addresses to be preserved in the traffic headers, a NATless CNI plugin that exposes the pod IP directly to the external networks (e.g. Calico, MACVLAN or IPVLAN CNI plugins) must be used.
     - req.inf.ntw. 14
     -
   * - ra2.ntw.012
     - Device Plugins
     - When hosting workloads matching the High Performance profile that require the use of FPGA, SR-IOV or other Acceleration Hardware, a Device Plugin for that FPGA or Acceleration Hardware must be used.
     - e.cap.016, e.cap.013
     - RI2 4.3.1
   * - ra2.ntw.013
     - Dual stack CNI
     - The networking solution deployed within the implementation must use a CNI-conformant Network Plugin that is able to support dual-stack IPv4/IPv6 networking.
     - req.inf.ntw. 04
     -
   * - ra2.ntw.014
     - Security Groups
     - The networking solution deployed within the implementation must support network policies.
     - infra.net.cfg .004
     -
   * - ra2.ntw.015
     - IPAM plugin for multiplexer
     - When a multiplexer/meta-plugin is used, a CNI-conformant IPAM Network Plugin must be installed to allocate IP addresses for secondary network interfaces across all nodes of the cluster.
     - req.inf.ntw. 10
     -

Storage components
------------------

In order for the storage solutions to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

.. list-table:: Storage Solution Specifications
   :widths: 10 10 40 20 20
   :header-rows: 1

   * - Ref
     - Specification
     - Details
     - Requirement Trace
     - Reference Implementation Trace
   * - ra2.stg.001
     - Ephemeral Storage
     - An implementation must support ephemeral storage, for the unpacked container images to be stored and executed from, as a directory in the filesystem on the worker node on which the container is running. See the Container runtimes section above for more information on how this meets the requirement for ephemeral storage for containers.
     -
     -
   * - ra2.stg.002
     - Kubernetes Volumes
     - An implementation may attach additional storage to containers using Kubernetes Volumes.
     -
     -
   * - ra2.stg.003
     - Kubernetes Volumes
     - An implementation may use Volume Plugins (see ra2.stg.005 below) to allow the use of a storage protocol (e.g., iSCSI, NFS) or management API (e.g., Cinder, EBS) for the attaching and mounting of storage into a Pod.
     -
     -
   * - ra2.stg.004
     - Persistent Volumes
     - An implementation may support Kubernetes Persistent Volumes (PV) to provide persistent storage for Pods. Persistent Volumes exist independent of the lifecycle of containers and/or pods.
     - req.inf.stg. 01
     -
   * - ra2.stg.005
     - Storage Volume Types
     - An implementation must support the following Volume types: emptyDir, ConfigMap, Secret and PersistentVolumeClaim. Other Volume plugins may be supported to allow for the use of a range of backend storage systems.
     -
     -
   * - ra2.stg.006
     - Container Storage Interface (CSI)
     - An implementation may support the Container Storage Interface (CSI), an Out-of-tree plugin. In order to support CSI, the feature gates CSIDriverRegistry and CSINodeInfo must be enabled. The implementation must use a CSI driver (`full list of CSI drivers <https://kubernetes-csi.github.io/docs/drivers.html>`__). An implementation may support ephemeral storage through a CSI-compatible volume plugin in which case the CSIInlineVolume feature gate must be enabled. An implementation may support Persistent Volumes through a CSI-compatible volume plugin in which case the CSIPersistentVolume feature gate must be enabled.
     -
     -
   * - ra2.stg.007
     -
     - An implementation should use Kubernetes Storage Classes to support automation and the separation of concerns between providers of a service and consumers of the service.
     -
     -

A note on object storage:

-  This Reference Architecture does not include any specifications for object
   storage, as this is neither a native Kubernetes object, nor something that is
   required by CSI drivers. Object storage is an application-level requirement
   that would ordinarily be provided by a highly scalable service offering rather
   than being something an individual Kubernetes cluster could offer.

..

   Todo: specifications/commentary to support req.inf.stg.04 (SDS) and req.inf.stg.05 (high performance and
   horizontally scalable storage). Also req.sec.gen.06 (storage resource isolation), req.sec.gen.10 (CIS - if
   applicable) and req.sec.zon.03 (data encryption at rest).

Service meshes
--------------

Application service meshes are not in scope for the architecture. The service mesh is a dedicated infrastructure layer
for handling service-to-service communication, and it is recommended to secure service-to-service communications within
a cluster and to reduce the attack surface. The benefits of the service mesh framework are described in
:ref:`chapters/chapter05:use transport layer security and service mesh`. In addition to securing communications, the
use of a service mesh extends Kubernetes capabilities regarding observability and reliability.

Network service mesh specifications are handled in section `4.5 Networking solutions <#networking-solutions>`__.

Kubernetes Application package manager
--------------------------------------

In order for the application package managers to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

.. list-table:: Kubernetes Application Package Specifications
   :widths: 10 10 40 20 20
   :header-rows: 1

   * - Ref
     - Specification
     - Details
     - Requirement Trace
     - Reference Implementation Trace
   * - ra2.pkg.001
     - API-based package management
     - A package manager must use the Kubernetes APIs to manage application artifacts. Cluster-side components such as Tiller are not supported.
     - req.int.api. 02
     -
   * - ra2.pkg.002
     - Helm version 3
     - All workloads must be packaged using Helm (version 3) charts.
     -
     -

Helm version 3 has been chosen as the Application packaging mechanism to ensure compliance with the
`ONAP ASD NF descriptor specification <https://wiki.onap.org/display/DW/Application+Service+Descriptor+%28ASD%29+and+pac
kaging+Proposals+for+CNF>`__ and `ETSI SOL0001 rel. 4 MCIOP specification <https://www.etsi.org/deliver/etsi_gs/NFV-SOL/
001_099/001/04.02.01_60/gs_NFV-SOL001v040201p.pdf>`__.

**Table 4-8:** Kubernetes Application Package Manager Specifications

Kubernetes workloads
--------------------

In order for the Kubernetes workloads to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

.. list-table:: Kubernetes Workload Specifications
   :widths: 10 20 50 10 10
   :header-rows: 1

   * - Ref
     - Specification
     - Details
     - Requirement Trace
     - Reference Implementation Trace
   * - ra2.app.001
     - `Root <https://github.com/opencontainers/runtime-spec/blob/master/config.md>`__ Parameter Group (OCI Spec)
     - Specifies the container's root filesystem.
     - TBD
     - N/A
   * - ra2.app.002
     - `Mounts <https://github.com/opencontainers/runtime-spec/blob/master/config.md#mounts>`__ Parameter Group (OCI Spec)
     - Specifies additional mounts beyond root.
     - TBD
     - N/A
   * - ra2.app.003
     - `Process <https://github.com/opencontainers/runtime-spec/blob/master/config.md#process>`__ Parameter Group (OCI Spec)
     - Specifies the container process.
     - TBD
     - N/A
   * - ra2.app.004
     - `Hostname <https://github.com/opencontainers/runtime-spec/blob/master/config.md#hostname>`__ Parameter Group (OCI Spec)
     - Specifies the container's hostname as seen by processes running inside the container.
     - TBD
     - N/A
   * - ra2.app.005
     - `User <https://github.com/opencontainers/runtime-spec/blob/master/config.md#user>`__ Parameter Group (OCI Spec)
     - User for the process is a platform-specific structure that allows specific control over which user the process runs as.
     - TBD
     - N/A
   * - ra2.app.006
     - Consumption of additional, non-default connection points
     - Any additional non-default connection points must be requested through the use of workload annotations or resource requests and limits within the container spec passed to the Kubernetes API Server.
     - req.int.api.01
     - N/A
   * - ra2.app.007
     - Host Volumes
     - Workloads should not use hostPath volumes, as `Pods with identical configuration <https://kubernetes.io/docs/concepts/storage/volumes/#hostpath>`__ (such as those created from a PodTemplate) may behave differently on different nodes due to different files on the nodes.
     - req.kcm.gen.02
     - N/A
   * - ra2.app.008
     - Infrastructure dependency
     - Workloads must not rely on the availability of the master nodes for the successful execution of their functionality (i.e. loss of the master nodes may affect non-functional behaviours such as healing and scaling, but components that are already running will continue to do so without issue).
     - TBD
     - N/A
   * - ra2.app.009
     - Device plugins
     - Workload descriptors must use the resources advertised by the device plugins to indicate their need for an FPGA, SR-IOV or other acceleration device.
     - TBD
     - N/A
   * - ra2.app.010
     - Node Feature Discovery (NFD)
     - Workload descriptors must use the labels advertised by `Node Feature Discovery <https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/index.html>`__ to indicate which node software of hardware features they need.
     - TBD
     - N/A
   * - ra2.app.011
     - Published helm chart
     - Helm charts of the CNF must be published into a helm registry and must not be used from local copies.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-helm-chart-is-published-helm_chart_published>`__
     - N/A
   * - ra2.app.012
     - Valid Helm chart
     - Helm charts of the CNF must be valid and should pass the helm lint validation.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-helm-chart-is-valid-helm_chart_vali   d>`__
     - N/A
   * - ra2.app.013
     - Rolling update
     - Rolling update of the CNF must be possible using Kubernetes deployments.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-the-cnf-can-perform-a-rolling-update-rolling_update>`__
     - N/A
   * - ra2.app.014
     - Rolling downgrade
     - Rolling downgrade of the CNF must be possible using Kubernetes deployments.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-a-cnf-version-can-be-downgraded-through-a-rolling_downgrade-rolling_downgrade>`__
     - N/A
   * - ra2.app.015
     - CNI compatibility
     - The CNF must use CNI compatible networking plugins.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-the-cnf-is-compatible-with-different-cnis-cni_compatibility>`__
     - N/A
   * - ra2.app.016
     - Kubernetes API stability
     - The CNF must not use any Kubernetes alpha API-s.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#poc-to-check-if-a-cnf-uses-kubernetes-alpha-apis-alpha_k8s_apis-alpha_k8s_apis>`__
     - N/A
   * - ra2.app.017
     - CNF resiliency (node drain)
     - CNF must not loose data, must continue to run and its readiness probe outcome must be Success even in case of a node drain and rescheduling occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-node-drain-occurs-node_drain>`__
     - N/A
   * - ra2.app.018
     - CNF resiliency (network latency)
     - CNF must not loose data, must continue to run and its readiness probe outcome must be Success even in case of network latency up to 2000 ms occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-network-latency-occurs-pod_network_latency>`__
     - N/A
   * - ra2.app.019
     - CNF resiliency (pod delete)
     - CNF must not loose data, must continue to run and its readiness probe outcome must be Success even in case of pod delete occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-disk-fill-occurs-disk_fill>`__
     - N/A
   * - ra2.app.020
     - CNF resiliency (pod memory hog)
     - CNF must not loose data, must continue to run and its readiness probe outcome must be Success even in case of pod memory hog occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-pod-memory-hog-occurs-pod_memory_hog>`__
     - N/A
   * - ra2.app.021
     - CNF resiliency (pod I/O stress)
     - CNF must not loose data, must continue to run and its readiness probe outcome must be Success even in case of pod I/O stress occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-pod-io-stress-occurs-pod_io_stress>`__
     - N/A
   * - ra2.app.022
     - CNF resiliency (pod network corruption)
     - CNF must not loose data, must continue to run and its readiness probe outcome must be Success even in case of pod network corruption occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-pod-network-corruption-occurs-pod_network_corruptio  n>`__
     - N/A
   * - ra2.app.023
     - CNF resiliency (pod network duplication)
     - CNF must not loose data, must continue to run and its readiness probe outcome must be Success even in case of pod network duplication occurs.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#test-if-the-cnf-crashes-when-pod-network-duplication-occurs-pod_network_duplication>`__
     - N/A
   * - ra2.app.024
     - CNF resiliency (pod DNS error)
     - CNF must not lose data, must continue to run and its readiness probe outcome must be Success even in case of pod DNS error occurs.
     -
     - N/A
   * - ra2.app.025
     - CNF local storage
     - CNF must not use local storage.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-the-cnf-uses-local-storage-no_local_volume_configuration>`__
     - N/A
   * - ra2.app.026
     - Liveness probe
     - All Pods of the CNF must have livenessProbe defined.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-there-is-a-liveness-entry-in-the-helm-chart-liveness>`__
     - N/A
   * - ra2.app.027
     - Readiness probe
     - All Pods of the CNF must have readinessProbe defined.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-there-is-a-readiness-entry-in-the-helm-chart-readiness>`__
     - N/A
   * - ra2.app.028
     - No access to container daemon sockets
     - The CNF must not have any of the container daemon sockets (e.g.: /var/run/docker.sock, /var/run/containerd.sock or /var/run/crio.sock) mounted.
     -
     - N/A
   * - ra2.app.029
     - No automatic service account mapping
     - Non specified service accounts must not be automatically mapped. To prevent this the automountServiceAccountToken: false flag must be set in all Pods of the CNF.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-there-are-service-accounts-that-are-automatically-mapped-application_credentials>`__
     - N/A
   * - ra2.app.030
     - No host network access
     - Host network must not be attached to any of the Pods of the CNF. hostNetwork attribute of the Pod specifications must be False or should not be specified.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-there-is-a-host-network-attached-to-a-pod-host_network>`__
     - N/A
   * - ra2.app.031
     - Host process namespace separation
     - Pods of the CNF must not share the host process ID namespace or the host IPC namespace. Pod manifests must not have the hostPID or the hostIPC attribute set to true.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-containers-are-running-with-hostpid-or-hostipc-privileges-host_pid_ipc_privileges>`__
     - N/A
   * - ra2.app.032
     - Resource limits
     - All containers and namespaces of the CNF must have defined resource limits for at least CPU and memory resources.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-containers-have-resource-limits-defined-resource_policies>`__
     - N/A
   * - ra2.app.033
     - Read only filesystem
     - All containers of the CNF must have a read only filesystem. The readOnlyRootFilesystem attribute of the Pods in the their securityContext should be set to true.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-containers-have-immutable-file-systems-immutable_file_systems>`__
     - N/A
   * - ra2.app.034
     - Container image tags
     - All referred container images in the Pod manifests must be referred by a version tag pointing to a concrete version of the image. latest tag must not be used.
     -
     - N/A
   * - ra2.app.035
     - No hardcoded IP addresses
     - The CNF must not have any hardcoded IP addresses in its Pod specifications.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-test-if-there-are-any-non-declarative-hardcoded-ip-addresses-or-subnet-masks-in-the-k8s-runtime-configuration>`__
     - N/A
   * - ra2.app.036
     - No node ports
     - Service declarations of the CNF must not contain nodePort definition.
     - `Kubernetes documentation <https://kubernetes.io/docs/concepts/services-networking/service/>`__
     - N/A
   * - ra2.app.037
     - Immutable config maps
     - ConfigMaps used by the CNF must be immutable.
     - `Kubernetes documentation <https://kubernetes.io/docs/concepts/configuration/configmap/#configmap-immutable>`__
     - N/A
   * - ra2.app.038
     - Horizontal scaling
     - Increasing and decreasing of the CNF capacity should be implemented using horizontal scaling. If horizontal scaling is supported, automatic scaling must be possible using Kubernetes `Horizontal Pod Autoscale (HPA) <https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/>`__ feature.
     - TBD
     - N/A
   * - ra2.app.039
     - CNF image size
     - The different container images of the CNF should not be bigger than 5GB.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-the-cnf-has-a-reasonable-image-size-reasonable_image_size>`__
     - N/A
   * - ra2.app.040
     - CNF startup time
     - Startup time of the Pods of a CNF should not be more than 60s where startup time is the time between starting the Pod until the readiness probe outcome is Success.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-the-cnf-have-a-reasonable-startup-time-reasonable_startup_time>`__
     - N/A
   * - ra2.app.041
     - No privileged mode
     - None of the Pods of the CNF should run in privileged mode.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-there-are-any-privileged-containers-kubscape-version-privileged_containers>`__
     - N/A
   * - ra2.app.042
     - No root user
     - None of the Pods of the CNF should run as a root user.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-any-containers-are-running-as-a-root-user-checks-the-user-outside-the-container-that-is-running-dockerd-non_root_user>`__
     - N/A
   * - ra2.app.043
     - No privilege escalation
     - None of the containers of the CNF should allow privilege escalation.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-there-are-any-privileged-containers-kubscape-version-privileged_containers>`__
     - N/A
   * - ra2.app.044
     - Non-root user
     - All Pods of the CNF should be able to execute with a non-root user having a non-root group. Both runAsUser and runAsGroup attributes should be set to a greater value than 999.
     - `CNCF CNF Testsuite <https://github.com/cncf/cnf-testsuite/blob/main/RATIONALE.md#to-check-if-containers-are-running-with-non-root-user-with-non-root-membership-non_root_containers>`__
     - N/A
   * - ra2.app.045
     - Labels
     - Pods of the CNF should define at least the following labels: app.kubernetes.io/name, app.kubernetes.io/version and app.kubernetes.io/part-of
     - `Kubernetes documentation <https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/>`__
     - N/A

Additional required components
------------------------------

   This chapter should list any additional components needed to provide the services defined in Chapter 3.2 (e.g., Prometheus)

