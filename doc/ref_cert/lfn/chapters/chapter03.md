[<< Back](../)

# 3. NFVI Test Case Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Introduction](#3.1)
* [3.2 Measurement Criteria](#3.2)
  * [3.2.1 Storage and IOPS](#3.2.1)
* [3.3 Measurement Types](#3.3)
  * [3.3.1 Performance & Resiliency Measurements](#3.3.1)
* [3.4 NFVI Test Cases](#3.4)

<a name="3.1"></a>
## 3.1 Introduction

> Scope of this chapter is to have a list of test cases needed (a detailed table of sort)

<a name="3.2"></a>
## 3.2 Measurement Criteria

Test validations will be corroborated, and confirmed, with direct comparison between measured results and documented non-functional requirements (NFRs) for applications, hardware and software configuration settings, and host systems.  Throughput, latency, concurrent connections/threads, are all examples of non-functional requirements which specify criteria which can be used to judge the operation of a system, rather than specific behaviours of the application which are defined by functional requirements.

This section attempts to summarize a categorical list of metrics used for test validations.  **For a complete list of metrics, and requirements, please refer to Reference Model**


<a name="3.2.1"></a>
### 3.2.1 Storage and IOPS

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

<a name="3.3"></a>
## 3.3 Measurement Criteria

<a name="3.3.1"></a>
### 3.3.1 Performance & Resiliency Measurements

The following table contains a lists of performance measurements, and/or capabilities, to be captured where feasible during test validations.  More specifically, the table contains:

- Exposed performance metrics per VNFC, vNIC or vCPU.  Specifically exposed performance metrics use a single VNF (PVP) dataplane test setup in a single host.  (e.g. _\*e.nfvi.per.met\*_)

- Monitoring capabilities available by NFVI.  The availability of these capabilities will be determined by the instance type used by the workloads. (e.g. _\*i.nfvi.mon.cap\*_)

- Internal performance metrics per NFVI node.  Specifically internal performance metrics use a baseline (Phy2Phy) dataplane test setup in a single host. (e.g. _\*i.nfvi.per.met\*_)

> _**NOTE**:  Refer to RM Chapter 4 for a list performance measurements and capabilities internal to the infrastructure._


| Ref                | NFVI Measurement             | Unit                | Definition/Notes                                             |
| ------------------ | ------------------------- | ------------------- | ------------------------------------------------------------ |
| e.nfvi.per.met.001 | Network throughput        | frames/s            | Throughput (aligned with ETSI GS NFV-TST 009 [2]) |
| e.nfvi.per.met.002 | Network latency           | second              | 99th percentile of one-way frame transfer time at throughput offered load level (aligned with ETSI GS NFV-TST 009 [2]) |
| e.nfvi.per.met.003 | Network Delay Variation   | second              | 99th percentile of Frame Delay Variation (FDV) at throughput offered load level (aligned with ETSI GS NFV-TST 009 [2]) |
| e.nfvi.per.met.004 | Simultaneous active flows | number              | Max simultaneous active L4 flows per vNIC before a new flow is dropped |
| e.nfvi.per.met.005 | New flows rate            | flows/s             | Max new L4 flow rate per vNIC                                |
| e.nfvi.per.met.006 | Storage throughput        | bytes/s or IO/s     | Max throughput per virtual block storage unit assigned to VNFC |
| e.nfvi.per.met.007 | Processing capacity       | test-specific       | Processing capacity test-specific score per vCPU and with all vCPU running multiple parallel workloads|
| i.nfvi.mon.cap.001 | Host CPU usage |  | Per Compute node. It needs to Maps to ETSI NFV-TST 008[1] clause 6, processor usage metric (NFVI exposed to VIM) and ETSI NFV-IFA 027 Mean Virtual CPU usage and Peak Virtual CPU usage (VIM exposed to VNFM). |
| i.nfvi.mon.cap.002 | Virtual compute resource CPU usage |  | QoS enablement |
| i.nfvi.mon.cap.003 | Host CPU utilization |  | Per Compute node. It needs to map to ETSI NFV-IFA 027 Mean Virtual CPU usage and Peak Virtual CPU usage (VIM, exposed to VNFM). |
| i.nfvi.mon.cap.004 | Virtual compute resource CPU utilization |  | Range (min, max) per VNFC |
| i.nfvi.mon.cap.005 | Monitoring of external storage IOPS | Yes/No | Transcoding Acceleration |
| i.nfvi.mon.cap.006 | Monitoring of external storage throughput | Yes/No | Programmable Acceleration |
| i.nfvi.mon.cap.007 | Monitoring of external storage capacity | Yes/No |  |
| i.nfvi.per.met.001 | Network throughput | frames/s | Throughput (aligned with ETSI GS NFV-TST 009 [2]) |
| i.nfvi.per.met.002 | Simultaneous active flows | number | Max simultaneous active L4 flows per node before a new flow is dropped |
| i.nfvi.per.met.003 | New flows rate               | flows/s  | Max new L4 flow rate per node                                |
| i.nfvi.per.met.004 | Processing capacity | test-specific | Processing capacity test-specific score per core and with all cores running multiple parallel workloads|
| i.nfvi.per.met.005 | Energy consumption           | W                   | Maximum energy consumption of the node without hosting any VNFC (but fully ready for it) |
| i.nfvi.per.met.006 | Network energy efficiency    | W/bits/s            | Energy consumption for the node at throughput offered load level, normalized to the bit rate |
| i.nfvi.per.met.007 | Processing energy efficiency | W/core | Energy consumption for the node during processing capacity test-specific score with all cores running multiple parallel workloads (i.nfvi.per.met.004), normalized to cores usable by VNFs |



<a name="3.4"></a>
## 3.4 NFVI Test Cases

> we need to have list of NFVI test cases in here.