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

+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
| Ref          | Specification| Details                                      | Requirement           | Reference             |
|              |              |                                              | Trace                 | Implementation Trace  |
+==============+==============+==========+===================================+=======================+=======================+
|``ra2.ch.001``|Huge pages    |When hosting workloads matching the High      |`infra.com.cfg.004 <./c|`4.3.1 <../../../ref_im|
|              |              |Performance profile, it **must** be possible  |hapter02.md#cloud-infra|pl/cntt-ri2/chapters/ch|
|              |              |to enable Huge pages (2048KiB and 1048576KiB) |structure-software-prof|apter04.md#installation|
|              |              |within the Kubernetes Node OS, exposing schedu|ile-requirements>`__   |-on-bare-metal-infratru|
|              |              |lable resources ``hugepages-2Mi`` and         |                       |cture>`__              |
|              |              |``hugepages-1Gi``.                            |                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.002``|SR-IOV capable|When hosting workloads matching the High      |`e.cap.013 <./chapter02|`3.3 <../../../ref_impl|
|              |NICs          |Performance profile, the physical machines on |.md#cloud-infrastructur|/cntt-ri2/chapters/chap|
|              |              |which the Kubernetes Nodes run **must** be    |e-software-profile-requ|ter03.md#infrastructure|
|              |              |equipped with NICs that are SR-IOV capable.   |irements>`__           |-requirements>`__      |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.003``|SR-IOV Virtual|When hosting workloads matching the High      |`e.cap.013 <./chapter02|`4.3.1 <../../../ref_im|
|              |Functions     |Performance profile, SR-IOV virtual functions |.md#cloud-infrastructur|pl/cntt-ri2/chapters/ch|
|              |Functions     |(VFs) **must** be configured within the       |e-software-profile-requ|apter04.md#installation|
|              |              |Kubernetes Node OS, as the SR-IOV Device      |irements>`__           |-on-bare-metal-infratru|
|              |              |Plugin does not manage the creation of these  |                       |cture>`__              |
|              |              |VFs.                                          |                       |                       |      
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.004``|CPU Simultaneo|SMT **must** be enabled in the BIOS on the    |`infra.hw.cpu.cfg.004  |`3.3 <../../../ref_impl|
|              |us Multi-Threa|physical machine on which the Kubernetes Node |<./chapter02.md#cloud-i|/cntt-ri2/chapters/chap|
|              |ding (SMT)    |runs.                                         |nfrastructure-hardware-|ter03.md#infrastructure|
|              |              |                                              |profile-require        |-requirements>`__      |
|              |              |                                              |ments>`__              |                       |      
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.005``|CPU Allocation|For Kubernetes nodes running as Virtual       |                       |                       |
|              |Ratio - VMs   |Machines, the CPU allocation ratio between    |                       |                       |
|              |              |vCPU and physical CPU core **must** be 1:1.   |                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.006``|CPU           |To ensure the CPU allocation ratio between    |`infra.com.cfg.001     |`3.3 <../../../ref_impl|
|              |Allocation    |vCPU and physical CPU core is 1:1, the sum of |<./chapter02.md#cloud-i|/cntt-ri2/chapters/chap|
|              |Ratio - Pods  |CPU requests and limits by containers in Pod  |nfrastructure-software-|ter03.md#infrastructure|
|              |              |specifications **must** remain less than the  |profile-require        |-requirements>`__      |
|              |              |allocatable quantity of CPU resources (i.e.   |ments>`__              |                       |
|              |              |``requests.cpu < allocatable.cpu`` and        |                       |                       |
|              |              |``limits.cpu < allocatable.cpu``).            |                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.007``|IPv6DualStack |To support IPv4/IPv6 dual stack networking,   |                       |                       | 
|              |              |the Kubernetes Node OS **must** support and   |                       |                       |
|              |              |be allocated routable IPv4 and IPv6 addresses.|                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.008``|Physical CPU  |The physical machines on which the Kubernetes |`infra.hw.cpu.cfg.001  |`3.3 <../../../ref_impl|
|              |Quantity      |Nodes run **must** be equipped with at least  |<./chapter02.md#cloud-i|/cntt-ri2/chapters/chap|
|              |              |2 physical sockets, each with at least 20     |nfrastructure-hardware-|ter03.md#infrastructure|
|              |              |CPU cores.                                    |profile-require        |-requirements>`__      |
|              |              |                                              |ments>`__,             |                       |
|              |              |                                              |`infra.hw.cpu.cfg.002  |                       |
|              |              |                                              |<./chapter02.md#cloud-i|                       |
|              |              |                                              |nfrastructure-hardware-|                       |
|              |              |                                              |profile-require        |                       |
|              |              |                                              |ments>`__              |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.009``|Physical      |The physical machines on which the Kubernetes |`infra.hw.stg.ssd.cfg.0|`3.3 <../../../ref_impl|
|              |Storage       |Nodes run **should** be equipped with Sold    |02 <./chapter02.md#clou|/cntt-ri2/chapters/chap|
|              |              |State Drives (SSDs).                          |d-infrastructure-hardwa|ter03.md#infrastructure|
|              |              |                                              |re-profile-require     |-requirements>`__      |
|              |              |                                              |ments>`__              |                       |
|              |              |                                              |                       |                       |      
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.010``|Local         |The Kubernetes Nodes **must** be equipped     |`e.cap.003 <./chapter02|`3.3 <../../../ref_impl|
|              |Filesystem    |with local filesystem capacity of at least    |.md#cloud-infrastructur|/cntt-ri2/chapters/chap|
|              |Storage       |320GB for unpacking and executing containers. |e-software-profile-capa|ter03.md#infrastructure|
|              |Quantity      |Note, extra should be provisioned to cater    |bilities>`__           |-requirements>`__      |
|              |              |for any overhead required by the Operating    |                       |                       |
|              |              |System and any required OS processes such as  |                       |                       |
|              |              |the container runtime, Kubernetes agents, etc.|                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.011``|Virtual Node  |If using VMs, the Kubernetes Nodes **must**   |`e.cap.001 <./chapter02|                       |
|              |CPU Quantity  |be equipped with at least 16 vCPUs. Note,     |.md#cloud-infrastructur|                       |
|              |              |extra should be provisioned to cater for any  |e-software-profile-capa|                       |
|              |              |overhead required by the Operating System and |bilities>`__           |                       |
|              |              |any required OS processes such as the         |                       |                       |
|              |              |container runtime, Kubernetes agents, etc.    |                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.012``|Kubernetes    |The Kubernetes Nodes **must** be equipped     |`e.cap.002 <./chapter02|`3.3 <../../../ref_impl|
|              |Node RAM      |with at least 32GB of RAM. Note, extra should |.md#cloud-infrastructur|/cntt-ri2/chapters/chap|
|              |Quantity      |be provisioned to cater for any overhead      |e-software-profile-capa|ter03.md#infrastructure|
|              |              |required by the Operating System and any      |bilities>`__           |-requirements>`__      |
|              |              |required OS processes such as the container   |                       |                       |
|              |              |runtime, Kubernetes agents, etc.              |                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.013``|Physical      |The physical machines on which the Kubernetes |`infra.hw.nic.cfg.001  |`3.3 <../../../ref_impl|
|              |NIC Quantity  |Nodes run **must** be equipped with at least  |<./chapter02.md#cloud-i|/cntt-ri2/chapters/chap|
|              |              |four (4) Network Interface Card (NIC) ports.  |nfrastructure-hardware-|ter03.md#infrastructure|
|              |              |                                              |profile-require        |-requirements>`__      |
|              |              |                                              |ments>`__              |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.014``|Physical      |The speed of NIC ports housed in the physical |`infra.hw.nic.cfg.002  |`3.3 <../../../ref_impl|
|              |NIC Speed -   |machines on which the Kubernetes Nodes run    |<./chapter02.md#cloud-i|/cntt-ri2/chapters/chap|
|              |Basic Profile |for workloads matching the Basic Profile      |nfrastructure-hardware-|ter03.md#infrastructure|
|              |              |**must** be at least 10Gbps.                  |profile-require        |-requirements>`__      |
|              |              |                                              |ments>`__              |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.015``|Physical      |The speed of NIC ports housed in the physical |`infra.hw.nic.cfg.002  |`3.3 <../../../ref_impl|
|              |NIC Speed -   |machines on which the Kubernetes Nodes run    |<./chapter02.md#cloud-i|/cntt-ri2/chapters/chap|
|              |High          |for workloads matching the High Performance   |nfrastructure-hardware-|ter03.md#infrastructure|
|              |Performance   |profile **must** be at least 25Gbps.          |profile-require        |-requirements>`__      |
|              |Profile       |                                              |ments>`__              |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.016``|Physical PCIe |The physical machines on which the Kubernetes |                       |                       |
|              |slots         |Nodes run **must** be equipped with at least  |                       |                       |
|              |              |eight (8) Gen3.0 PCIe slots, each with at     |                       |                       |
|              |              |least eight (8) lanes.                        |                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.017``|Immutable     |Whether physical or virtual machines are      |`req.gen.cnt.02 <./chap|`4.3.1 <../../../ref_im|
|              |infrastructure|used, the Kubernetes Node **must not** be     |ter02.md#kubernetes-arc|pl/cntt-ri2/chapters/ch|
|              |              |changed after it is instantiated. New changes |hitecture-require      |apter04.md#installation|
|              |              |to the Kubernetes Node must be implemented as |ments>`__              |-on-bare-metal-infratru|
|              |              |new Node instances. This covers any changes   |                       |cture>`__              |
|              |              |from BIOS through Operating System to running |                       |                       |
|              |              |processes and all associated configurations.  |                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+
|``ra2.ch.018``|NFD           |`Node Feature Discovery <https://kubernetes-si|TBD                    |`4.3.1 <../../../ref_im|
|              |              |gs.github.io/node-feature-discovery/stable/get|                       |pl/cntt-ri2/chapters/ch|
|              |              |-started/index.html>`__ **must** be used to ad|                       |apter04.md#installa    |
|              |              |vertise the detailed software and hardware    |                       |tion-on-bare-metal-infr|
|              |              |capabilities of each node in the Kubernetes   |                       |atructure>`__          |
|              |              |Cluster.                                      |                       |                       |
+--------------+--------------+----------------------------------------------+-----------------------+-----------------------+

