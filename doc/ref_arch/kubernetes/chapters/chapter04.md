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

<a name="4.2"></a>
## 4.2 Host OS

> This chapter should describe the requirements for a host os to run the software stack of Reference Architecture 2.

<a name="4.3"></a>
## 4.3 Kubernetes

> This chapter should discuss:
> * The version of version range of Kubernetes and the mandatory components needed for Kubernetes (e.g.: etcd, cadvisor)
> * Which optional features are used and which optional API-s are available
> * Which [alfa or beta features](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) are used

<a name="4.4"></a>
## 4.4 Container runtimes

> This chapter should describe which container runtimes are part of the Reference Architecture.

<a name="4.5"></a>
## 4.5 CNI plugins

The used CNI multiplexer/metapulgin must be [DANM](https://github.com/nokia/danm)
as it provides the possibility to use several other CNI plugins (`req.inf.ntw.16`) and provides an API based solution to administer the networks (`req.inf.ntw.10`) from a central point (`req.inf.ntw.11`).<br>

The following table contains a comparision of relevant features and requirements in Multus and DANM.

| Requirement | Support in Multus | Support in DANM |
|-------------|-------------------|-----------------|
| `req.inf.ntw.01` | Supported | Supported |
| `req.inf.ntw.02` | Supported via an other CNI plugin | Supported via an other CNI plugin |
| `req.inf.ntw.03` | Supported via an other CNI plugin | Supported |
| `req.inf.ntw.04` | Supported via an other CNI plugin | Supported via an other CNI plugin |
| `req.inf.ntw.06` | Supported | Supported |
| `req.inf.ntw.07` | Supported | Supported |
| `req.inf.ntw.08` | Supported | Supported |
| `req.inf.ntw.09` | Supported via LCM tools |  Supported via LCM tools |
| `req.inf.ntw.10` | Not supported | Suported |
| `req.inf.ntw.11` | Not supported | Partially supported |
| `req.inf.ntw.14` | Supported via an other CNI plugin | Supported via an other CNI plugin |
| `req.inf.ntw.15` | Not relevant | Not relevant |
| `req.inf.ntw.16` | Supported | Supported |
| Cluster wide IP address management | Not suported | Supported |
| Service based dicovery of all provisioned interfaces | Not supported | Supported |

 [Calico](https://github.com/projectcalico/cni-plugin) must be used as the CNI what complies with the basic networking assumptions of Kubernetes based on the requirement `req.inf.ntw.02` due to it's capability to handle `NetworkPolicies`, what is missing from [Flannel](https://github.com/coreos/flannel-cni).
For the network of signalling connections the built in IPVLAN CNI of DANM must be used as it provides NAT-less connectivity (`req.inf.ntw.03`). For the user plane network(s) fullfilling requirement `req.inf.ntw.04` the [User Space CNI](https://github.com/intel/userspace-cni-network-plugin) must be used.

> Editors note: The usage SR-IOV in container environments, therefore the inclusion of an SR-IOV CNI plugin to the architecture is under debate.

<a name="4.6"></a>
## 4.5 Storage components

> This chapter should describe the components used to provide storage services by the reference architecture.

<a name="4.7"></a>
## 4.7 Service meshes

No service meshes are part of the architecture.

<a name="4.8"></a>
## 4.8 Kubernetes Application package manager

The reference architecture must support the usage of a Kubernetes Application package manager using the Kubernetes API-s, like [Helm v3](https://v3.helm.sh/).

<a name="4.9"></a>
## 4.9 Supplementary components (okay, this is a bad heading, but I do not have any better)

> This chapter should list all the supplementary components needed to provide the services defined in Chapter 3.2 (e.g: Prometheus)
