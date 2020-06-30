[<< Back](../)

# 4. Operational Runbook
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Prerequisites](#4.2)
* [4.3 Installation of the Reference Implementation](#4.3)
  * [4.3.1 Host Provisioning](#4.3.1)
  * [4.3.2 Kubernetes Provisioning](#4.3.2)
* [4.4 Validation of the Reference Implementation](#4.4)
* [4.5 Automation Tooling](#4.5)

<a name="4.1"></a>
## 4.1 Introduction

This chapter describes the steps to install Kubernetes based Reference Implementation (RI-2). The entire installation is divided into two stages - Host provisioning and Kubernetes provisioning. The host provisioning stage is provided here for information only and can be skipped when using Bare Metal Providers like Packet, etc. The Kubernetes provisioning stage is agnostic to the host provisioning stage, in that there is no dependency between the installer used for the Kubernetes provisioning stage and any tools used in the host provisioning stage.

<a name="4.2"></a>
## 4.2 Prerequisites

Before attempting the installation, please ensure that all requirements described in [Chapter 3](./chapter03.md) are met.
(More details to follow)

<a name="4.3"></a>
## 4.3 Installation of the Reference Implementation

<a name="4.3.1"></a>
### 4.3.1 Host Provisioning

Host provisioning is the operation of preparing a host before the software stack can be installed on them. This includes (and not limited to) installing an operating system, configuring network so that the hosts are reachable via SSH, configuring storage, etc.

A former OPNFV bare-metal provisioner XCI, now referred to as [Cloud Infra Automation Framework](https://docs.nordix.org/submodules/infra/engine/docs/user-guide.html#framework-user-guide) and hosted by Nordix Labs has been used in the host provisioning stage. The mentioned framework uses [Bifrost](https://docs.openstack.org/bifrost/latest/) for provisioning virtual and bare-metal hosts. It performs this automated deployment by using Ansible playbooks and [Ironic](https://docs.openstack.org/ironic/latest/).

Before initiating a deployment, two configuration templates, referred to as POD Descriptor File (PDF) and Installer Descriptor File (IDF) in OPNFV terminology need to be defined. Both PDF and IDF files are modeled as YAML schema.

A PDF is a hardware configuration template that includes hardware characteristics of the jumphost host and the set of compute/controller hosts. For each host, the following characteristics should be defined:
- CPU, disk and memory information
- Remote management parameters
- Network interfaces list including name, MAC address, IP address, link speed

IDF includes information about network information required by the installer. All the networks along with possible VLAN, DNS, and gateway information should be defined here.

More details regarding these descriptor files as well as their schema are very well documented in [RI-1 Chapter 8](../../cntt-ri/chapters/chapter08.md#opnfv-descriptor-files-1).

After filling in the PDF and IDF with correct information, the user needs to generate SSH keypair, add a user to the sudo group and have passwordless sudo enabled. After this the deployment can be initiated by cloning the repo, navigating to the engine directory and running the deploy command

`./deploy.sh -o <OStype>-p file:///<pdf.yaml> -i file:///<idf.yaml> -l provision`

Currently, Ubuntu 18.04 and CentOS 7.8 are supported (default Ubuntu 18.04). Support for other operating systems can be added as well depending on the requirements.

After the hosts have been provisioned successfully, one can set up host networking for Kubernetes and run Kubernetes provisioning tooling from CNF Testbed or Intel’s BMRA playbooks to configure and install k8s and other plugins (Refer 4.3.2)

<a name="4.3.2"></a>
### 4.3.2 Kubernetes Provisioning

For provisioning Kubernetes in the Reference Implementation, existing tools should be used to set up a baseline cluster. The initial goal is to cover at least a subset of the requirements described in the [Reference Architecture 2 (RA-2)](../../../ref_arch/kubernetes), with the possibility of extending the implementation to cover more requirements over time.

Initial efforts have been looking at the features of different installers, which has been used to select a few open source Kubernetes provisioning tools for proof of concept deployments. Common for these tools is the use of Ansible and Helm to assist with deploying Kubernetes, configuring the host and adding additional features and functionality to the cluster. 

Depending on the tool used for provisioning, there are likely configuration parameters that will need to be modified before running the installer:
- Host information (IPs for SSH)
- Cluster information (Master/worker node distribution and datastore)
- CPU isolation (Kernel)
- Memory allocation (Hugepages)
- Network interfaces (PFs/VFs and drivers)
- Additional Kubernetes features (device plugins, CNIs)

Once completed, the cluster must be accessible through the `kubectl` CLI from the master nodes. It is possible to interact with the cluster from a jumphost outside of the cluster by using the kubeconfig file, usually found in `$HOME/.kube/config` on the master nodes. This file can be copied to the jumphost and referenced through the `KUBECONFIG` environment variable, after which the cluster can be managed through `kubectl` from the jumphost.

While the presentation of resources can depend on the specific features and functionality, a good way to start is to check the node status for allocatable resources as follows:
```
kubectl get nodes
kubectl get node <NAME> -o json | jq ".status.allocatable"
```

Resources related to networks are usually handled differently, with the exception of hardware resources which are usually listed under each node. There are two common CNI multiplexers that are both considered for the RI-2, [Multus](https://github.com/intel/multus-cni) and [DANM](https://github.com/nokia/danm). They both provide similar functionlity, but with some differences in how resources are defined, configured and consumed.

For the ongoing proof of concept work related to both RA-2 and RI-2, some of the features specifically aimed at production ready deployments are initially omitted. These features are mostly part of the below topics:
- High availability
- Network infrastucture
- Storage
- Security

As work progresses with the proof of concept it is expected that additional features will be added.

<a name="4.4"></a>
## 4.4 Validation of the Reference Implementation

> Describe the steps to run through to validate the RI.  Will need automated tests available and a simple way to run them.


<a name="4.5"></a>
## 4.5 Automation Tooling

> Describe the automation tooling used and any specific configurations needed.
