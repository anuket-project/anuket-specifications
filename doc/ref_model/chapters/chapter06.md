[<< Back](../../ref_model)
# 6 External Interfaces

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 Cloud Infrastructure APIs](#6.2)
  * [6.2.1 Tenant Level APIs](#6.2.1)
  * [6.2.2 Hardware Acceleration Interfaces and APIs](#6.2.2)
* [6.3 Intra-Cloud Infrastructure Interfaces](#6.3)
  * [6.3.1. Hypervisor Hardware Interface](#6.3.1)
* [6.4 Enabler Services Interfaces](#6.4)


<a name="6.1"></a>
## 6.1 Introduction
In this document’s earlier chapters, the various resources and capabilities of the Cloud Infrastructure have been catalogued and the workloads have been profiled with respect to those capabilities. The intent behind this chapter and an “API Layer” is to similarly provide a single place to catalogue and thereby codify, a common set of open APIs to access (i.e. request, consume, control, etc.) the aforementioned resources, be them directly exposed to the workloads, or purely internal to the Cloud Infrastructure.

It is a further intent of this chapter and this document to ensure the APIs adopted for CNTT Cloud Infrastructure implementations are open and not proprietary, in support of compatibility, component substitution, and ability to realize maximum value from existing and future test heads and harnesses.

While it is the intent of this chapter to catalogue the APIs, it is not the intent of this chapter to reprint the APIs, as this would make maintenance of the chapter impractical and the length of the chapter disproportionate within the Reference Model document. Instead, the APIs selected for CNTT Cloud Infrastructure implementations and specified in this chapter, will be incorporated by reference and URLs for the latest, authoritative versions of the APIs, provided in the References section of this document.

Although the document does not attempt to reprint the APIs themselves, where appropriate and generally where the mapping of resources and capabilities within the Cloud Infrastructure to objects in APIs would be otherwise ambiguous, this chapter shall provide explicit identification and mapping.

In addition to the raw or base-level Cloud Infrastructure functionality to API and object mapping, it is further the intent to specify an explicit, normalized set of APIs and mappings to control the logical interconnections and relationships between these objects, notably, but not limited to, support of SFC (Service Function Chaining) and other networking and network management functionality.

This chapter specifies the abstract interfaces (API, CLI, etc.) supported by the Cloud Infrastructure Reference Model. The purpose of this chapter is to define and catalogue a common set of open (not proprietary) APIs, of the following types:

- Cloud Infrastructure APIs: These APIs are provided to the workloads (i.e. exposed), by the infrastructure in order for workloads to access (i.e. request, consume, control, etc.) Cloud Infrastructure resources.
- Intra-Cloud Infrastructure APIs: These APIs are provided and consumed directly by the infrastructure. These APIs are purely internal to the Cloud Infrastructure and are not exposed to the workloads.
- Enabler Services APIs: These APIs are provided by non-Cloud Infrastructure services and provide capabilities that are required for a majority of workloads, e.g. DHCP, DNS, NTP, DBaaS, etc.

<a name="6.2"></a>
## 6.2 Cloud Infrastructure APIs
The Cloud Infrastructure APIs consist of set of APIs that are externally and internally visible. The externally visible APIs are made available for orchestration and management of the execution environments that host workloads while the internally visible APIs support actions on the hypervisor and the physical resources. The ETSI NFV Reference MANO Architecture (**Figure 6-1**) shows a number of Interface points where specific or sets of APIs are supported. For the scope of the reference model the relevant interface points are shown in **Table 6-1**.

<p align="center"><img src="../figures/ch09-etsi-nfv-architecture-mapping.png" alt="ETSI NFV architecture mapping" title="ETSI NFV architecture mapping" width="65%"/></p>
<p align="center"><b>Figure 6-1:</b> ETSI NFV architecture mapping</p>

| Interface Point | Cloud Infrastructure Exposure | Interface Between                     | Description                                                                                                                                                                                                                                                                                                     |
|-----------------|---------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vi-Ha           | Internal NFVI | Software Layer and Hardware Resources | 1. Discover/collect resources and their configuration information <br>2. Create execution environment (e.g., VM) for workloads (VNF)                                                                                                                                                                            |
| Vn-Nf           | External      | NFVI and VM (VNF)                     | Here VNF represents the execution environment. The interface is used to specify interactions between the VNF and abstract NFVI accelerators. The interfaces can be used to discover, configure, and manage these acceleartors and for the VNF to register/deregister for receiving accelerator events and data. |
| NF-Vi           | External      | NFVI and VIM                          | 1. Discover/collect physical/virtual resources and their configuration information<br>2. Manage (create, resize, (un) suspend, reboot, etc.) physical/virtualised resources<br>3. Physical/Virtual resources configuration changes<br>4. Physical/Virtual resource configuration.                               |
| Or-Vi           | External      | VNF Orchestrator and VIM              | See below                                                                                                                                                                                                                                                                                                       |
| Vi-Vfm         | External      | VNF Manager and VIM                   | See below                                                                                                                                                                                                                                                                                                       |

<p align="center"><b>Table 6-1:</b> NFVI and VIM Interfaces with Other System Components in the ETSI NFV architecture</p>

The Or-Vi and Vi-VNfm are both specifying interfaces provided by the VIM and therefore are related. The Or-Vi reference point is used for exchanges between NFV Orchestrator and VIM, and supports the following interfaces; virtualised resources refers to virtualised compute, storage, and network resources:

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

In the abstraction model of the Cloud Infrastructure (**Chapter 3**) a conceptual model of a Tenant (**Figure 3-2**) represents the slice of a cloud zone dedicated to a workload. This slice, the Tenant, is composed of virtual resources being utilized by workloads within that Tenant. The Tenant has an assigned quota of virtual resources, a set of users can perform operations as per their assigned roles, and the Tenant exists within a Cloud Zone. The APIs will specify the allowed operations on the Tenant including its component virtual resources and the different APIs can only be executed by users with the appropriate roles. For example, a Tenant may only be allowed to be created and deleted by Cloud Zone administrators while virtual compute resources could be allowed to be created and deleted by Tenant administrators.

For a workload to be created in a Tenant also requires APIs for the management (creation, deletion, and operation) of the Tenant, software flavours (Chapter 5), Operating System and workload images (“Images”), Identity and Authorization (“Identity”), virtual resources, security, and the workload application (“stack”).

A virtual compute resource is created as per the flavour template (specifies the compute, memory, and local storage capacity) and is launched using an image with access and security credentials; once launched, it is referred to as a virtual compute instance or just “Instance”). Instances can be launched by specifying the compute, memory, and local storage capacity parameters instead of an existing flavour; reference to flavours covers the situation where the capacity parameters are specified. IP addresses and storage volumes can be attached to a running Instance.

| Resource        | Create | List | Attach | Detach | Delete | Notes                                                                                                       |
|-----------------|--------|------|--------|--------|--------|-------------------------------------------------------------------------------------------------------------|
| Flavour         | +      | +    |        |        | +      |                                                                                                             |
| Image           | +      | +    |        |        | +      | Create/delete by appropriate administrators                                                                 |
| Key pairs       | +      | +    |        |        | +      |                                                                                                             |
| Privileges      |        |      |        |        |        | Created and managed by Cloud Service Provider(CSP)  administrators                                          |
| Role            | +      | +    |        |        | +      | Create/delete by authorized administrators where roles are assigned privileges and mapped to users in scope |
| Security Groups | +      | +    |        |        | +      | Create and delete only by VDC administrators                                                                |
| Stack           | +      | +    |        |        | +      | Create/delete by VDC users with appropriate role                                                            |
| Virtual Storage | +      | +    | +      | +      | +      | Create/delete by VDC users with appropriate role                                                            |
| User            | +      | +    |        | +      | +      | Create/delete only by VDC administrators                                                                    |
| Tenant          | +      | +    |        | +      | +      | Create/delete only by Cloud Zone administrators                                                             |
| Virtual compute | +      | +    |        | +      | +      | Create/delete by VDC users with appropriate role.  Additional operations would include suspend/unsuspend    |
| Virtual network | +      | +    | +      | +      | +      | Create/delete by VDC users with appropriate role                                                            |

<p align="center"><b>Table 6-2:</b> API types for a minimal set of resources.</p>

**Table 6-2** specifies a minimal set of operations for a minimal set of resources that are needed to orchestrate workloads. The actual APIs for the listed operations will be specified in the Reference Architectures; each listed operation could have a number of associated APIs with a different set of parameters. For example, create virtual resource using an image or a device.

<a name="6.2.2"></a>
### 6.2.2 Hardware Acceleration Interfaces

**Acceleration Interface Specifications**
ETSI GS NFV-IFA 002 [7] defines a technology and implementation independent virtual accelerator, the accelerator interface requirements and specifications that would allow a workload to leverage a Virtual Accelerator. The virtual accelerator is modelled on extensible para-virtualised devices (EDP). ETSI GS NFV-IFA 002 [7] specifies the architectural model in Chapter 4 and the abstract interfaces for management, configuration, monitoring, and Data exchange in Chapter 7.

ETSI NFV-IFA 019 3.1.1 [8] has defined a set of technology independent interfaces for acceleration resource life cycle management. These operations allow: allocation, release, and querying of acceleration resource, get and reset statistics, subscribe/unsubscribe (terminate) to fault notifications, notify (only used by NFVI), and get alarm information.

These acceleration interfaces are summarized here in Table 6.3 only for convenience.

<table>
<tr><th>  Request </th> <th> Response </th> <th> From, To </th> <th> Type </th> <th>  Parameter  </th> <th> Description </th></tr>
<tr><td rowspan="3"> InitAccRequest </td><td rowspan="3"> InitAccResponse </td><td rowspan="3"> VNF → NFVI </td> <td>  Input </td> <td>  accFilter </td> <td>  the accelartor sub-system(s) to initialize and retrieve their capabilities. </td></tr>
<tr><td> Filter </td><td> accAttributeSelector </td><td> attribute names of accelerator capabilities  </td></tr>
<tr><td> Output </td><td> accCapabilities </td><td> acceleration sub-system capabilities  </td></tr>
<tr><td rowspan="2">  RegisterForAccEventRequest </td><td rowspan="2"> RegisterForAccEventResponse </td><td rowspan="2"> VNF → NFVI </td><td> Input </td><td> accEvent </td><td> event the VNF is interested in  </td></tr>
<tr><td> Input </td><td> vnfEventHandlerId </td><td> the handler for NFVI to use when notifying the VNF of the event  </td></tr>
<tr><td rowspan="2">  AccEventNotificationRequest </td><td rowspan="2"> AccEventNotificationResponse </td><td rowspan="2"> NFVI → VNF </td><td> Input </td><td> vnfEventHandlerId </td><td> Handler used by VNF registering for this event  </td></tr>
<tr><td> Input </td><td> accEventMetaData </td><td>   </td></tr>
<tr><td>  DeRegisterForAccEventRequest </td><td> DeRegisterForAccEventResponse </td><td> VNF → NFVI </td><td> Input </td><td> accEvent </td><td> Event VNF is deregistering from  </td><td> 
<tr><td>  ReleaseAccRequest </td><td> ReleaseAccResponse </td><td> VNF → NFVI </td><td>  </td><td>  </td><td>   </td></tr>
<tr><td rowspan="2">  ModifyAccConfigurationRequest </td><td rowspan="2"> ModifyAccConfigurationResponse </td><td rowspan="2"> VNF → NFVI </td><td> Input </td><td> accConfigurationData </td><td> Config data for accelerator  </td></tr>
<tr><td> Input </td><td> accSubSysConfigurationData </td><td> Config data for accelerator sub-system  </td></tr>
<tr><td  rowspan="3">  GetAccConfigsRequest </td><td rowspan="3"> GetAccConfigsResponse </td><td rowspan="3"> VNF → NFVI </td><td> Input </td><td> accFilter </td><td> Filter for subsystems from which config data requested  </td></tr>
<tr><td> Input </td><td> accConfigSelector </td><td> attributes of config types  </td></tr>
<tr><td> Output </td><td> accComfigs </td><td> Config info (only for the specified attributes) for specified subsystems  </td></tr>
<tr><td rowspan="2">  ResetAccConfigsRequest </td><td rowspan="2"> ResetAccConfigsResponse </td><td rowspan="2"> VNF → NFVI </td><td> Input </td><td> accFilter </td><td> Filter for subsystems for which config is to be reset  </td></tr>
<tr><td> Input </td><td> accConfigSelector </td><td> attributes of config types whose values will be reset  </td></tr>
<tr><td rowspan="3">  AccDataRequest </td><td rowspan="3"> AccDataResponse </td><td rowspan="3"> VNF → NFVI </td><td> Input </td><td> accData </td><td> Data (metadata) sent too accelerator  </td></tr>
<tr><td> Input </td><td> accChannel </td><td> Channel data is to be sent to  </td></tr>
<tr><td> Output </td><td> accData </td><td> Data from accelerator  </td></tr>
<tr><td rowspan="2">  AccSendDataRequest </td><td rowspan="2"> AccSendDataResponse </td><td rowspan="2"> VNF → NFVI </td><td> Input </td><td> accData </td><td> Data (metadata) sent too accelerator  </td></tr>
<tr><td> Input </td><td> accChannel </td><td> Channel data is to be sent to  </td></tr>
<tr><td rowspan="3">  AccReceiveDataRequest </td><td rowspan="3"> AccReceiveDataResponse </td><td rowspan="3"> VNF → NFVI </td><td> Input </td><td> maxNumberOfDataItems </td><td> Max number of data items to be received  </td></tr>
<tr><td> Input </td><td> accChannel </td><td> Channel data is requested from  </td></tr>
<tr><td> Output </td><td> accData </td><td> Data received form Accelerator  </td></tr>
<tr><td rowspan="2">  RegisterForAccDataAvailableEventRequest </td><td rowspan="2"> RegisterForAccDataAvailableEventResponse </td><td rowspan="2"> VNF → NFVI </td><td> Input </td><td> regHandlerId </td><td> Registration Identifier  </td></tr>
<tr><td> Input </td><td> accChannel </td><td> Channel where event is requested for  </td></tr>
<tr><td>  AccDataAvailableEventNotificationRequest </td><td> AccDataAvailableEventNotificationResponse </td><td> NFVI → VNF </td><td> Input </td><td> regHandlerId </td><td> Reference used by VNF when registering for the event  </td></tr>
<tr><td>  DeRegisterForAccDataAvailableEventRequest </td><td> DeRegisterForAccDataAvailableEventResponse </td><td> VNF → NFVI </td><td> Input </td><td> accChannel </td><td> Channel related to the event   </td></tr>
<tr><td rowspan="3">  AllocateAccResourceRequest </td><td rowspan="3"> AllocateAccResourceResponse </td><td rowspan="3"> VIM → NFVI </td><td> Input </td><td> attachTargetInfo </td><td> the resource the accelerator is to be attached to (e.g., VM)  </td></tr>
<tr><td> Input </td><td> accResourceInfo </td><td> Accelerator Information  </td></tr>
<tr><td> Output </td><td> accResourceId </td><td> Id if successful  </td></tr>
<tr><td>  ReleaseAccResourceRequest </td><td> ReleaseAccResourceResponse </td><td> VIM → NFVI </td><td> Input </td><td> accResourceId </td><td> Id of resource to be released  </td></tr>
<tr><td rowspan="3">  QueryAccResourceRequest </td><td rowspan="3"> QueryAccResourceResponse </td><td rowspan="3"> VIM → NFVI </td><td> Input </td><td> hostId </td><td> Id of specified host  </td></tr>
<tr><td> Input </td><td> Filter </td><td> Specifies the accelerators for which query applies  </td></tr>
<tr><td> Output </td><td> accQueryResult </td><td> Details of the accelerators matching the input filter located in the selected host.  </td></tr>
<tr><td rowspan="3">  GetAccStatisticsRequest </td><td rowspan="3"> GetAccStatisticsResponse </td><td rowspan="3"> VIM → NFVI </td><td> Input </td><td> accFilter </td><td> Accelerator subsystems from which data is requested  </td></tr>
<tr><td> Input </td><td> accStatSelector </td><td> attributes of AccStatistics whose data will be returned  </td></tr>
<tr><td> Output </td><td> accStatistics </td><td> Statistics data of the accelerators matching the input filter located in the selected host.  </td></tr>
<tr><td rowspan="2">  ResetAccStatisticsRequest </td><td rowspan="2"> ResetAccStatisticsResponse </td><td rowspan="2"> VIM → NFVI </td><td> Input </td><td> accFilter </td><td> Accelerator subsystems for which data is to be reset  </td></tr>
<tr><td> Input </td><td> accStatSelector </td><td> attributes of AccStatistics whose data will be reset  </td></tr>
<tr><td rowspan="3">  SubscribeRequest </td><td rowspan="3"> SubscribeResponse </td><td rowspan="3"> VIM → NFVI </td><td> Input </td><td> hostId </td><td> Id of specified host  </td></tr>
<tr><td> Input </td><td> Filter </td><td> Specifies the accelerators and related alarmsThe filter could include accelerator information, severity of the alarm, etc.  </td></tr>
<tr><td> Output </td><td> SubscriptionId </td><td> Identifier of the successfully created subscription.  </td></tr>
<tr><td rowspan="2">  UnsubscribeRequest </td><td rowspan="2"> UnsubscribeResponse </td><td rowspan="2"> VIM → NFVI </td><td> Input </td><td> hostId </td><td> Id of specified host  </td></tr>
<tr><td> Input </td><td> SubscriptionId </td><td> Identifier of the subscription to be unsubscribed.  </td></tr>
<tr><td>  Notify </td><td>  </td><td> NFVI → VIM </td><td>  </td><td>  </td><td> NFVI notifies an alarm to VIM  </td></tr>
<tr><td rowspan="3">  GetAlarmInfoRequest </td><td rowspan="3"> GetAlarmInfoResponse </td><td rowspan="3"> VIM → NFVI </td><td> Input </td><td> hostId </td><td> Id of specified host  </td></tr>
<tr><td> Input </td><td> Filter </td><td> Specifies the accelerators and related alarms. The filter could include accelerator information, severity of the alarm, etc.  </td></tr>
<tr><td> Output </td><td> Alarm </td><td> Information about the alarms if filter matches an alarm.  </td></tr>
<tr><td rowspan="2">  AccResourcesDiscoveryRequest </td><td rowspan="2"> AccResourcesDiscoveryResponse </td><td rowspan="2"> VIM → NFVI </td><td> Input </td><td> hostId </td><td> Id of specified host  </td></tr>
<tr><td> Output </td><td> discoveredAccResourceInfo </td><td> Information on the acceleration resources discovered within the NFVI.  </td></tr>
<tr><td rowspan="3">  OnloadAccImageRequest </td><td rowspan="3"> OnloadAccImageResponse </td><td rowspan="3"> VIM → NFVI </td><td> Input </td><td> accResourceId </td><td> Identifier of the chosen accelerator in the NFVI.  </td></tr>
<tr><td> Input </td><td> accImageInfo </td><td> Information about the acceleration image.  </td></tr>
<tr><td> Input </td><td> accImage </td><td> The binary file of acceleration image.  </td></tr>
</table>

<p align="center"><b>Table 6-3:</b> Hardware Acceleration Interfaces in the ETSI NFV architecture</p>

<a name="6.3"></a>
## 6.3 Intra-Cloud Infrastructure Interfaces

<a name="6.3.1"></a>
### 6.3.1. Hypervisor Hardware Interface

Table 6-1 lists a number of NFVI and VIM interfaces, including the internal VI-Ha interface. The VI-Ha interface allows the hypervisor to control the physical infrastructure; the hypervisor acts under VIM control. The VIM issues all requests and responses using the NF-VI interface; requests and responses include commands, configuration requests, policies, updates, alerts, and response to infrastructure results. The hypervisor also provides information about the health of the physical infrastructure resources to the VM.  All these activities, on behalf of the VIM, are performed by the hypervisor using the VI-Ha interface. While no abstract APIs have yet been defined for this internal VI-Ha interface, ETSI GS NFV-INF 004 [9] defines a set of requirements and details of the information that is required by the VIM from the physical infrastructure resources. Hypervisors utilize various programs to get this data including BIOS, IPMI, PCI, I/O Adapters/Drivers, etc.

<a name="6.4"></a>
## 6.4. Enabler Services Interfaces
An operational cloud needs a set of standard services to function. Services such as NTP for time synchronization, DHCP for IP address allocation, DNS for obtaining IP addresses for domain names, and LBaaS (version 2) to distribute incoming requests amongst a pool of designated resources.

<!---## References
Network Functions Virtualisation (NFV); Infrastructure; Hypervisor Domain. ETSI GS NFV-INF 004 V1.1.1 [9]
Network Functions Virtualisation (NFV); Acceleration Technologies; VNF Interfaces Specification ETSI GS NFV-IFA 002 V2.4.1 [7]
Network Functions Virtualisation (NFV); Acceleration Technologies; Acceleration Resource Management Interface Specification; NFV IFA 019 V3.1.1 [8]
Network Functions Virtualisation (NFV); Management and Orchestration; Or-Vi reference point - Interface and Information Model Specification; ETSI GS NFV-IFA 005 V3.1.1 [10]--->