**Table 4-1:** Node Specifications

Node Operating System
---------------------

In order for a Host OS to be compliant with this Reference Architecture it must meet the following requirements:

+--------------+---------------+-----------------------------------------------+-----------------------+-----------------------+
| Ref          | Specification | Details                                       | Requirement           | Reference             |
|              |               |                                               | Trace                 | Implementation Trace  |
+==============+===============+===========+===================================+=======================+=======================+
|``ra2.os.001``| Linux         | A deb/rpm compatible distribution of Linux    | tbd                   | tbd                   |
|              | Distribution  | (this must be used for the master nodes, and  |                       |                       |
|              |               | can be used for worker nodes).                |                       |                       |
+--------------+---------------+-----------------------------------------------+-----------------------+-----------------------+
|``ra2.os.002``| Linux Kernel  | A version of the Linux kernel that is         | tbd                   | tbd                   |
|              | Version       | compatible with kubeadm - this has been       |                       |                       |
|              |               | chosen as the baseline because kubeadm is     |                       |                       |
|              |               | focussed on installing and managing the       |                       |                       |
|              |               | lifecycle of Kubernetes and nothing else,     |                       |                       |
|              |               | hence it is easily integrated into            |                       |                       |
|              |               | higher-level and more complete tooling for    |                       |                       |
|              |               | the full lifecycle management of the          |                       |                       |
|              |               | infrastructure, cluster add-ons, etc.         |                       |                       |
+--------------+---------------+-----------------------------------------------+-----------------------+-----------------------+
|``ra2.os.003``| Windows       | Windows Server (this can be used for          | tbd                   | tbd                   |
|              | Server        | worker nodes, but be aware of the             |                       |                       |
|              |               | limitations).                                 |                       |                       |
+--------------+---------------+-----------------------------------------------+-----------------------+-----------------------+
|``ra2.os.004``| Disposable    | In order to support req.gen.cnt.03 (immutable | tbd                   | tbd                   |
|              | OS            | infrastructure), the Host OS must be          |                       |                       |
|              |               | disposable, meaning the configuration of the  |                       |                       |
|              |               | Host OS (and associated infrastructure such   |                       |                       |
|              |               | as VM or bare metal server) must be           |                       |                       |
|              |               | consistent - e.g. the system software and     |                       |                       |
|              |               | configuration of that software must be        |                       |                       |
|              |               | identical apart from those areas of           |                       |                       |
|              |               | configuration that must be different such as  |                       |                       |
|              |               | IP addresses and hostnames.                   |                       |                       |
+--------------+---------------+-----------------------------------------------+-----------------------+-----------------------+
|``ra2.os.005``| Automated     | This approach to configuration management     | tbd                   | tbd                   |
|              | Deployment    | supports req.lcm.gen.01 (automated            |                       |                       |
|              |               | deployments)                                  |                       |                       |
+--------------+---------------+-----------------------------------------------+-----------------------+-----------------------+

