[<< Back](../)

# 3. NFVI Test Case Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Introduction](#3.1)
* [3.2 Assumptions](#3.2)
* [3.3 Requirement Type](#3.3)
* [3.4 Profile Catalog](#3.4)
* [3.5 Software & Hardware Reference](#3.5)
* [3.6 Options & Extensions](#3.6)
* [3.7 Measurement Criteria](#3.7)
  * [3.7.1 Storage and IOPS](#3.7.1)
* [3.8 Measurement Types](#3.8)
  * [3.8.1 Performance Measurements](#3.8.1)
  * [3.8.2 Resiliency Measurements](#3.8.2)
* [3.9 NFVI Test Cases](#3.9)

<a name="3.1"></a>
## 3.1 Introduction

> Scope of this chapter is to have a list of test cases needed (a detailed table of sort)

<a name="3.2"></a>
## 3.2 Assumptions

Content to be written:
- Assumptions:  Automatable, Integrated with CICD tool chain

<a name="3.3"></a>
## 3.3 Requirement Type

Content to be written:
-  Type of requirement:  Bare metal, API, etc

<a name="3.4"></a>
## 3.4 Profile Catalog

Content to be written:
-  Table showing Profile Catalog

<a name="3.5"></a>
## 3.5 Software & Hardware Reference

Content to be written:
- Identify SW Reference
- Identify HW Reference

<a name="3.6"></a>
## 3.6 Options & Extensions

Content to be written:
- Options Available / Configured
- Extensions Available / Configured

<a name="3.7"></a>
## 3.7 Measurement Criteria

Test validations will be corroborated, and confirmed, with direct comparison between measured results and documented non-functional requirements (NFRs) for applications, hardware and software configuration settings, and host systems.  Throughput, latency, concurrent connections/threads, are all examples of non-functional requirements which specify criteria which can be used to judge the operation of a system, rather than specific behaviours of the application which are defined by functional requirements.

This section attempts to summarize a categorical list of metrics used for test validations.  **For a complete list of metrics, and requirements, please refer to Reference Model**


<a name="3.7.1"></a>
### 3.7.1 Storage and IOPS

_**IOPS**_ validations for Storage, and/or Storage Extensions, will be included as part of the final NFVI verification, and validation, process.  

From a definition perspective, IOPS is the standard unit of measurement for I/O (Input/Output) operations per second. This measurement is a performance-based measurement and is usually seen written as**(1)**:

- **Total IOPS**: Average number of I/O operations per second.
- **Read IOPS**: Average number of read I/O operations per second.
- **Write IOPS**: Average number of write I/O operations per second.

For example, if you have a disk that is capable of doing a 100 IOPS, it means that it is theoretically capable of issuing a 100 read and or write operations per second.  This is in theory.  In reality, additional time is needed to actually process the 100 reads/writes.  This additional time is referred to as "latency", which reduces the total IOPS that is calculated, and measured.  Latency needs needs to be measured, and included in the IOPS calculation.  Latency will tell us how long it takes to process a single I/O request, and is generally in the 2 millisecond (ms) range per IO operation for a physical disk, through 20+ ms, at which time users will notice an impact in their experience**(2)**.  

Additional factors to consider when measuring IOPS:


- Take into consideration the percentage of Input (write) vs. Output (reads) operations, as Writes can be more resource intensive.
- Determine if Reads were performed from Cache, as this this may (will) result in faster performance, and faster IOPS.
- Confirm the storage types (Physical, RAID), as storage arrays with linear, or sequential reading/writing may (will) be slower.
- Identify the block size used, as using large block sizes vs. small block sizes can (will) impact IOPS performance.
- Determine Hard Disk Speeds (HDD in RPMs) used, as the higher the RPMS, the potential for faster IOPS performance.
- Quantify the number of disk controllers used to process the number of requested IO requests.
- Determine the specific work-load requirements, as this will dictate speed, controllers, disk RPM, and latency tolerances.  

For additional insight, or deeper understanding and reading of IOPS, refer to the references below.

<a name="3.8"></a>
## 3.8 Measurement Types

<a name="3.8.1"></a>
#### 3.8.1 Performance Measurements

**Objectives**

The NFVI performance measurements aim at assessing the performance of a given NFVI implementation on the execution plane (i.e., excluding VIM) by providing it with a set of significant metrics to be measured.

They should allow validating the performance of any software and/or hardware NFVI implementation as described in Reference Model.

Of course, they can also be used for other purposes, such as:
- fine tuning of software and/or hardware NFVI configuration (e.g., the number of cores dedicated to the DPDK vSwitch)
- comparing the performances of different software or hardware technologies (e.g., DPDK vSwitch vs hardware-offloaded vSwitch)
- assessing the performance impact of specific features (e.g., with or without encapsulation)


**Metrics Baseline**

For the purpose of validation, a baseline of the performance metrics is required for comparison with the results of their measurements on the NFVI implementation to be validated.

That baseline is a set of threshold values which could be determined by **measuring the performance metrics on Reference Implementations**.

The validation can then be based on simple pass/fail test results or on a grade (e.g., "class" A, B or C) provided by the combination of pass/fail results for 2 different threshold values of some (or all) metrics.


**Metrics Description**

Two categories of metrics are considered depending on whether they are related to either the VNF domain or the NFVI domain itself:

- Metrics related to the VNF domain are defined from VNF perspective (i.e., per VNFC, per vNIC, per vCPU...) and should concern VNF as well as NFVI actors. 
- Metrics related to the NFVI domain are defined per NFVI node ; their measurement is based on virtual workloads (i.e., VM or container) in order to reflect the performance of a NFVI node with a given profile ; they should only concern NFVI actors. 

The following table contains the list of performance metrics related to the VNF domain.

| Reference         | Name                           | Unit          | Definition/Notes                                             |
| ----------------- | ------------------------------ | ------------- | ------------------------------------------------------------ |
| vnf.nfvi.perf.001 | vNIC throughput                | bits/s        | Throughput per vNIC                                          |
| vnf.nfvi.perf.002 | vNIC latency                   | second        | Frame transfer time to vNIC at the throughput (vnf.nfvi.perf.001) |
| vnf.nfvi.perf.003 | vNIC delay variation           | second        | Frame Delay Variation (FDV) to vNIC at the throughput (vnf.nfvi.perf.001) |
| vnf.nfvi.perf.004 | vNIC simultaneous active flows | number        | Simultaneous active L3/L4 flows per vNIC before a new flow is dropped |
| vnf.nfvi.perf.005 | vNIC new flows rate            | flows/s       | New L3/L4 flows rate per vNIC                                |
| vnf.nfvi.perf.006 | Storage throughput             | bytes/s       | Throughput per virtual storage unit                          |
| vnf.nfvi.perf.007 | vCPU capacity                  | test-specific score | Compute capacity per vCPU                                    |

The following table contains the list of performance metrics related to the NFVI domain.

| Reference           | Name                           | Unit          | Definition/Notes                                           |
| ------------------- | ------------------------------ | ------------- | ---------------------------------------------------------- |
| infra.nfvi.perf.001 | Node network throughput        | bits/s        | Network throughput per node                                |
| infra.nfvi.perf.002 | Node simultaneous active flows | number        | Simultaneous active L3/L4 flows per node before a new flow is dropped |
| infra.nfvi.perf.003 | Node new flows rate            | flows/s       | New L3/L4 flows rate per node                              |
| infra.nfvi.perf.004 | Node storage throughput        | bytes/s       | Storage throughput per node                                |
| infra.nfvi.perf.005 | Physical core capacity         | test-specific score | Compute capacity per physical core usable by VNFs          |
| infra.nfvi.perf.006 | Energy consumption             | W             | Energy consumption of the node without hosting any VNFC    |
| infra.nfvi.perf.007 | Network energy efficiency      | W/bits/s      | Energy consumption of the node at the network throughput (infra.nfvi.perf.001), normalized to the measured bit rate |
| infra.nfvi.perf.008 | Storage energy efficiency      | W/bits/s      | Energy consumption of the node at the storage throughput (infra.nfvi.perf.004), normalized to the measured byte rate |
| infra.nfvi.perf.009 | Compute energy efficiency      | W/core        | Energy consumption of the node during compute capacity test (vnf.nfvi.perf.007 or infra.nfvi.perf.005), normalized to the number of physical cores usable by VNFs |


**MVP Metrics**

The following metrics should be considered as MVP:

- vnf.nfvi.perf.001,002,006,007
- infra.nfvi.perf.001,005,006,007,009


**Network Metrics Measurement Test Cases**

The network performance metrics are vnf.nfvi.perf.001-005 and infra.nfvi.perf.001-003,006.

The different possible test cases are defined by each of the 3 following test traffic conditions.

- **Test traffic path across NFVI**

  3 traffic path topologies should be considered:

  - ***North/South traffic***, between VNFCs whitin a node and outside NFVI  
    This can be provided by PVP test setup of ETSI GS NFV-TST009.

  - ***East/West intra-node traffic***, between VNFCs within a node  
    This can be provided by a V2V (Virtual-to-Virtual) test setup and, in some cases, by PVVP test setup of ETSI GS NFV-TST009.  

  - ***East/West inter-node traffic***, between VNFCs in different nodes      
    This can be provided by VPV (Virtual-Physical-Virtual) test setup and, in some cases, by PVVP test setup between 2 nodes.

- **Test traffic processing by NFVI**

  Different processing complexity applicable to the traffic crossing the NFVI should be considered, including especially (but not exhaustively):
  - ***L2 processing*** (Ethernet switching), possibly including VLAN tagging/mapping and encapsulation (e.g., VXLAN)
  - ***L3 processing*** (IP routing), possibly including L2 processing
  - ***L4 stateful processing*** (e.g., FW, NAT, SFC), also including L3 processing
  - ***Encryption*** (e.g., IPSec ESP tunneling)
    
- **Test traffic profile**

  Two different test traffic profiles should be considered according to the two VNF types that must be provided with network connectivity by the NFVI.

  - ***Forwarded traffic*** for L3/L4 forwarding VNF (e.g., PGW, FW)

    It is based on ETSI GS NFV-TST009 and it should be:

    -  **bidirectional UDP traffic** with **0.001%** frame loss ratio, **300B** average frame size, **10k** L3/L4 flows,
    - between a **traffic generator** and a **traffic receiver** through a **L3 forwarding** pseudo-VNF with sufficient capacity not to be the test bottleneck.

    Latency and delay variation measurement should be the 99th percentile of measured values for one-way frame transfer (i.e. from generator to receiver).

    The main OPNFV test tools candidates for that purpose are NFVbench and VSPerf.

    > _**Note:** to be studied whether additional frame sizes and flows number should be considered_
    
  - ***Client-server traffic*** for L4/L7 endpoint VNF (e.g., MME, CDN)

    It should be:

    - **bidirectional TCP traffic** with **1400B** maximum frame size, **5k** TCP sessions,
    - between **2 TCP client&server endpoints**, one or both as pseudo-VNF, with sufficient capacity not to be the test bottleneck.
        
    *Note*: the maximum TCP frame size can be forced by configuring TCP endpoint link MTU.

    The main OPNFV test tools candidates for that purpose are Functest (VMTP and Shaker) and Yardstick (TC011 and TC083).
        
    > _**Note:** to be studied whether metrics related to latency and flows for that traffic profile should be considered (how? with UDP and/or ICMP test traffic in addition?)_

The combination of each of those 3 test conditions types and the different NFVI profiles results in a wide matrix of test cases (potentially more than 50 cases).
Furthermore, these test cases should be combined with the different metrics resulting in a huge number of measurements (potentially more than 400 measurements).
For the efficiency of the validation, only the most relevant combinations should be kept.

This optimization should be based on the following principles:

1. NFVI domain metrics measurement: on PVP topology only
2. Metrics measurement with forwarded traffic: with no L4 stateful processing
3. Basic and Compute intensive profiles metrics measurement: client-server traffic profile only
4. Flows & latency related metrics measurement: for PVP only

The following table proposed a possible optimized matrix model of the test cases against the metrics to be measured. 

|                     | **NFVI Profiles**   | **B & C**      |                |                |                | **N**         |                |
| ------------------- | ------------------- | -------------- | -------------- | -------------- | -------------- | ------------- | -------------- |
|                     | **Test Cases**      | V2V - L2 - SRV | VPV - L3 - SRV | PVP - L2 - SRV | PVP - L4 - SRV | PVP - L2- SRV | PVP - L2 - FWD |
|                     |                     |                |                |                |                |               |                |
| **MVP Metrics**     | vnf.nfvi.perf.001   | 50Gbps         | 20Gbps         | 20Gbps         | 10Gbps         | 40Gbps        | 40Gbps         |
|                     | vnf.nfvi.perf.002   | n/a (4)        | n/a (4)        | ?              | ?              | ?             | 0.5ms          |
|                     | infra.nfvi.perf.001 | n/a (1)        | n/a (1)        | 40Gbps         | 20Gbps         | 60Gbps        | 80Gbps         |
|                     | infra.nfvi.perf.007 | n/a (1)        | n/a (1)        | ? W/Gbps       | ? W/Gbps       | ? W/Gbps      | ? W/Gbps       |
|                     |                     |                |                |                |                |               |                |
| **Non-MVP Metrics** | vnf.nfvi.perf.003   | n/a (4)        | n/a (4)        | ?              | ?              | ?             | 1ms            |
|                     | vnf.nfvi.perf.004   | n/a (4)        | n/a (4)        | ?              | ?              | ?             | 500k           |
|                     | vnf.nfvi.perf.005   | n/a (4)        | n/a (4)        | ?              | ?              | ?             | 100kfps        |
|                     | infra.nfvi.perf.002 | n/a (1)        | n/a (1)        | ?              | ?              | ?             | 1G             |
|                     | infra.nfvi.perf.003 | n/a (1)        | n/a (1)        | ?              | ?              | ?             | 200kfps        |

*Table notes*:
- Values are only indicative (see "Metrics Baseline" below)
- L2/L3/L4 refers to network processing layer
  - L2 for Ethernet switching
  - L3 for IP routing
  - L4 for IP routing with L4 stateful processing (e.g. NAT)
- SRV/FWD refers to the traffic profile (and pseudo-VNF type implied)
  - SRV for client-server traffic (and L4/L7 endpoint pseudo-VNF)
  - FWD for forwarded traffic (and L3/L4 forwarding pseudo-VNF)


**Energy Metrics Measurement Test Cases**

Energy metrics (infra.nfvi.perf.006-009) should be considered carefully for NFVI validation since energy consumption may vary a lot across processor architectures, models and power management features.

They mainly enable to have metrics available regarding NFVI environment footprint. They also allow energy-based comparison of different NFVI software implementations running on a same physical NFVI hardware implementation.

OPNFV tool as possible basis: https://docs.opnfv.org/en/latest/testing/ecosystem/energy-monitoring.html


**Storage Metrics Measurement Test Cases**

Metric (MVP): vnf.nfvi.perf.006 and infra.nfvi.perf.004,008

Main OPNFV test tool candidates: Yardstick (TC 005), StorPerf

> _**Note:** to be completed _


**Compute Metrics Measurement Test Cases**

The compute performance metrics are vnf.nfvi.perf.007 and infra.nfvi.perf.004,009.

Each compute performance test should be performed with all vCPU of the node running multiple parallel workloads and the result is then normalized:
- to the number of vCPU, for the vCPU capacity measurements (vnf.nfvi.perf.007)
- to the number of physical core usable by VNFs, for the physical core capacity and compute energy efficiency measurements infra.nfvi.perf.004,009)

Main OPNFV test tool candidate: Yardstick (TC014)

> _**Note:** to be studied: how to define the different possible test cases, especially the different workload profiles (i.e., pseudo-VNF) to consider_


<a name="3.8.2"></a>
#### 3.8.2 Resiliency Measurements


<a name="3.9"></a>
## 3.9 NFVI Test Cases

> we need to have list of NFVI test cases in here.
