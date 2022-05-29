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

In order for the Kubernetes components to be conformant with the Reference Architecture they must be implemented as per
the following specifications:

+-----------+------------------+---------------------------------------------------+----------------+-----------------+
| Ref       | Specification    | Details                                           | Requirement    | Reference       |
|           |                  |                                                   | Trace          | Implementation  |
|           |                  |                                                   |                | Trace           |
+===========+==================+===================================================+================+=================+
|ra2.k8s.001| Kubernetes       | The Kubernetes distribution, product, or          | `req.gen.cnt.  | `4.3.1 <../../. |
|           | Conformance      | installer used in the implementation **must** be  | 03 <./chapter0 | ./ref_impl/cntt |
|           |                  | listed in the `Kubernetes Distributions and       | 2.md#kubernete | -ri2/chapters/c |
|           |                  | Platforms document <https://docs.google.com/sprea | s-architecture | hapter04.md#ins |
|           |                  | dsheets/d/1uF9BoDzzisHSQemXHIKegMhuythuq_GL3N1mlU | -requirement   | tallation-on-ba |
|           |                  | UK2h0/edit#gid=0>`__ and marked (X) as conformant | s>`__          | re-metal-infrat |
|           |                  | for the Kubernetes version defined in `README <.. |                | ructure>`__     |
|           |                  | /README.md#required-versions-of-most-important-co |                |                 |
|           |                  | mponents>`__.                                     |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.002| Highly available | An implementation **must** consist of either      | `req.gen.rsl.  | `4.3.1 <../../. |
|           | etcd             | three, five or seven nodes running the etcd       | 02 req.gen.avl | ./ref_impl/cntt |
|           |                  | service (can be colocated on the master nodes, or | .01 <./chapter | -ri2/chapters/c |
|           |                  | can run on separate nodes, but not on worker      | 02.md#kubernet | hapter04.md#ins |
|           |                  | nodes).                                           | es-architectur | tallation-on-ba |
|           |                  |                                                   | e-requirement  | re-metal-infrat |
|           |                  |                                                   | s>`__          | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.003| Highly available | An implementation **must** consist of at least    |                |                 |
|           | control plane    | one master node per availability zone or fault    |                |                 |
|           |                  | domain to ensure the high availability and        |                |                 |
|           |                  | resilience of the Kubernetes control plane        |                |                 |
|           |                  | services.                                         |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.012| Control plane    | A master node **must** run at least the following | `req.gen.rsl.  | `4.3.1 <../../. |
|           | services         | Kubernetes control plane services:                | 02 <./chapter0 | ./ref_impl/cntt |
|           |                  | ``kube-apiserver``, ``kube-scheduler`` and        | 2.md#kubernete | -ri2/chapters/c |
|           |                  | ``kube-controller-manager``.                      | s-architecture | hapter04.md#ins |
|           |                  |                                                   | -requirement   | tallation-on-ba |
|           |                  |                                                   | s>`__,         | re-metal-infrat |
|           |                  |                                                   | `req.gen.avl.  | ructure>`__     |
|           |                  |                                                   | 01 <./chapter0 |                 |
|           |                  |                                                   | 2.md#kubernete |                 |
|           |                  |                                                   | s-architecture |                 |
|           |                  |                                                   | -requirement   |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.004| Highly available | An implementation **must** consist of at least    | `req.gen.rsl.  |                 |
|           | worker nodes     | one worker node per availability zone or fault    | 01 <./chapter0 |                 |
|           |                  | domain to ensure the high availability and        | 2.md#kubernete |                 |
|           |                  | resilience of workloads managed by Kubernetes     | s-architecture |                 |
|           |                  |                                                   | -requirement   |                 |
|           |                  |                                                   | s>`__,         |                 |
|           |                  |                                                   | `req.gen.avl.  |                 |
|           |                  |                                                   | 01 <./chapter0 |                 |
|           |                  |                                                   | 2.md#kubernete |                 |
|           |                  |                                                   | s-architecture |                 |
|           |                  |                                                   | -requirement   |                 |
|           |                  |                                                   | s>`__,         |                 |
|           |                  |                                                   | `req.kcm.gen.  |                 |
|           |                  |                                                   | 02 <./chapter0 |                 |
|           |                  |                                                   | 2.md#kubernete |                 |
|           |                  |                                                   | s-architecture |                 |
|           |                  |                                                   | -requirement   |                 |
|           |                  |                                                   | s>`__,         |                 |
|           |                  |                                                   | `req.inf.com.  |                 |
|           |                  |                                                   | 01 <./chapter0 |                 |
|           |                  |                                                   | 2.md#kubernete |                 |
|           |                  |                                                   | s-architecture |                 |
|           |                  |                                                   | -requirement   |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.005| Kubernetes API   | In alignment with the `Kubernetes version support |                |                 |
|           | Version          | policy <https://kubernetes.io/docs/setup/release/ |                |                 |
|           |                  | version-skew-policy/#supported-versions>`__, an   |                |                 |
|           |                  | implementation **must** use a Kubernetes version  |                |                 |
|           |                  | as per the subcomponent versions table in `README |                |                 |
|           |                  | <../README.md#required-versions-of-most-important |                |                 |
|           |                  | -components>`__.                                  |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.006| NUMA Support     | When hosting workloads matching the High          | `e.cap.007 <ch |                 |
|           |                  | Performance profile, the ``TopologyManager`` and  | apter02.md#clo |                 |
|           |                  | ``CPUManager`` feature gates **must** be enabled  | ud-infrastruct |                 |
|           |                  | and configured on the kubelet (note,              | ure-software-p |                 |
|           |                  | TopologyManager is enabled by default in          | rofile-capabil |                 |
|           |                  | Kubernetes v1.18 and later, with CPUManager       | ities>`__      |                 |
|           |                  | enabled by default in Kubernetes v1.10 and        | `infra.com.cfg |                 |
|           |                  | later). ``--feature-gates="...,                   | .002 <./chapte |                 |
|           |                  | TopologyManager=true,CPUManager=true"             | r02.md#cloud-i |                 |
|           |                  | --topology-manager-policy=single-numa-node        | nfrastructure- |                 |
|           |                  | --cpu-manager-policy=static``                     | software-profi |                 |
|           |                  |                                                   | le-requirement |                 |
|           |                  |                                                   | s>`__          |                 |
|           |                  |                                                   | `infra.hw.cpu. |                 |
|           |                  |                                                   | cfg.003 <./cha |                 |
|           |                  |                                                   | pter02.md#clou |                 |
|           |                  |                                                   | d-infrastructu |                 |
|           |                  |                                                   | re-hardware-pr |                 |
|           |                  |                                                   | ofile-requirem |                 |
|           |                  |                                                   | ents>`__       |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.007| DevicePlugins    | When hosting workloads matching the High          | Various, e.g.  | `4.3.1 <../../. |
|           | Feature Gate     | Performance profile, the DevicePlugins feature    | `e.cap.013 <ch | ./ref_impl/cntt |
|           |                  | gate **must** be enabled (note, this is enabled   | apter02.md#clo | -ri2/chapters/c |
|           |                  | by default in Kubernetes v1.10 or later).         | ud-infrastruct | hapter04.md#ins |
|           |                  | ``--feature-gates="...,DevicePlugins=true,..."``  | ure-software-p | tallation-on-ba |
|           |                  |                                                   | rofile-capabil | re-metal-infrat |
|           |                  |                                                   | ities>`__      | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.008| System Resource  | To avoid resource starvation issues on nodes, the | `i.cap.014 <ch |                 |
|           | Reservations     | implementation of the architecture **must**       | apter02.md#clo |                 |
|           |                  | reserve compute resources for system daemons and  | ud-infrastruct |                 |
|           |                  | Kubernetes system daemons such as kubelet,        | ure-software-p |                 |
|           |                  | container runtime, etc. Use the following kubelet | rofile-capabil |                 |
|           |                  | flags: ``--reserved-cpus=[a-z]``, using two of    | ities>`__      |                 |
|           |                  | ``a-z`` to reserve 2 SMT threads.                 |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.009| CPU Pinning      | When hosting workloads matching the High          | `infra.com.cfg |                 |
|           |                  | Performance profile, in order to support CPU      | .003 <./chapte |                 |
|           |                  | Pinning, the kubelet **must** be started with the | r02.md#cloud-i |                 |
|           |                  | ``--cpu-manager-policy=static`` option. (Note,    | nfrastructure- |                 |
|           |                  | only containers in ``Guaranteed`` pods - where    | software-profi |                 |
|           |                  | CPU resource ``requests`` and ``limits`` are      | le-requirement |                 |
|           |                  | identical - and configured with positive-integer  | s>`__          |                 |
|           |                  | CPU ``requests`` will take advantage of this. All |                |                 |
|           |                  | other Pods will run on CPUs in the remaining      |                |                 |
|           |                  | shared pool.)                                     |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.010| IPv6DualStack    | To support IPv6 and IPv4, the ``IPv6DualStack``   | `req.inf.ntw.  |                 |
|           |                  | feature gate **must** be enabled on various       | 04 <./chapter0 |                 |
|           |                  | components (requires Kubernetes v1.16 or later).  | 2.md#kubernete |                 |
|           |                  | kube-apiserver:                                   | s-architecture |                 |
|           |                  | ``--feature-gates="IPv6DualStack=true"``.         | -requirement   |                 |
|           |                  | kube-controller-manager:                          | s>`__          |                 |
|           |                  | ``--feature-gates="IPv6DualStack=true"            |                |                 |
|           |                  | --cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR>            |                |                 |
|           |                  | --service-cluster-ip-range=<IPv4 CIDR>,           |                |                 |
|           |                  | <IPv6 CIDR> --node-cidr-mask-size-ipv4 ¦          |                |                 |
|           |                  | --node-cidr-mask-size-ipv6`` defaults to /24 for  |                |                 |
|           |                  | IPv4 and /64 for IPv6. kubelet:                   |                |                 |
|           |                  | ``--feature-gates="IPv6DualStack=true"``.         |                |                 |
|           |                  | kube-proxy: ``--cluster-cidr=<IPv4 CIDR>,         |                |                 |
|           |                  | <IPv6 CIDR>                                       |                |                 |
|           |                  | --feature-gates="IPv6DualStack=true"``            |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.011| Anuket profile   | To clearly identify which worker nodes are        |                |                 |
|           | labels           | compliant with the different profiles defined by  |                |                 |
|           |                  | Anuket the worker nodes **must** be labelled      |                |                 |
|           |                  | according to the following pattern: an            |                |                 |
|           |                  | ``anuket.io/profile/basic`` label must be set to  |                |                 |
|           |                  | ``true`` on the worker node if it can fulfil the  |                |                 |
|           |                  | requirements of the basic profile and an          |                |                 |
|           |                  | ``anuket.io/profile/network-intensive`` label     |                |                 |
|           |                  | must be set to ``true`` on the worker node if it  |                |                 |
|           |                  | can fulfil the requirements of the High           |                |                 |
|           |                  | Performance profile. The requirements for both    |                |                 |
|           |                  | profiles can be found in `chapter 2 <./chapter02. |                |                 |
|           |                  | md#reference-model-requirements>`__               |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.012| Kubernetes APIs  | Kubernetes `Alpha API <https://kubernetes.io/docs |                |                 |
|           |                  | /reference/using-api/#api-versioning>`__ are      |                |                 |
|           |                  | recommended only for testing, therefore all Alpha |                |                 |
|           |                  | APIs **must** be disabled.                        |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.013| Kubernetes APIs  | Backward compatibility of all supported GA APIs   |                |                 |
|           |                  | of Kubernetes **must** be supported.              |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.014| Security Groups  | Kubernetes **must** support NetworkPolicy         |                |                 |
|           |                  | feature.                                          |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.015| Publishing       | Kubernetes **must** support LoadBalancer          |                |                 |
|           | Services         | `Publishing Service (ServiceTypes) <https://kuber |                |                 |
|           | (ServiceTypes)   | netes.io/docs/concepts/services-networking/servic |                |                 |
|           |                  | e/#publishing-services-service-types>`__.         |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.016| Publishing       | Kubernetes **must** support                       |                |                 |
|           | Services         | `Ingress <https://kubernetes.io/docs/concepts/ser |                |                 |
|           | (ServiceTypes)   | vices-networking/ingress/>`__.                    |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.017| Publishing       | Kubernetes **should** support NodePort            | `req.inf.ntw.  |                 |
|           | Services         | `Publishing Service (ServiceTypes) <https://kuber | 17 <chapter02. |                 |
|           | (ServiceTypes)   | netes.io/docs/concepts/services-networking/servic | md#kubernetes- |                 |
|           |                  | e/#publishing-services-service-types>`__.         | architecture-r |                 |
|           |                  |                                                   | equirement     |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.018| Publishing       | Kubernetes **should** support ExternalName        |                |                 |
|           | Services         | `Publishing Service (ServiceTypes) <https://kuber |                |                 |
|           | (ServiceTypes)   | netes.io/docs/concepts/services-networking/servic |                |                 |
|           |                  | e/#publishing-services-service-types>`__.         |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.k8s.019| Kubernetes APIs  | Kubernetes Beta APIs **must** be supported only   | `req.int.api.  |                 |
|           |                  | when a stable GA of the same version doesn't      | 04 <./chapter0 |                 |
|           |                  | exist.                                            | 2.md#kubernete |                 |
|           |                  |                                                   | s-architecture |                 |
|           |                  |                                                   | -requirement   |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+

**Table 4-4:** Kubernetes Specifications

Container runtimes
------------------

+-----------+------------------+---------------------------------------------------+----------------+-----------------+
| Ref       | Specification    | Details                                           | Requirement    | Reference       |
|           |                  |                                                   | Trace          | Implementation  |
|           |                  |                                                   |                | Trace           |
+===========+==================+===================================================+================+=================+
|ra2.crt.001| Conformance with | The container runtime **must** be implemented as  | `req.gen.ost.  | `4.3.1 <../../. |
|           | OCI 1.0 runtime  | per the `OCI 1.0 <https://github.com/opencontaine | 01 <chapter02. | ./ref_impl/cntt |
|           | spec             | rs/runtime-spec/blob/master/spec.md>`__ (Open     | md#kubernetes- | -ri2/chapters/c |
|           |                  | Container Initiative 1.0) specification.          | architecture-r | hapter04.md#ins |
|           |                  |                                                   | equirement     | tallation-on-ba |
|           |                  |                                                   | s>`__          | re-metal-infrat |
|           |                  |                                                   |                | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.crt.002| Kubernetes       | The Kubernetes container runtime **must** be      | `req.gen.ost.  | `4.3.1 <../../. |
|           | Container        | implemented as per the `Kubernetes Container      | 01 <chapter02. | ./ref_impl/cntt |
|           | Runtime          | Runtime Interface (CRI) <https://kubernetes.io/bl | md#kubernetes- | -ri2/chapters/c |
|           | Interface (CRI)  | og/2016/12/container-runtime-interface-cri-in-kub | architecture-r | hapter04.md#ins |
|           |                  | ernetes/>`__                                      | equirement     | tallation-on-ba |
|           |                  |                                                   | s>`__          | re-metal-infrat |
|           |                  |                                                   |                | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+

**Table 4-5:** Container Runtime Specifications

Networking solutions
--------------------

In order for the networking solution(s) to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

+-----------+------------------+---------------------------------------------------+----------------+-----------------+
| Ref       | Specification    | Details                                           | Requirement    | Reference       |
|           |                  |                                                   | Trace          | Implementation  |
|           |                  |                                                   |                | Trace           |
+===========+==================+===================================================+================+=================+
|ra2.ntw.001| Centralised      | The networking solution deployed within the       | `req.inf.ntw.  | `4.3.1 <../../. |
|           | network          | implementation **must** be administered through   | 03 <chapter02. | ./ref_impl/cntt |
|           | administration   | the Kubernetes API using native Kubernetes API    | md#kubernetes- | -ri2/chapters/c |
|           |                  | resources and objects, or Custom Resources.       | architecture-r | hapter04.md#ins |
|           |                  |                                                   | equirement     | tallation-on-ba |
|           |                  |                                                   | s>`__          | re-metal-infrat |
|           |                  |                                                   |                | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.002| Default Pod      | The networking solution deployed within the       | `req.gen.ost.  | `4.3.1 <../../. |
|           | Network - CNI    | implementation **must** use a CNI-conformant      | 01 <chapter02. | ./ref_impl/cntt |
|           |                  | Network Plugin for the Default Pod Network, as    | md#kubernetes- | -ri2/chapters/c |
|           |                  | the alternative (kubenet) does not support        | architecture-r | hapter04.md#ins |
|           |                  | cross-node networking or Network Policies.        | equirement     | tallation-on-ba |
|           |                  |                                                   | s>`__,         | re-metal-infrat |
|           |                  |                                                   | `req.inf.ntw.  | ructure>`__     |
|           |                  |                                                   | 08 <chapter02. |                 |
|           |                  |                                                   | md#kubernetes- |                 |
|           |                  |                                                   | architecture-r |                 |
|           |                  |                                                   | equirement     |                 |
|           |                  |                                                   | s>`__          |                 |
|           |                  |                                                   |                |                 |
|           |                  |                                                   |                |                 |
|           |                  |                                                   |                |                 |
|           |                  |                                                   |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.003| Multiple         | The networking solution deployed within the       | `e.cap.004 <ch | `4.3.1 <../../. |
|           | connection       | implementation **must** support the capability to | apter02.md#clo | ./ref_impl/cntt |
|           | points           | connect at least FIVE connection points to each   | ud-infrastruct | -ri2/chapters/c |
|           |                  | Pod, which are additional to the default          | ure-software-p | hapter04.md#ins |
|           |                  | connection point managed by the default Pod       | rofile-capabil | tallation-on-ba |
|           |                  | network CNI plugin.                               | ities>`__      | re-metal-infrat |
|           |                  |                                                   |                | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.004| Multiple         | The networking solution deployed within the       | `req.inf.ntw.  | `4.3.1 <../../. |
|           | connection       | implementation **must** ensure that all           | 03 <chapter02. | ./ref_impl/cntt |
|           | points           | additional non-default connection points are      | md#kubernetes- | -ri2/chapters/c |
|           | presentation     | requested by Pods using standard Kubernetes       | architecture-r | hapter04.md#ins |
|           |                  | resource scheduling mechanisms such as            | equirement     | tallation-on-ba |
|           |                  | annotations or container resource requests and    | s>`__          | re-metal-infrat |
|           |                  | limits.                                           |                | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.005| Multiplexer /    | The networking solution deployed within the       | `req.inf.ntw.  | `4.3.1 <../../. |
|           | meta-plugin      | implementation **may** use a                      | 06 <chapter02. | ./ref_impl/cntt |
|           |                  | multiplexer/meta-plugin.                          | md#kubernetes- | -ri2/chapters/c |
|           |                  |                                                   | architecture-r | hapter04.md#ins |
|           |                  |                                                   | equirement     | tallation-on-ba |
|           |                  |                                                   | s>`__,         | re-metal-infrat |
|           |                  |                                                   | `req.inf.ntw.  | ructure>`__     |
|           |                  |                                                   | 07 <chapter02. |                 |
|           |                  |                                                   | md#kubernetes- |                 |
|           |                  |                                                   | architecture-r |                 |
|           |                  |                                                   | equirement     |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.006| Multiplexer /    | If used, the selected multiplexer/meta-plugin     | `req.gen.ost.  | `4.3.1 <../../. |
|           | meta-plugin CNI  | **must** integrate with the Kubernetes control    | 01 <chapter02. | ./ref_impl/cntt |
|           | Conformance      | plane via CNI.                                    | md#kubernetes- | -ri2/chapters/c |
|           |                  |                                                   | architecture-r | hapter04.md#ins |
|           |                  |                                                   | equirement     | tallation-on-ba |
|           |                  |                                                   | s>`__          | re-metal-infrat |
|           |                  |                                                   |                | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.007| Multiplexer /    | If used, the selected multiplexer/meta-plugin     | `req.gen.ost.  | `4.3.1 <../../. |
|           | meta-plugin CNI  | **must** support the use of multiple              | 01 <chapter02. | ./ref_impl/cntt |
|           | Plugins          | CNI-conformant Network Plugins.                   | md#kubernetes- | -ri2/chapters/c |
|           |                  |                                                   | architecture-r | hapter04.md#ins |
|           |                  |                                                   | equirement     | tallation-on-ba |
|           |                  |                                                   | s>`__,         | re-metal-infrat |
|           |                  |                                                   | `req.inf.ntw.  | ructure>`__     |
|           |                  |                                                   | 06 <chapter02. |                 |
|           |                  |                                                   | md#kubernetes- |                 |
|           |                  |                                                   | architecture-r |                 |
|           |                  |                                                   | equirement     |                 |
|           |                  |                                                   | s>`__,         |                 |
|           |                  |                                                   | `req.inf.ntw.  |                 |
|           |                  |                                                   | 06 <chapter02. |                 |
|           |                  |                                                   | md#kubernetes- |                 |
|           |                  |                                                   | architecture-r |                 |
|           |                  |                                                   | equirement     |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.008| SR-IOV Device    | When hosting workloads that match the High        | `e.cap.013 <ch | `4.3.1 <../../. |
|           | Plugin for High  | Performance profile and require SR-IOV            | apter02.md#clo | ./ref_impl/cntt |
|           | Performance      | acceleration, a Device Plugin for SR-IOV **must** | ud-infrastruct | -ri2/chapters/c |
|           |                  | be used to configure the SR-IOV devices and       | ure-software-p | hapter04.md#ins |
|           |                  | advertise them to the ``kubelet``.                | rofile-capabil | tallation-on-ba |
|           |                  |                                                   | ities>`__      | re-metal-infrat |
|           |                  |                                                   |                | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.009| Multiple         | When a multiplexer/meta-plugin is used, the       | `req.gen.ost.  | `4.3.1 <../../. |
|           | connection       | additional non-default connection points **must** | 01 <chapter02. | ./ref_impl/cntt |
|           | points with      | be managed by a CNI-conformant Network Plugin.    | md#kubernetes- | -ri2/chapters/c |
|           | multiplexer /    |                                                   | architecture-r | hapter04.md#ins |
|           | meta-plugin      |                                                   | equirement     | tallation-on-ba |
|           |                  |                                                   | s>`__          | re-metal-infrat |
|           |                  |                                                   |                | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.010| User plane       | When hosting workloads matching the High          | `infra.net.acc | `4.3.1 <../../. |
|           | networking       | Performance profile, CNI network plugins that     | .cfg.001 <chap | ./ref_impl/cntt |
|           |                  | support the use of DPDK, VPP, and/or SR-IOV       | ter02.md#cloud | -ri2/chapters/c |
|           |                  | **must** be deployed as part of the networking    | -infrastructur | hapter04.md#ins |
|           |                  | solution.                                         | e-software-pro | tallation-on-ba |
|           |                  |                                                   | file-requireme | re-metal-infrat |
|           |                  |                                                   | nts>`__        | ructure>`__     |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.011| NATless          | When hosting workloads that require source and    | `req.inf.ntw.  |                 |
|           | connectivity     | destination IP addresses to be preserved in the   | 14 <chapter02. |                 |
|           |                  | traffic headers, a NATless CNI plugin that        | md#kubernetes- |                 |
|           |                  | exposes the pod IP directly to the external       | architecture-r |                 |
|           |                  | networks (e.g. Calico, MACVLAN or IPVLAN CNI      | equirement     |                 |
|           |                  | plugins) **must** be used.                        | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.012| Device Plugins   | When hosting workloads matching the High          | `e.cap.016 <ch | `4.3.1 <../../. |
|           |                  | Performance profile that require the use of FPGA, | apter02.md#clo | ./ref_impl/cntt |
|           |                  | SR-IOV or other Acceleration Hardware, a Device   | ud-infrastruct | -ri2/chapters/c |
|           |                  | Plugin for that FPGA or Acceleration Hardware     | ure-software-p | hapter04.md#ins |
|           |                  | **must** be used.                                 | rofile-capabil | tallation-on-ba |
|           |                  |                                                   | ities>`__,     | re-metal-infrat |
|           |                  |                                                   | `e.cap.013 <ch | ructure>`__     |
|           |                  |                                                   | apter02.md#clo |                 |
|           |                  |                                                   | ud-infrastruct |                 |
|           |                  |                                                   | ure-software-p |                 |
|           |                  |                                                   | rofile-capabil |                 |
|           |                  |                                                   | ities>`__      |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.013| Dual stack CNI   | The networking solution deployed within the       | `req.inf.ntw.  |                 |
|           |                  | implementation **must** use a CNI-conformant      | 04 <chapter02. |                 |
|           |                  | Network Plugin that is able to support dual-stack | md#kubernetes- |                 |
|           |                  | IPv4/IPv6 networking.                             | architecture-r |                 |
|           |                  |                                                   | equirement     |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.014| Security Groups  | The networking solution deployed within the       | `infra.net.cfg |                 |
|           |                  | implementation **must** support network policies. | .004 <chapter0 |                 |
|           |                  |                                                   | 2.md#cloud-inf |                 |
|           |                  |                                                   | rastructure-so |                 |
|           |                  |                                                   | ftware-profile |                 |
|           |                  |                                                   | -requirement   |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ntw.015| IPAM plugin for  | When a multiplexer/meta-plugin is used, a         | `req.inf.ntw.  |                 |
|           | multiplexer      | CNI-conformant IPAM Network Plugin **must** be    | 10 <chapter02. |                 |
|           |                  | installed to allocate IP addresses for secondary  | md#kubernetes- |                 |
|           |                  | network interfaces across all nodes of the        | architecture-r |                 |
|           |                  | cluster.                                          | equirement     |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+

**Table 4-6:** Networking Solution Specifications

Storage components
------------------

In order for the storage solutions to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

+-----------+------------------+---------------------------------------------------+----------------+-----------------+
| Ref       | Specification    | Details                                           | Requirement    | Reference       |
|           |                  |                                                   | Trace          | Implementation  |
|           |                  |                                                   |                | Trace           |
+===========+==================+===================================================+================+=================+
|ra2.stg.001| Ephemeral        | An implementation must support ephemeral storage, |                |                 |
|           | Storage          | for the unpacked container images to be stored    |                |                 |
|           |                  | and executed from, as a directory in the          |                |                 |
|           |                  | filesystem on the worker node on which the        |                |                 |
|           |                  | container is running. See the `Container runtimes |                |                 |
|           |                  | <#container-runtimes>`__ section above for more   |                |                 |
|           |                  | information on how this meets the requirement for |                |                 |
|           |                  | ephemeral storage for containers.                 |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.stg.002| Kubernetes       | An implementation may attach additional storage   |                |                 |
|           | Volumes          | to containers using Kubernetes Volumes.           |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.stg.003| Kubernetes       | An implementation may use Volume Plugins (see     |                |                 |
|           | Volumes          | ``ra2.stg.005`` below) to allow the use of a      |                |                 |
|           |                  | storage protocol (e.g., iSCSI, NFS) or management |                |                 |
|           |                  | API (e.g., Cinder, EBS) for the attaching and     |                |                 |
|           |                  | mounting of storage into a Pod.                   |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.stg.004| Persistent       | An implementation may support Kubernetes          | `req.inf.stg.  |                 |
|           | Volumes          | Persistent Volumes (PV) to provide persistent     | 01 <chapter02. |                 |
|           |                  | storage for Pods. Persistent Volumes exist        | md#kubernetes- |                 |
|           |                  | independent of the lifecycle of containers        | architecture-r |                 |
|           |                  | and/or pods.                                      | equirement     |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.stg.005| Storage Volume   | An implementation must support the following      |                |                 |
|           | Types            | Volume types: ``emptyDir``, ``ConfigMap``,        |                |                 |
|           |                  | ``Secret`` and ``PersistentVolumeClaim``. Other   |                |                 |
|           |                  | Volume plugins may be supported to allow for the  |                |                 |
|           |                  | use of a range of backend storage systems.        |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.stg.006| Container        | An implementation may support the Container       |                |                 |
|           | Storage          | Storage Interface (CSI), an Out-of-tree plugin.   |                |                 |
|           | Interface (CSI)  | In order to support CSI, the feature gates        |                |                 |
|           |                  | ``CSIDriverRegistry`` and ``CSINodeInfo`` must be |                |                 |
|           |                  | enabled. The implementation must use a CSI driver |                |                 |
|           |                  | (a full list of CSI drivers can be found `here    |                |                 |
|           |                  | <https://kubernetes-csi.github.io/docs/drivers.ht |                |                 |
|           |                  | ml>`__). An implementation may support ephemeral  |                |                 |
|           |                  | storage through a CSI-compatible volume plugin in |                |                 |
|           |                  | which case the ``CSIInlineVolume`` feature gate   |                |                 |
|           |                  | must be enabled. An implementation may support    |                |                 |
|           |                  | Persistent Volumes through a CSI-compatible       |                |                 |
|           |                  | volume plugin in which case the                   |                |                 |
|           |                  | ``CSIPersistentVolume`` feature gate must be      |                |                 |
|           |                  | enabled.                                          |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.stg.007|                  | An implementation should use Kubernetes Storage   |                |                 |
|           |                  | Classes to support automation and the separation  |                |                 |
|           |                  | of concerns between providers of a service and    |                |                 |
|           |                  | consumers of the service.                         |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+

**Table 4-7:** Storage Solution Specifications

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
`5.4.3 <./chapter05.md#use-transport-layer-security-and-service-mesh>`__. In addition to securing communications, the
use of a service mesh extends Kubernetes capabilities regarding observability and reliability.

Network service mesh specifications are handled in section `4.5 Networking solutions <#networking-solutions>`__.

Kubernetes Application package manager
--------------------------------------

In order for the application package managers to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

+-----------+------------------+---------------------------------------------------+----------------+-----------------+
| Ref       | Specification    | Details                                           | Requirement    | Reference       |
|           |                  |                                                   | Trace          | Implementation  |
|           |                  |                                                   |                | Trace           |
+===========+==================+===================================================+================+=================+
|ra2.pkg.001| API-based        | A package manager must use the Kubernetes APIs to | `req.int.api.  |                 |
|           | package          | manage application artifacts. Cluster-side        | 02 <./chapter0 |                 |
|           | management       | components such as Tiller are not supported.      | 2.md#kubernete |                 |
|           |                  |                                                   | s-archit       |                 |
|           |                  |                                                   | ecture-require |                 |
|           |                  |                                                   | ments>`__      |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.pkg.002| Helm version 3   | All workloads must be packaged using Helm         |                |                 |
|           |                  | (version 3) charts.                               |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+

Helm version 3 has been chosen as the Application packaging mechanism to ensure compliance with the
`ONAP ASD NF descriptor specification <https://wiki.onap.org/display/DW/Application+Service+Descriptor+%28ASD%29+and+pac
kaging+Proposals+for+CNF>`__ and `ETSI SOL0001 rel. 4 MCIOP specification <https://www.etsi.org/deliver/etsi_gs/NFV-SOL/
001_099/001/04.02.01_60/gs_NFV-SOL001v040201p.pdf>`__.

**Table 4-8:** Kubernetes Application Package Manager Specifications

Kubernetes workloads
--------------------

In order for the Kubernetes workloads to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

+-----------+------------------+---------------------------------------------------+------------------+----------------+
| Ref       | Specification    | Details                                           | Requirement      | Reference      |
|           |                  |                                                   | Trace            | Implementation |
|           |                  |                                                   |                  | Trace          |
+===========+==================+===================================================+==================+================+
|ra2.app.001| `Root <https://g | Specifies the container's root filesystem.        | TBD              | N/A            |
|           | ithub.com/openco |                                                   |                  |                |
|           | ntainers/runtime |                                                   |                  |                |
|           | -spec/blob/maste |                                                   |                  |                |
|           | r/config.md>`__  |                                                   |                  |                |
|           | Parameter Group  |                                                   |                  |                |
|           | (OCI Spec)       |                                                   |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.002| `Mounts <https:/ | Specifies additional mounts beyond root.          |TBD               | N/A            |
|           | /github.com/open |                                                   |                  |                |
|           | containers/runti |                                                   |                  |                |
|           | me-spec/blob/mas |                                                   |                  |                |
|           | ter/config.md#mo |                                                   |                  |                |
|           | unts>`__         |                                                   |                  |                |
|           | Parameter Group  |                                                   |                  |                |
|           | (OCI Spec)       |                                                   |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.003| `Process <https: | Specifies the container process.                  | TBD              | N/A            |
|           | //github.com/ope |                                                   |                  |                |
|           | ncontainers/runt |                                                   |                  |                |
|           | ime-spec/blob/ma |                                                   |                  |                |
|           | ster/config.md#p |                                                   |                  |                |
|           | rocess>`__       |                                                   |                  |                |
|           | Parameter Group  |                                                   |                  |                |
|           | (OCI Spec)       |                                                   |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.004| `Hostname <https | Specifies the container's hostname as seen by     | TBD              | N/A            |
|           | ://github.com/op | processes running inside the container.           |                  |                |
|           | encontainers/run |                                                   |                  |                |
|           | time-spec/blob/m |                                                   |                  |                |
|           | aster/config.md# |                                                   |                  |                |
|           | hostname>`__     |                                                   |                  |                |
|           | Parameter Group  |                                                   |                  |                |
|           | (OCI Spec)       |                                                   |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.005| `User <https://g | User for the process is a platform-specific       | TBD              | N/A            |
|           | ithub.com/openco | structure that allows specific control over which |                  |                |
|           | ntainers/runtime | user the process runs as.                         |                  |                |
|           | -spec/blob/maste |                                                   |                  |                |
|           | r/config.md#use  |                                                   |                  |                |
|           | r>`__ Parameter  |                                                   |                  |                |
|           | Group (OCI Spec) |                                                   |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.006| Consumption of   | Any additional non-default connection points must | `req.int.api.01  | N/A            |
|           | additional,      | be requested through the use of workload          | <chapter02.md#ku |                |
|           | non-default      | annotations or resource requests and limits       | bernetes-archite |                |
|           | connection       | within the container spec passed to the           | cture-requiremen |                |
|           | points           | Kubernetes API Server.                            | ts>`__           |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.007| Host Volumes     | Workloads should not use ``hostPath`` volumes, as | `req.kcm.gen.02  | N/A            |
|           |                  | `Pods with identical configuration <https://kuber | <chapter02.md#ku |                |
|           |                  | netes.io/docs/concepts/storage/volumes/#hostpat   | bernetes-archite |                |
|           |                  | h>`__ (such as those created from a PodTemplate)  | cture-requiremen |                |
|           |                  | may behave differently on different nodes due to  | ts>`__.          |                |
|           |                  | different files on the nodes.                     |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.008| Infrastructure   | Workloads must not rely on the availability of    | TBD              | N/A            |
|           | dependency       | the master nodes for the successful execution of  |                  |                |
|           |                  | their functionality (i.e. loss of the master      |                  |                |
|           |                  | nodes may affect non-functional behaviours such   |                  |                |
|           |                  | as healing and scaling, but components that are   |                  |                |
|           |                  | already running will continue to do so without    |                  |                |
|           |                  | issue).                                           |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.009| Device plugins   | Workload descriptors must use the resources       | TBD              | N/A            |
|           |                  | advertised by the device plugins to indicate      |                  |                |
|           |                  | their need for an FPGA, SR-IOV or other           |                  |                |
|           |                  | acceleration device.                              |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.010| Node Feature     | Workload descriptors must use the labels          | TBD              | N/A            |
|           | Discovery (NFD)  | advertised by `Node Feature Discovery <https://ku |                  |                |
|           |                  | bernetes-sigs.github.io/node-feature-discovery/st |                  |                |
|           |                  | able/get-started/index.html>`__ to indicate which |                  |                |
|           |                  | node software of hardware features they need.     |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.011| Published helm   | Helm charts of the CNF must be published into a   | `CNCF CNF        | N/A            |
|           | chart            | helm registry and must not be used from local     | Testsuite        |                |
|           |                  | copies.                                           | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#te |                |
|           |                  |                                                   | st-if-the-helm-c |                |
|           |                  |                                                   | hart-is-publishe |                |
|           |                  |                                                   | d-helm_chart_pub |                |
|           |                  |                                                   | lished>`__       |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.012| Valid Helm chart | Helm charts of the CNF must be valid and should   | `CNCF CNF        | N/A            |
|           |                  | pass the `helm lint` validation.                  | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#te |                |
|           |                  |                                                   | st-if-the-helm-c |                |
|           |                  |                                                   | hart-is-valid-he |                |
|           |                  |                                                   | lm_chart_vali    |                |
|           |                  |                                                   | d>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.013| Rolling update   | Rolling update of the CNF must be possible using  | `CNCF CNF        | N/A            |
|           |                  | Kubernetes deployments.                           | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -test-if-the-cnf |                |
|           |                  |                                                   | -can-perform-a-r |                |
|           |                  |                                                   | olling-update-ro |                |
|           |                  |                                                   | lling_update>`__ |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.014| Rolling          | Rolling downgrade of the CNF must be possible     | `CNCF CNF        | N/A            |
|           | downgrade        | using Kubernetes deployments.                     | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-a-cnf- |                |
|           |                  |                                                   | version-can-be-d |                |
|           |                  |                                                   | owngraded-throug |                |
|           |                  |                                                   | h-a-rolling_down |                |
|           |                  |                                                   | grade-rolling_do |                |
|           |                  |                                                   | wngrade>`__      |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.015| CNI              | The CNF must use CNI compatible networking        | `CNCF CNF        | N/A            |
|           | compatibility    | plugins.                                          | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-the-cn |                |
|           |                  |                                                   | f-is-compatible- |                |
|           |                  |                                                   | with-different-c |                |
|           |                  |                                                   | nis-cni_compatib |                |
|           |                  |                                                   | ility>`__        |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.016| Kubernetes API   | The CNF must not use any Kubernetes alpha API-s.  | `CNCF CNF        | N/A            |
|           | stability        |                                                   | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#po |                |
|           |                  |                                                   | c-to-check-if-a- |                |
|           |                  |                                                   | cnf-uses-kuberne |                |
|           |                  |                                                   | tes-alpha-apis-a |                |
|           |                  |                                                   | lpha_k8s_apis-al |                |
|           |                  |                                                   | pha_k8s_apis>`__ |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.017| CNF resiliency   | CNF must not loose data, must continue to run and | `CNCF CNF        | N/A            |
|           | (node drain)     | its readiness probe outcome must be Success even  | Testsuite        |                |
|           |                  | in case of a node drain and rescheduling occurs.  | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#te |                |
|           |                  |                                                   | st-if-the-cnf-cr |                |
|           |                  |                                                   | ashes-when-node- |                |
|           |                  |                                                   | drain-occurs-nod |                |
|           |                  |                                                   | e_drain>`__      |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.018| CNF resiliency   | CNF must not loose data, must continue to run and | `CNCF CNF        | N/A            |
|           | (network         | its readiness probe outcome must be Success even  | Testsuite        |                |
|           | latency)         | in case of network latency up to 2000 ms occurs.  | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#te |                |
|           |                  |                                                   | st-if-the-cnf-cr |                |
|           |                  |                                                   | ashes-when-netwo |                |
|           |                  |                                                   | rk-latency-occur |                |
|           |                  |                                                   | s-pod_network_la |                |
|           |                  |                                                   | tency>`__        |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.019| CNF resiliency   | CNF must not loose data, must continue to run and | `CNCF CNF        | N/A            |
|           | (pod delete)     | its readiness probe outcome must be Success even  | Testsuite        |                |
|           |                  | in case of pod delete occurs.                     | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#te |                |
|           |                  |                                                   | st-if-the-cnf-cr |                |
|           |                  |                                                   | ashes-when-disk- |                |
|           |                  |                                                   | fill-occurs-disk |                |
|           |                  |                                                   | _fill>`__        |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.020| CNF resiliency   | CNF must not loose data, must continue to run and | `CNCF CNF        | N/A            |
|           | (pod memory hog) | its readiness probe outcome must be Success even  | Testsuite        |                |
|           |                  | in case of pod memory hog occurs.                 | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#te |                |
|           |                  |                                                   | st-if-the-cnf-cr |                |
|           |                  |                                                   | ashes-when-pod-m |                |
|           |                  |                                                   | emory-hog-occurs |                |
|           |                  |                                                   | -pod_memory_ho   |                |
|           |                  |                                                   | g>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.021| CNF resiliency   | CNF must not loose data, must continue to run and | `CNCF CNF        | N/A            |
|           | (pod I/O stress) | its readiness probe outcome must be Success even  | Testsuite        |                |
|           |                  | in case of pod I/O stress occurs.                 | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#te |                |
|           |                  |                                                   | st-if-the-cnf-cr |                |
|           |                  |                                                   | ashes-when-pod-i |                |
|           |                  |                                                   | o-stress-occurs- |                |
|           |                  |                                                   | pod_io_stres     |                |
|           |                  |                                                   | s>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.022| CNF resiliency   | CNF must not loose data, must continue to run and | `CNCF CNF        | N/A            |
|           | (pod network     | its readiness probe outcome must be Success even  | Testsuite        |                |
|           | corruption)      | in case of pod network corruption occurs.         | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#te |                |
|           |                  |                                                   | st-if-the-cnf-cr |                |
|           |                  |                                                   | ashes-when-pod-n |                |
|           |                  |                                                   | etwork-corruptio |                |
|           |                  |                                                   | n-occurs-pod_net |                |
|           |                  |                                                   | work_corruptio   |                |
|           |                  |                                                   | n>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.023| CNF resiliency   | CNF must not loose data, must continue to run and | `CNCF CNF        | N/A            |
|           | (pod network     | its readiness probe outcome must be Success even  | Testsuite        |                |
|           | duplication)     | in case of pod network duplication occurs.        | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#te |                |
|           |                  |                                                   | st-if-the-cnf-cr |                |
|           |                  |                                                   | ashes-when-pod-n |                |
|           |                  |                                                   | etwork-duplicati |                |
|           |                  |                                                   | on-occurs-pod_ne |                |
|           |                  |                                                   | twork_duplicatio |                |
|           |                  |                                                   | n>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.024| CNF resiliency   | CNF must not loose data, must continue to run and |                  | N/A            |
|           | (pod DNS error)  | its readiness probe outcome must be Success even  |                  |                |
|           |                  | in case of pod DNS error occurs.                  |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.025| CNF local        | CNF must not use local storage.                   | `CNCF CNF        | N/A            |
|           | storage          |                                                   | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -test-if-the-cnf |                |
|           |                  |                                                   | -uses-local-stor |                |
|           |                  |                                                   | age-no_local_vol |                |
|           |                  |                                                   | ume_configuratio |                |
|           |                  |                                                   | n>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.026| Liveness probe   | All Pods of the CNF must have `livenessProbe`     | `CNCF CNF        | N/A            |
|           |                  | defined.                                          | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -test-if-there-i |                |
|           |                  |                                                   | s-a-liveness-ent |                |
|           |                  |                                                   | ry-in-the-helm-c |                |
|           |                  |                                                   | hart-livenes     |                |
|           |                  |                                                   | s>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.027| Readiness probe  | All Pods of the CNF must have `readinessProbe`    | `CNCF CNF        | N/A            |
|           |                  | defined.                                          | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -test-if-there-i |                |
|           |                  |                                                   | s-a-readiness-en |                |
|           |                  |                                                   | try-in-the-helm- |                |
|           |                  |                                                   | chart-readines   |                |
|           |                  |                                                   | s>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.028| No access to     | The CNF must not have any of the container        |                  | N/A            |
|           | container        | daemon sockets (e.g.: `/var/run/docker.sock`,     |                  |                |
|           | daemon sockets   | `/var/run/containerd.sock` or                     |                  |                |
|           |                  | `/var/run/crio.sock`) mounted.                    |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.029| No automatic     | Non specified service accounts must not be        | `CNCF CNF        | N/A            |
|           | service account  | automatically mapped. To prevent this             | Testsuite        |                |
|           | mapping          | `automountServiceAccountToken: false flag must be | <https://github. |                |
|           |                  | set in all Pods of the CNF.                       | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-there- |                |
|           |                  |                                                   | are-service-acco |                |
|           |                  |                                                   | unts-that-are-au |                |
|           |                  |                                                   | tomatically-mapp |                |
|           |                  |                                                   | ed-application_c |                |
|           |                  |                                                   | redentials>`__   |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.030| No host network  | Host network must not be attached to any of the   | `CNCF CNF        | N/A            |
|           | access           | Pods of the CNF. hostNetwork attribute of the Pod | Testsuite        |                |
|           |                  | specifications must be False or should not be     | <https://github. |                |
|           |                  | specified.                                        | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-there- |                |
|           |                  |                                                   | -is-a-host-netwo |                |
|           |                  |                                                   | rk-attached-to-a |                |
|           |                  |                                                   | -pod-host_networ |                |
|           |                  |                                                   | k>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.031| Host process     | Pods of the CNF must not share the host process   | `CNCF CNF        | N/A            |
|           | namespace        | ID namespace or the host IPC namespace. Pod       | Testsuite        |                |
|           | separation       | manifests must not have the `hostPID` or the      | <https://github. |                |
|           |                  | `hostIPC` attribute set to true.                  | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-contai |                |
|           |                  |                                                   | ners-are-running |                |
|           |                  |                                                   | -with-hostpid-or |                |
|           |                  |                                                   | -hostipc-privile |                |
|           |                  |                                                   | ges-host_pid_ipc |                |
|           |                  |                                                   | _privileges>`__  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.032| Resource limits  | All containers and namespaces of the CNF must     | `CNCF CNF        | N/A            |
|           |                  | have defined resource limits for at least CPU and | Testsuite        |                |
|           |                  | memory resources.                                 | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-contai |                |
|           |                  |                                                   | ners-have-resour |                |
|           |                  |                                                   | ce-limits-define |                |
|           |                  |                                                   | d-resource_polic |                |
|           |                  |                                                   | ies>`__          |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.033| Read only        | All containers of the CNF must have a read only   | `CNCF CNF        | N/A            |
|           | filesystem       | filesystem. The `readOnlyRootFilesystem`          | Testsuite        |                |
|           |                  | attribute of the Pods in the their                | <https://github. |                |
|           |                  | `securityContext` should be set to true.          | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-contai |                |
|           |                  |                                                   | ners-have-immuta |                |
|           |                  |                                                   | ble-file-systems |                |
|           |                  |                                                   | -immutable_file_ |                |
|           |                  |                                                   | systems>`__      |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.034| Container image  | All referred container images in the Pod          |                  | N/A            |
|           | tags             | manifests must be referred by a version tag       |                  |                |
|           |                  | pointing to a concrete version of the image.      |                  |                |
|           |                  | `latest` tag must not be used.                    |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.035| No hardcoded IP  | The CNF must not have any hardcoded IP addresses  | `CNCF CNF        | N/A            |
|           | addresses        | in its Pod specifications.                        | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -test-if-there-a |                |
|           |                  |                                                   | re-any-non-decla |                |
|           |                  |                                                   | rative-hardcoded |                |
|           |                  |                                                   | -ip-addresses-or |                |
|           |                  |                                                   | -subnet-masks-in |                |
|           |                  |                                                   | -the-k8s-runtime |                |
|           |                  |                                                   | -configuratio    |                |
|           |                  |                                                   | n>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.036| No node ports    | Service declarations of the CNF must not contain  | `Kubernetes      | N/A            |
|           |                  | `nodePort` definition.                            | documentation    |                |
|           |                  |                                                   | <https://kuberne |                |
|           |                  |                                                   | tes.io/docs/conc |                |
|           |                  |                                                   | epts/services-ne |                |
|           |                  |                                                   | tworking/service |                |
|           |                  |                                                   | />`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.037| Immutable config |ConfigMaps used by the CNF must be immutable.      | `Kubernetes      | N/A            |
|           | maps             |                                                   | documentation    |                |
|           |                  |                                                   | <https://kuberne |                |
|           |                  |                                                   | tes.io/docs/conc |                |
|           |                  |                                                   | epts/configurati |                |
|           |                  |                                                   | on/configmap/#co |                |
|           |                  |                                                   | nfigmap-immutabl |                |
|           |                  |                                                   | e>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+ 
|ra2.app.038| Horizontal       | Increasing and decreasing of the CNF capacity     | TBD              | N/A            |
|           | scaling          | should be implemented using horizontal scaling.   |                  |                |
|           |                  | If horizontal scaling is supported, automatic     |                  |                |
|           |                  | scaling must be possible using Kubernetes         |                  |                |
|           |                  | `Horizontal Pod Autoscale (HPA) <https://kubernet |                  |                |
|           |                  | es.io/docs/tasks/run-application/horizontal-pod-a |                  |                |
|           |                  | utoscale/>`__ feature.                            |                  |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.039| CNF image size   | The different container images of the CNF should  | `CNCF CNF        | N/A            |
|           |                  | not be bigger than 5GB.                           | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-the-cn |                |
|           |                  |                                                   | f-has-a-reasonab |                |
|           |                  |                                                   | le-image-size-re |                |
|           |                  |                                                   | asonable_image_s |                |
|           |                  |                                                   | ize>`__          |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.040| CNF startup time | Startup time of the Pods of a CNF should not be   | `CNCF CNF        | N/A            |
|           |                  | more than 60s where startup time is the time      | Testsuite        |                |
|           |                  | between starting the Pod until the readiness      | <https://github. |                |
|           |                  | probe outcome is Success.                         | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-the-cn |                |
|           |                  |                                                   | f-have-a-reasona |                |
|           |                  |                                                   | ble-startup-time |                |
|           |                  |                                                   | -reasonable_star |                |
|           |                  |                                                   | tup_time>`__     |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.041| No privileged    | None of the Pods of the CNF should run in         | `CNCF CNF        | N/A            |
|           | mode             | privileged mode.                                  | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-there- |                |
|           |                  |                                                   | are-any-privileg |                |
|           |                  |                                                   | ed-containers-ku |                |
|           |                  |                                                   | bscape-version-p |                |
|           |                  |                                                   | rivileged_contai |                |
|           |                  |                                                   | ners>`__         |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.042| No root user     | None of the Pods of the CNF should run as a root  | `CNCF CNF        | N/A            |
|           |                  | user.                                             | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-any-co |                |
|           |                  |                                                   | ntainers-are-run |                |
|           |                  |                                                   | ning-as-a-root-u |                |
|           |                  |                                                   | ser-checks-the-u |                |
|           |                  |                                                   | ser-outside-the- |                |
|           |                  |                                                   | container-that-i |                |
|           |                  |                                                   | s-running-docker |                |
|           |                  |                                                   | d-non_root_use   |                |
|           |                  |                                                   | r>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.043| No privilege     | None of the containers of the CNF should allow    | `CNCF CNF        | N/A            |
|           | escalation       | privilege escalation.                             | Testsuite        |                |
|           |                  |                                                   | <https://github. |                |
|           |                  |                                                   | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-there- |                |
|           |                  |                                                   | are-any-privileg |                |
|           |                  |                                                   | ed-containers-ku |                |
|           |                  |                                                   | bscape-version-p |                |
|           |                  |                                                   | rivileged_contai |                |
|           |                  |                                                   | ners>`__         |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.044| Non-root user    | All Pods of the CNF should be able to execute     | `CNCF CNF        | N/A            |
|           |                  | with a non-root user having a non-root group.     | Testsuite        |                |
|           |                  | Both `runAsUser` and `runAsGroup` attributes      | <https://github. |                |
|           |                  | should be set to a greater value than 999.        | com/cncf/cnf-tes |                |
|           |                  |                                                   | tsuite/blob/main |                |
|           |                  |                                                   | /RATIONALE.md#to |                |
|           |                  |                                                   | -check-if-contai |                |
|           |                  |                                                   | ners-are-running |                |
|           |                  |                                                   | -with-non-root-u |                |
|           |                  |                                                   | ser-with-non-roo |                |
|           |                  |                                                   | t-membership-non |                |
|           |                  |                                                   | _root_container  |                |
|           |                  |                                                   | s>`__            |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+
|ra2.app.045| Labels           | Pods of the CNF should define at least the        | `Kubernetes      | N/A            |
|           |                  | following labels:  app.kubernetes.io/name,        | documentation    |                |
|           |                  | app.kubernetes.io/version and                     | <https://kuberne |                |
|           |                  | app.kubernetes.io/part-of                         | tes.io/docs/conc |                |
|           |                  |                                                   | epts/overview/wo |                |
|           |                  |                                                   | rking-with-objec |                |
|           |                  |                                                   | ts/common-label  |                |
|           |                  |                                                   | s/>`__           |                |
+-----------+------------------+---------------------------------------------------+------------------+----------------+

**Table 4-9:** Kubernetes Workload Specifications

Additional required components
------------------------------

   This chapter should list any additional components needed to provide the services defined in Chapter 3.2 (e.g., Prometheus)