**Table 4-2:** Operating System Requirements

Table 4-3 lists the kernel versions that comply with this Reference Architecture specification.

+-------------+-------------------+---------------------------+
| OS Family   | Kernel Version(s) | Notes                     |
+=============+===================+===========================+
| Linux       | 3.10+             |                           |
+-------------+-------------------+---------------------------+
| Windows     | 1809 (10.0.17763) | For worker nodes only     |
+-------------+-------------------+---------------------------+

**Table 4-3:** Operating System Versions



Kubernetes
----------

In order for the Kubernetes components to be conformant with the Reference Architecture they must be implemented as per the following specifications:

=============== ================================== ==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== ====================================================================================================================================================================================================================================================================================================== =====================================================================================================
Ref             Specification                      Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Requirement Trace                                                                                                                                                                                                                                                                                      Reference Implementation Trace
=============== ================================== ==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== ====================================================================================================================================================================================================================================================================================================== =====================================================================================================
``ra2.k8s.001`` Kubernetes Conformance             The Kubernetes distribution, product, or installer used in the implementation **must** be listed in the `Kubernetes Distributions and Platforms document <https://docs.google.com/spreadsheets/d/1uF9BoDzzisHSQemXHIKegMhuythuq_GL3N1mlUUK2h0/edit#gid=0>`__ and marked (X) as conformant for the Kubernetes version defined in `README <../README.md#required-versions-of-most-important-components>`__.                                                                                                                                                                                                            `req.gen.cnt.03 <./chapter02.md#kubernetes-architecture-requirements>`__                                                                                                                                                                                                                               `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.k8s.002`` Highly available etcd              An implementation **must** consist of either three, five or seven nodes running the etcd service (can be colocated on the master nodes, or can run on separate nodes, but not on worker nodes).                                                                                                                                                                                                                                                                                                                                                                                                                      `req.gen.rsl.02 req.gen.avl.01 <./chapter02.md#kubernetes-architecture-requirements>`__                                                                                                                                                                                                                `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.k8s.003`` Highly available control plane     An implementation **must** consist of at least one master node per availability zone or fault domain to ensure the high availability and resilience of the Kubernetes control plane services.
``ra2.k8s.012`` Control plane services             A master node **must** run at least the following Kubernetes control plane services: ``kube-apiserver``, ``kube-scheduler`` and ``kube-controller-manager``.                                                                                                                                                                                                                                                                                                                                                                                                                                                         `req.gen.rsl.02 <./chapter02.md#kubernetes-architecture-requirements>`__, `req.gen.avl.01 <./chapter02.md#kubernetes-architecture-requirements>`__                                                                                                                                                     `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.k8s.004`` Highly available worker nodes      An implementation **must** consist of at least one worker node per availability zone or fault domain to ensure the high availability and resilience of workloads managed by Kubernetes                                                                                                                                                                                                                                                                                                                                                                                                                               `req.gen.rsl.01 <./chapter02.md#kubernetes-architecture-requirements>`__, `req.gen.avl.01 <./chapter02.md#kubernetes-architecture-requirements>`__, `req.kcm.gen.02 <./chapter02.md#kubernetes-architecture-requirements>`__, `req.inf.com.01 <./chapter02.md#kubernetes-architecture-requirements>`__
``ra2.k8s.005`` Kubernetes API Version             In alignment with the `Kubernetes version support policy <https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions>`__, an implementation **must** use a Kubernetes version as per the subcomponent versions table in `README <../README.md#required-versions-of-most-important-components>`__.
``ra2.k8s.006`` NUMA Support                       When hosting workloads matching the High Performance profile, the ``TopologyManager`` and ``CPUManager`` feature gates **must** be enabled and configured on the kubelet (note, TopologyManager is enabled by default in Kubernetes v1.18 and later, with CPUManager enabled by default in Kubernetes v1.10 and later). ``--feature-gates="...,TopologyManager=true,CPUManager=true" --topology-manager-policy=single-numa-node --cpu-manager-policy=static``                                                                                                                                                       `e.cap.007 <chapter02.md#cloud-infrastructure-software-profile-capabilities>`__ `infra.com.cfg.002 <./chapter02.md#cloud-infrastructure-software-profile-requirements>`__ `infra.hw.cpu.cfg.003 <./chapter02.md#cloud-infrastructure-hardware-profile-requirements>`__
``ra2.k8s.007`` DevicePlugins Feature Gate         When hosting workloads matching the High Performance profile, the DevicePlugins feature gate **must** be enabled (note, this is enabled by default in Kubernetes v1.10 or later). ``--feature-gates="...,DevicePlugins=true,..."``                                                                                                                                                                                                                                                                                                                                                                                  Various, e.g. `e.cap.013 <chapter02.md#cloud-infrastructure-software-profile-capabilities>`__                                                                                                                                                                                                          `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.k8s.008`` System Resource Reservations       To avoid resource starvation issues on nodes, the implementation of the architecture **must** reserve compute resources for system daemons and Kubernetes system daemons such as kubelet, container runtime, etc. Use the following kubelet flags: ``--reserved-cpus=[a-z]``, using two of ``a-z`` to reserve 2 SMT threads.                                                                                                                                                                                                                                                                                         `i.cap.014 <chapter02.md#cloud-infrastructure-software-profile-capabilities>`__
``ra2.k8s.009`` CPU Pinning                        When hosting workloads matching the High Performance profile, in order to support CPU Pinning, the kubelet **must** be started with the ``--cpu-manager-policy=static`` option. (Note, only containers in ``Guaranteed`` pods - where CPU resource ``requests`` and ``limits`` are identical - and configured with positive-integer CPU ``requests`` will take advantage of this. All other Pods will run on CPUs in the remaining shared pool.)                                                                                                                                                                    `infra.com.cfg.003 <./chapter02.md#cloud-infrastructure-software-profile-requirements>`__
``ra2.k8s.010`` IPv6DualStack                      To support IPv6 and IPv4, the ``IPv6DualStack`` feature gate **must** be enabled on various components (requires Kubernetes v1.16 or later). kube-apiserver: ``--feature-gates="IPv6DualStack=true"``. kube-controller-manager: ``--feature-gates="IPv6DualStack=true" --cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR> --service-cluster-ip-range=<IPv4 CIDR>,<IPv6 CIDR> --node-cidr-mask-size-ipv4 ¦ --node-cidr-mask-size-ipv6`` defaults to /24 for IPv4 and /64 for IPv6. kubelet: ``--feature-gates="IPv6DualStack=true"``. kube-proxy: ``--cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR> --feature-gates="IPv6DualStack=true"`` `req.inf.ntw.04 <./chapter02.md#kubernetes-architecture-requirements>`__
``ra2.k8s.011`` Anuket profile labels              To clearly identify which worker nodes are compliant with the different profiles defined by Anuket the worker nodes **must** be labelled according to the following pattern: an ``anuket.io/profile/basic`` label must be set to ``true`` on the worker node if it can fulfil the requirements of the basic profile and an ``anuket.io/profile/network-intensive`` label must be set to ``true`` on the worker node if it can fulfil the requirements of the High Performance profile. The requirements for both profiles can be found in `chapter 2 <./chapter02.md#reference-model-requirements>`__
``ra2.k8s.012`` Kubernetes APIs                    Kubernetes `Alpha API <https://kubernetes.io/docs/reference/using-api/#api-versioning>`__ are recommended only for testing, therefore all Alpha APIs **must** be disabled.
``ra2.k8s.013`` Kubernetes APIs                    Backward compatibility of all supported GA APIs of Kubernetes **must** be supported.
``ra2.k8s.014`` Security Groups                    Kubernetes **must** support NetworkPolicy feature.
``ra2.k8s.015`` Publishing Services (ServiceTypes) Kubernetes **must** support LoadBalancer `Publishing Service (ServiceTypes) <https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types>`__.
``ra2.k8s.016`` Publishing Services (ServiceTypes) Kubernetes **must** support `Ingress <https://kubernetes.io/docs/concepts/services-networking/ingress/>`__.
``ra2.k8s.017`` Publishing Services (ServiceTypes) Kubernetes **should** support NodePort `Publishing Service (ServiceTypes) <https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types>`__.                                                                                                                                                                                                                                                                                                                                                                                                                                   `req.inf.ntw.17 <chapter02.md#kubernetes-architecture-requirements>`__
``ra2.k8s.018`` Publishing Services (ServiceTypes) Kubernetes **should** support ExternalName `Publishing Service (ServiceTypes) <https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types>`__.
``ra2.k8s.019`` Kubernetes APIs                    Kubernetes Beta APIs **must** be supported only when a stable GA of the same version doesn't exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  `req.int.api.04 <./chapter02.md#kubernetes-architecture-requirements>`__
=============== ================================== ==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== ====================================================================================================================================================================================================================================================================================================== =====================================================================================================

