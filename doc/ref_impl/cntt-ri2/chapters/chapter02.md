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

| RA2 Section | RA2 Reference  | Specification | Requirement | Requirement for Basic Profile | Requirement for Network Intensive Profile | RI2 Traceability |
|---|---|---|---|---|---|---|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.001`|Huge Pages|It must be possible to enable Huge Pages (2048KiB and 1048576KiB) within the Kubernetes Node OS, exposing schedulable resources `hugepages-2Mi` and `hugepages-1Gi`.|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.002`|SR-IOV Capable NICs|When hosting workloads matching the Network Intensive profile, the physical machines on which the Kubernetes Nodes run must be equipped with NICs that are SR-IOV capable.|Not required|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.003`|SR-IOV Virtual Functions|When hosting workloads matching the Network Intensive profile, SR-IOV virtual functions (VFs) must be created within the Kubernetes Node OS, as the SR-IOV Device Plugin does not manage the creation of these VFs.|Not required|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.004`|CPU Simultaneous Multi-Threading (SMT)|SMT must be enabled in the BIOS on the physical machine on which the Kubernetes Node runs.|True|True|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.006`|CPU Allocation Ratio - Pods|To ensure the CPU allocation ratio between vCPU and physical CPU core is 1:1, the sum of CPU requests and limits by containers in Pod specifications must remain less than the allocatable quantity of CPU resources (i.e. `requests.cpu` < `allocatable.cpu` and `limits.cpu` < `allocatable.cpu`).|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.008`|Physical CPU Quantity|The physical machines on which the Kubernetes Nodes run must be equipped with at least 2 physical sockets, each of at least 20 CPU cores.|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.009`|Physical Storage|The physical machines on which the Kubernetes Nodes run should be equipped with Sold State Drives (SSDs).|Should support|Should support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.010`|Local Filesystem Storage Quantity|The Kubernetes Nodes must be equipped with local filesystem capacity of at least 320GB for unpacking and executing containers. Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.012`|Kubernetes Node RAM Quantity|The Kubernetes Nodes must be equipped with at least 32GB of RAM. Note, extra should be provisioned to cater for any overhead required by the Operating System and any required OS processes such as the container runtime, Kubernetes agents, etc.|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.013`|Physical NIC Quantity|The physical machines on which the Kubernetes Nodes run must be equipped with at least four (4) Network Interface Card (NIC) ports.|Must support|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.014`|Physical NIC Speed - Basic Profile|The NIC ports housed in the physical machines on which the Kubernetes Nodes run for workloads matching the Basic Profile must be at least 10Gbps.|Must support|N/A|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.015`|Physical NIC Speed - Network Intensive Profile|The NIC ports housed in the physical machines on which the Kubernetes Nodes run for workloads matching the Network Intensive profile must be at least 25Gbps.|N/A|Must support|[3.3](./chapter03.md#33-infrastructure-requirements)|
|[4.2 Kubernetes Node](/doc/ref_arch/kubernetes/chapters/chapter04.md#42-kubernetes-node)|`ra2.ch.017`|Immutable Infrastructure|Whether physical or virtual machines are used, the Kubernetes Node is not changed after it is made ready for use. New changes to the Kubernetes Node are rolled out as new instances. This covers any changes from BIOS through Operating System to running processes and all associated configurations.|Must support|Must support|[4.3.1](./chapter04.md#431-installation-on-bare-metal-infratructure)|

## 2.3 Reference Implementation Requirements

| RI2 Ref # | Category | Sub-category | Description | RI2 Traceability |
|---|---|---|---|---|
||||||
