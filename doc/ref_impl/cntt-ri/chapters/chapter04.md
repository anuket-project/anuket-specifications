[<< Back](../)

# 4. Lab Requirements

<a name="toc"></a>
## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Lab Requirement](#4.2)
* [4.3 Lab Topology](#4.3)
* [4.4 Lab HW Spec](#4.4)
* [4.5 Lab Use Guidelines](#4.5)


<a name="4.1"></a>
## 4.1 Introdcution


<a name="4.2"></a>
## 4.2 Lab Requirement

- Controller Nodes:
  - 3 x
    - 2x dual-port 10Gbps NIC.
    - 2.2GHz 14C/28T.
    - 256GB RAM.
    - 10TB HDD.
    - 3.2TB SSD.
- Compute Node
  - 10x
    - 2x dual-port 25Gbps NIC.
    - 2.2GHz 24C/48T.
    - 512GB RAM.
    - 2TB HDD
    - Supports 2x Nodes for B/N/C flavors
- Jump/Baremetal manager
  - 1x
    - 2x dual-port 10Gbps NIC.
    - 2.2GHz 14C/28T.
    - 256GB RAM.
    - 10TB HDD
- Networking
  - 1x Spine Switch
    - Total: 32x100G
  - 2x Leaf Switch
    - 48 x 25/10G
    - 6 x 100G
- 1x 48u Rack
- Cables and Transcievers

<a name="4.3"></a>
## 4.3 Lab Topology


<a name="4.4"></a>
## 4.4 Lab HW Spec


<a name="4.5"></a>
## 4.5 Lab Use Guidelines

**SETUP & Maintenance**

OPNFV will facilitate the need for lab procurment, as required, for projects which come into their front door for verification and validation.

Individual companies that donated a lab would be responsible for setup and maintenance of a community lab. Labs, once setup, will be shared and posted in a wiki https://wiki.opnfv.org/display/pharos/Community+Labs.

The wiki will contain information such as:
- Lab Location
- Number of physical and virtual PODS which are available
- Contact person
- Policy info for use
- Access instructions, include VPN
- Lab Topolgy
- Resrouce Availability

**N+1 Labs Use Strategy**

The "lab" concept could mean one physical POD or multiple PODs in a community lab.  In practice, a person requesting a lab can apply for multiple PODs, where POD 1 can be "Lab 1", POD 2+3 can be "Lab 2", etc, all subject to the availability of PODs. Each "Lab" can be used for different purpose such as "Reference Implementation (RI) Lab 1" (POD 1), "RI Lab 2" (POD 2+3), etc.

The requestor for labs needs to know only the number of PODs that are needed.  Then, apply for use of PODs according to the requirement.

Talk to the Lab Owners if special hardware or topology requirements are needed, such as special NIC or hardware accelerators or if 8 servers in one POD is a different default setting from the lab settings.  The Lab Owner will check to see if lab config changes can be made to accommodate the test need.

**Lab Quantities and Duration of Lab Use**

There is no limit to the number of labs which can be secured, or the duration.  The limiting factor is resource available.  Lab Owners reserve the right to reclaim underutilized labs and reassign to other teams where there is demand for labs.  It is important that the Lab User have a schedule and plan in place to utilize the labs to retain the lab for testing.