**Table 4-2:** Kubernetes Specifications

Container runtimes
------------------

=============== ============================================ ======================================================================================================================================================================================================== ====================================================================== =====================================================================================================
Ref             Specification                                Details                                                                                                                                                                                                  Requirement Trace                                                      Reference Implementation Trace
=============== ============================================ ======================================================================================================================================================================================================== ====================================================================== =====================================================================================================
``ra2.crt.001`` Conformance with OCI 1.0 runtime spec        The container runtime **must** be implemented as per the `OCI 1.0 <https://github.com/opencontainers/runtime-spec/blob/master/spec.md>`__ (Open Container Initiative 1.0) specification.                 `req.gen.ost.01 <chapter02.md#kubernetes-architecture-requirements>`__ `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.crt.002`` Kubernetes Container Runtime Interface (CRI) The Kubernetes container runtime **must** be implemented as per the `Kubernetes Container Runtime Interface (CRI) <https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/>`__ `req.gen.ost.01 <chapter02.md#kubernetes-architecture-requirements>`__ `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
=============== ============================================ ======================================================================================================================================================================================================== ====================================================================== =====================================================================================================

**Table 4-3:** Container Runtime Specifications

Networking solutions
--------------------

In order for the networking solution(s) to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

=============== ======================================================= ========================================================================================================================================================================================================================================================================== ================================================================================================================================================================ =====================================================================================================
Ref             Specification                                           Details                                                                                                                                                                                                                                                                    Requirement Trace                                                                                                                                                Reference Implementation Trace
=============== ======================================================= ========================================================================================================================================================================================================================================================================== ================================================================================================================================================================ =====================================================================================================
``ra2.ntw.001`` Centralised network administration                      The networking solution deployed within the implementation **must** be administered through the Kubernetes API using native Kubernetes API resources and objects, or Custom Resources.                                                                                     `req.inf.ntw.03 <chapter02.md#kubernetes-architecture-requirements>`__                                                                                           `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.002`` Default Pod Network - CNI                               The networking solution deployed within the implementation **must** use a CNI-conformant Network Plugin for the Default Pod Network, as the alternative (kubenet) does not support cross-node networking or Network Policies.                                              `req.gen.ost.01 <chapter02.md#kubernetes-architecture-requirements>`__, `req.inf.ntw.08 <chapter02.md#kubernetes-architecture-requirements>`__                   `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.003`` Multiple connection points                              The networking solution deployed within the implementation **must** support the capability to connect at least FIVE connection points to each Pod, which are additional to the default connection point managed by the default Pod network CNI plugin.                     `e.cap.004 <chapter02.md#cloud-infrastructure-software-profile-capabilities>`__                                                                                  `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.004`` Multiple connection points presentation                 The networking solution deployed within the implementation **must** ensure that all additional non-default connection points are requested by Pods using standard Kubernetes resource scheduling mechanisms such as annotations or container resource requests and limits. `req.inf.ntw.03 <chapter02.md#kubernetes-architecture-requirements>`__                                                                                           `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.005`` Multiplexer/meta-plugin                                 The networking solution deployed within the implementation **may** use a multiplexer/meta-plugin.                                                                                                                                                                          `req.inf.ntw.06 <chapter02.md#kubernetes-architecture-requirements>`__, `req.inf.ntw.07 <chapter02.md#kubernetes-architecture-requirements>`__                   `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.006`` Multiplexer/meta-plugin CNI Conformance                 If used, the selected multiplexer/meta-plugin **must** integrate with the Kubernetes control plane via CNI.                                                                                                                                                                `req.gen.ost.01 <chapter02.md#kubernetes-architecture-requirements>`__                                                                                           `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.007`` Multiplexer/meta-plugin CNI Plugins                     If used, the selected multiplexer/meta-plugin **must** support the use of multiple CNI-conformant Network Plugins.                                                                                                                                                         `req.gen.ost.01 <chapter02.md#kubernetes-architecture-requirements>`__, `req.inf.ntw.06 <chapter02.md#kubernetes-architecture-requirements>`__                   `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.008`` SR-IOV Device Plugin for High Performance               When hosting workloads that match the High Performance profile and require SR-IOV acceleration, a Device Plugin for SR-IOV **must** be used to configure the SR-IOV devices and advertise them to the ``kubelet``.                                                        `e.cap.013 <chapter02.md#cloud-infrastructure-software-profile-capabilities>`__                                                                                  `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.009`` Multiple connection points with multiplexer/meta-plugin When a multiplexer/meta-plugin is used, the additional non-default connection points **must** be managed by a CNI-conformant Network Plugin.                                                                                                                               `req.gen.ost.01 <chapter02.md#kubernetes-architecture-requirements>`__                                                                                           `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.010`` User plane networking                                   When hosting workloads matching the High Performance profile, CNI network plugins that support the use of DPDK, VPP, and/or SR-IOV **must** be deployed as part of the networking solution.                                                                               `infra.net.acc.cfg.001 <chapter02.md#cloud-infrastructure-software-profile-requirements>`__                                                                      `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.011`` NATless connectivity                                    When hosting workloads that require source and destination IP addresses to be preserved in the traffic headers, a NATless CNI plugin that exposes the pod IP directly to the external networks (e.g. Calico, MACVLAN or IPVLAN CNI plugins) **must** be used.              `req.inf.ntw.14 <chapter02.md#kubernetes-architecture-requirements>`__
``ra2.ntw.012`` Device Plugins                                          When hosting workloads matching the High Performance profile that require the use of FPGA, SR-IOV or other Acceleration Hardware, a Device Plugin for that FPGA or Acceleration Hardware **must** be used.                                                                `e.cap.016 <chapter02.md#cloud-infrastructure-software-profile-capabilities>`__, `e.cap.013 <chapter02.md#cloud-infrastructure-software-profile-capabilities>`__ `4.3.1 <../../../ref_impl/cntt-ri2/chapters/chapter04.md#installation-on-bare-metal-infratructure>`__
``ra2.ntw.013`` Dual stack CNI                                          The networking solution deployed within the implementation **must** use a CNI-conformant Network Plugin that is able to support dual-stack IPv4/IPv6 networking.                                                                                                           `req.inf.ntw.04 <chapter02.md#kubernetes-architecture-requirements>`__
``ra2.ntw.014`` Security Groups                                         The networking solution deployed within the implementation **must** support network policies.                                                                                                                                                                              `infra.net.cfg.004 <chapter02.md#cloud-infrastructure-software-profile-requirements>`__
``ra2.ntw.015`` IPAM plugin for multiplexer                             When a multiplexer/meta-plugin is used, a CNI-conformant IPAM Network Plugin **must** be installed to allocate IP addresses for secondary network interfaces across all nodes of the cluster.                                                                              `req.inf.ntw.10 <chapter02.md#kubernetes-architecture-requirements>`__
=============== ======================================================= ========================================================================================================================================================================================================================================================================== ================================================================================================================================================================ =====================================================================================================

