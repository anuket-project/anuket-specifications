[<< Back](../../ref_model)
# 6 External Interfaces
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction.](#6.1)
* [6.2 NFVI APIs.](#6.2)
  * [6.2.1 Tenant Level APIs.](#6.2.1)
  * [6.2.2 Hardware Acceleration Interfaces and APIs.](#6.2.2)
* [6.3 Intra-NFVI Interfaces.](#6.3)
  * [6.3.1. Hypervisor Hardware Interface.](#6.3.1)
* [6.4 Enabler Services Interfaces.](#6.4)


<a name="6.1"></a>
## 6.1 Introduction
In this document’s earlier chapters, the various resources and capabilities of the NFVI have been catalogued and the workloads (VNFs) have been profiled with respect to those capabilities. The intent behind this chapter and an “API Layer” is to similarly provide a single place to catalogue and thereby codify, a common set of open APIs to access (i.e. request, consume, control, etc.) the aforementioned resources, be them directly exposed to the VNFs, or purely internal to the NFVI.

It is a further intent of this chapter and this document to ensure the APIs adopted for CNTT NFVI implementations are open and not proprietary, in support of compatibility, component substitution and ability to realize maximum value from existing and future test heads and harnesses.

While it is the intent of this chapter, when included in a Reference Architecture, to catalogue the APIs, it is not the intent of this chapter to reprint the APIs, as this would make maintenance of the chapter impractical and the length of the chapter disproportionate within the Reference Model document. Instead, the APIs selected for CNTT NFVI implementations and specified in this chapter, will be incorporated by reference and URLs for the latest, authoritative versions of the APIs, provided in the References section of this document.

Although the document does not attempt to reprint the APIs themselves, where appropriate and generally where the mapping of resources and capabilities within the NFVI to objects in APIs would be otherwise ambiguous, this chapter shall provide explicit identification and mapping.

In addition to the raw or base-level NFVI functionality to API and object mapping, it is further the intent to specify an explicit, normalized set of APIs and mappings to control the logical interconnections and relationships between these objects, notably, but not limited to, support of SFC (Service Function Chaining) and other networking and network management functionality.

Chapter 3 introduced a model of the Network Function Virtualisation Infrastructure (NFVI). Figure 3-1 shows an overview of the NFVI model including the external application programming interface (API)/ user interface (UI) for providing access to the NFVI management functions. Section 3.3 lists the actions supported by the NFVI Management Software.  This chapter specifies the abstract interfaces (API, CLI, etc.) supported by the NFVI Reference Model. The purpose of this chapter is to define and catalogue a common set of open (not proprietary) APIs, of the following types:

- NFVI APIs: These APIs are provided to the VNF workloads (i.e. exposed), by the infrastructure in order for VNF workloads to access (i.e. request, consume, control, etc.) NFVI resources.
- Intra-NFVI APIs: These APIs are provided and consumed directly by the infrastructure. These APIs are purely internal to the NFVI and are not exposed to the workloads.
- Enabler Services APIs: These APIs are provided by non-NFVI services and provide capabilities that are required for a majority of VNF workloads, e.g. DHCP, DNS, NTP, DBaaS, etc.

<a name="6.2"></a>
## 6.2 NFVI APIs
The NFVI APIs consist of set of APIs that are externally and internally visible. The externally visible APIs are made available for orchestration and management of the execution environments that host workloads (e.g., VNFs) while the internally visible APIs support actions on the hypervisor and the physical resources. The ETSI NFV Reference Architecture Framework (**Figure 6-1**) shows a number of Interface points where specific or sets of APIs are supported. For the scope of the reference model the relevant interface points are shown in **Table 6-1**.

<p align="center"><img src="../figures/ch01_etsi_archi_mapping_v2.PNG" alt="ETSI NFVI Interface" title="ETSI NFVI Interface" width="65%"/></p>
<p align="center"><b>Figure 6-1:</b> ETSI NFVI Interface points.</p>

| Interface Point | NFVI Exposure | Interface Between | Description|
|--------------|--------------|--------------|--------------|
| Vi-Ha | Internal NFVI | Software Layer and Hardware Resources | 1. Discover/collect resources and their configuration information <br>2. Create execution environment (e.g., VM) for workloads (VNF) |
| Vn-Nf|  External | NFVI and VM (VNF) | Here VNF represents the execution environment. The interface is used to specify interactions between the VNF and abstract NFVI accelerators. The inetrafecs can be used to discover, configure and manage these acceleartors and for the VNF to register/deregister for receiving acceleartor events and data. |
| NF-Vi | External | NFVI and VIM | 1. Discover/collect physical/virtual resources and their configuration information<br>2. Manage (create, resize, (un) suspend, reboot, etc.) physical/virtualised resources<br>3. Physical/Virtual resources configuration changes<br>4. Physical/Virtual resource configuration. |
| Or-Vi | External | VNF Orchestrator and VIM | See below |
| Vi-Vnfm | External | VNF Manager and VIM | See below |

<p align="center"><b>Table 6-1:</b> NFVI and VIM Interfaces with Other System Components.</p>

The Or-Vi and Vi-VNfm are both specifying interfaces provided by the VIM and therefore are related. The Or-Vi reference point is used for exchanges between NFV Orchestrator and VIM, and supports the following interfaces; virtualised resources refers to virtualised compute, storage and network resources:

- Software Image Management
- Virtualised Resources Information Management
- Virtualised Resources Capacity Management (only VNF Orchestrator and VIM (Or-Vi))
- Virtualised Resources Management
- Virtualised Resources Change Management
- Virtualised Resources Reservation Management
- Virtualised Resources Quota Management
- Virtualised Resources Performance Management
- Virtualised Resources Fault Management
- Policy Management
- Network Forwarding Path (NFP) Management (only VNF Orchestrator and VIM (Or-Vi))

<a name="6.2.1"></a>
### 6.2.1 Tenant Level APIs

In the abstraction model of the NFVI (**Chapter 3**) a conceptual model of a Tenant (**Figure 3-2**) represents the slice of a cloud zone dedicated to a VNF. This slice, the Tenant, is composed of virtual resources being utilized by VNFs within that Tenant. The Tenant has an assigned quota of virtual resources, a set of users can perform operations as per their assigned roles, and the Tenant exists within a Cloud Zone. The APIs will specify the allowed operations on the Tenant including its component virtual resources and the different APIs can only be executed by users with the appropriate roles. For example, a Tenant may only be allowed to be created and deleted by Cloud Zone administrators while virtual compute resources could be allowed to be created and deleted by Tenant administrators.

For a VNF stack to be created in a Tenant also requires APIs for the management (creation, deletion and operation) of the Tenant, software flavours (Chapter 5), Operating System and VNF images (“Images”), Identity and Authorization (“Identity”), virtual resources, security and the VNF application (“stack”).

A virtual compute resource is created as per the flavour template (specifies the compute, memory and local storage capacity) and is launched using an image with access and security credentials; once launched, it is referred to as a virtual compute instance or just “Instance”). Instances can be launched by specifying the compute, memory and local storage capacity parameters instead of an existing flavour; reference to flavours coves the situation where the capacity parameters are specified. IP addresses and storage volumes can be attached to a running Instance.

| Resource | Create | List | Attach | Detach | Delete | Notes |
|-----------------|--------|------|--------|--------|--------|-------------------------------------------------------------------------------------------------------------|
| Flavour | + | + |  |  | + |  |
| Image | + | + |  |  | + | Create/delete by appropriate administrators |
| Key pairs | + | + |  |  | + |  |
| Privileges |  |  |  |  |  | Created and managed by Cloud Service Provider(CSP)  administrators |
| Role | + | + |  |  | + | Create/delete by authorized administrators where roles are assigned privileges and mapped to users in scope |
| Security Groups | + | + |  |  | + | Create and delete only by VDC administrators |
| Stack | + | + |  |  | + | Create/delete by VDC users with appropriate role |
| Virtual Storage | + | + | + | + | + | Create/delete by VDC users with appropriate role |
| User | + | + |  | + | + | Create/delete only by VDC administrators |
| Tenant | + | + |  | + | + | Create/delete only by Cloud Zone administrators |
| Virtual compute | + | + |  | + | + | Create/delete by VDC users with appropriate role.  Additional operations would include suspend/unsuspend |
| Virtual network | + | + | + | + | + | Create/delete by VDC users with appropriate role |

<p align="center"><b>Table 6-2:</b> API types for a minimal set of resources.</p>

**Table 6-2** specifies a minimal set of operations for a minimal set of resources that are needed to orchestrate VNF workloads. The actual APIs for the listed operations will be specified in the Reference Architectures; each listed operation could have a number of associated APIs with a different set of parameters. For example, create virtual resource using an image or a device.

<a name="6.2.2"></a>
### 6.2.2 Hardware Acceleration Interfaces

**Acceleration Interface Specifications**
ETSI GS NFV-IFA 002 defines a technology and implementation independent virtual accelerator, the accelerator interface requirements and specifications that would allow a VNF to leverage a Virtual Accelerator. The virtual accelerator is modeled on extensible para-virtualised devices (EDP). ETSI GS NFV-IFA 002 specifies the architectural model in Chapter 4 and the abstract interfaces for management, configuration, monitoring and Data exchange in Chapter 7.

ETSI ETSI (Ref: NFV IFA 019 v03101p) has defined a set of technology independent interfaces for acceleration resource life cycle management. These operations allow: allocation, release and querying of acceleration resource, get and reset statistics, subscribe/unsubscribe (terminate) to fault notifications, notify (only used by NFVI) and get alarm information.

These acceleration interfaces are summarized here in Table 6.3 only for convenience.

| **Request**|**Response**|**From, To**|**Type**|**Parameter**|**Description** |
| ------------|------------|------------|------------|------------|------------ |
| InitAccRequest|InitAccResponse|VNF → NFVI|Input|accFilter|the accelartor sub-system(s) to initialize and retrieve their capabilities. |
| |||Filter|accAttributeSelector|attribute names of accelerator capabilities |
| |||Output|accCapabilities|acceleration sub-system capabilities |
| RegisterForAccEventRequest|RegisterForAccEventResponse|VNF → NFVI|Input|accEvent|event the VNF is interested in |
| |||Input|vnfEventHandlerId|the handler for NFVI to use when notifying the VNF of the event |
| AccEventNotificationRequest|AccEventNotificationResponse|NFVI → VNF|Input|vnfEventHandlerId|Handler used by VNF registering |
| for this event |
| |||Input|accEventMetaData| |
| DeRegisterForAccEventRequest|DeRegisterForAccEventResponse|VNF → NFVI|Input|accEvent|Event VNF is deregistering from |
| ReleaseAccRequest|ReleaseAccResponse|VNF → NFVI||| |
| ModifyAccConfigurationRequest|ModifyAccConfigurationResponse|VNF → NFVI|Input|accConfigurationData|Config data for accelerator |
| |||Input|accSubSysConfigurationData|Config data for accelerator sub-system |
| GetAccConfigsRequest|GetAccConfigsResponse|VNF → NFVI|Input|accFilter|Filter for subsystems from which config data requested |
| |||Input|accConfigSelector|attributes of config types |
| |||Output|accComfigs|Config info (only for the specified attributes) for specified subsystems |
| ResetAccConfigsRequest|ResetAccConfigsResponse|VNF → NFVI|Input|accFilter|Filter for subsystems for which config is to be reset |
| |||Input|accConfigSelector|attributes of config types whose values will be reset |
| AccDataRequest|AccDataResponse|VNF → NFVI|Input|accData|Data (metadata) sent too accelerator |
| |||Input|accChannel|Channel data is to be sent to |
| |||Output|accData|Data from accelerator |
| AccSendDataRequest|AccSendDataResponse|VNF → NFVI|Input|accData|Data (metadata) sent too accelerator |
| |||Input|accChannel|Channel data is to be sent to |
| AccReceiveDataRequest|AccReceiveDataResponse|VNF → NFVI|Input|maxNumberOfDataItems|Max number of data items to be received |
| |||Input|accChannel|Channel data is requested from |
| |||Output|accData|Data received form Accelerator |
| RegisterForAccDataAvailableEventRequest|RegisterForAccDataAvailableEventResponse|VNF → NFVI|Input|regHandlerId|Registration Identifier |
| |||Input|accChannel|Channel where event is requested for |
| AccDataAvailableEventNotificationRequest|AccDataAvailableEventNotificationResponse|NFVI → VNF|Input|regHandlerId|Reference used by VNF when registering for the event |
| DeRegisterForAccDataAvailableEventRequest|DeRegisterForAccDataAvailableEventResponse|VNF → NFVI|Input|accChannel|Channel related to the event  |
| AllocateAccResourceRequest|AllocateAccResourceResponse|VIM → NFVI|Input|attachTargetInfo|the resource the |
| accelerator is to be attached to (e.g., VM) |
| |||Input|accResourceInfo|Accelerator Information |
| |||Output|accResourceId|Id if successful |
| ReleaseAccResourceRequest|ReleaseAccResourceResponse|VIM → NFVI|Input|accResourceId|Id of resource to be released |
| QueryAccResourceRequest|QueryAccResourceResponse|VIM → NFVI|Input|hostId|Id of specified host |
| |||Input|Filter|Specifies the accelerators for which query applies |
| |||Output|accQueryResult|Details of the accelerators matching the input filter located in the selected host. |
| GetAccStatisticsRequest|GetAccStatisticsResponse|VIM → NFVI|Input|accFilter|Accelerator subsystems from which data is requested |
| |||Input|accStatSelector|attributes of AccStatistics whose data will be returned |
| |||Output|accStatistics|Statistics data of the accelerators |
| matching the input filter located in the |
| selected host. |
| ResetAccStatisticsRequest|ResetAccStatisticsResponse|VIM → NFVI|Input|accFilter|Accelerator subsystems for which data is to be reset |
| |||Input|accStatSelector|attributes of AccStatistics whose data will be reset |
| SubscribeRequest|SubscribeResponse|VIM → NFVI|Input|hostId|Id of specified host |
| |||Input|Filter|Specifies the accelerators and related alarmsThe filter could include accelerator information, severity of the alarm, etc. |
| |||Output|SubscriptionId|Identifier of the successfully created |
| subscription. |
| UnsubscribeRequest|UnsubscribeResponse|VIM → NFVI|Input|hostId|Id of specified host |
| |||Input|SubscriptionId|Identifier of the subscription to be |
| unsubscribed. |
| Notify||NFVI → VIM|||NFVI notifies an alarm to VIM |
| GetAlarmInfoRequest|GetAlarmInfoResponse|VIM → NFVI|Input|hostId|Id of specified host |
| |||Input|Filter|Specifies the accelerators and related alarmsThe filter could include accelerator information, severity of the alarm, etc. |
| |||Output|Alarm|Information about the alarms if filter matches an alarm. |
|  |
| AccResourcesDiscoveryRequest|AccResourcesDiscoveryResponse|VIM → NFVI|Input|hostId|Id of specified host |
| |||Output|discoveredAccResourceInfo|Information on the acceleration resources discovered within the NFVI. |
| OnloadAccImageRequest|OnloadAccImageResponse|VIM → NFVI|Input|accResourceId|Identifier of the chosen accelerator in the NFVI. |
| |||Input|accImageInfo|Information about the acceleration image. |
| |||Input|accImage|The binary file of acceleration image. |

<p align="center"><b>Table 6-3:</b> Hardware Acceleration Interfaces.</p>

<a name="6.3"></a>
## 6.3 Intra-NFVI Interfaces

<a name="6.3.1"></a>
### 6.3.1. Hypervisor Hardware Interface

Table 6-1 lists a number of NFVI and VIM inetrfaces, including the internal VI-Ha intterface. the The VI-Ha interface allows the hypervisor to control the physical infrastructure; the hypervisor acts under VIM control. The VIM issues all requests and responses using the NF-VI interface; requests and responses include commands, configuration requests, policies, updates, alerts and response to infrastructure results. The hypervisor also provides information about the health of the physical infrastructure resources to the VM.  All these activities, on behalf of the VIM, are performed by the hypervisor using the VI-Ha interface. While no abstract APIs have yet been defined for this internal VI-Ha interface, ETSI GS NFV-INF 004 defines a set of requirements and details of the information that is required by the VIM from the physical infrastructure resources. Hypervisors utilize various programs to get this data including BIOS, IPMI, PCI, I/O Adapters/Drivers, etc.

<a name="6.4"></a>
## 6.4. Enabler Services Interfaces
An operational cloud needs a set of standard services to function. Services such as NTP for time synchronization, DHCP for IP address allocation, DNS for obtaining IP addresses for domain names, and LBaaS (version 2) to distribute incoming requests amongst a pool of designated resources.

## References
Network Functions Virtualisation (NFV); Infrastructure; Hypervisor Domain. ETSI GS NFV-INF 004
Network Functions Virtualisation (NFV); Acceleration Technologies; VNF Interfaces SpecificationETSI. GS NFV-IFA 002 v2.4.1
Network Functions Virtualisation (NFV); Acceleration Technologies; Acceleration Resource Management Interface Specification; NFV IFA 019 v03101p
Network Functions Virtualisation (NFV); Management and Orchestration; Or-Vi reference point - Interface and Information Model Specification; ETSI GS NFV-IFA 005 V3.2.1
