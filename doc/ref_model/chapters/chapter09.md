[<< Back](../../ref_model)
# 9 Infrastructure Operations and Lifecycle Management


## Table of Contents
* [9.1 Introduction](#9.1)
* [9.2 Configuration and Lifecycle Management](#9.2)
* [9.3 Assurance](#9.3)
* [9.4 Capacity Management](#9.4)
* [9.5 Automation](#9.5)
  * [9.5.1 Infrastructure LCM Automation](#9.5.1)
  * [9.5.2 Software Onboarding Automation and CI/CD Requirements](#9.5.2)
  * [9.5.3 Tenant creation automation](#9.5.3)
* [9.6 Telemetry and Observability]

<a name="9.1"></a>
## 9.1 Introduction

The purpose of this chapter is to define the capabilities required of the infrastructure to ensure it is effectively supported, maintained and otherwise lifecycle-managed by Operations teams.  This includes requirements relating to the need to be able to maintain infrastructure services "in-service" without impacting the applications and workloads, whilst minimising human labour. It shall also capture any exceptions and related assumptions.

There are three main business operating frameworks that are commonly known and used across the Telecommunications industry related to the topics in this chapter:
- FCAPS (ISO model for network management)
- eTOM (TM Forum Business Process Framework (eTOM))
- ITIL (ITIL 4.0 attempts to adapt IT Service Management practices to the cloud environment needs)

The chapters below roughly map to these frameworks as follows:
| Chapter Name | FCAPS | eTOM | ITIL |
| --- | --- | --- | --- |
| Configuration and Lifecycle Management | Configuration | Fulfilment |Configuration, Release, Change |
| Assurance | Performance, Fault | Assurance |Event, Incident |
| Capacity Management | Configuration | Fulfilment |Capacity Management|

<a name="9.2"></a>

> **Note:**  The above mapping is provided for the general orientation purpose only.  Detailed mapping of the required Cloud Infrastructure Lifecycle Management capabilities to any of these frameworks is beyond the scope of this document.

## 9.2 Configuration and Lifecycle Management

Configuration management is concerned with defining the configuration of infrastructure and its components, and tracking (observing) the running configuration of that infrastructure, and any changes that take place. Modern configuration management practices such as desired state configuration management also mean that any changes from the desired state that are observed (aka the delta) are rectified by an orchestration / fulfilment component of the configuration management system. This "closed loop" mitigates against configuration drift in the infrastructure and its components. Our recommendation is to keep these closed loops as small as possible to reduce complexity and risk of error. Figure 9-1 shows the configuration management "loop" and how this relates to lifecycle management.

<p align="center"><img src="../figures/ch09_config_mgmt.png" alt="Configuration and Lifecycle Management" title="Configuration and Lifecycle Management" width="65%"/></p>
<p align="center"><b>Figure 9-1:</b> Configuration and Lifecycle Management</p>

The initial desired state might be for 10 hosts with a particular set of configuration attributes, including the version of the hypervisor and any management agents. The configuration management system will take that as input (1) and configure the infrastructure as required (2). It will then observe the current state periodically over time (3) and in the case of a difference between the desired state and the observed state it will calculate the delta (4) and re-configure the infrastructure (5). For each lifecycle stage (create, update, delete) this loop takes place - for example if an update to the hypervisor version is defined in the desired state, the configuration management system will calculate the delta (e.g. v1 --> v2) and re-configure the infrastructure as required.

However, the key requirements for the infrastructure and infrastructure management are those interfaces and reference points in the red box - where configuration is **set**, and where it is **observed**. Table 9-2 lists the main components and capabilities required in order to manage the configuration and lifecycle of those components.


<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>set / observe</th>
      <th>Capability</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan=6>Cloud Infrastructure Management Software</td>
      <td rowspan=3>Set</td>
      <td>Target software / firmware version</td>
      <td>Software: v1.2.1</td>
    </tr>
    <tr>
      <td>Desired configuration attribute</td>
      <td>dhcp_lease_time: 86400</td>
    </tr>
    <tr>
      <td>Desired component quantities</td>
      <td># hypervisor hosts: 10</td>
    </tr>
    <tr>
      <td rowspan=3>Observe</td>
      <td>Observed software / firmware version</td>
      <td>Software: v1.2.1</td>
    </tr>
    <tr>
      <td>Observed configuration attribute</td>
      <td>dhcp_lease_time: 86400</td>
    </tr>
    <tr>
      <td>Observed component quantities</td>
      <td># hypervisor hosts: 10</td>
    </tr>
    <tr>
      <td rowspan=6>Cloud Infrastructure Software</td>
      <td rowspan=3>Set</td>
      <td>Target software version</td>
      <td>Hypervisor software: v3.4.1</td>
    </tr>
    <tr>
      <td>Desired configuration attribute</td>
      <td>management_int: eth0</td>
    </tr>
    <tr>
      <td>Desired component quantities</td>
      <td># NICs for data: 6</td>
    </tr>
    <tr>
      <td rowspan=3>Observe</td>
      <td>Observed software / firmware version</td>
      <td>Hypervisor software: v3.4.1</td>
    </tr>
    <tr>
      <td>Observed configuration attribute</td>
      <td>management_int: eth0</td>
    </tr>
    <tr>
      <td>Observed component quantities</td>
      <td># NICs for data: 6</td>
    </tr>
    <tr>
      <td rowspan=4>Infrastructure Hardware</td>
      <td rowspan=2>Set</td>
      <td>Target software / firmware version</td>
      <td>Storage controller firmware: v10.3.4</td>
    </tr>
    <tr>
      <td>Desired configuration attribute</td>
      <td>Virtual disk 1: RAID1 [HDD1, HDD2]</td>
    </tr>
    <tr>
      <td rowspan=2>Observe</td>
      <td>Observed software / firmware version</td>
      <td>Storage controller firmware: v10.3.4</td>
    </tr>
    <tr>
      <td>Observed configuration attribute</td>
      <td>Virtual disk 1: RAID1 [HDD1, HDD2]</td>
    </tr>
  </tbody>
</table>
<p align="center"><b>Table 9-2:</b> Configuration and Lifecycle Management Capabilities</p>

This leads to the following table (Table 9-3) which defines the standard interfaces that should be made available by the infrastructure and Cloud Infrastructure Management components to allow for successful Configuration Management.

| Component | Interface Standard | Link |
| --- | --- | --- |
| Infrastructure Management | Defined in RA specifications | RA-1, RA-2 |
| Infrastructure Software | Defined in RA specifications | RA-1, RA-2 |
| Infrastructure Hardware | Redfish API | DMTF RedFish specification [11] |

<p align="center"><b>Table 9-3:</b> Interface Standards for Configuration Management</p>

<a name="9.3"></a>
## 9.3 Assurance

Assurance is concerned with:
- The proactive and reactive maintenance activities that are required to ensure infrastructure services are available as per defined performance and availability levels.
- Continuous monitoring of the status and performance of individual components and of the service as a whole.
- Collection and analysis of performance data, which is used to identify potential issues including the ability to resolve the issue with no customer impact.

There are the following requirement types:
1. Data collection from all components, e.g.
    - The ability to collect data relating to events (transactions, security events, physical interface up/down events, warning events, error events, etc.)
    - The ability to collect data relating to component status (up/down, physical temperature, disk speed, etc.)
    - The ability to collect data relating to component performance (used CPU resources, storage throughput, network bandwidth in/out, API transactions, transaction response times, etc.)
2. Capabilities of the Infrastructure Management Software to allow for in-service maintenance of the Infrastructure Software and Hardware under its management, e.g.
    - The ability to mark a physical compute node as being in some sort of "maintenance mode" and for the Infrastructure Management Software to ensure all running workloads are moved off or rescheduled on to other available nodes (after checking that there is sufficient capacity) before marking the node as being ready for whatever maintenance activity needs to be performed
    - The ability to co-ordinate, automate, and allow the declarative input of in-service software component upgrades - such as internal orchestration and scheduler components in the Infrastructure Management Software

Note that the above only refers to components - it is expected that any "service" level assurance doesn't add any further requirements onto the infrastructure, but rather takes the data extracted and builds service models based on the knowledge it has of the services being offered.

<a name="9.4"></a>
## 9.4 Capacity Management

Capacity Management is a potentially wide ranging process that includes taking demand across lines of business, analysing data about the infrastructure that is running, and calculating when additional infrastructure might be required, or when infrastructure might need to be decommissioned.

As such the requirements for Capacity Management on the infrastructure are covered by the Assurance and Configuration and Lifecycle Management sections above. The Assurance section deals with the collection of data - there is no reason to consider that this would be done by a different mechanism for Capacity Management as it is for Assurance - and the Configuration and Lifecycle Management section deals with the changes being made to the infrastructure hardware, software, and management components (e.g. changing of number of hypervisor hosts from 10 to 12).

<a name="9.5"></a>
## 9.5 Automation

<a name="9.5.1"></a>
### 9.5.1 Infrastructure LCM Automation

<a name="9.5.1.1"></a>
#### 9.5.1.1. Hardware Configuration CI/CD

<a name="9.5.1.1"></a>
#### 9.5.1.2. Networking Automation

<a name="9.5.1.1"></a>
#### 9.5.1.3. Software Development CI/CD


<a name="9.5.2"></a>
### 9.5.2 Software Onboarding Automation and CI/CD Requirements

<a name="9.5.2.1"></a>
#### 9.5.2.1 Software Onboarding Automation
For software deployment, as far as Cloud Infrastructure services or workloads are concerned, automation is the core of DevOps concept. Automation allows to eliminate manual processes, reducing human errors and speeding software deployments. The prerequisite is to install CI/CD tools chain to:
- Build, package, test application/software
- Store environment's parameters and configurations
- Automate the delivery and deployment
 
The CI/CD pipeline is used to deploy, test and update the Cloud Infrastructure services, and also to onboard workloads hosted on the infrastructure. Typically, this business process consists of the following key phases:
1. Tenant Engagement and Software Evaluation:
    - In this phase the request from the tenant to host a workload on the Cloud Infrastructure platform is assessed and a decision made on whether to proceed with the hosting request.
    - If the Cloud infrastructure software needs to be updated or installed, an evaluation is made of the impacts (including to tenants) and if it is OK to proceed 
    - This phase may also involve the tenant accessing a pre-staging environment to perform their own evaluation and/or pre-staging activities in preparation for later onboarding phases.
2. Software Packaging:
    - The main outcome of this phase is to produce the software deployable image and the deployment manifests (such as TOSCA blueprints or HEAT templates or Helm charts) that will define the Cloud Infrastructure service attributes. 
    - The software packaging can be automated or performed by designated personnel, through self-service capabilities (for tenants) or by the Cloud Infrastructure Operations team.
3. Software Validation and Certification:
    - In this phase the software is deployed and tested to validate it against the service design and other Operator specific acceptance criteria, as required.
    - Software validation and certification should be automated using CI/CD toolsets / pipelines and Test as a Service (TaaS) capabilities.
4. Publish Software:
    - Tenant Workloads: After the software is certified the final onboarding process phase is for it to be published to the Cloud Infrastructure production catalogue from where it can be instantiated on the Cloud Infrastructure platform by the tenant.
    - Cloud Infrastructure software: After the software is certified, it is scheduled for deployment inconcurrence with the user community.
    
All phases described above can be automated using technology specific toolsets and procedures.  Hence, details of such automation are left for the technology specific Reference Architecture and Reference Implementation specifications.

<a name="9.5.2.2"></a>
#### 9.5.2.2 Software CI/CD Requirements
The requirements including for CI/CD for ensuring software security scans, image integrity checks, OS version checks, etc. prior to deployment, are listed in the Table 9-4 (below). Please note that the tenant processes for application LCM (such as updates) are out of scope. For the purpose of these requirements, CI includes Continuous Delivery, and CD refers to Continuous Deployment.

Ref # | Description | Comments/Notes
---|---|---
auto.cicd.001 | The CI/CD pipeline must support deployment on any cloud and cloud infrastructures including different hardware accelerators. | CI/CD pipelines automate CI/CD best practices into repeatable workflows for integrating code and configurations into builds, testing builds including validation against design and operator specific criteria, and delivery of the product onto a runtime environment.<br>Example of an open-source cloud native CI/CD framework is the Tekton project (https://tekton.dev/)
auto.cicd.002 | The CI/CD pipelines must use event-driven task automation | 
auto.cicd.003 | The CI/CD pipelines should avoid scheduling tasks | 
auto.cicd.004 | The CI/CD pipeline is triggered by a new or updated software release being loaded into a repository | The software release cane be source code files, configuration files, images, manifests.<br>Operators may support a single or multiple repositories and may, thus, specify which repository is to be used for these release.<br>An example, of an open source repository is the CNCF Harbor (https://goharbor.io/)
auto.cicd.005 | The CI pipeline must scan source code and manifests to validate for compliance with design and coding best practices. | 
auto.cicd.006 | The CI pipeline must support build and packaging of images and deployment manifests from source code and configuration files. | 
auto.cicd.007 | The CI pipeline must scan images and manifests to validate for compliance with security requirements.  | Refer to RM Chapter 07 (https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter07.md#79-consolidated-security-requirements).<br>Examples of such security requirements include only ingesting images, source code, configuration files, etc. only form trusted sources.
auto.cicd.008 | The CI pipeline must validate images and manifests | Example, different tests
auto.cicd.009 | The CI pipeline must validate with all hardware offload permutations and without hardware offload | 
auto.cicd.010 | The CI pipeline must promote validated images and manifests to be deployable. | Example, promote from a development repository to a production repository
auto.cicd.011 | The CD pipeline must verify and validate the tenant request | Example, RBAC, request is within quota limits, affinity/anti-affinity, …
auto.cicd.012 | The CD pipeline after all validations must turn over control to orchestration of the software | |
auto.cicd.013 | The CD pipeline must be able to deploy into Development, Test and Production environments | |
auto.cicd.014 | The CD pipeline must be able to automatically promote software from Development to Test and Production environments | |

<p align="center"><b>Table 9-4:</b> Automation CI/CD</p>

<a name="9.5.3"></a>
### 9.5.3 Tenant Creation Automation

<a name="9.5.3.1"></a>
#### 9.5.3.1. Pre-tenant Creation Requirements

<a name="9.5.3.2"></a>
#### 9.5.3.2. Tenant Networking Automation


<a name="9.6"></a>
#### 9.6. Telemetry and Observability

Operating complex distributed systems, such as a Telco network, is a demanding and challenging task, that is continuously being increased as the network complexity and the production excellence requirements grow. There are multiple reasons why it is so, but they originate in the nature of the system concept. To reach the ability of providing Telco services, a complex system is decomposed into multiple different functional blocks, called network functions. Internal communication between the diverse network functions of a distributed system is based on message exchange. To formalize this communication, clearly defined interfaces are introduced, and protocols designed. Even though the architecture of a Telco network is systematically formalized on the worldwide level, heterogeneity of services, functions, interfaces, and protocols cannot be avoided. By adding the multi-vendor approach in implementation of Telco networks, the outcome is indeed a system with remarkably high level of complexity which requires significant efforts for managing and operating it.

To ensure proper support and flawless work in the large ecosystem of end user services, a formalized approach directed towards high reliability and scalability of systems is required. The discipline which applies well known practices of software engineering to operations is called Site Reliability Engineering. It was conceived at Google, as a means to overcome missing limitations of the common DevOps approach.

Common supporting system (OSS – Operation Support System, BSS – Business Support System) requirements are redefined, driven by introduction of new technologies in computing infrastructure; modern data centres with abstraction of resources – known as virtualization and cloud computing. This brings many advantages – such as easy scaling, error recovery, reaching a high level of operational autonomy etc., but also many new challenges in the Telecom network management space. Those novel challenges are mostly directed towards the dynamical nature of the system, orientation towards microservices instead of a silo approach, and huge amounts of data which has to be processed in order to understand the internal status of the system. Hence the need of improved ways to monitor systems - observability.


<a name="9.6.1"></a>
#### 9.6.1. Why Observability

Knowing the status of all services and functions at all levels in a cloud based service offering is essential to act fast, ideally pro-actively before users notice and most importantly, before they call the help desk. This requires to collect alarms and telemetry data from the physical layer (wires), the cloud infrastructure up to the network, application and services virtualized functions (VNF) running on top of Cloud Infrastructure, typically isolated by tenants.		

Long term trending data are essential for capacity planning purposes and typically collected, aggregated and kept over the full lifespan. To keep the amount of data collected manageable, automatic data reduction algorithms are typically used, e.g. by merging data points from the smallest intervals to more granular intervals.

A cloud typically consists of one or more regional data centers, central offices, and edge sites. These are managed from redundant central management sites, each hosted in their own data centers.

While many Telco Clouds start as a vertical cloud by hosting one prime application, e.g. IMS, the intent is to host more applications over time in order to truly maximize the cloud to its full potential. Therefore it is pure coincidence to have the same team responsible and manage the infrastructure and the application running on top. Network services and applications deployed on a Telco Cloud are managed by separate teams, within the same or different organizations and a monitoring solution must be capable of keeping the collection of monitoring data isolated between tenants and NFVI. At the same time, some monitoring data from the NFVI layer must selectively be available to tenant monitoring applications in order to correlate e.g. VNF metrics with the underlying infrastructure it currently runs on.

<a name="9.6.2"></a>
#### 9.6.2. What to Monitor

These physical and virtual devices need to be monitored: 

* Network Services across sites and tenants 							
* Virtualized functions per site and tenant
* Individual Virtual Machines and Containers
* Virtualization infrastructure components
* Physical servers (compute) and network elements
* Toolservers with their applications (DNS, IdM, ZTP, etc) 
* Cabling 

<a name="9.6.3"></a>
#### 9.6.3. The Architecture

In geographically dispersed large cloud deployments, a given telco cloud may have several cloud infrastructure components as well a large set of virtualized workloads (VNF/CNFs). It is important to monitor all of these workloads and infrastructure components. Furthermore, it is even more important to be able to correlate between the metrics provided by these entities to determine the performance and/or issues in such deployments. 

The cloud deployment tends to shrink and expand based upon the customer demand. Therefore, an architecture is required that can scale on demand and does not force a strong tie between various entities. This means, the workloads and cloud infrastructure components that provide telemetry/performance metrics must not be burdened to discover each other. The capacity (e.g. speed, storage) of one component must not force overrun or underrun situations that would cause critical data to be lost or delayed to a point to render it useless. 

Operators in charge of the Cloud Infrastructure (physical infra plus virtualization platform) require very detailed alarms and metrics to efficiently run their platform. While they need indicators about how well or poorly individual virtual machines and containers run, they don’t need a view inside these workloads. In fact, what and how workloads do is none of the NFVI operators business. The architecture must allow for different consumers to grant or deny access to available resources.

Multiple workloads or network services can be deployed onto one or more sites. These workloads require logical separation so that their metrics don’t mix by accident or simply based on security and privacy requirements. This is achieved by deploying these workloads within their own tenant space. All virtualization platforms offer such isolation down to virtual networks per tenant.


<a name="9.6.3.1"></a>
#### 9.6.3.1. Push Vs. Pull

Two widely deployed models for providing telemetry data are pull and push. 

 <a name="9.6.3.1.1"></a>
#### 9.6.3.1.1. Pull Model

Typical characteristics of a pull model are:

* The consumers are required to discover the producers of the data
* Once the producers are identified, there should be a tight relationship (synchronization) between the producer and consumer. For example, if a producer encounters a LCM (Life Cycle Management) event - such as it moves to a different location or reboots/restarts, the consumer must re-discover it and bind the relationship again - makes the systems very complex in terms of configuration as well management. 
* Data is pulled explicitly by the consumer. The consumer must have appropriate bandwidth, compute power, and storage to deal with this data - example SNMP pull/walks

 <a name="9.6.3.1.2"></a>
#### 9.6.3.1.2. Push Model

Typical characteristics of a push model are:

* Declarative definition of destination - The producers of data know explicitly where to stream/push their data
* A “well known” data broker is utilized - all consumers and producers know about it through declarative definition. The data broker can be a bus such as RabitMQ, Apache Kafka, Apache Pulsar
* No restrictions on the bandwidth or data storage constraints on producers or consumers. Producers produce the data and stream/push it to the broker and consumers pull the data from the broker. No explicit sync is required between producers and consumers. 
* LCM (Life Cycle Management) events, such as moves, reboot/restarts, of consumers or producers have no impact on others.
* Producers and consumers can be added/removed at will. No impact on the system. This makes this model very flexible and scalable and better suited for large (or small) geographically dispersed telco clouds. 
* Example of push model are gRPC, SNMP traps, syslogs






