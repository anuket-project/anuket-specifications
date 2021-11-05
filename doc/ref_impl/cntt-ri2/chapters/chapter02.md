[<< Back](../)

# 2. Reference Implementation Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction](#21-introduction)
  * [2.1.1 Definitions](#211-definitions)
* [2.2 Reference Architecture Specification](#2.2)
* [2.3 Reference Implementation Requirements](#2.3)

## 2.1 Introduction

This chapter will use the requirements defined in the Kubernetes Reference
Architecture and only make additional entries in section [2.3](#2.3) if there
are additional requirements needed for this Reference Implementation.

## 2.1.1 Definitions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC2119](https://www.ietf.org/rfc/rfc2119.txt).

## 2.2 Reference Architecture Specification

| RA2 Section | RA2 Reference  | Specification | Requirement for Basic Profile | Requirement for Network Intensive Profile | RI2 Traceability |
|---|---|---|---|---|---|
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

| RI2 Ref # | Category | Sub-category | Description | RI2 Traceability |
|---|---|---|---|---|
||||||