**Table 4-4:** Networking Solution Specifications

Storage components
------------------

In order for the storage solutions to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

=============== ================================= ============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== ====================================================================== ==============================
Ref             Specification                     Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Requirement Trace                                                      Reference Implementation Trace
=============== ================================= ============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== ====================================================================== ==============================
``ra2.stg.001`` Ephemeral Storage                 An implementation must support ephemeral storage, for the unpacked container images to be stored and executed from, as a directory in the filesystem on the worker node on which the container is running. See the `Container runtimes <#container-runtimes>`__ section above for more information on how this meets the requirement for ephemeral storage for containers.
``ra2.stg.002`` Kubernetes Volumes                An implementation may attach additional storage to containers using Kubernetes Volumes.
``ra2.stg.003`` Kubernetes Volumes                An implementation may use Volume Plugins (see ``ra2.stg.005`` below) to allow the use of a storage protocol (e.g., iSCSI, NFS) or management API (e.g., Cinder, EBS) for the attaching and mounting of storage into a Pod.
``ra2.stg.004`` Persistent Volumes                An implementation may support Kubernetes Persistent Volumes (PV) to provide persistent storage for Pods. Persistent Volumes exist independent of the lifecycle of containers and/or pods.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      `req.inf.stg.01 <chapter02.md#kubernetes-architecture-requirements>`__
``ra2.stg.005`` Storage Volume Types              An implementation must support the following Volume types: ``emptyDir``, ``ConfigMap``, ``Secret`` and ``PersistentVolumeClaim``. Other Volume plugins may be supported to allow for the use of a range of backend storage systems.
``ra2.stg.006`` Container Storage Interface (CSI) An implementation may support the Container Storage Interface (CSI), an Out-of-tree plugin. In order to support CSI, the feature gates ``CSIDriverRegistry`` and ``CSINodeInfo`` must be enabled. The implementation must use a CSI driver (a full list of CSI drivers can be found `here <https://kubernetes-csi.github.io/docs/drivers.html>`__). An implementation may support ephemeral storage through a CSI-compatible volume plugin in which case the ``CSIInlineVolume`` feature gate must be enabled. An implementation may support Persistent Volumes through a CSI-compatible volume plugin in which case the ``CSIPersistentVolume`` feature gate must be enabled.
``ra2.stg.007``                                   An implementation should use Kubernetes Storage Classes to support automation and the separation of concerns between providers of a service and consumers of the service.
=============== ================================= ============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================== ====================================================================== ==============================

