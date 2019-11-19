[<< Back](../../ref_model)
# 8 Compliance, Verification, and Certification
<!--<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>-->
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction.](#8.1)
* [8.2 Requirements.](#8.2)
   * [8.2.1 Reference Implementations Requirements.](#8.2.1)
   * [8.2.2 Certification Requirements.](#8.2.2)
   * [8.2.3 Badging Requirements.](#8.2.3)
   * [8.2.4 Test Cases Selection Requirements.](#8.2.4)
* [8.3 Guidelines.](#8.3)
  * [8.3.1 Entry/Exit Criteria.](#8.3.1)
  * [8.3.2 Quality Assurance.](#8.3.2)
  * [8.3.3 Test Categories.](#8.3.3)

<a name="8.1"></a>
## 8.1 Introduction

Having deterministic NFVI metrics and capabilities expected for a given profile, allows NFVI solutions to be characterised, validated, and verified against those metrics and capabilities, and therefore report the results in a standard format. This will allow operators to understand in depth the details and the differentiation a given solution can provide against other options.

Additionally standardising on infrastructure profiles allows VNFs to be characterised, validated, and certified against a given profile by using reference NFVI implementations as demonstrated in Figure below. Where VNFs are using multiple profiles (different VNF-C written against different profiles), multiple Reference NFVI implementations should be used.

<a name="8.2"></a>
## 8.2 Requirements

<a name="8.2.1"></a>
### 8.2.1 Reference Implementations Requirements

For compliance, verification, and certification of NFVI solutions provided for a given NFVI Profile, it is required to have a reference implementation of each profile so it can be used for compliance, validation, and certification purposes.

Those reference implementations need to reflect on their corresponding profiles and deliver all metrics and capabilities promised. They need to use open source components. Figure below shows the various reference implementations required for each profile, they are:

- NFVI SW Reference implementation.
- NFVI HW Reference implementation.
- VNF reference implementation.

<p align="center"><img src="../figures/ch8_NFVI_ref_profiles_impementations.jpg" alt="NFVI RI Profiles" title="NFVI RI Profiles" width="70%"/></p>
<p align="center"><b>Figure 8-1:</b> Reference NFVI Profiles Implementation and Reference VNFs Implementations for each profile.</p>

<a name="8.2.2"></a>
### 8.2.1 Certification Requirements

<a name="8.2.2.1"></a>
#### 8.2.2.1 Certification of Vendor supplied NFVI solutions.

Infrastructure Abstraction and Profiling allows NFVI SW vendors to provide solutions that are suitable for a given profile (as demonstrated in Figure below). Having NFVI solutions tailored towards a given profile makes it easier to verify, certify and test that solution against that profile using the reference implementation of the profile mentioned previously.

<p align="center"><img src="../figures/ch8_NFVI_vendor_supplied_sw_solutions.jpg" alt="NFVI Vendor SW Solutions" title="NFVI Vendor SW Solutions" width="70%"/></p>
<p align="center"><b>Figure 8-2:</b> Vendor Supplied NFVI SW Solutions</p>

Similarly, Infrastructure Abstraction and Profiling allows NFVI HW vendors to provide solutions that are suitable for a given profile (as demonstrated in Figure below). Having NFVI hardware solutions tailored towards a given profile makes it easier to verify, certify and test that hardware solution against that profile using the reference implementation of the profile mentioned previously.

<p align="center"><img src="../figures/ch8_NFVI_vendor_supplied_hw_solutions.jpg" alt="NFVI Vendor HW Solutions" title="NFVI Vendor HW Solutions" width="70%"/></p>
<p align="center"><b>Figure 8-3:</b> Vendor Supplied NFVI HW Solutions</p>

Figure below demonstrates how a given NFVI SW solution can be validated and certified against a given profile by using a reference HW implementation and a reference NFVI implementation.

<p align="center"><img src="../figures/ch8_NFVI_certifying_vendor_sw_solutions.jpg" alt="Certifying NFVI Vendor SW Solutions" title="Certifying NFVI Vendor SW Solutions" width="70%"/></p>
<p align="center"><b>Figure 8-4:</b> Certifying Vendor NFVI SW Solutions</p>

Similarly, to characterise, validate, and certify NFVI HW solution against a given profile, both NFVI SW reference implementation and a VNF reference implementation are needed as demonstrated as in Figure below.

<p align="center"><img src="../figures/ch8_NFVI_certifying_vendor_hw_solutions.jpg" alt="Certifying NFVI Vendor HW Solutions" title="Certifying NFVI Vendor HW Solutions" width="70%"/></p>
<p align="center"><b>Figure 8-5:</b> Certifying Vendor NFVI HW Solutions</p>

Finally, NFVI vendors can characterise, validate, and certify an entire NFVI platform (both SW & HW) against a given profile by using a VNF reference implementation as shown in Figure below.

<p align="center"><img src="../figures/ch8_NFVI_certifying_vendor_swhw_solutions.jpg" alt="Certifying NFVI Vendor SW/HW Solutions" title="Certifying NFVI Vendor SW/HW Solutions" width="70%"/></p>
<p align="center"><b>Figure 8-6:</b> Certifying Vendor NFVI SW/HW Solutions</p>

<a name="8.2.2.2"></a>
#### 8.2.2.2 Certification of Vendor supplied VNF solutions.

<p align="center"><img src="../figures/ch8_certifying_vendor_supplied_vnfs.jpg" alt="Certifying Vendor Supplied VNFs" title="Certifying Vendor Supplied VNFs" width="70%"/></p>
<p align="center"><b>Figure 8-7:</b> Certifying Vendor Supplied VNFs</p>


<a name="8.2.3"></a>
### 8.2.3 Badging Requirements

> to be added

<a name="8.2.4"></a>
### 8.2.4 Test Case Selection Requirements

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
| `req.tests.13` | Maturity       | Test projects providing test cases **must** be mature and active to ensure availability and maintenance of test case implementations over an extended period of time. Criteria for maturity include code quality, test coverage, release history of the project, release cadence, and contributor base. |
| `req.tests.14` | Scope          | Test cases **must** pass on all reference implementations of the targeted reference architecture. |
| `req.tests.15` | Scope          | Test cases **must** be traceable to a requirement based on the reference model or a reference architecture. |


<a name="8.3"></a>
## 8.3 Guidelines


<a name="8.3.1"></a>
## 8.3.1 Entry/Exit Criteria

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

<a name="8.3.2"></a>
### 8.3.2 Quality Assurance

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

<a name="8.3.3"></a>
### 8.3.3 Test Categories | Cases

The following five test categories have been identified as minimal testing required to verify NFVI interoperability to satisfy the needs of VNF developer teams.

- **Baremetal**: Validate Control and compute nodes hardware.
- **VNF**: After VNF on boarded we are validating end to end resources like Tenant, Network (L2/L3), CPU Pining, security policies, Affinity anti-affinity roles and flavours etc.
- **Compute Component**: Validate/Document VMs status and connectivity result after performing each of listed steps. Best candidate for this testing would be identify compute node that holds VMs which has l2 and l3 connectivity.
- **Control Plane Component**: Validating different Control plane components and API.
- **Security**: Validating user RBAC Roles and User group policies.