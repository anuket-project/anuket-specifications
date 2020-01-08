[<< Back](../)

# 7. Integration
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [7.1 Introduction](#7.1)
* [7.2 Pre-requisites](#7.2)
* [7.3 Requirements Gathering](#7.3)
* [7.4 Access and Connectivity](#7.4)
* [7.5 Descriptor File Preparations](#7.5)
* [7.6 Deployment Installer & Install Steps](#7.6)
* [7.7 Deployment Validations](#7.7)
* [7.8 CICD Tool Chain (use of, process, and scripts)](#7.8)
* [7.9 Jenkins Setup & Job Creation](#7.9)
* [7.10 Compliance Validation (steps, process)](#7.10)
 
<a name="7.1"></a>
## 7.1 Introduction

This chapter provides general installation procedures for laboratory integrated components. The installation steps include the general installation process of deploying k8s on the Openstack cloud environment and deploying ONAP using OOM.

<a name="7.2"></a>
## 7.2 Prerequisites

The following are pre-requisites to be completed in advance of software deployments:

1.  Bare-metal validations: confirming delivery, rack, stack, of env and that env is "ready" for software deployments (e.g. BIOS, firmware, boot order, health, disk config, port / socket validations, MAC/NIC status, etc)

<a name="7.3"></a>
## 7.3 Requirements Gathering

Requirements gathering processes and steps:

1.  RA Requirements Gathering process
2.  Infra Requirements and Selection Process

<a name="7.4"></a>
## 7.4 Access & Connectivity

Logical steps for lab access and connectivity.

Sample steps provided mimic those utilized for POD10 test lab access.

<a name="7.5"></a>
## 7.5 Descriptor File Preparations

We use OpenStack VMs to host the Highly-Available Kubernetes Workers and the following will use several virtual machines as nodes to deploy a kubernetes cluster on the Openstack cloud.
Recommended virtual machine cluster hardware requirements are provided below.
 OOM Hardware Requirements
 
 RAM| HD	|vCores	| Ports
 ---| ---|------ | ----
224GB|2100GB|112	|0.0.0.0/0 (all open)

* Note: this is for a full ONAP deployment (all components). Customizing ONAP to deploy only components that are needed will drastically reduce the requirements.

Based on all hardware resource requirements, we allocate all hardware resources to 3 master nodes and 5 compute nodes.
1.	Three(3) Master servers : 8 core 16G RAM  disk 200G
A group of processes related to cluster management, such as etcd, API Server, Controller Manager, and Scheduler, are running on the Master node. These processes implement the resource management, Pod scheduling, elastic scaling, security control, and system monitoring functions of the entire cluster, and they are all completed automatically.
2.	Five (5) Compute servers : 16 core 32G RAM  disk 200G
Kubelet, Proxy, and Docker daemon are running on each Node. They are responsible for managing the life cycle of the Pod on this node and implementing the function of service proxy.
3.	NFS server : 4core 8G RAM 		disk 500G

A complete ONAP needs to meet the following requirements:

Docker|	Kubernetes	|Helm	|kubectl	|ONAP	|RKE
 -----| -----------|------ | -----|----|----
18.09.x	|1.15.2|	2.14.2|	1.15.2|	el alto	|0.2.1

<a name="7.6"></a>
## 7.6 Deployment Installer & Install Steps
### 7.6.1 Configure Rancher Kubernetes Engine (RKE)
Install RKE
Download and install RKE on a VM，RKE requires a “cluster.yml” as input. “cluster.yml” describes a Kubernetes cluster that will be mapped onto the OpenStack VMs created earlier in this guide.
* Prepare cluster.yml
Before this configuration file can be used the external address and the internal_address must be mapped for each control and worker node in this file.
 For example claster.yml
* Run RKE
From within the same directory as the cluster.yml file, simply execute:

`> rke up` 

**Install Kubectl**

* Validate deployment

 `> cp kube_config_cluster.yml ~/.kube/config.onap`

 `> export KUBECONFIG=~/.kube/config.onap`

 `> kubectl config use-context onap`

`> kubectl get nodes -o=wide`

**Install Helm**

Example Helm client install on Linux:

`> wget http://storage.googleapis.com/kubernetes-helm/helm-v2.14.2-linux-amd64.tar.gz`

`> tar -zxvf helm-v2.14.2-linux-amd64.tar.gz`

`> sudo mv linux-amd64/helm /usr/local/bin/helm`

* Initialize Kubernetes Cluster for use by Helm

`> kubectl -n kube-system create serviceaccount tiller`

`> kubectl create clusterrolebinding tiller --clusterrole=cluster-admin --serviceaccount=kube-system:tiller`

`> helm init --service-account tiller`

`> kubectl -n kube-system  rollout status deploy/tiller-deploy`

**Setting up an NFS share for Multinode Kubernetes Clusters**

 Deploying applications to a Kubernetes cluster requires Kubernetes nodes to share a common, distributed filesystem. In this tutorial, we will setup an NFS Master, and configure all Worker nodes a Kubernetes cluster to play the role of NFS slaves.
It is recommneded that a separate VM, outside of the kubernetes cluster, be used. This is to ensure that the NFS Master does not compete for resources with Kubernetes Control Plane or Worker Nodes.

* Apply customization script for NFS Server VM

**ONAP Deployment via OOM**

OOM deploys and manages ONAP on a pre-established Kubernetes cluster.
Once a kubernetes environment is available, follow the following instructions to deploy ONAP.

Step 1. Clone the OOM repository from ONAP gerrit:

`> git clone -b <BRANCH> http://gerrit.onap.org/r/oom --recurse-submodules`
`> cd oom/kubernetes` 

where <BRANCH> can be an offical release tag, such as 4.0.0-ONAP for Dublin 5.0.1-ONAP for El Alto.

Step 2. Install Helm Plugins required to deploy ONAP:

`> sudo cp -R ~/oom/kubernetes/helm/plugins/ ~/.helm` 
 
 Step 3. Customize the helm charts like oom/kubernetes/onap/values.yaml or an override file like onap-all.yaml, onap-vfw.yaml or openstack.yaml file to suit your deployment with items like the OpenStack tenant information.
 
 Step 4. To setup a local Helm server to server up the ONAP charts:
 
 `> helm serve &`
 
 Note the port number that is listed and use it in the Helm repo add as follows:
 
  `> helm repo add local http://127.0.0.1:8879 `
  
 Step 5. Verify your Helm repository setup with:
 
  `> helm repo list `
 `NAME   URL `
 `local  http://127.0.0.1:8879 `

Step 6. Build a local Helm repository (from the kubernetes directory):

`> make all; make onap`

Step 7. Display the onap charts that available to be deployed:

`> helm search onap -l`

NAME      |          	CHART VERSION	|APP VERSION	DESCRIPTION                                 

local/onap     |         	5.0.0     |  	Dublin  Open Network Automation Platform (ONAP)

local/aaf       |        	5.0.0     |          ONAP Application Authorization Framework

local/aai       |          	5.0.0    |    	        ONAP Active and Available Inventory

local/appc      |          	5.0.0      |  	        Application Controller

local/cassandra     |      	5.0.0        	|        ONAP cassandra

local/cds            |     	5.0.0        	  |      ONAP Controller Design Studio (CDS)

local/clamp        |       	5.0.0        	  |      ONAP Clamp

local/cli           |      	5.0.0        	|        ONAP Command Line Interface

local/common      |        	5.0.0       | 	        Common templates for inclusion in other charts

local/consul       |       	5.0.0        	|        ONAP Consul Agent`

Step 8. Once the repo is setup, installation of ONAP can be done with a single command
To deploy all ONAP applications use this command:

`> cd oom/kubernetes`

`> helm deploy dev local/onap --namespace onap -f onap/resources/overrides/onap-all.yaml -f onap/resources/overrides/environment.yaml -f onap/resources/overrides/openstack.yaml --timeout 900`

<a name="7.7"></a>
## 7.7 Deployment Validations

Details explaining:
- Validation Tests Run
- Expected outpus
- Explanation of Pass/Fail
- Disposition, or next steps, based on test results (e.g. handling of failures, handoff to next tier with passing results)

<a name="7.8"></a>
## 7.8 CICD Tool Chain (use of, process, and scripts)]

Placeholder to describe the CICD tool chain used in RI validations.  

Include flow diagram.

<a name="7.9"></a>
## 7.9 Jenkins Setup & Job Creation

Placeholder to describe the process, access, steps, instance, etc, information for the setup of Jenkins, the jobs required for validation, and the results dashboard.

<a name="7.10"></a>
## 7.10 Compliance Validation (steps, process)

Placholder to describe the purpose, steps, and process, using the Jenkins Jobs, Tool Chain, and Test Case requirements mapping to perform validations.  