**Table 4-6:** Storage Solution Specifications

A note on object storage:

-  This Reference Architecture does not include any specifications for object
   storage, as this is neither a native Kubernetes object, nor something that is
   required by CSI drivers. Object storage is an application-level requirement
   that would ordinarily be provided by a highly scalable service offering rather
   than being something an individual Kubernetes cluster could offer.

..

   Todo: specifications/commentary to support req.inf.stg.04 (SDS) and req.inf.stg.05 (high performance and horizontally scalable storage). Also req.sec.gen.06 (storage resource isolation), req.sec.gen.10 (CIS - if applicable) and req.sec.zon.03 (data encryption at rest).

Service meshes
--------------

Application service meshes are not in scope for the architecture. The service mesh is a dedicated infrastructure layer for handling service-to-service communication, and it is recommended to secure service-to-service communications within a cluster and to reduce the attack surface. The benefits of the service mesh framework are described in `5.4.3 <./chapter05.md#use-transport-layer-security-and-service-mesh>`__. In addition to securing communications, the use of a service mesh extends Kubernetes capabilities regarding observability and reliability.

Network service mesh specifications are handled in section `4.5 Networking solutions <#networking-solutions>`__.

Kubernetes Application package manager
--------------------------------------

In order for the application package managers to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

=============== ============================ ========================================================================================================================================= ======================================================================== ==============================
Ref             Specification                Details                                                                                                                                   Requirement Trace                                                        Reference Implementation Trace
=============== ============================ ========================================================================================================================================= ======================================================================== ==============================
``ra2.pkg.001`` API-based package management A package manager must use the Kubernetes APIs to manage application artifacts. Cluster-side components such as Tiller are not supported. `req.int.api.02 <./chapter02.md#kubernetes-architecture-requirements>`__
=============== ============================ ========================================================================================================================================= ======================================================================== ==============================

