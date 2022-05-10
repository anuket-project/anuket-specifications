Reference Implementation Requirements
=====================================

Introduction
------------

This chapter will use the requirements defined in the Kubernetes Reference Architecture and only make additional
entries in :ref:chapters/chapter02:`Reference Architecture Specification` if there are additional requirements needed
for this Reference Implementation.

Definitions
-----------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in `RFC2119 <https://www.ietf.org/rfc/rfc2119.txt>`__.

Reference Architecture Specification
------------------------------------

.. list-table:: Traceability of Reference Architecture Requirements
    :widths: 10 15 35 10 10 20
    :header-rows: 1

    * - RA2 Section
      - RA2 Reference
      - Specification
      - Requirement for Basic Profile
      - Requirement for Network Intensive Profile
      - RI2 Traceability
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.001``
      - Huge pages
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.002``
      - SR-IOV Capable NICs
      - Not required
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.003``
      - SR-IOV Virtual Functions
      - Not required
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.004``
      - CPU Simultaneous Multi-Threading (SMT)
      - True
      - True
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.006``
      - CPU Allocation Ratio - Pods
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.008``
      - Physical CPU Quantity
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.009``
      - Physical Storage
      - Should support
      - Should support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.010``
      - Local Filesystem Storage Quantity
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.012``
      - Kubernetes Node RAM Quantity
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.013``
      - Physical NIC Quantity
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.014``
      - Physical NIC Speed - Basic Profile
      - Must support
      - N/A
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.015``
      - Physical NIC Speed - Network Intensive Profile
      - N/A
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter03:Infrastructure Requirements`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes Node`
      - ``ra2.ch.017``
      - Immutable Infrastructure
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes`
      - ``ra2.k8s.001``
      - Kubernetes Conformance
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes`
      - ``ra2.k8s.002``
      - Highly available etcd
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes`
      - ``ra2.k8s.005``
      - Kubernetes API Version
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Kubernetes`
      - ``ra2.k8s.006``
      - NUMA Support
      - Not required
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Container Runtimes`
      - ``ra2.crt.001``
      - Conformance with OCI 1.0 runtime spec
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Container Runtimes`
      - ``ra2.crt.002``
      - Kubernetes Container Runtime Interface (CRI)
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.001``
      - Centralised network administration
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.002``
      - Default Pod Network - CNI
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.003``
      - Multiple connection points
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.004``
      - Multiple connection points presentation
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.005``
      - Multiplexer /meta-plugin
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.006``
      - Multiplexer/meta-plugin CNI Conformance
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.007``
      - Multiplexer/meta-plugin CNI Plugins
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.008``
      - SR-IOV Device Plugin for Network Intensive
      - Not required
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.009``
      - Multiple connection points with multiplexer/meta-plugin
      - Must support
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.010``
      - User plane networking
      - Not required
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
    * - :ref:`ref_arch/kubernetes/chapters/chapter04:Networking Solutions`
      - ``ra2.ntw.012``
      - Optional Device Plugins
      - Not required
      - Must support
      - :ref:`ref_impl/cntt-ri2/chapters/chapter04:Installation on Bare Metal Infratructure`
