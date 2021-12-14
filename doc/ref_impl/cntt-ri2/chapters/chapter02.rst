Reference Implementation Requirements
=====================================

Introduction
------------

This chapter will use the requirements defined in the Kubernetes Reference
Architecture and only make additional entries in
`Section `2.3 <./chapter02.html#reference-architecture-specification>`__
if there are additional requirements needed for this Reference Implementation.

Definitions
-----------

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
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
