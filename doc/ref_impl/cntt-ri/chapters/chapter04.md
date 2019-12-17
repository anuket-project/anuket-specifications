[<< Back](../)

# 4. Lab Requirements

<a name="toc"></a>
## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Lab Requirement](#4.2)
* [4.3 Lab Topology](#4.3)
* [4.4 Lab Use Guidelines](#4.4)


<a name="4.1"></a>
## 4.1 Introduction
This chapter provides the laboratory hardware requirements needed to deploy the reference implementation.  These requirements represent a minimum set of requirements, where different labs may have hardware or capabilities exceeding these minimum specifications.  

The lab provides a set of physical servers, supported by a dedicated network infrastructure.  Users should be provided access to the servers, their operating systems, and out-of-band management (i.e. IPMI, IDRAC, ILO, etc.).  

<a name="4.2"></a>
## 4.2 Lab Requirements

Labs are organized into one or more *Pods*, where the *Pod* provides the complete set of resources [servers and network(s)] necessary to support the reference implementation installation and operation.  

A CNTT compliant *Pod* shall meet the following requirements.

1. One (1) physical server dedicated as a Jump / Test Host
2. Six (6) physical servers, serving as either compute or controllers
3. A configured network topology allowing for: Out-of-Band Management, Admin, Public, Private, and Storage Networks

The Jump Host / Test Host system will be utilized to install and manage the operation of the *Pod*.  For example, the system can be used to host the installer software used to deploy and configure OpenStack on the other physical servers.  Once installed, the system may be used to run test automations or it may be used to generate test traffic intended to measure the performance of a VNF operating within the *Pod*.  To support these operations, the physical server provided for the Jump / Test Host shall meet the same hardware requirements as compute / controller, as outline below.  In this context, the system may be considered as a miscellaneous use  or general purpose system.

<a name="4.2.1"></a>
### 4.2.1 Physical Server Requirements
Each server shall meet the following minimum specifications:

- **CPU**
  - 2x x86_64 CPU sockets (both populated), providing 24 cores each, 48 simultaneous multi-threads (SMT), at 2.2 GHz
- **Memory**
  - 512 GB RAM
- **Storage**
  - 3.2 TB SSD via SATA 6 Gbps
  - Storage should present as at least 3 or more disks to the OS, allowing for usage as CEPH storage nodes, or similar.
- **Network Interfaces** (note 1)
  - 4x 25 Gbps Ethernet Ports, implemented as two separate dual port NICs
  - Out-of-band Management Port

Note 1: At least 1 network interface must be capable of performing PXE boot and that network must be available to both the Jump / Test Host and each physical server.

<a name="4.2.2"></a>

## 4.2.2 Lab Network Hardware & Topology

Labs that are hosting multiple *Pods* should utilize a leaf / spine topology when interconnecting *Pods* or physical servers. This is especially important in the cases where the physical servers constituting a *Pod* are not located in the same physical rack or are not connected to the same leaf switch. At least one leaf switch will be provided for each *Pod*, with interface speeds matching the above server specifications.  In this context, the reference to the single leaf refers to the logical appearance of switch, compared to topologies providing 2 or more leaf switches to provide high availability.

Leaf switches must provide interfaces matching the physical server specifications above and northbound (spine connections) of 100 Gbps connections. Spine switches must provide the corresponding 100 Gbps interfaces to each leaf switch.  The minimum requirement is one spine switch.

The minimum networking configuration must provide at least VLANs to partition the various networks required for the reference implementation deployment and separation of each *Pod*, if multiple *Pods* are hosted within the labs.   

The *Pod* network topology should provide at least 2 networks with preallocated IP addressing schemes for the *out-of-band management* network and the *Public* network.  The *Public* network must be able to reach / access the public Internet.  At least IPv4 addresses must be available, ideally IPv6 address space should also be supported.

Remote users shall access the lab via a VPN gateway, that shall also provide basic security and separation from the public Internet.  Both the *Public* and *out-of-band management* networks shall be accessible through the VPN connection.

***EDITORS NOTE: Provide a figure showing the basic lab topology, include the VPN, Pod / Servers, Switch, and management / public networks.***

<a name="4.4"></a>

## 4.4 Lab Use Guidelines

**SETUP & Maintenance**

OPNFV will facilitate the need for lab procurement, as required, for projects which come into their front door for verification and validation.

Individual companies that donated a lab would be responsible for setup and maintenance of a community lab. Labs, once setup, will be shared and posted in a wiki https://wiki.opnfv.org/display/pharos/Community+Labs.

The wiki will contain information such as:
- Lab Location
- Number of physical and virtual PODS which are available
- Contact person
- Policy info for use
- Access instructions, include VPN
- Lab Topology
- Resource Availability

**N+1 Labs Use Strategy**

The "lab" concept could mean one physical POD or multiple PODs in a community lab.  In practice, a person requesting a lab can apply for multiple PODs, where POD 1 can be "Lab 1", POD 2+3 can be "Lab 2", etc, all subject to the availability of PODs. Each "Lab" can be used for different purpose such as "Reference Implementation (RI) Lab 1" (POD 1), "RI Lab 2" (POD 2+3), etc.

The requester for labs needs to know only the number of PODs that are needed.  Then, apply for use of PODs according to the requirement.

Talk to the Lab Owners if special hardware or topology requirements are needed, such as special NIC or hardware accelerators or if 8 servers in one POD is a different default setting from the lab settings.  The Lab Owner will check to see if lab config changes can be made to accommodate the test need.

**Lab Quantities and Duration of Lab Use**

There is no limit to the number of labs which can be secured, or the duration.  The limiting factor is resource available.  Lab Owners reserve the right to reclaim underutilized labs and reassign to other teams where there is demand for labs.  It is important that the Lab User have a schedule and plan in place to utilize the labs to retain the lab for testing.
