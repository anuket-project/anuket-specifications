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

+----------+-------------------+---------------------------------------------------+----------------+-----------------+
| Ref      | Specification     | Details                                           | Requirement    | Reference       |
|          |                   |                                                   | Trace          | Implementation  |
|          |                   |                                                   |                | Trace           |
+==========+===================+===================================================+================+=================+
|ra2.ch.001| Huge pages        | When hosting workloads matching the High          | `infra.com.cfg | `4.3.1 <../../. |
|          |                   | Performance profile, it **must** be possible to   | .004 <./chapte | ./ref_impl/cntt |
|          |                   | enable Huge pages (2048KiB and 1048576KiB) within | r02.md#cloud-i | -ri2/chapters/c |
|          |                   | the Kubernetes Node OS, exposing schedulable      | nfrastructure- | hapter04.md#ins |
|          |                   | resources ``hugepages-2Mi`` and ``hugepages-1Gi`` | software-profi | tallation-on-ba |
|          |                   | .                                                 | le-requirement | re-metal-infrat |
|          |                   |                                                   | s>`__          | ructure>`__     |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.002| SR-IOV capable    | When hosting workloads matching the High          | `e.cap.013 <./ | `3.3 <../../../ |
|          | NICs              | Performance profile, the physical machines on     | chapter02.md#c | ref_impl/cntt-r |
|          |                   | which the Kubernetes Nodes run **must** be        | loud-infrastru | i2/chapters/cha |
|          |                   | equipped with NICs that are SR-IOV capable.       | cture-software | pter03.md#infra |
|          |                   |                                                   | -profile-requi | structure-requi |
|          |                   |                                                   | rements>`__    | rements>`__     |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.003| SR-IOV Virtual    | When hosting workloads matching the High          | `e.cap.013 <./ | `4.3.1 <../../. |
|          | Functions         | Performance profile, SR-IOV virtual functions     | chapter02.md#c | ./ref_impl/cntt |
|          |                   | (VFs) **must** be configured within the           | loud-infrastru | -ri2/chapters/c |
|          |                   | Kubernetes Node OS, as the SR-IOV Device Plugin   | cture-software | hapter04.md#ins |
|          |                   | does not manage the creation of these VFs.        | -profile-requi | tallation-on-ba |
|          |                   |                                                   | rements>`__    | re-metal-infrat |
|          |                   |                                                   |                | ructure>`__     |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.004| CPU Simultaneous  | SMT **must** be enabled in the BIOS on the        | `infra.hw.cpu. | `3.3 <../../../ |
|          | Multi-Threading   | physical machine on which the Kubernetes Node     | cfg.004 <./cha | ref_impl/cntt-r |
|          | (SMT)             | runs.                                             | pter02.md#clou | i2/chapters/cha |
|          |                   |                                                   | d-infrastructu | pter03.md#infra |
|          |                   |                                                   | re-hardware-pr | structure-requi |
|          |                   |                                                   | ofile-requirem | rements>`__     |
|          |                   |                                                   | ents>`__       |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.005| CPU Allocation    | For Kubernetes nodes running as Virtual Machines, |                |                 |
|          | Ratio - VMs       | the CPU allocation ratio between vCPU and         |                |                 |
|          |                   | physical CPU core **must** be 1:1.                |                |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.006| CPU Allocation    | To ensure the CPU allocation ratio between vCPU   | `infra.com.cfg | `3.3 <../../../ |
|          | Ratio - Pods      | and physical CPU core is 1:1, the sum of CPU      | .001 <./chapte | ref_impl/cntt-r |
|          |                   | requests and limits by containers in Pod          | r02.md#cloud-i | i2/chapters/cha |
|          |                   | specifications **must** remain less than the      | nfrastructure- | pter03.md#infra |
|          |                   | allocatable quantity of CPU resources (i.e.       | software-profi | structure-requi |
|          |                   | ``requests.cpu < allocatable.cpu`` and            | le-requirement | rements>`__     |
|          |                   | ``limits.cpu < allocatable.cpu``).                | s>`__          |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.007| IPv6DualStack     | To support IPv4/IPv6 dual stack networking, the   |                |                 |
|          |                   | Kubernetes Node OS **must** support and be        |                |                 |
|          |                   | allocated routable IPv4 and IPv6 addresses.       |                |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.008| Physical CPU      | The physical machines on which the Kubernetes     | `infra.hw.cpu. | `3.3 <../../../ |
|          | Quantity          | Nodes run **must** be equipped with at least 2    | cfg.001 <./cha | ref_impl/cntt-r |
|          |                   | physical sockets, each with at least 20 CPU       | pter02.md#clou | i2/chapters/cha |
|          |                   | cores.                                            | d-infrastructu | pter03.md#infra |
|          |                   |                                                   | re-hardware-pr | structure-requi |
|          |                   |                                                   | ofile-requirem | rements>`__     |
|          |                   |                                                   | ents>`__,      |                 |
|          |                   |                                                   | `infra.hw.cpu. |                 |
|          |                   |                                                   | cfg.002 <./cha |                 |
|          |                   |                                                   | pter02.md#clou |                 |
|          |                   |                                                   | d-infrastructu |                 |
|          |                   |                                                   | re-hardware-pr |                 |
|          |                   |                                                   | ofile-requirem |                 |
|          |                   |                                                   | ents>`__       |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.009| Physical Storage  | The physical machines on which the Kubernetes     | `infra.hw.stg. | `3.3 <../../../ |
|          |                   | Nodes run **should** be equipped with Sold State  | ssd.cfg.002 <. | ref_impl/cntt-r |
|          |                   | Drives (SSDs).                                    | /chapter02.md# | i2/chapters/cha |
|          |                   |                                                   | cloud-infrastr | pter03.md#infra |
|          |                   |                                                   | ucture-hardwar | structure-requi |
|          |                   |                                                   | e-profile-requ | rements>`__     |
|          |                   |                                                   | irements>`__   |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.010| Local Filesystem  | The Kubernetes Nodes **must** be equipped with    | `e.cap.003 <./ | `3.3 <../../../ |
|          | Storage Quantity  | local filesystem capacity of at least 320GB for   | chapter02.md#c | ref_impl/cntt-r |
|          |                   | unpacking and executing containers. Note, extra   | loud-infrastru | i2/chapters/cha |
|          |                   | should be provisioned to cater for any overhead   | cture-software | pter03.md#infra |
|          |                   | required by the Operating System and any required | -profile-capab | structure-requi |
|          |                   | OS processes such as the container runtime,       | ilities>`__    | rements>`__     |
|          |                   | Kubernetes agents, etc.                           |                |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.011| Virtual Node CPU  | If using VMs, the Kubernetes Nodes **must** be    | `e.cap.001 <./ |                 |
|          | Quantity          | equipped with at least 16 vCPUs. Note, extra      | chapter02.md#c |                 |
|          |                   | should be provisioned to cater for any overhead   | loud-infrastru |                 |
|          |                   | required by the Operating System and any required | cture-software |                 |
|          |                   | OS processes such as the container runtime,       | -profile-capab |                 |
|          |                   | Kubernetes agents, etc.                           | ilities>`__    |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.012| Kubernetes Node   | The Kubernetes Nodes **must** be equipped with at | `e.cap.002 <./ | `3.3 <../../../ |
|          | RAM Quantity      | least 32GB of RAM. Note, extra should be          | chapter02.md#c | ref_impl/cntt-r |
|          |                   | provisioned to cater for any overhead required by | loud-infrastru | i2/chapters/cha |
|          |                   | the Operating System and any required OS          | cture-software | pter03.md#infra |
|          |                   | processes such as the container runtime,          | -profile-capab | structure-requi |
|          |                   | Kubernetes agents, etc.                           | ilities>`__    | rements>`__     |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.013| Physical NIC      | The physical machines on which the Kubernetes     | `infra.hw.nic. | `3.3 <../../../ |
|          | Quantity          | Nodes run **must** be equipped with at least four | cfg.001 <./cha | ref_impl/cntt-r |
|          |                   | (4) Network Interface Card (NIC) ports.           | pter02.md#clou | i2/chapters/cha |
|          |                   |                                                   | d-infrastructu | pter03.md#infra |
|          |                   |                                                   | re-hardware-pr | structure-requi |
|          |                   |                                                   | ofile-requirem | rements>`__     |
|          |                   |                                                   | ents>`__       |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.014| Physical NIC      | The speed of NIC ports housed in the physical     | `infra.hw.nic. | `3.3 <../../../ |
|          | Speed - Basic     | machines on which the Kubernetes Nodes run for    | cfg.002 <./cha | ref_impl/cntt-r |
|          | Profile           | workloads matching the Basic Profile **must** be  | pter02.md#clou | i2/chapters/cha |
|          |                   | at least 10Gbps.                                  | d-infrastructu | pter03.md#infra |
|          |                   |                                                   | re-hardware-pr | structure-requi |
|          |                   |                                                   | ofile-requirem | rements>`__     |
|          |                   |                                                   | ents>`__       |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.015| Physical NIC      | The speed of NIC ports housed in the physical     | `infra.hw.nic. | `3.3 <../../../ |
|          | Speed - High      | machines on which the Kubernetes Nodes run for    | cfg.002 <./cha | ref_impl/cntt-r |
|          | Performance       | workloads matching the High Performance profile   | pter02.md#clou | i2/chapters/cha |
|          | Profile           | **must** be at least 25Gbps.                      | d-infrastructu | pter03.md#infra |
|          |                   |                                                   | re-hardware-pr | structure-requi |
|          |                   |                                                   | ofile-requirem | rements>`__     |
|          |                   |                                                   | ents>`__       |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.016| Physical PCIe     | The physical machines on which the Kubernetes     |                |                 |
|          | slots             | Nodes run **must** be equipped with at least      |                |                 |
|          |                   | eight (8) Gen3.0 PCIe slots, each with at least   |                |                 |
|          |                   | eight (8) lanes.                                  |                |                 |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.017| Immutable         | Whether physical or virtual machines are used,    | `req.gen.cnt.0 | `4.3.1 <../../. |
|          | infrastructure    | the Kubernetes Node **must not** be changed       | 2 <./chapter02 | ./ref_impl/cntt |
|          |                   | after it is instantiated. New changes to the      | .md#kubernetes | -ri2/chapters/c |
|          |                   | Kubernetes Node must be implemented as new Node   | -architecture- | hapter04.md#ins |
|          |                   | instances. This covers any changes from BIOS      | require        | tallation-on-ba |
|          |                   | through Operating System to running processes and | ments>`__      | re-metal-infrat |
|          |                   | all associated configurations.                    |                | ructure>`__     |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+
|ra2.ch.018| NFD               | `Node Feature Discovery <https://kubernetes-sigs. | TBD            | `4.3.1 <../../. |
|          |                   | github.io/node-feature-discovery/stable/get-start |                | ./ref_impl/cntt |
|          |                   | ed/index.html>`__ **must** be used to advertise   |                | -ri2/chapters/c |
|          |                   | the detailed software and hardware capabilities   |                | hapter04.md#ins |
|          |                   | of each node in the Kubernetes Cluster.           |                | tallation-on-ba |
|          |                   |                                                   |                | re-metal-infrat |
|          |                   |                                                   |                | ructure>`__     |
+----------+-------------------+---------------------------------------------------+----------------+-----------------+

**Table 4-1:** Node Specifications

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

**Table 4-2:** Kubernetes Specifications

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

**Table 4-3:** Container Runtime Specifications

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

**Table 4-4:** Networking Solution Specifications

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

**Table 4-6:** Storage Solution Specifications

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

**Table 4-7:** Kubernetes Application Package Manager Specifications

Kubernetes workloads
--------------------

In order for the Kubernetes workloads to be conformant with the Reference
Architecture they must be implemented as per the following specifications:

+-----------+------------------+---------------------------------------------------+----------------+-----------------+
| Ref       | Specification    | Details                                           | Requirement    | Reference       |
|           |                  |                                                   | Trace          | Implementation  |
|           |                  |                                                   |                | Trace           |
+===========+==================+===================================================+================+=================+
|ra2.app.001| `Root <https://g | Specifies the container's root filesystem.        | TBD            | N/A             |
|           | ithub.com/openco |                                                   |                |                 |
|           | ntainers/runtime |                                                   |                |                 |
|           | -spec/blob/maste |                                                   |                |                 |
|           | r/config.md>`__  |                                                   |                |                 |
|           | Parameter Group  |                                                   |                |                 |
|           | (OCI Spec)       |                                                   |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.app.002| `Mounts <https:/ | Specifies additional mounts beyond root.          |TBD             | N/A             |
|           | /github.com/open |                                                   |                |                 |
|           | containers/runti |                                                   |                |                 |
|           | me-spec/blob/mas |                                                   |                |                 |
|           | ter/config.md#mo |                                                   |                |                 |
|           | unts>`__         |                                                   |                |                 |
|           | Parameter Group  |                                                   |                |                 |
|           | (OCI Spec)       |                                                   |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.app.003| `Process <https: | Specifies the container process.                  | TBD            | N/A             |
|           | //github.com/ope |                                                   |                |                 |
|           | ncontainers/runt |                                                   |                |                 |
|           | ime-spec/blob/ma |                                                   |                |                 |
|           | ster/config.md#p |                                                   |                |                 |
|           | rocess>`__       |                                                   |                |                 |
|           | Parameter Group  |                                                   |                |                 |
|           | (OCI Spec)       |                                                   |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.app.004| `Hostname <https | Specifies the container's hostname as seen by     | TBD            | N/A             |
|           | ://github.com/op | processes running inside the container.           |                |                 |
|           | encontainers/run |                                                   |                |                 |
|           | time-spec/blob/m |                                                   |                |                 |
|           | aster/config.md# |                                                   |                |                 |
|           | hostname>`__     |                                                   |                |                 |
|           | Parameter Group  |                                                   |                |                 |
|           | (OCI Spec)       |                                                   |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.app.005| `User <https://g | User for the process is a platform-specific       | TBD            | N/A             |
|           | ithub.com/openco | structure that allows specific control over which |                |                 |
|           | ntainers/runtime | user the process runs as.                         |                |                 |
|           | -spec/blob/maste |                                                   |                |                 |
|           | r/config.md#use  |                                                   |                |                 |
|           | r>`__ Parameter  |                                                   |                |                 |
|           | Group (OCI Spec) |                                                   |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.app.006| Consumption of   | The workload must request additional non-default  | `req.int.api.  | N/A             |
|           | additional,      | connection points through the use of workload     | 01 <chapter02. |                 |
|           | non-default      | annotations or resource requests and limits       | md#kubernetes- |                 |
|           | connection       | within the container spec passed to the           | architecture-r |                 |
|           | points           | Kubernetes API Server.                            | equirement     |                 |
|           |                  |                                                   | s>`__          |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.app.007| Host Volumes     | Workloads should not use ``hostPath`` volumes, as | `req.kcm.gen.  | N/A             |
|           |                  | `Pods with identical configuration <https://kuber | 02 <chapter02. |                 |
|           |                  | netes.io/docs/concepts/storage/volumes/#hostpat   | md#kubernetes- |                 |
|           |                  | h>`__ (such as those created from a PodTemplate)  | architecture-r |                 |
|           |                  | may behave differently on different nodes due to  | equirement     |                 |
|           |                  | different files on the nodes.                     | s>`__.         |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.app.008| Infrastructure   | Workloads must not rely on the availability of    | TBD            | N/A             |
|           | dependency       | the master nodes for the successful execution of  |                |                 |
|           |                  | their functionality (i.e. loss of the master      |                |                 |
|           |                  | nodes may affect non-functional behaviours such   |                |                 |
|           |                  | as healing and scaling, but components that are   |                |                 |
|           |                  | already running will continue to do so without    |                |                 |
|           |                  | issue).                                           |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.app.009| Device plugins   | Workload descriptors must use the resources       | TBD            | N/A             |
|           |                  | advertised by the device plugins to indicate      |                |                 |
|           |                  | their need for an FPGA, SR-IOV or other           |                |                 |
|           |                  | acceleration device.                              |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+
|ra2.app.010| Node Feature     | Workload descriptors must use the labels          | TBD            | N/A             |
|           | Discovery (NFD)  | advertised by `Node Feature Discovery <https://ku |                |                 |
|           |                  | bernetes-sigs.github.io/node-feature-discovery/st |                |                 |
|           |                  | able/get-started/index.html>`__ to indicate which |                |                 |
|           |                  | node software of hardware features they need.     |                |                 |
+-----------+------------------+---------------------------------------------------+----------------+-----------------+

**Table 4-8:** Kubernetes Workload Specifications

Additional required components
------------------------------

   This chapter should list any additional components needed to provide the services defined in Chapter 3.2 (e.g., Prometheus)

