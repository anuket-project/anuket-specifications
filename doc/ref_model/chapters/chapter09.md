[<< Back](../../ref_model)
# 9 Infrastructure Operations and Lifecycle Management
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [9.1 Introduction](#9.1)
* [9.2 Configuration and Lifecycle Management](#9.2)
* [9.3 Assurance](#9.3)
* [9.4 Capacity Management](#9.4)


<a name="9.1"></a>
## 9.1 Introduction

The purpose of this chapter is to define the capabilities required of the infrastructure to ensure it is effectively supported, maintained and otherwise lifecycle-managed by Operations teams.  This includes requirements relating to the need to be able to maintain infrastructure services "in-service" without impacting the applications and VNFs, whilst minimising human labour. It shall also capture any exceptions and related assumptions.

According to the scope laid out in chapter 1, this chapter will include any requirements of the infrastructure (NFVI) and the infrastructure management (VIM) capabilities. This is reflected in Figure 9-1 below - the main area of interest for this chapter being the reference points between the reference model scope (in red) and the OSS/BSS block at the top.

<p align="center"><img src="../figures/ch01_etsi_archi_mapping_v2.PNG" alt="ETSI NFVI Interface" title="ETSI NFVI Interface" width="65%"/></p>
<p align="center"><b>Figure 9-1:</b> ETSI NFVI Interface points.</p>

Note this may seem like a large overlap with the topics in Chapter 6, however that chapter focusses primarily on the interfaces provided by the VIM and NFVI to VNFM and NFV workloads, not the interfaces used to manage the NFVI and VIM themselves.

There are two main business operating frameworks that are commonly known and used across the Telecommunications industry related to the topics in this chaper:
- FCAPS (ISO model for network management)
- eTOM (TM Forum Business Process Framework (eTOM))

The chapters below roughly map to these frameworks as follows:

<table>
  <thead>
    <tr>
      <th>Chapter Name</th>
      <th>FCAPS</th>
      <th>eTOM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Configuration and Lifecycle Management</td>
      <td>Configuration</td>
      <td>Fulfilment</td>
    </tr>
    <tr>
      <td rowspan=2>Assurance</td>
      <td>Performance</td>
      <td rowspan=2>Assurance</td>
    </tr>
    <tr>
      <td>Fault</td>
    </tr>
    <tr>
      <td>Capacity Management</td>
      <td>Configuration</td>
      <td>Fulfilment</td>
    </tr>
  </tbody>
</table>
<p align="center"><b>Table 9-1:</b> Operating Frameworks</p>

<a name="9.2"></a>
## 9.2 Configuration and Lifecycle Management

Configuration management is concerned with defining the configuration of infrastructure and its components, and tracking (observing) the running configuration of that infrastructure and any changes that take place. Modern configuration management practices such as desired state configuration management also mean that any changes from the desired state that are observed (aka the delta) are rectified by an orchestration / fulfilment component of the configuration management system. This "closed loop" mitigates against configuration drift in the infrastructure and its components. Our recommendation is to keep these closed loops as small as possible to reduce complexity and risk of error. Figure 9-2 shows the configuration management "loop" and how this relates to lifecycle management.

<p align="center"><img src="../figures/ch09_config_mgmt.png" alt="Configuration and Lifecycle Management" title="Configuration and Lifecycle Management" width="65%"/></p>
<p align="center"><b>Figure 9-2:</b> Configuration and Lifecycle Management</p>

The initial desired state might be for 10 hosts with a particular set of configuration attributes, including the version of the hypervisor and any management agents. The configuration management system will take that as input (1) and configure the infrastructure as required (2). It will then observe the current state periodically over time (3) and in the case of a difference between the desired state and the observed state it will calculate the delta (4) and re-configure the infrastructure (5). For each lifecycle stage (create, update, delete) this loop takes place - for example if an update to the hypervisor version is defined in the desired state, the configuration management system will calculate the delta (e.g. v1 --> v2) and re-configure the infrastructure as required.

However, the key requirements for the infrastructure and infrastructure management are those interfaces and reference points in the red box - where configuration is **set**, and where it is **observed**. Table 9-1 lists the main components and capabilities required in order to manage the configuration and lifecycle of those components.

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
      <td rowspan=6>Infrastructure Management (VIM) Software</td>
      <td rowspan=3>Set</td>
      <td>Target software / firmware version</td>
      <td>VIM software: v1.2.1</td>
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
      <td>VIM software: v1.2.1</td>
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
      <td rowspan=6>Infrastructure (NFVI) Software</td>
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

This leads to the following table (Table 9-3) which defines the standard interfaces that should be made available by the infrastructure and infrastructure management (VIM) components to allow for successful Configuration Management.

| Component | Interface Standard | Link |
| --- | --- | --- |
| Infrastructure Management | ... | ... |
| Infrastructure Software | ... | ... |
| Infrastructure Hardware | Redfish API | [DMTF Specification](https://www.dmtf.org/standards/redfish) |

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
    - The ability to collect data relating to component performance (total CPU used, storage throughput, network bandwidth in/out, API transactions, transaction response times, etc.)
2. Capabilities of the Infrastructure Management Software to allow for in-service maintenance of the Infrastructure Software and Hardware under its management, e.g.
    - The ability to mark a physical compute node as being in some sort of "maintenance mode" and for the Infrastructure Management Software to ensure all running workloads are moved off or rescheduled on to other available nodes (after checking that there is sufficient capacity) before marking the node as being ready for whatever maintenance activity needs to be performed
    - The ability to co-ordinate, automate and allow the declarative input of in-service software component upgrades - such as internal orchestration and scheduler components in the Infrastructure Management Software

Note that the above only refers to components - it is expected that any "service" level assurance doesn't add any further requirements onto the infrastructure, but rather takes the data extracted and builds service models based on the knowledge it has of the services being offered.

<a name="9.4"></a>
## 9.4 Capacity Management

Capacity Management is a potentially wide ranging process that includes taking demand across lines of business, analysing data about the infrastructure that is running and calculating when additional infrastructure might be required, or when infrastructure might need to be decommissioned.

As such the requirements for Capacity Management on the infrastructure are covered by the Assurance and Configuration and Lifecycle Management sections above. The Assurance section deals with the collection of data - there is no reason to consider that this would be done by a different mechanism for Capacity Management as it is for Assurance - and the Configuration and Lifecycle Management section deals with the changes being made to the infrastructure hardware, software and management components (e.g. changing of number of hypervisor hosts from 10 to 12).