**Table 4-7:** Kubernetes Application Package Manager Specifications

Kubernetes workloads
--------------------

In order for the Kubernetes workloads to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

=============== ======================================================================================================================= =================================================================================================================================================================================================================================================================================================== ======================================================================= ==============================
Ref             Specification                                                                                                           Details                                                                                                                                                                                                                                                                                             Requirement Trace                                                       Reference Implementation Trace
=============== ======================================================================================================================= =================================================================================================================================================================================================================================================================================================== ======================================================================= ==============================
``ra2.app.001`` `Root <https://github.com/opencontainers/runtime-spec/blob/master/config.md>`__ Parameter Group (OCI Spec)              Specifies the container's root filesystem.                                                                                                                                                                                                                                                          TBD                                                                     N/A
``ra2.app.002`` `Mounts <https://github.com/opencontainers/runtime-spec/blob/master/config.md#mounts>`__ Parameter Group (OCI Spec)     Specifies additional mounts beyond root.                                                                                                                                                                                                                                                            TBD                                                                     N/A
``ra2.app.003`` `Process <https://github.com/opencontainers/runtime-spec/blob/master/config.md#process>`__ Parameter Group (OCI Spec)   Specifies the container process.                                                                                                                                                                                                                                                                    TBD                                                                     N/A
``ra2.app.004`` `Hostname <https://github.com/opencontainers/runtime-spec/blob/master/config.md#hostname>`__ Parameter Group (OCI Spec) Specifies the container's hostname as seen by processes running inside the container.                                                                                                                                                                                                               TBD                                                                     N/A
``ra2.app.005`` `User <https://github.com/opencontainers/runtime-spec/blob/master/config.md#user>`__ Parameter Group (OCI Spec)         User for the process is a platform-specific structure that allows specific control over which user the process runs as.                                                                                                                                                                             TBD                                                                     N/A
``ra2.app.006`` Consumption of additional, non-default connection points                                                                The workload must request additional non-default connection points through the use of workload annotations or resource requests and limits within the container spec passed to the Kubernetes API Server.                                                                                           `req.int.api.01 <chapter02.md#kubernetes-architecture-requirements>`__  N/A
``ra2.app.007`` Host Volumes                                                                                                            Workloads should not use ``hostPath`` volumes, as `Pods with identical configuration <https://kubernetes.io/docs/concepts/storage/volumes/#hostpath>`__ (such as those created from a PodTemplate) may behave differently on different nodes due to different files on the nodes.                   `req.kcm.gen.02 <chapter02.md#kubernetes-architecture-requirements>`__. N/A
``ra2.app.008`` Infrastructure dependency                                                                                               Workloads must not rely on the availability of the master nodes for the successful execution of their functionality (i.e. loss of the master nodes may affect non-functional behaviours such as healing and scaling, but components that are already running will continue to do so without issue). TBD                                                                     N/A
``ra2.app.009`` Device plugins                                                                                                          Workload descriptors must use the resources advertised by the device plugins to indicate their need for an FPGA, SR-IOV or other acceleration device.                                                                                                                                               TBD                                                                     N/A
``ra2.app.010`` Node Feature Discovery (NFD)                                                                                            Workload descriptors must use the labels advertised by `Node Feature Discovery <https://kubernetes-sigs.github.io/node-feature-discovery/stable/get-started/index.html>`__ to indicate which node software of hardware features they need.                                                          TBD                                                                     N/A
=============== ======================================================================================================================= =================================================================================================================================================================================================================================================================================================== ======================================================================= ==============================

**Table 4-8:** Kubernetes Workload Specifications

Additional required components
------------------------------

   This chapter should list any additional components needed to provide the services defined in Chapter 3.2 (e.g., Prometheus)

