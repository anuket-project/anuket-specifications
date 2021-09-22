[<< Back](../../openstack)

# 7. Operations and Life Cycle Management
<p align="right"><img src="../figures/bogo_sdc.png" alt="Still Developing Content" title="Bogo: Still Developing Content" width="35%"/></p>

## Table of Contents
* [7.1 Introduction ](#7.1)
  * [Procedural versus Declarative code](#7.1.1)
  * [Mutable versus Immutable infrastructure](#7.1.2)
* [7.2 Cloud Infrastructure and VIM configuration management ](#7.2)
  * [7.2.1 Provisioning](#7.2.1)
  * [7.2.2 Configuration Management](#7.2.2)
* [7.3 Cloud Infrastructure and VIM Maintenance ](#7.3)
* [7.4 Logging, Monitoring and Analytics ](#7.4)
  * [7.4.1 Logging](#7.4.1)
  * [7.4.2 Monitoring](#7.4.2)
  * [7.4.3 Alerting](#7.4.3)
  * [7.4.4 Logging, Monitoring, and Analytics (LMA) Framework](#7.4.4)



<a name="7.1"></a>
## 7.1 Introduction
To create an Infrastructure as a Service (IaaS) cloud requires the provisioning and deployment of the underlying infrastructure (compute, networking and storage) and deployment, configuration and management of the necessary software on the infrastructure; in the process of deploying the software, configuration of the infrastructure may also need to be performed. 

Instead of deploying the infrastructure components and services manually, the current best practice is to write *code* (Infrastructure as Code, IaC - see section 7.4.4 below) to define, provision, deploy, configure and manage the IaaS cloud infrastructure and services. IaC tools allow the entire provisioning, configuration and management processes to be automated. The desired state of the infrastructure and services is represented in a set of human readable, machine executable, and version-controlled files. With version control, it is easy to roll back to an older version and have access to the history of all committed changes.

The provisioning of the infrastructure is typically performed by provisioning tools while the deployment of the software and the configuration of the software, and where needed the infrastructure, falls in the domain of configuration management tools. A single tool may support both provisioning and configuration management.

Operators may choose certain paradigms with respect to how they provision and configure their IaaS cloud. These paradigms will drive the selection of the provisioning and configuration tools. In this chapter we will discuss the capabilities of provisioning and configuration management systems; some open-source tools may be mentioned but their capabilities are beyond the scope of this chapter. 

<a name="7.1.1"></a>
### 7.1.1 Procedural versus Declarative code
The procedural style IaC tools require code that specifies how to achieve the desired state. Whilst the declarative style IaC tools require code that specifies the desired state (what not how).  The major difference between the two styles emerges when changes to the desired state are required. In the procedural style, the change is coded in terms of the difference between the desired and current states while in the declarative style the new desired state is specified. In the procedural style since the state difference has to be coded, a new code file has to be created for each change; in the declarative style the existing code file is updated with the new state information. In the declarative style knowledge of the current state is not required. In the procedural style, knowledge of the current state has to be manually figured by tracing the created code files and the order in which they were applied.

<a name="7.1.2"></a>
### 7.1.2 Mutable versus Immutable infrastructure
In the mutable infrastructure paradigm, software updates are made in place. Over time this can lead to configuration drift where each server becomes slightly different from other servers. In the immutable infrastructure paradigm, new servers are deployed with the new software version and then the old servers are undeployed. 

<a name="7.2"></a>
## 7.2 Cloud Infrastructure and VIM configuration management
In the Reference Model, [Chapter 9 Configuration and Lifecycle Management]( ../../../ref_model/chapters/chapter09.md#92-configuration-and-lifecycle-management) defines the functions of Configuration and Life Cycle Management (LCM).  To operate and manage a scalable cloud, that minimises operational costs, requires tools that incorporate systems for automated provisioning and deployment, and managing configurations that ensures the correctness and integrity of the deployed and configured systems. 

<a name="7.2.1"></a>
### 7.2.1. Provisioning 
This section deals with automated provisioning of the Cloud Infrastructure; for example, provisioning the servers, switches, routers, networking (e.g., subnets, routing tables, load balancers, etc.), databases and all required operating systems (Servers, switches, etc.). 

The following are the minimum tasks that need to be performed by automation:
- **Pre-boot configuration** such as BIOS/RAID/IPMI settings: Hardware manufacturers typically have their proprietary interface for these tasks but standards such as Redfish are being increasingly utilised. Consider using tooling to ensure consistency across all infrastructure components.
- **Bootloader installation** of base Network Operating System (NOS) on networking equipment or the Operating System (OS) should be performed using PXE; again consider tooling to ensure consistency across all infrastructure components.

**Configuration and subsequent software installation** is then handed over to a configuration management tool or life cycle manager.

[OpenStack TripleO]( https://docs.openstack.org/project-deploy-guide/tripleo-docs/latest/index.html) documentation, and similar documentation from OpenStack vendors, delves into great detail on the provisioning of servers (bare metal), deploying and configuring OpenStack services. 

In the [Reference Implementation Chapter 06]( ../../../ref_impl/cntt-ri/chapters/chapter06.md) a set of Installer requirements are specified with a couple of Installers (such as Airship and Triple-O) described in  [Reference Implementation Chapter 8.5]( ../../../ref_impl/cntt-ri/chapters/chapter08.md#85-available-installers). It should be noted that the installers choosen in order to automate deployment depend on the cloud provider.

Systems such as [Airship]( https://www.airshipit.org/) are not only provisioning tools but also a configuration management system. For example, [Airship]( https://readthedocs.org/projects/airship-treasuremap/downloads/pdf/latest/) specifies how to provision and deploy the IaaS, and on how to update configuration including OpenStack services.

For Airship, [Reference Implementation Chapter 8.5.1.1]( ../../../ref_impl/cntt-ri/chapters/chapter08.md#8511-descriptor-file-preparations) specifies the required descriptor files and in [Reference Implementation Chapter 8.5.1.2](../../../ref_impl/cntt-ri/chapters/chapter08.md#8512-deployment-installer--install-steps) describes the steps to provision the OpenStack based IaaS.  

<a name="7.2.2"></a>
### 7.2.2. Configuration Management
The configuration management system ensures the correctness and integrity of the deployed and configured systems. The tools provide the assurance that the expected software is running with the expected configurations on correctly configured nodes that continue to be configured correctly. 

Configuration Management is composed of the following activities:

- Desired (Target) State: a version of the software and hardware and their configurations. Depending upon the configuration management system these configurations are specified in cookbooks, playbooks, manifests, etc. The configuration specifications in these artefacts are used to configure the different types of nodes, BIOS, operating systems, hypervisor and OpenStack services (through settings within their config files such as nova.conf, etc.).

- Current State: the current configuration of software and hardware as provided by monitoring systems.

- State variance mitigation: The CM system, on discovering a variance between the desired and current states, acts to drive the state to the desired state. Each CM system accomplishes the task in different ways.

<a name="7.3"></a>
## 7.3 Cloud Infrastructure and VIM Maintenance
Cloud Infrastructure and VIM Maintenance activities can be classified as
1.	Deployment of additional infrastructure components (or removal of infrastructure components)
1.	Cloud Infrastructure Configuration changes 
1.	VIM Configuration changes 
1.	Version changes (upgrade) of Cloud Infrastructure software (for example, Host Operating System, Hypervisor, etc.)
1.	Version changes of VIM Software (or component services) 

**Deployment (or removal) of infrastructure components** 

In declarative tools, the code with the specified desired state (for example, number of compute servers) is modified to the new desired state. The IaC tool then ensures that the desired state is achieved.
In procedural tools, the step-by-step code to deploy (remove) infrastructure components needs to be specified. Existing code can be cloned, and appropriate changes made to get to the desired state.

**Configuration and Version Changes** 

Configuration and Version Changes are made in a similar fashion to the “Deployment of infrastructure components” except that the IaC tools used maybe different.


<a name="7.4"></a>
## 7.4 Logging, Monitoring and Analytics
- Logging
- Monitoring 
- Alerting
- Logging, Monitoring, and Analytics (LMA) Framework

<a name="7.4.1"></a>
### 7.4.1. Logging
A log, in the context of computing, is the automatically produced and time-stamped documentation 
of events relevant to a particular system. All software, including operating systems, middleware and 
applications produce log files. 
Enterprises and vendors may have custom monitoring and logging solutions. 
The  logging and monitoring systems capture events and 
data of interest to the Cloud Infrastructure and workloads so that appropriate actions can be taken. For example, 

- Operating systems and web servers maintain an access log of all access requests, session details and file access.
- Databases maintain a transaction log of all transactions executed including any added, changed and deleted data.
- Audit logs record chronological documentation of any activities that may have affected a 
particular operation or event. Data typically includes resources accessed, destination and source 
addresses, and a timestamp and login information for the person who accessed the resources.

Some of the data is to support the metrics collection specified in the [Reference Model Chapter 4: Infrastructure Capabilities, Metrics and Catalogue](../../../ref_model/chapters/chapter04.md).

Logs have multiple operational uses including for:

1. Regulatory Compliance and Security Information and Event Management (SIEM) featuring the automated gathering, analysis and correlation of log data across all systems and devices across an operator to provide real-time analysis, event prioritisation, reporting, notification and alerting
1. Monitoring across systems in real-time to detect particular log events, patterns, anomalies or inactivity to gauge system and application health
1. Identify system and application performance and configuration issues
1. Root cause analysis for system and application failures and errors
1. Ensuring that operational objectives and SLAs are met

<a name="7.4.2"></a>
### 7.4.2. Monitoring
Monitoring is the process of collecting, aggregating, and analyzing values that improve awareness of 
the components' characteristics and behaviour. The data from various parts of the environment are collected 
into a monitoring system that is responsible for storage, aggregation, visualisation, and initiating automated 
responses when the values meet specific threshold.

Monitoring systems fulfill many related functions. Their first responsibility is to accept and store incoming 
and historical data. While values representing the current point in time are useful, it is almost always more 
helpful to view those numbers in relation to past values to provide context around changes and trends. 

<a name="7.4.3"></a>
### 7.4.3. Alerting
Alerting is the responsive component of a monitoring system that performs actions based on changes in metric 
values. Alert definitions are composed of two components: a metrics-based condition or threshold, and an 
action to perform when the values fall outside of the acceptable conditions.

While monitoring systems are incredibly useful for active interpretation and investigation, one of the primary
benefits of a complete monitoring system is letting administrators disengage from the system. Alerts allow the
specification of situations that make sense to actively manage, while relying on the passive monitoring of the 
software to watch for changing conditions.

<a name="7.4.4"></a>
### 7.4.4. Logging, Monitoring, and Analytics (LMA) Framework
In this section, a possible framework utilising Prometheus, Fluentd, Elasticsearch and Kibana is given as an example only.


<p align="center"><img src="../figures/RA1-Ch07-Monitoring-Logging-Framework.png" alt="Monitoring and Logging Framework"><b>
  Figure 7-1: Monitoring and Logging Framework</b> </p>

The monitoring and logging framework (**Figure 7-1**) leverages Prometheus as the monitoring engine and 
Fluentd for logging. In addition, the framework uses Elasticsearch to store and organise logs for easy access. 
Prometheus agents pull information from individual components on every host.  Fluentd, an open-source data 
collector, unifies data collection and consumption for better use and understanding of data. Fluentd captures 
the access, application and system logs.


