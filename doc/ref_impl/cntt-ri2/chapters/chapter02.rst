<<<<<<< HEAD
<<<<<<< HEAD
# 2. Reference Implementation Requirements

![State](../figures/bogo_ifo.png)
=======
# Reference Implementation Requirements
<<<<<<< HEAD
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>
>>>>>>> 355bf2ba ([RI2] cleanup of markdown for upcoming conversion)
=======
![Scope](../figures/bogo_ifo.png)
>>>>>>> 339390ea ([RI2] replacing HTML tags with markdown)
=======
Reference Implementation Requirements
=====================================
>>>>>>> f8660d8b ([RI2] Converting markdown to rst after cleanup)

Introduction
------------

This chapter will use the requirements defined in the Kubernetes Reference
Architecture and only make additional entries in
`Section `2.3 <./chapter02.html#reference-architecture-specification>`__
if there are additional requirements needed for this Reference Implementation.

Definitions
-----------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
<<<<<<< HEAD
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC2119](https://www.ietf.org/rfc/rfc2119.txt).

## Reference Architecture Specification

| RA2 Section | RA2 Reference  | Specification | Requirement for Basic Profile | Requirement for Network Intensive Profile | RI2 Traceability |
|---|---|---|---|---|---|
<<<<<<< HEAD
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.001`|Huge pages|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.002`|SR-IOV Capable NICs|Not required|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.003`|SR-IOV Virtual Functions|Not required|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.004`|CPU Simultaneous Multi-Threading (SMT)|True|True|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.006`|CPU Allocation Ratio - Pods|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.008`|Physical CPU Quantity|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.009`|Physical Storage|Should support|Should support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.010`|Local Filesystem Storage Quantity|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.012`|Kubernetes Node RAM Quantity|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.013`|Physical NIC Quantity|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.014`|Physical NIC Speed - Basic Profile|Must support|N/A|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.015`|Physical NIC Speed - Network Intensive Profile|N/A|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.017`|Immutable Infrastructure|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.3 Kubernetes](../../../ref_arch/kubernetes/chapters/chapter04.md#43-kubernetes)|`ra2.k8s.001`|Kubernetes Conformance|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.3 Kubernetes](../../../ref_arch/kubernetes/chapters/chapter04.md#43-kubernetes)|`ra2.k8s.002`|Highly available etcd|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.3 Kubernetes](../../../ref_arch/kubernetes/chapters/chapter04.md#43-kubernetes)|`ra2.k8s.005`|Kubernetes API Version|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.3 Kubernetes](../../../ref_arch/kubernetes/chapters/chapter04.md#43-kubernetes)|`ra2.k8s.006`|NUMA Support|Not required|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.4 Container runtimes](../../../ref_arch/kubernetes/chapters/chapter04.md#44-container-runtimes)|`ra2.crt.001`|Conformance with OCI 1.0 runtime spec|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.4 Container runtimes](../../../ref_arch/kubernetes/chapters/chapter04.md#44-container-runtimes)|`ra2.crt.002`|Kubernetes Container Runtime Interface (CRI)|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.001`|Centralised network administration|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.002`|Default Pod Network - CNI|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.003`|Multiple connection points|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.004`|Multiple connection points presentation|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.005`|Multiplexer/meta-plugin|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.006`|Multiplexer/meta-plugin CNI Conformance|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.007`|Multiplexer/meta-plugin CNI Plugins|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.008`|SR-IOV Device Plugin for Network Intensive|Not required|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.009`|Multiple connection points with multiplexer/meta-plugin|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.010`|User plane networking|Not required|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#45-networking-solutions)|`ra2.ntw.012`|Optional Device Plugins|Not required|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|

## 2.3 Reference Implementation Requirements
=======
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.001`|Huge Pages|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.002`|SR-IOV Capable NICs|Not required|Must support|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.003`|SR-IOV Virtual Functions|Not required|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.004`|CPU Simultaneous Multi-Threading (SMT)|True|True|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.006`|CPU Allocation Ratio - Pods|Must support|Must support|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.008`|Physical CPU Quantity|Must support|Must support|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.009`|Physical Storage|Should support|Should support|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.010`|Local Filesystem Storage Quantity|Must support|Must support|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.012`|Kubernetes Node RAM Quantity|Must support|Must support|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.013`|Physical NIC Quantity|Must support|Must support|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.014`|Physical NIC Speed - Basic Profile|Must support|N/A|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.015`|Physical NIC Speed - Network Intensive Profile|N/A|Must support|[3.3](./chapter03.md#infrastructure-requirements)|
|[4.2 Kubernetes Node](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes-node)|`ra2.ch.017`|Immutable Infrastructure|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.3 Kubernetes](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes)|`ra2.k8s.001`|Kubernetes Conformance|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.3 Kubernetes](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes)|`ra2.k8s.002`|Highly available etcd|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.3 Kubernetes](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes)|`ra2.k8s.005`|Kubernetes API Version|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.3 Kubernetes](../../../ref_arch/kubernetes/chapters/chapter04.md#kubernetes)|`ra2.k8s.006`|NUMA Support|Not required|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.4 Container runtimes](../../../ref_arch/kubernetes/chapters/chapter04.md#container-runtimes)|`ra2.crt.001`|Conformance with OCI 1.0 runtime spec|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.4 Container runtimes](../../../ref_arch/kubernetes/chapters/chapter04.md#container-runtimes)|`ra2.crt.002`|Kubernetes Container Runtime Interface (CRI)|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.001`|Centralised network administration|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.002`|Default Pod Network - CNI|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.003`|Multiple connection points|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.004`|Multiple connection points presentation|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.005`|Multiplexer/meta-plugin|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.006`|Multiplexer/meta-plugin CNI Conformance|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.007`|Multiplexer/meta-plugin CNI Plugins|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.008`|SR-IOV Device Plugin for Network Intensive|Not required|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.009`|Multiple connection points with multiplexer/meta-plugin|Must support|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.010`|User plane networking|Not required|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|
|[4.5 Networking solutions](../../../ref_arch/kubernetes/chapters/chapter04.md#networking-solutions)|`ra2.ntw.012`|Optional Device Plugins|Not required|Must support|[4.3.1](./chapter04.md#installation-on-bare-metal-infratructure)|

## Reference Implementation Requirements
>>>>>>> 355bf2ba ([RI2] cleanup of markdown for upcoming conversion)

| RI2 Ref # | Category | Sub-category | Description | RI2 Traceability |
|---|---|---|---|---|
||||||
=======
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in `RFC2119 <https://www.ietf.org/rfc/rfc2119.txt>`__.

Reference Architecture Specification
------------------------------------

+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| RA2 Section            | RA2 Reference   | Specification          | Requirement for Basic  | Requirement for        | RI2 Traceability       |
|                        |                 |                        | Profile                | Network Intensive      |                        |
|                        |                 |                        |                        | Profile                |                        |
+========================+=================+========================+========================+========================+========================+
| `4.2 Kubernetes        | ``ra2.ch.001``  | Huge pages             | Must support           | Must support           | `4.3.1                 |
| Node <../.             |                 |                        |                        |                        | <./chapter04.md#       |
| ./../ref_arch/kubernet |                 |                        |                        |                        | installation-on-bare-m |
| es/chapters/chapter04. |                 |                        |                        |                        | etal-infratructure>`__ |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.002``  | SR-IOV Capable NICs    | Not required           | Must support           | `3.3 <./               |
| Node <../.             |                 |                        |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 |                        |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.003``  | SR-IOV Virtual         | Not required           | Must support           | `4.3.1                 |
| Node <../.             |                 | Functions              |                        |                        | <./chapter04.md#       |
| ./../ref_arch/kubernet |                 |                        |                        |                        | installation-on-bare-m |
| es/chapters/chapter04. |                 |                        |                        |                        | etal-infratructure>`__ |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.004``  | CPU Simultaneous       | True                   | True                   | `3.3 <./               |
| Node <../.             |                 | Multi-Threading (SMT)  |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 |                        |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.006``  | CPU Allocation Ratio - | Must support           | Must support           | `3.3 <./               |
| Node <../.             |                 | Pods                   |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 |                        |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.008``  | Physical CPU Quantity  | Must support           | Must support           | `3.3 <./               |
| Node <../.             |                 |                        |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 |                        |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.009``  | Physical Storage       | Should support         | Should support         | `3.3 <./               |
| Node <../.             |                 |                        |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 |                        |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.010``  | Local Filesystem       | Must support           | Must support           | `3.3 <./               |
| Node <../.             |                 | Storage Quantity       |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 |                        |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.012``  | Kubernetes Node RAM    | Must support           | Must support           | `3.3 <./               |
| Node <../.             |                 | Quantity               |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 |                        |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.013``  | Physical NIC Quantity  | Must support           | Must support           | `3.3 <./               |
| Node <../.             |                 |                        |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 |                        |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.014``  | Physical NIC Speed -   | Must support           | N/A                    | `3.3 <./               |
| Node <../.             |                 | Basic Profile          |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 |                        |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.015``  | Physical NIC Speed -   | N/A                    | Must support           | `3.3 <./               |
| Node <../.             |                 | Network Intensive      |                        |                        | chapter03.md#infrastru |
| ./../ref_arch/kubernet |                 | Profile                |                        |                        | cture-requirements>`__ |
| es/chapters/chapter04. |                 |                        |                        |                        |                        |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.2 Kubernetes        | ``ra2.ch.017``  | Immutable              | Must support           | Must support           | `4.3.1                 |
| Node <../.             |                 | Infrastructure         |                        |                        | <./chapter04.md#       |
| ./../ref_arch/kubernet |                 |                        |                        |                        | installation-on-bare-m |
| es/chapters/chapter04. |                 |                        |                        |                        | etal-infratructure>`__ |
| md#kubernetes-node>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.3                   | ``ra2.k8s.001`` | Kubernetes Conformance | Must support           | Must support           | `4.3.1                 |
| Kubernetes             |                 |                        |                        |                        | <./chapter04.md#       |
| <../../../ref_arch/kub |                 |                        |                        |                        | installation-on-bare-m |
| ernetes/chapters/chapt |                 |                        |                        |                        | etal-infratructure>`__ |
| er04.md#kubernetes>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.3                   | ``ra2.k8s.002`` | Highly available etcd  | Must support           | Must support           | `4.3.1                 |
| Kubernetes             |                 |                        |                        |                        | <./chapter04.md#       |
| <../../../ref_arch/kub |                 |                        |                        |                        | installation-on-bare-m |
| ernetes/chapters/chapt |                 |                        |                        |                        | etal-infratructure>`__ |
| er04.md#kubernetes>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.3                   | ``ra2.k8s.005`` | Kubernetes API Version | Must support           | Must support           | `4.3.1                 |
| Kubernetes             |                 |                        |                        |                        | <./chapter04.md#       |
| <../../../ref_arch/kub |                 |                        |                        |                        | installation-on-bare-m |
| ernetes/chapters/chapt |                 |                        |                        |                        | etal-infratructure>`__ |
| er04.md#kubernetes>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.3                   | ``ra2.k8s.006`` | NUMA Support           | Not required           | Must support           | `4.3.1                 |
| Kubernetes             |                 |                        |                        |                        | <./chapter04.md#       |
| <../../../ref_arch/kub |                 |                        |                        |                        | installation-on-bare-m |
| ernetes/chapters/chapt |                 |                        |                        |                        | etal-infratructure>`__ |
| er04.md#kubernetes>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.4 Container         | ``ra2.crt.001`` | Conformance with OCI   | Must support           | Must support           | `4.3.1                 |
| runtimes <../../.      |                 | 1.0 runtime spec       |                        |                        | <./chapter04.md#       |
| ./ref_arch/kubernetes/ |                 |                        |                        |                        | installation-on-bare-m |
| chapters/chapter04.md# |                 |                        |                        |                        | etal-infratructure>`__ |
| container-runtimes>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.4 Container         | ``ra2.crt.002`` | Kubernetes Container   | Must support           | Must support           | `4.3.1                 |
| runtimes <../../.      |                 | Runtime Interface      |                        |                        | <./chapter04.md#       |
| ./ref_arch/kubernetes/ |                 | (CRI)                  |                        |                        | installation-on-bare-m |
| chapters/chapter04.md# |                 |                        |                        |                        | etal-infratructure>`__ |
| container-runtimes>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.001`` | Centralised network    | Must support           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | administration         |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 |                        |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.002`` | Default Pod Network -  | Must support           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | CNI                    |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 |                        |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.003`` | Multiple connection    | Must support           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | points                 |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 |                        |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.004`` | Multiple connection    | Must support           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | points presentation    |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 |                        |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.005`` | M                      | Must support           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | ultiplexer/meta-plugin |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 |                        |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.006`` | M                      | Must support           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | ultiplexer/meta-plugin |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 | CNI Conformance        |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.007`` | M                      | Must support           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | ultiplexer/meta-plugin |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 | CNI Plugins            |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.008`` | SR-IOV Device Plugin   | Not required           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | for Network Intensive  |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 |                        |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.009`` | Multiple connection    | Must support           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | points with            |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 | m                      |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 | ultiplexer/meta-plugin |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.010`` | User plane networking  | Not required           | Must support           | `4.3.1                 |
| solutions <../../../   |                 |                        |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 |                        |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+
| `4.5 Networking        | ``ra2.ntw.012`` | Optional Device        | Not required           | Must support           | `4.3.1                 |
| solutions <../../../   |                 | Plugins                |                        |                        | <./chapter04.md#       |
| ref_arch/kubernetes/ch |                 |                        |                        |                        | installation-on-bare-m |
| apters/chapter04.md#ne |                 |                        |                        |                        | etal-infratructure>`__ |
| tworking-solutions>`__ |                 |                        |                        |                        |                        |
+------------------------+-----------------+------------------------+------------------------+------------------------+------------------------+

.. _reference-implementation-requirements-1:

Reference Implementation Requirements
-------------------------------------

========= ======== ============ =========== ================
RI2 Ref # Category Sub-category Description RI2 Traceability
========= ======== ============ =========== ================
\
========= ======== ============ =========== ================
<<<<<<< HEAD

.. |Scope| image:: ../figures/bogo_ifo.png
>>>>>>> f8660d8b ([RI2] Converting markdown to rst after cleanup)
=======
>>>>>>> c3f5a0a5 ([RI2] removing bogometers)
