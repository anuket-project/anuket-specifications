[<< Back](../../openstack)

# 4. Component Level Architecture
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Host OS](#4.2)
* [4.3 Kubernetes](#4.3)
* [4.4 Container runtimes](#4.4)
* [4.5 CNI plugins](#4.5)
* [4.6 Storage components](#4.6)
* [4.7 Service meshes](#4.7)
* [4.8 Container package managers](#4.8)
* [4.9 Supplementary components](#4.9)

<a name="4.1"></a>
## 4.1 Introduction

This chapter will describe in detail the Kubernetes Reference Architecture in terms of the functional capabilities and how they relate to the Reference Model requirements, i.e. how the infrastructure profiles are delivered and described.

Figure 4-1 below shows the architectural components that are described in the subsequent sections of this chapter.

<p align="center"><img src="../figures/ch04_k8s_architecture.png" alt="Kubernetes Reference Architecture" Title="Kubernetes Reference Architecture" width="65%"/></p>
<p align="center"><b>Figure 4-1:</b> Kubernetes Reference Architecture</p>

<a name="4.2"></a>
## 4.2 Host OS

In order for a Host OS to be compliant with this Reference Architecture it must meet the following requirements:
- A deb/rpm compatible distribution of Linux (this must be used for the master nodes, and can be used for worker nodes).
- Windows Server 2019 (this can be used for worker nodes, but be aware of the [limitations](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#limitations)).
- In order to support `req.gen.cnt.03` and `req.lcm.gen.01` and `req.lcm.adp.04`, the Host OS must be disposable and therefore the configuration of the Host OS (and associated infrastructure such as VM or bare metal server) must be consistent - e.g. the system software and configuration of that software must be identical apart from those areas of configuration that must be different such as IP addresses and hostnames.

<a name="4.3"></a>
## 4.3 Kubernetes

> This chapter should discuss:
> * The version of version range of Kubernetes and the mandatory components needed for Kubernetes (e.g.: etcd, cadvisor)
> * Which optional features are used and which optional API-s are available
> * Which [alfa or beta features](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) are used

- Master node services (e.g. kube-apiserver) and worker node services (e.g. consumer workloads) must be kept separate - i.e. there must be at least one master node, and at least one worker node
- In order to support `req.gen.rsl.01`, `req.gen.rsl.02` and `req.gen.avl.01` a Reference Implementation must:
    - Consist of either three, five or seven nodes running the etcd state database (can be colocated on the master nodes, or can run on separate nodes)
    - At least one master node per availability zone or fault domain to ensure the high availability and resilience of Kubernetes control plane services
    - At least one worker node per availability zone or fault domain to ensure the high availability and resilience of workloads managed by Kubernetes
- Workloads must ***not*** rely on the availability of the master nodes for the successful execution of their functionality (i.e. loss of the master nodes may affect non-functional behaviours such as healing and scaling, but components that are already running will continue to do so without issue)

<a name="4.4"></a>
## 4.4 Container runtimes

In order to support `req.inf.com.03`, the chosen runtime must be compliant with the [Kubernetes Container Runtime Interface (CRI)](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/).  Examples of container runtimes that are compliant with this specification are (note this is not a complete list and in no particular order):
- container-d (with CRI plugin enabled, which it is by default)
- rkt
- Docker CE (via the dockershim, which is currently built in to the kubelet)
- CRI-O
- Frakti

If privileged containers are required (not recommended) then a container runtime that provides additional security isolation is required in order to support `req.sec.gen.01` and `req.sec.gen.04`.  This could be via the use of lightweight virtual machines (e.g. Kata) or alternative sandbox methods (e.g. gVisor).  For more information see the [Security chapter](./chapter06.md).

> To add: details and RA2 specifications relating to runtimes in order to meet RM features and requirements from RM chapters 4 and 5.

<a name="4.5"></a>
## 4.5 CNI plugins

> This chapter should describe which CNI plugins are part of the Rerefence Architecture.

<a name="4.6"></a>
## 4.5 Storage components

> This chapter should describe the components used to provide storage services by the reference architecture.

<a name="4.7"></a>
## 4.7 Service meshes

> This chapter should describe which service meshes are part of the Reference Architecture. For the shake of simplcity this chapter should discuss both the "normal" service meshes and Network Service Mesh.

<a name="4.8"></a>
## 4.8 Kubernetes Application package manager

The reference architecture must support the usage of a Kubernetes Application package manager using the Kubernetes API-s, like [Helm v3](https://v3.helm.sh/).

<a name="4.9"></a>
## 4.9 Supplementary components (okay, this is a bad heading, but I do not have any better)

> This chapter should list all the supplementary components needed to provide the services defined in Chapter 3.2 (e.g: Prometheus)
