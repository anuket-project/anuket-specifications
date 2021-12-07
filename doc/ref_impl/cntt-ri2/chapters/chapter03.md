# 3. Lab Requirements

![State](../figures/bogo_lsf.png) <!-- width="35" -->

## Table of Contents
* [3.1 Introduction](#3.1)
* [3.2 Access and Connectivity](#3.2)
* [3.3 Infrastructure Requirements](#3.3)
* [3.4 Software Requirements](#3.4)



<a name="3.1"></a>
## 3.1 Introduction

The purpose of this chapter is to list and describe the requirements on labs used to deploy and run the RI2. Overall, the RI2 serves the following purposes which guide the definition of requirements in this chapter:

1. RI2 is an implementation of and a proving ground for the [Reference Architecture 2 (RA2) specification](../../../ref_arch/kubernetes). RI2 is verified against RA2 through the [Reference Conformance 2 (RC2) specification](../../../ref_cert/RC2).
1. RI2 will align itself with the requirements of the Anuket Assured Program.
1. RI2 enables software vendors of CNFs and cloud container platforms to deploy a reference implementation in their environment to develop and validate against.

As a result of these, RI2 must be deployable in different lab environments:

1. internal development labs of software vendors, operators and 3<sup>rd</sup> party test labs
1. public community labs (e.g. Anuket (formerly OPNFV))
1. resources hosted by cloud infrastructure providers (e.g. [Equinix Metal](https://metal.equinix.com/))

In addition, lab environments must meet specific requirements on hardware resources (e.g. compute and storage), capabilities (e.g. support for SR-IOV), and connectivity (e.g., number of NICs) to run the RI2. The following sections describe the resulting requirements in detail.



<a name="3.2"></a>
## 3.2 Access and Connectivity

This section describes the access and connectivity requirements for labs used to deploy an RI.


<a name="3.2.1"></a>
### 3.2.1 Lab Access

The requirements on and means of accessing a given lab differ per hosting organization and use case:

* **Community labs**, such as those hosted by Anuket, must provide remote access from the Internet to allow usage of the lab resources by community members. Remote access shall be managed and secured by means of VPN or SSH gateways. Both the public and out-of-band management networks of the lab shall be accessible from the VPN / SSH gateway host.

* Access to lab resources hosted by **public cloud providers** is managed by the cloud provider.

* Access to **internal development and test labs** of software vendors, operators and 3<sup>rd</sup> party test labs is managed by the corresponding entity and not expected to be available to community members outside of the respective organization.

For all community-focused activities, access to the respective lab infrastructure must be made available to community members through an application process, irrespective of whether the infrastructure is hosted in Anuket labs, 3<sup>rd</sup> party labs or public cloud infrastructure.


<a name="3.2.2"></a>
### 3.2.2 Connectivity

The network topology should provide at least 2 networks with preallocated IP addressing schemes for the out-of-band management network and the Public network. The Public network must be able to reach / access the public Internet, preferably directly or via an enterprise proxy. IPv4 as well as IPv6 addresses must be available. At least 1 network interface must be capable of performing PXE boot and that network must be available to both the jump / test host and each physical or virtual server.

The network fabric shall comprise redundant layer 2 connectivity between hosts. The switching hardware shall support VLANs for separating networks as well as supporting line speeds corresponding to the speeds of the NICs listed below.


<a name="3.3"></a>
## 3.3 Infrastructure Requirements

The requirements on infrastructure hardware used to deploy and run the RI2 are as follows:

1. One (1) physical or virtual server dedicated as a jump / test host
1. Five (5) physical or virtual servers, serving as either master (controller) or compute/worker nodes

The jump / test host allows to install and manage the operation of the RI2. For example, the host can be used to execute the installer software to deploy and configure the RI2 on the other physical or virtual servers. Once installed, the host may be used to run test tools or it may be used to generate test traffic intended for performance measurements. To support the latter, the server provided for the jump / test host shall meet similar hardware requirements as the master (controller) / compute hosts. If the jump host is used only for deployment or execution of functional tests after deployment, a VM with the resources as outlined below is sufficient.

Each server shall meet the following minimum specifications:

* CPU
  *  2x 20 core x86_64 CPUs, for a total of 40 cores (80+ threads with SMT)
* Memory
  * 256 GB RAM
* Storage
  * 1.0 TB SSD
  * Additional bulk storage can be added as HDD
* Network
  * 25Gbps+ network solution
  * Additional NICs/ports (10Gbps+) can be present
  * Ideally at least 2 ports per socket (NUMA)
  * NICs must be SR-IOV capable

Note that the minimum specifications listed above map to the recommended specifications. Additional devices, such as FPGA, GPU, QAT, etc., may also be added depending on the configuration. For more details on the requirements per infrastructure profile, please refer to [RA2 Chapter 2](../../../ref_arch/kubernetes/chapters/chapter02.md).

A virtual jump / test host can be a VM with the following specifications:

* CPU
  *  4x vCPUs x86_64
* Memory
  * 8 GB RAM
* Storage
  * 50GB disk (SSD backed)
* Network Interfaces
  * 1x vNIC (virtio device) for OAM, access to public Kubernetes APIs, and traffic generation
  * 1x vNIC (virtio device) for out-of-band management of physical servers (e.g., IPMI or RedFish for power cycling)



<a name="3.4"></a>
## 3.4 Software Requirements

The following section describes requirements on the installer software of the RI2 and the validation scripts.

The overall installation process should be logically separated in a host provisioning and a Kubernetes installation phase. This serves the purpose to allow deployment of the RI2 on different infrastructures, such as bare-metal private cloud deployments or on public cloud infrastructure providers. By logically separating the installation, the same Kubernetes deployment tooling can be re-used across a variety of infrastructures, thereby enabling re-use of RI2 components.

The RI2 installer shall support deployments without internet connectivity. This allows for air-gapped deployments in internal development and verification labs.

The RI2 installation framework must allow for fully automatic deployment and configuration of RI2 features and components as defined in RA2 (for instance CNI plugins) without manual post-deployment configuration.

All software components that are part of the RI2 installation framework must be open source.
