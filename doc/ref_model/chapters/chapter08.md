[<< Back](../../ref_model)
# 8 Compliance, Verification, and Certification
<!--<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>-->
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction.](#8.1)
* [8.2 Requirements.](#8.2)
   * [8.2.1 Certification Requirements.](#8.2.1)
   * [8.2.2 Badging Requirements.](#8.2.2)
   * [8.2.3 Test Cases Selection Requirements.](#8.2.3)
* [8.3 Measurements.](#8.3)
   * [8.3.1 Performance & Resiliency Measurements.](#8.3.1)
   * [8.3.2 Storage and IOPS.](#8.3.2)
* [8.4 Guidelines.](#8.4)
  * [8.4.1 Entry/Exit Criteria.](#8.4.1)
  * [8.4.2 Quality Assurance.](#8.4.2)
  * [8.4.3 Test Categories.](#8.4.3)
* [8.5 References.](#8.5)

<a name="8.1"></a>
### 8.1 Introduction

<a name="8.2"></a>
### 8.2 Requirements


<a name="8.2.1"></a>
### 8.2.1 Certification Requirements

<a name="8.2.2"></a>
### 8.2.2 Badging Requirements

<a name="8.2.3"></a>
### 8.2.3 Test Case Selection Requirements

This section lists requirements test cases must fulfill to be eligible for
inclusion in the NFVI and/or VNF compliance test suite.  These requirements act
as a checklist to gate the inclusion of test cases.


| Ref # | Category   | Description |
|----|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `req.tests.01` | Implementation | Test cases and tools **must** be implemented in an open source project and publicly available. |
| `req.tests.02` | Implementation | Test cases and tools **should** be self-contained and not require downloading additional data from external systems at runtime. |
| `req.tests.03` | Implementation | Test cases and tools **must not** require dynamic interaction with external systems or resources, e.g., of OPNFV, LFN or others. |
| `req.tests.04` | Implementation | Test cases and tools **must** generate machine- and human-readable output, i.e. logs and result files. |
| `req.tests.05` | Implementation | The execution of all test case **must** be idem-potent, i.e., test cases handle setup and teardown of resources and revert state changes of the system under test performed by the test case. |
| `req.tests.06` | Implementation | Test cases and tools **must** run against a fully deployed and operational system under test, i.e., not isolated individual components. |
| `req.tests.07` | Implementation | Test cases and tools **must not** require un-merged patches to the relevant upstream projects. |
| `req.tests.08` | Implementation | Test tools **must** allow selective execution of individual test cases even if test cases are part of a larger test suite. |
| `req.tests.09` | Implementation | NFVI tests and test tools **must** run independently of the method of NFVI platform installation. |
| `req.tests.10` | Implementation | NFVI tests and test tools **must** run independently of platform components not specified in the corresponding reference archiecture, i.e., allowing different backend implementations such as storage backends or SDN controllers. |
| `req.tests.11` | Documentation  | Test cases and tools **must** be documented, comprising a reference to all targeted reference architectures, pre- and post-conditions, basic test flow execution, and pass/fail criteria. |
| `req.tests.12` | Documentation  | Documentation of test cases and tools **must** be publicly available. |
| `req.tests.13` | Maturity       | Test projects providing test cases **must** be mature and active to ensure availability and maintenance of test case implementations over an extended period of time. Criteria for maturity include code quality, test coverage, release history of the project, release cadence, and contributer base. |
| `req.tests.14` | Scope          | Test cases **must** pass on all reference implementations of the targeted reference architecture in the OPNFV CI/CD pipeline. |
| `req.tests.15` | Scope          | Test cases **must** be traceable to a requirement based on the reference model or a reference architecture. |

<a name="8.3"></a>
### 8.3 Measurements

Test validations will be corroborated, and confirmed, with direct comparison between measured results and documented non-functional requirements (NFRs) for applications, hardware and software configuration settings, and host systems.  Throughput, latency, concurrent connections/threads, are all examples of non-functional requirements which specify criteria which can be used to judge the operation of a system, rather than specific behaviours of the application which are defined by functional requirements.

This section attempts to summarize a categorical list of metrics used for test validations.  **For a complete list of metrics, and requirements, please refer to Reference Model**

<a name="8.3.1"></a>
### 8.3.1 Performance & Resiliency Measurements

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

<a name="8.3.2"></a>
### 8.3.2 Storage and IOPS

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


<a name="8.4"></a>
## 8.4 Guidelines


<a name="8.4.1"></a>
## 8.4.1 Entry/Exit Criteria

**Entrance Criteria for testing and validation includes _Demonstration of Reference Architecture Implementation and Delivery of the following_:**
1. **Design & Requirements**
   - Design, Configuration, Features, SLAs, and Capability documentation complete
   - Users stories / Adherence to CNTT Model principles and guidelines
   - Chosen Reference Architecture Matches a Reference Architecture from the product catalog
2. **Environment**
    -  Lab assets/resources and respective s/w rev levels are specified, with confirmation of compatibility across external systems
    -  Tenant needs identified
    -  All connectivity, network, image, VMs, delivered with successful pairwise tests
    -  Lab instrumented for proper monitoring
3. **Planning & Delivery**
    - Kickoff / Acceptance Criteria reviews performed
    - Delivery commitments, timelines, and cadence accepted
    - Confirm backward compat. across software/flavour rev levels
4. **Data / VNFs / Security**
    - Images, Heat Templates, Preload Sheets available
    - Images uploaded to tenant space
    - External system test data needs identified
    - Owners (NFVI, VNF, PTL, etc) documented
    - Security Compliance Satisfied (_Refer to_ CNTT Chapter 7 Security _for additional tests, scans, and vulnerabilities validations_)
5. **Test Case Contributions**
    - VNF Developer/Supplier validations to be performed documented and supplied
    - NFVi validations to be performed supplied (e.g. echo, manifest)
    - Test to ensure users are added and have correct privileges for the tenant
    - Test to ensure quota against submitted request for the respective tenant
    - Test to ensure custom flavours against submitted request for respective tenants

Exit Criteria includes Demonstration of Compliance, Verification, Performance, and Validation, of Reference Architecture Implementation, and Delivery of the following:

1. **Certification tenants**
    - All Test Cases have a status of Passed, Failed, N/A or Out-scoped.
    - All Severity 1 and Severity 2 issues are resolved.
    - All Issues have been Resolved or the Project/Component Team has voted unanimously for a Conditional Certification.
    - Known defects, or issues, are clearly documented and furnished to Telco providers with certification notes.
    - Certification Notification(s) issued.
1. **Operational Considerations**
    - Orchestration capabilities verified to be working as expected.
    - Fabric setup/configuration validations successfully passed.
    - Openstack API endpoint is reachable and working for that zone.
    - Compute zones and cinder types verified.
    - Standard images verified to exist (and usable).
    - Network object created (and working, as in IPs are bindable and usable).
    - Resolver overlay/DNS traffic/port 53 overlay on gateway is working properly.
    - Designate is working, domain preferably created, and maybe test A record created/verified to be resolvable.
    - Standard NTP servers are working and verified (using tenant's CIDR source IP).
    - NFVI/VNF is tested at steady state and high load.
    - Continuously monitored to ensure SLAs are met and used as feedback to load/perf tests.
    - Passing Interoperability Validations: 
      1. Compatibility Checks (e.g. documented s/w, driver rev levels, etc, in use and confirmed compatible between Platform and VNF); 
      1. Integration Checks (e.g. empirical validation confirming positive performance and stability between Platform and VNF; for example, packet loss within acceptable tolerances)
1. **End User Consideration**
    - Component redundancy to ensure graceful updates without disruption of services
    - Thin provisioning storage should handle actual full quota usage cases
    - Load balancing should support elasticity
    - Auto-healing databases (any component related db) when out of sync
    - Obvious, but, supports all required network functionality (all protocols, service chaining, VLAN trunking, QoS marking, probe/mirror, etc)
    - Supports NFV migration
    - Supports snapshots and backups of large volumes
    - Pre-check or audit failures during NFV deployment should allow follow-up mitigation, when possible, rather than killing deployment and rolling back

<a name="8.4.2"></a>
### 8.4.2 Quality Assurance

**Assumptions**
NFVI+VNF testing will be considered **Testable** if the follow qualifiers are present in a test execution, and subsequent result:

- Ability to perform Conformance, or Verification of Artifacts to ensure designs (RM/RA/RI) are delivered per specification

- Ability to Control (or manipulate), manifestations of RM/RA/RI for the purposes to adjust the test environment, and respective cases, scenarios, and apparatus, to support actual test validations

- Ability to monitor, measure, and report, Validations performed against a target, controlled system under test

In addition, respective Entrance criteria is a prerequisite which needs to be satisfied for NFVI+VNF to be considered **Testable**.

**Dependencies**
NFVI+VNF verification will rely upon test harnesses, test tools, and test suites.  

- NFVI+VNF verifications will be performed against well defined instance types consisting of a HW and SW Profile, Configured Options, and Applied Extensions (See image.)

<p align="center"><img src="../figures/ch8_NFVI_VNF_Instance_Type.jpg" alt="scope" title="NFVI+VNF Instance Type" width="100%"/></p>

<p align="center"> <b>Figure 8-1:</b> NFVI+VNF Instance Type.</p>

<a name="8.4.3"></a>
### 8.4.3 Test Categories | Cases

The following five test categories have been identified as minimal testing required to verify NFVI interoperability to satisfy the needs of VNF developer teams.

- **Baremetal**: Validate Control and compute nodes hardware.
- **VNF**: After VNF on boarded we are validating end to end resources like Tenant, Network (L2/L3), CPU Pining, security policies, Affinity anti-affinity roles and flavours etc.
- **Compute Component**: Validate/Document VMs status and connectivity result after performing each of listed steps. Best candidate for this testing would be identify compute node that holds VMs which has l2 and l3 connectivity.
- **Control Plane Component**: Validating different Control plane components and API.
- **Security**: Validating user RBAC Roles and User group policies.

<a name="8.5"></a>
### 8.5 References

1. _IOPS - I/O (Input/Output) operations per second_, by Vangie Beal.  Retrieved from https://www.webopedia.com/TERM/I/IOPS.html on 9/18/2019.
2. _The ultimate IOPS cheat sheet!_, by Bas van Kaam.  Retrieved from https://www.basvankaam.com/2014/07/29/the-ultimate-iops-cheat-sheet/ on 9/18/2019.
3. _An explanation of IOPS and latency_, by Dimitris Krekoukias.  Retrieved from http://recoverymonkey.org/2012/07/26/an-explanation-of-iops-and-latency/ on 9/18/2019.