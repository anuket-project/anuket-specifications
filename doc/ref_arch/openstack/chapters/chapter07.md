[<< Back](../../openstack)

# 7. Operations and Life Cycle Management
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [7.1 Introduction](#7.1)
* [7.2 NFVI and VIM configuration management ](#7.2)
  * [7.2.1 Provisioning](#7.2.1)
  * [7.2.2 Configuration Management](#7.2.2)
* [7.3 NFVI and VIM Maintenance ](#7.3)
* [7.4 Logging, Monitoring and Analytics ](#7.4)
  * [7.4.1 Logging](#7.4.1)
  * [7.4.2 Monitoring](#7.4.2)
  * [7.4.3 Alerting](#7.4.3)
  * [7.4.4 Logging, Monitoring, and Analytics (LMA) Framework](#7.4.4)

<a name="7.1"></a>
## 7.1 Introduction

To create an Infrastructure as a Service (IaaS) cloud requires the provisioning and deployment of the underlying infrastructure (compute, networking and storage) and deployment, configuration and management of the necessary software on the infrastructure; in the process of deploying the software, configuration of the infrastructure may also need to be performed. 

Instead of deploying the infrastructure components and services manually, the current best practice is to write *code* (infrastructure as a Code, IaC) to define, provision, deploy, configure and manage the IaaS cloud infrastructure and services. IaC tools allows the entire provisioning, configuration and management processes to be automated. The desired state of the infrastructure and services is represented in a set of human readable, machine executable, and version-controlled files. With version control, it is easy to roll back to an older version and have access to the history of all committed changes.

The provisioning of the infrastructure is typically performed by provisioning tools while the deployment of the software and the configuration of the software, and where needed the infrastructure, falls in the domain of configuration management tools. A single tool may support both provisioning and configuration management.

Operators may choose certain paradigms with respect to how they provision and configure their IaaS cloud. These paradigms will drive the selection of the provisioning and configuration tools. In this chapter we will discuss the capabilities of provisioning and configuration management systems; some open source tools may be mentioned but their capabilities are beyond the scope of this chapter. 

##### Procedural versus Declarative code
The procedural style IaC tools require code that specifies how to achieve the desired state. Whilst the declarative style IaC tools require code that specifies the desired state (what not how).  The major difference between the two styles emerges when changes to the desired state are required. In the procedural style, the change is coded in terms of the difference between the desired and current states while in the declarative style the new desired state is specified. In the procedural style since the state difference has to be coded, a new code file has to be created for each change; in the declarative style the existing code file is updated with the new state information. In the declarative style knowledge of the current state is not required. In the procedural style, knowledge of the current state has to be manually figured by tracing the created code files and the order in which they were applied.

##### Mutable versus Immutable infrastructure
In the mutable infrastructure paradigm, software updates are made in place. Over time this can lead to configuration drift where each server becomes slightly different from all other servers. In the immutable infrastructure paradigm, new servers are deployed with the new software version and then the old servers are undeployed.  

<a name="7.2"></a>
## 7.2 NFVI and VIM configuration management
In [Chapter 9.2 Configuration and Lifecycle Management]( https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter09.md#92-configuration-and-lifecycle-management) defines the functions of Configuration and Life Cycle Management (LCM).  To operate and manage a scalable cloud, that minimizes operational costs, requires tools that incorporates systems for automated provisioing and deployment, and managing configurations that ensures the correctness and integrity of the deployed and configured systems. 

<a name="7.2.1"></a>
### 7.2.1. Provisioning 
This section deals with automated provisioning of the cloud infrastructure; for example, provisioning the servers, switches, routers, networking (e.g., subnets, routing tables, load balancers, etc.), databases and all required operating systems (Servers, switches, etc.). 

[OpenStack TripleO]( https://docs.openstack.org/project-deploy-guide/tripleo-docs/latest/index.html) documentation, and similar documentation from OpenStack vendors, delves into great detail on the provisioning of servers (bare metal), deploying and configuring OpenStack services. 

In the [Reference Implementation Chapter 06]( https://github.com/cntt-n/CNTT/blob/master/doc/ref_impl/cntt-ri/chapters/chapter06.md) a set of Installer requirements are specified with a couple of Installers (such as Airship and Triple-O) described in  [Reference Implementation Chapter 8.5]( https://github.com/cntt-n/CNTT/blob/master/doc/ref_impl/cntt-ri/chapters/chapter08.md#85-available-installers). It should be noted that systems such as [Airship]( https://www.airshipit.org/) are not only provisioning tools but also a configuration management system. For example, [Airship]( https://readthedocs.org/projects/airship-treasuremap/downloads/pdf/latest/) specifies how to provision and deploy the IaaS, and on how to update configuration including OpenStack services.

For Airship, [Reference Implementation Chapter 8.5.1.1]( https://github.com/cntt-n/CNTT/blob/master/doc/ref_impl/cntt-ri/chapters/chapter08.md#8511-descriptor-file-preparations) specifies the required descriptor files and in [Reference Implementation Chapter 8.5.1.2](https://github.com/cntt-n/CNTT/blob/master/doc/ref_impl/cntt-ri/chapters/chapter08.md#8512-deployment-installer--install-steps) describes the steps to provision the OpenStack based IaaS.  

<a name="7.2.2"></a>
### 7.2.2. Configuration Management
The configuration management system ensures the correctness and integrity of the deployed and configured systems. The tools provide the assurance that the expected software is running with the expected configurations on correctly configured nodes that continue to be configured correctly. 

Configuration Management is composed of the following activities:

- Desired (Target) State: a version of the software and hardware and their configurations. Depending upon the configuration management system these configurations are specified in cookbooks, playbooks, manifests, etc. The configuration specifications in these artefacts is used to configure the different types of nodes, BIOS, operating systems, hypervisor and OpenStack services (through settings within their config files such as nova.conf, etc.).

- Current State: the current configuration of software and hardware as provided by monitoring systems

- State variance mitigation: The CM system, on discovering a variance between the desired and current states, acts to drive the state to the desired state. Each CM system accomplishes the task in different ways.


<a name="7.3"></a>
## 7.3 NFVI and VIM Maintenance

NFVI and VIM Maintenance activities can be classified as
1.	Deployment (or de-deployment) of infrastructure components
1.	NFVI Configuration changes 
1.	VIM Configuration changes 
1.	Version changes (upgrade) of NFVI software (for example, Host Operating System, Hypervisor, etc.)
1.	Version changes of VIM Software (or component services) 

**Deployment (or de-deployment) of infrastructure components** 

In declarative tools, the code with the specified desired state (for example, number of compute servers) is modified to the new desired state. The IaC tool then ensures that the desired state is achieved.
In procedural tools, the step-by-step code to deploy (de-deploy) infrastructure components need to be specified. Existing code can be cloned, and appropriate changes made to get to the desired state.

**Configuration and Version Changes** 

Configuration and Version Changes are made in a similar fashion to the “Deployment of infrastructure components” except that the IaC tools used maybe different.


<a name="7.4"></a>
## 7.4 Logging, Monitoring and Analytics





