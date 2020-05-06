[<< Back](../)

# 3. Requirements for Labs
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Introduction](#3.1)
* [3.2 Access and Connectivity](#3.2)
* [3.3 Cloud Infrastructure Software Profile](#3.3)
* [3.4 Cloud Infrastructure Hardware Profile](#3.4)



<a name="3.1"></a>
## 3.1 Introduction

The purpose of this chapter is to list and describe the requirements on labs used to deploy and run the RI2. Overall, the RI2 serves two purposes which guide the definition of requirements in this chapter:

1. RI2 serves as a baseline and proving ground for developing the [Reference Conformance 2 (RC2) specification](../../ref_cert/RC2) as well as the Cloud Native OVP program (LINK), and
1. RI2 enables software vendors of CNFs and cloud container platforms to deploy a reference implementation in their development environment to develop and validate against.

As a result of those two main use cases, RI2 must be deployable in different lab environments:

1. internal development labs of software vendors, operators and 3rd party test labs,
1. public community labs (e.g. OPNFV),
1. resources hosted by cloud infrastructure providers (e.g. Packet.com)

In addition, lab environments must meet specific requirements on hardware resources (e.g. compute and storage), capabilities (e.g. support for SR-IOV), and connectivity (e.g., number of NICs) to run the RI2. The following sections describe the resulting requirements in detail.



<a name="3.2"></a>
## 3.2 Access and Connectivity

This section describes the access and connectivity requirements for labs used to deploy an RI.


<a name="3.2.1"></a>
### 3.2.1 Lab Access

The requirements on and means of accessing a given lab differ per hosting organization and use case:

* **Community labs**, such as those hosted by OPNFV, must provide remote access from the Internet to allow usage of the lab resources by community members. Remote access shall be managed and secured by means of VPN or SSH gateways. Both the public and out-of-band management networks of the lab shall be accessible from the VPN / SSH gateway host.

* Access to lab resources hosted by **public cloud providers** is managed by the cloud provider. If a public cloud provider is chosen to host community-based development resources, access to those resources shall be available to all community members by means of a application process. 

* Access to **internal development and test labs** of software vendors, operators and 3rd party test labs is managed by the corresponding entity and not expected to be available to community members outside of the respective organization.


<a name="3.2.2"></a>
### 3.2.2 Connectivity

The network fabric in the lab must support the following networks:

* Out-of-Band hardware management
* Admin (host OS access)
* Public (external / Internet facing network)
* Private (cluster internal network)
* Storage

The network topology should provide at least 2 networks with preallocated IP addressing schemes for the out-of-band management network and the Public network. The Public network must be able to reach / access the public Internet, preferably directly or via an enterprise proxy. At least IPv4 addresses must be available, ideally IPv6 address space should also be supported. At least 1 network interface must be capable of performing PXE boot and that network must be available to both the jump / test host and each physical or virtual server.

The network fabric shall comprise redundant layer 2 connectivity between hosts. The switching hardware shall support VLANs for separating networks as well as supporting line speeds corresponding to the speeds of the NICs listed below. 


<a name="3.3"></a>
## 3.3 Infrastructure Requirements

The requirements on infrastructure hardware used to deploy and run the RI2 are as follows:

1. One (1) physical or virtual server dedicated as a jump / test host
1. Six (6) physical or virtual servers, serving as either controller or compute/worker nodes

The jump / test host allows to install and manage the operation of the RI2. For example, the host can be used to execute the installer software to deploy and configure the RI2 on the other physical or virtual servers. Once installed, the host may be used to run test tools or it may be used to generate test traffic intended for performance measurements. To support the latter, the server provided for the jump / test host shall meet similar hardware requirements as the controller / compute hosts. If only functional tests are run on the test host after deployment, a VM with fewer resources as outlined below is sufficient.

Each server shall meet the following minimum specifications:

* CPU
  *  2x x86_64 CPU sockets, providing 20 cores each, 40 simultaneous multi-threads (SMT), at 2.2 GHz
* Memory
  * 256 GB RAM
* Storage
  * 1.0 TB SSD via SATA 6 Gbps
* Network Interfaces
  * 4x 10 Gbps Ethernet Ports
  * Out-of-band Management Port (physical server only)



<a name="3.4"></a>
## 3.4 Software Requirements

The following section describes requirements on the installer software of the RI2 and the validation scripts.

The overall installation process should be logically separated in a node provisioning and a Kubernetes installation phase. This serves the purpose to allow deployment of the RI2 on different infrastructures, such as bare-metal private cloud deployments or on public cloud infrastructure providers. By logically separating the installation, the same Kubernetes deployment tooling can be re-used across a variety of infrastructures, thereby enabling re-use of RI2 components.

The RI2 installer shall support deployments without internet connectivity. This allows for air-gapped deployments in internal development and verification labs.

The RI2 installation framework must allow for fully automatic deployment and configuration of RI2 features and components as defined in RA2 (for instance CNI plugins) without manual post-deployment configuration.

All software components that are part of the RI2 installation framework must be open source.
