[<< Back](../../ref_model)
# 8 Annex
<!--<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>-->
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction.](#8.1)
* [8.2 Generic Test Cases.](#8.2)
* [8.3 Architecture specific test cases (if needed).](#8.3)
  * [8.3.1 OpenStack (OS).](#8.3.1)
  * [8.3.2 Kubernetes (K8s).](#8.3.2)

<!--
* [8.4 General Thoughts](#8.4)
-->

<a name="8.1"></a>
## 8.1 Introduction

This Chapter 8 Annex contains test cases to be executed during NFVI validations to ensure a Reference Implementation of CNTT Reference Architecture is in compliance.  The Linux Foundation Networking (LFN) OPNFV Verified Program (OVP), in partnership with the Compliance Verification Committee (CVC), will provide tracking and governance for RM/RA/RI verifications.

<a name="8.2"></a>
## 8.2 Generic Test Cases

The following test projects, and their respective test cases, must be executed with each reference implementation. More specific test cases are listed below, which may be a subset of test cases run within these test suites listed.

<a name="8.3"></a>
## 8.3 Architecture Specific Test Cases (if needed)

<a name="8.3.1"></a>
### 8.3.1 OpenStack (OS)

**FuncTest**

FuncTest test suites must be run as part of NFVi validation against all OpenStack based reference implementations. At a minimum, FuncTest executions will include execution of the functest-smoke and functional-benchmarking test suites.

Additional Resources for FuncTest:
- [Project Description](https://wiki.opnfv.org/display/functest/Opnfv+Functional+Testing#OpnfvFunctionalTesting-Testcases)
- [User Guide](https://opnfv-functest.readthedocs.io/en/stable-hunter/testing/user/userguide/index.html)
- [Test Suite Overview](https://opnfv-functest.readthedocs.io/en/stable-hunter/testing/user/userguide/test_overview.html)

Example, or Reference, Functest Status Reporting Artifacts:
- [Rally Verification](http://artifacts.opnfv.org/functest/functest-opnfv-functest-smoke-iruya-tempest_full-run-259/results/tempest_full/tempest-report.html)
- [Rally Tasks](http://artifacts.opnfv.org/functest/functest-opnfv-functest-benchmarking-iruya-rally_full-run-169/results/rally_full/rally_full.html)

**Baremetal**

**SUMMARY:** Control and compute node hardware, bios, firmware, network interfaces, and base operating system configuration must be validated.
- Interface - Validate nic status for all member in bond1 group
- Interface - MTU speed for bond1 interface
- Grub - SR-IOV is enabled
- Numa - Validate numa configuration on each node
- Numa - Validate total memory available is distributed equally across numa boundaries
- VFs - Validate VF creation on each PCI SYS Interface.
- Modules - Validate necessary kernel modules are loaded
- OS: IPTables are enabled.
- OS: System time on all hosts is synchronized to a common set of NTP servers
- OS: Dedicate mount point for following file system
  - /var/log
  - /var/lib/nova
- OS: Validate Huge Pages are configured and enabled based on target infrastructure. (not available for all flavours)
  - Validate Hugepage size configuration
  - Validate Hugepage total number configuration
- OS: Validate proxy/iptables implementation
- Validate proxy configuration after server reboot
- Validate routing table after server reboot
- BIOS: Validate Boot order
- Validate Kernel version against Reference Implementation
- Validate BIOS version against Reference Implementation
- Validate Firmware version against Reference Implementation
- CPU Performance mode validation
- Compare CPU verification server specs

**VNF Interoperability**

**SUMMARY:** Validation of end to end openstack resources, including: Tenant, Network (L2/L3), CPU Pinning, Security Policies, Affinity/Anti-Affinity, Roles, Flavours, etc.

- Validate security profiles against a reference VNF
  - Validate blocking ICMP traffic blocks two reference VNFs from pinging each other
  - Validate allowing ICMP traffic allows two reference VNFs from pinging each other
- Validate image upload to glance
- Validate host aggregate creation
- Validate assignment of nodes to host aggregate
- Provider Network - SRIOV - VLAN (where applicable, allowing a device, such as a network adapter, to separate access to its resources among various PCIe hardware functions)
- OAM Network
- Create routers across 2 tenant network (optional - i.e. create virtual router on two different tenants and validate the network connectivity between the two)
- Validate anti-affinity and affinity rules
- Validate user ability to force VM landing on given hypervisor host
- Create VMs using flavour defined above and Attached ceph storage
- Validate VM is able to extract meta data
- Validate VM connectivity between SR-IOV Network
- Validate SRIOV Port mapping to OS/VF (where applicable)
- Validate VM connectivity between L3/Tenant network
- Validate VM connectivity between L3/Network traffic passing through router
- Validate user-data script gets execute as part of POST VM creation in your stack
- Delete all Heat stack created as part of this testing
- Validate VM host-dev mapping to physical host
- Validate hairpinning Solution -- Communication between 2 VMs residing on same compute should not go over wire

**Compute Component**

**SUMMARY:** Validate/Document VMs status and connectivity result after performing each of listed steps.
- Restart libvirt pod
- Restart nova-compute pod
- Restart openvswitch-db pod
- Restart openvswitch-vswitchd pod
- Restart neutron-ovs-agent pod
- Restart neutron-sriov-agent pod (where applicable)

**Control Plane Components**

**SUMMARY:** Validate RabbitMQ, Ceph, Mariadb and Openstack components, including: Nova, Glance, Heat, and Keystone. Resiliancy is validated by shutting down service under test in one or more pods, making API calls against that service, and validating service is still working as expected.
- Validate RabbitMQ resiliency
- Validate nova-api resiliency
- Validate nova-api-metadata
- Validate nova-conductor
- Validate nova-scheduler
- Validate nova-placement-api
- Validate nova-console-auth
- Validate nova-novnc-proxy
- Validate nova-rabbitmq
- Validate glance-api
- Validate glance-registry
- Validate glance-rabbitmq
- Validate heat-api
- Validate heat-cfn
- Validate heat-engine
- Validate heat-rabbitmq
- Validate keystone-api
- Validate keystone-rabbitmq
- Validate keystone-rabbitmq
- Validate mariadb cluster is in sync
- Studown mariadb and upon restart ensure its sync up with masterdb
- Validate ceph (if including in implementation)
- Restart ceph-osd (if including in implementation)
- Validate VNF is working as expected following ceph service restart

**Security**

**SUMMARY:** See [chapter 7](./chapter07.md) for security requirements

<a name="8.3.2"></a>
### 8.3.2 Kubernetes (K8s)

TBD

<!--
<a name="8.5"></a>
## 8.5 General Thoughts.

## Synopsis

Ensure Reference Implementation of CNTT Reference Model and CNTT Reference Architecture meets industry driven quality assurance standards for compliance, verification and validation.  The OPNFV Verified Program (OVP), by Linux Foundation Networking (LFN), in partnership with the Compliance Verification Committee (CVC), will provide tracking and governance for RM/RA verification.

For the purposes of this chapter, NFVI+VNF testing will be performed for **Verification** and **Validations** purpose.  **Certifications**, which are Out of Scope, include a measured performance of the adherence to, and demonstrated proficiency with, all aspects of software delivery including but no limited to planning, logistics for communication, and development of which there are no code developed/delivered with the NFVI+VNF testing and verification.

<a name="x.x"></a>
## Introduction

**Objective**<br>
Perform NFVI+VNF Verification and Validations using CNTT reference architecture, leveraging the existing OPNFV and CVC Intake and Validation Process to onboard and validate new test projects for NFVI compliance.  Upstream projects will define features/capabilities, test scenarios, and test cases to augment existing OVP test harnesses to be executed via the OVP Ecosystem.

**Scope and Test Methodology**
- Manifest Verifications (aka CVC Compliance) will ensure the NFVI is compliant, and delivered for testing, with hardware and software profile specifications defined by the Ref Model and Ref Architecture.
- Empirical Validation with Reference Golden VNFs (aka CVC Validation) will ensure the NFVI runs with a set of VNF Families, or Classes, to minic production-like VNF connectivity, for the purposes of interopability checks.
- Candidate VNF Validation (Validation & Performance) will ensure complete interoperablity of VNF behaviour on the NFVI leverage VVP/VNFSDK test suites.  Testing ensures VNF can be spun up, modified, or removed, on the target NFVI (aka Interoperability).

**Different Distributions**
The three step methodolgy described above of verifying Manifest compliance, exeucting Empirical Golden VNF transactions, and performing Interopability Testing is the same validation proces regardless of the Distribution used to establish a cloud topology, and the components and serivces used in the client software stack.  


**Not in Scope**

- Functional testing/validation of the VNF is not in scope.
- ONAP is not used in the process flow for NFVI verifications, or validations.
- Upgrades to VNFs, and the respective processes of verifying upgrade procedures and validating (testing) the success and compatibility of upgrades is not in scope.

**Chapter Purpose**<br>
This chapter includes process flow, logistics, and requirements which must be satisfied to ensure Network Function Virtualisation Infrastructure (NFVI) meets the design, feature, and capability expectations of VNF developers promoting both the use and scalability of Software Defined Networking (SDN) capabilities.  Upstream projects will define features/capabilities, test scenarios, and test cases which will be used to augment OVP test harnesses for infrastructure verification purposes.  Existing processes, communication mediums, and related technologies will be utilized where feasible.  Ultimately, test results of certified NFVI+VNF will reduce the amount of time and cost it takes each operator to on-board and maintain vendor provided VNFs.

<p align="center"><img src="../figures/ch10_ref_model_lfn.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 8-1:</b> CNTT relation to LFN OVP</p>

<a name="x.x"></a>
## Principles and Guidelines

The objectives of the verification program are to deliver a validated implementation of reference architecture which satisfies infrastructure needs for VNF-developer teams, leveraging the OVP ecosystem as the vehicle for delivering validated NFVI.

These core principles will guide NFV verification deliverables:

<a name="x.x.x"></a>
### Overarching Objectives and Goals

1. Deliver verified implementation of reference architecture which satisfies infrastructure needs for VNF-developer teams.
2. All accomplished with augmentation to the current OVP ecosystem.
3. Increase probability VNFs will on-board and function with minimal problems, or issues, during initial instantiation of VNF.
4. Test Harnesses will be portable, or compatible, across all RAs/Distributions which already conform to standard interfaces and services.

<a name="x.x.x"></a>
### Verification Methodologies
<ol>
<li>Engineering package validations will be performed against targeted infrastructure/architecture.</li>
<li>Configuration settings/features/capabilities will be baseline</li>
<li>Entrance Criteria Guidelines will be satisfied prior to OPNFV verification (i.e. Supplier needs to submit/agree/conform)
<ol>
<li>Conform to CNTT ref model</li>
<li>Confirm to ref arch</li>
<li>Submit standard documentation</li>
<li>Adhere to security compliance</li>
</ol>
</li>
<li>Exit Criteria Guidelines will be satisfied prior to issuance of OPNFV compliance badges.
<ol>
<li>Certification for Tenants (OVP Ecosystem)</li>
<li>Operaitonal Considerations (Telco Perspective)</li>
<li>End User Considerations (Telco Perspective)</li>
</ol>
</li>
<li>Test runs using reference model VNFs will validate RA chosen by the VNF-supplier meets developer needs</li>
<li>Verification decisions will be based on data. Test harness is &ldquo;compatible&rdquo;, or &ldquo;conforms&rdquo; to testing against standard interfaces and services</li>
<li>VNF functionality easily tested w/ addition of Supplier Apparatus</li>
<li>Leverage test harnesses from existing open source projects where practical, and applicable.&nbsp;</li>
</ol>

<a name="x.x.x"></a>
### Governance
1. Certification badges will be presented by the CVC<br>
2. CVC will maintain requirements for certification<br>

<a name="x.x"></a>
## Terms and Resources

**Terms utilized throughout this chapter are intended to align with CVC definitions, and their use through CVC documentation, guidelines, and standards.**

NFVI+VNF testing will be performed for **Verification** and **Validations** purpose.  
- **Verification** will be used to indicate conformance to design requirement specifications.  Activities involved Reviews and Walk-Throughs to ensure the NFVI is delivered per implementation specifications.
- **Validations** is used to indicate testing performed to confirm the actual output of a product meets the expected, or desired outcome, or behaviour.
- **Certfications**, which are Out of Scope, include a measured performance of the adherence to, and demonstrated proficiency with, all aspects of software delivery including but no limited to planning, development (of which there are no code developed/delivered), and logistics for communications.

Source information for additional reading:
- [https://www.softwaretestingmaterial.com/verification-and-validation/](https://www.softwaretestingmaterial.com/verification-and-validation/ "What is Verification And Validation In Software Testing")

- [http://softwaretestingfundamentals.com/verification-vs-validation/ ](http://softwaretestingfundamentals.com/verification-vs-validation/  "Verification vs Validation")

- [https://users.ece.cmu.edu/~koopman/des_s99/verification/](https://users.ece.cmu.edu/~koopman/des_s99/verification/ "Verification/Validation/Certification")

<a name="x.x.x"></a>
### Terms

Additional Terms utilized throughout the document:

<table>
  <tr><th>Term</th><th>Description</th></tr>
  <tr><td>AZ</td><td>AZ	Availability Zone</td></tr>
	<tr><td>Compatibility</td><td>the capacity for two systems to work together without having to be altered to do so, e.g. same data formats</td></tr>
	<tr><td>Compliance</td><td>a state of being in accordance with established guidelines or specifications</td></tr>
  <tr><td>CPE</td><td>Customer Premises Equipment</td></tr>
  <tr><td>CVC</td><td>Compliance and Verification Committee</td></tr>
  <tr><td>ETSI</td><td>European Telecommunications Standards Institute</td></tr>
  <tr><td>ETSI NFV-TST</td><td>ETSI - Network Functions Virtualisation - Test</td></tr>
  <tr><td>ETSI NFV-IFA</td><td>ETSI - Network Functions Virtualisation - Infrastructure</td></tr>
  <tr><td>GB</td><td>Gigabit</td></tr>
  <tr><td>Hareness (Test)</td><td>automated test framework (test engine, scrip repository) configured to test a program unit by running it under varying conditions and monitoring its behaviour and outputs</td></tr>
  <tr><td>HW</td><td>Hardware</td></tr>
<tr><td>IMS</td> <td>IP Multimedia Subsystem</td></tr>
<tr><td>I/O</td> <td>Input/Output</td></tr>
<tr><td>MB</td> <td>Megabit</td></tr>
<tr><td>NFV</td> <td>Network Function Virtualization</td></tr>
<tr><td>NFVI</td> <td>NFV Infrastructure</td></tr>
<tr><td>NUMA</td> <td>Non-Unified Memory Access</td></tr>
<tr><td>OPNFV</td> <td>Open Platform for NFV</td></tr>
 <tr><td>OVP</td><td>OPNFV Verification Program (OVP)</td></tr>
<tr><td>RAM</td><td>Random Access Memory</td></tr>
<tr><td>Scenario (Test)</td>	<td>any functionality that can be tested; synonymous with use case, or collection of test steps to complete a user workflow</td></tr>
<tr><td>SDN</td>	<td>Software Defined Networking</td></tr>
<tr><td>SD-WAN</td>	<td>Software Defined Wide Area Network</td></tr>
<tr><td>SLA</td>	<td>Service Level Agreement</td></tr>
<tr><td>SUT</td>	<td>System Under Test</td></tr>
<tr><td>SW</td>	<td>Software</td></tr>
<tr><td>vCPU</td>	<td>Virtual CPU (Central Processing Unit)</td></tr>
<tr><td>vNIC</td>	<td>Virtual NIC (Network Interface Card)</td></tr>
<tr><td>vRouter</td>	<td>Virtual Router</td></tr>
<tr><td>vSwitch</td>	<td>Virtual Switch</td></tr>
<tr><td>Validation</td>	<td>esting performed to confirm the actual output of a product meets the expected, or desired outcome, or behaviour</td></tr>
	<tr><td>Verification</td>	<td>conformance to design requirement specifications; Reviews and Walk-Throughs to ensure a product delivered meets implementation specifications</td></tr>
<tr><td>VIM</td>	<td>Virtual Infrastructure Manager</td></tr>
<tr><td>VNF</td>	<td>Virtualised Network Function</td></tr>
<tr><td>VNF-C</td>	<td>VNF Component (can be hosted on a VM, Container, etc)</td></tr>
<tr><td>VNFM</td>	<td>VNF Manager</td></tr>
</table>

- **Verification** will be used to indicate conformance to design requirement specifications.  Activities involved Reviews and Walk-Throughs to ensure the NFVI is delivered per implementation specifications.  
- **Validations** is used to indicate testing performed to confirm the actual output of a product meets the expected, or desired outcome, or behaviour.  

<a name="x.x"></a>
## Lifecycle and Process Flow

**NOT MVP**

<a name="x.x.x"></a>
### Project Mgmt

**NOT MVP**

How certifications are requested, processed, managed, what lab(s) is used, life cycle management

<a name="x.x.x"></a>
### OPNFV Iterations & Communications

**NOT MVP**

OPNNV Iterations with the CNTT (mgmt and communication of)

<a name="x.x.x"></a>
### Onboarding RA and Supplier VNF

**NOT MVP**

Onboarding (for OVP certification)

<a name="x.x.x"></a>
### SLAs and Issue Resolution

**NOT MVP**

Expectations for acknowlegment and turn-round from onboarding, verifications, and issue resolution.

<a name="x.x.x"></a>
### RA Verification

**NOT MVP**

Process flow for RA (Infra) Validation and Verfiication

<a name="x.x"></a>
## Current OVP and CVC Process

<a name="x.x.x"></a>
### Process (CVC)

<p><u><strong>CVC Compliance, Verification, and Certification governing framework consists of: </strong></u>&nbsp;</p>
<ul>
<li><strong>Compliance testing</strong>: compares the system under test against the specifications / standards</li>
<li><strong>Validation testing:</strong> ensures the system under test is operating according to its intended / required purpose</li>
<li><strong>Performance testing</strong>: measures how well the system under test performs its specific purpose(s)</li>
</ul>
<p><u><strong>OVP certifications are accomplished as a two-part process: </strong></u></p>
<ol>
<li>OPNFV provides Test Tools and Test Cases to OVP.</li>
<li>OVP provides vendor NFVI products a &ldquo;badge&rdquo; claiming &ldquo;OPNFV-certified&rdquo; once OVP testing passes successfully (via Dovetail).</li>
</ol>

<a name="x.x.x"></a>
### Process (OPNFV)

<p><strong>OPNFV Releases, and their repsective test verificaitons and validations requires 1) the implentation and adoption of an Installer to perform the needed installation and distirbution of infrastructure componetns and services, 2) identification and acceptance of a Feature Project introducing new, or enhanced, platform capabilities, and 3) an appropriate Test Project explicitly calling out the test use cases and scenarnios for verificaiton and validation.</strong></p>

<p><strong>More specifically:</strong></p>
<p><strong><u>Release Status</u></strong></p>
<ul>
<li>Installer oriented release. CNTT does not recommended any specific installer. An agnostic approach is taken that allows for an implementation to determine their own installer.</li>
<li>Multiple installers exist</li>
<li>Multiple scenarios exist, with one scenario represents a certain integration group and a certain configuration</li>
<li>All releases must pass CI（Continuous Integration) test</li>
<li>OVP includes test cases that at lease one OPNFV release scenario can pass</li>
</ul>
<p><u><strong>Feature Projects</strong></u></p>
<ul>
<li>Define a certain feature for the OPNFV release, e.g. high availability</li>
<li>Work with upstream projects to develop features</li>
<li>Work with testing projects to define and co-develop feature tests</li>
<li>Work with installer projects to develop certain scenarios including the feature</li>
</ul>
<p><strong><span style="text-decoration: underline;">Test scenarios</span> </strong></p>
<ul>
<li>Derived from Projects coming into OPNFV for release scoping, resulting in test cases used by OVP for verification and certification.&nbsp;</li>
<li>Only test cases that can let one of the scenarios pass can be included in OVP.</li>
<li>This is a procedure to make sure OVP test cases are written in a right way</li>
</ul>
<p>&nbsp;</p>

<p align="center"><img src="../figures/ch8_OPNFV_current_projects_and_releases.jpg" alt="OPNFV Projects and Releases" title="OPNFV Projects and Releases" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: OPNFV (current) Projects and Releases Process</p>

<a name="x.x.x"></a>
### Test Framework and Supported Test Cases
<p><u><strong>Test frameworks and supported test cases for OVP Certifications include (OPNFV and ONAP):</strong></u></p>
<ol>
<li><u><strong>OPNFV</strong></u><u> &ndash; </u><u><strong>NFVI Testing and Certification</strong></u>
<ol>
<li><strong>CVC Category:&nbsp; Validation, Compliance</strong></li>
<li><strong>Purpose</strong>: <strong>NFVI platform is checked against the Open Stack requirements</strong></li>
<li>Test framework, test result database and Web UI
<ul>
<li><strong>Dovetail</strong> project</li>
</ul>
</li>
<li>Test tools, test cases and test execution
<ul>
<li>API testing (<strong>FuncTest</strong>)</li>
<li>Performance and HA (<strong>Yardstick</strong>)</li>
<li>Load testing (<strong>Bottleneck</strong>)</li>
</ul>
</li>
</ol>
</li>
</ol>
<ol start="2">
<li><u><strong>ONAP</strong></u><u> &ndash; </u><u><strong>VNF Testing and Certification</strong></u>
<ol>
<li><strong>CVC Category:&nbsp; Compliance, Performance</strong></li>
<li><strong>Purpose: VNF template is checked against the ONAP Requirements</strong>
<ul>
<li>VNF Validation/Packaging Compliance (HEAT and TOSCA/CSAR/VFD)</li>
<li>Web front-end integrated with OPNFV Dovetail Web UI</li>
<li>Future plan: testing of VNF lifecycle, VNF functions, VNF performance</li>
</ul>
</li>
</ol>
</li>
</ol>
<p>NOTE:&nbsp;&nbsp;<strong>VNF Validation Testing </strong>- CVC and ONAP teams are working to develop the initial life-cycle tests for VNF devices.&nbsp; The first release will run on the "basic open stack" meeting ONAP requirements. Future versions would require this to be the reference NFVI defined by CNTT</p>

## 8.6 CNTT/NFVI Compliance, Verification, and Certification Strategy

<a name="x.x.x"></a>
### Methodology.

Perform VNF interoperability verifications against an implementation of CNTT reference architecture, leveraging existing OPNFV Intake Process. Upstream projects will define features/capabilities, test scenarios, and test cases to augment existing OVP test harnesses to be executed via the OVP Ecosystem.

3rd Party test platforms may also be leveraged, if desired.

<p align="center"><img src="../figures/ch8_certifying_methodlogy.jpg" alt="Certification Methodology" title="Certification Methodology" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Certification Methodology</p>

<a name="x.x.x"></a>
### OVP/CVC Certification Strategy & Vehicle.
<p><strong>NFVI+VNF validations consist of a three part process for Compliance, Validation, and Performance.&nbsp; </strong>Adherenence to <strong>Security</strong> standards are equally important and addressed in Chapter 7.</p>
<p>The three part verificaiton process includes <strong>NFVI Manifest Validations</strong>, <strong>Emprical Baseline measurements against targeted VNF families</strong>, and <strong>Candidate VNF verifications</strong>.&nbsp; More specifically,</p>
<ul>
<li><strong>NFVI Verification (</strong><em>Compliance</em><strong>):</strong> NFVI is the SUT, ensuring NFVI is compliant with specs of Ref Model and Ref Architecture accomplished with&nbsp;<strong>Manifest Validations</strong> (performed via Echo Tests)&nbsp;</li>
<li><strong>Empirical Validation with Reference VNF (</strong><em>Validation</em><strong>):</strong> NFVI is the SUT, ensuring NFVI runs with Golden VNFs and is instrumented to objectively validate resources through consumption and measurement</li>
<li><strong>Candidate VNF Certification (</strong><em>Validation &amp; Performance</em><strong>):</strong> VNF is the SUT, ensuring VNFs operate with Ref Model and Ref Arch leveraging VVP/CVP/VFNSDK Test Suites</li>
<li><strong>Security</strong>: Ensures NFVI+VNF is free from known security vulnerabilities, utilizing industry standard cyber security frameworks <em>(Refer to CNTT Chapter 7 Security for additional test/verification details)</em></li>
</ul>
<p>Validations are performed against an <strong>Infrastructure Profile Catalog</strong>, <strong>VNF performance profile</strong>, and <strong>targeted VNF class</strong> or family for baseline measurements.</p>
<p>The <strong>Infrastucture Profile Catalog</strong>&nbsp;contains the following attributes:&nbsp;</p>
<ul>
<li>Profile is a collection of (limited) options offered by the infrastructure to the VNF
<ul>
<li>Capabilities</li>
<li>Metrics</li>
<li>Compute flavours</li>
<li>Interface options</li>
<li>Storage extensions</li>
<li>Acceleration capabilities</li>
</ul>
</li>
<li>Profiles are offered to VNFs as an instance types with predefined compute flavours (T-shirt size)
<ul>
<li>A particular set of options is an instance type</li>
<li>Compute flavours: S, M, L</li>
</ul>
</li>
</ul>
<p><strong>VNF performance profiles</strong>, for which NFVI validations will support and be verified against, are defined as basic, network intensive, and compute intensive. Details for each of these profiles can be found in <a href=https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter02.md#2.3>chapter 2.3</a>.

<p align="center"><img src="../figures/ch02_infra_profiles.PNG" alt="BNC VNF Categories" title="BNC VNF Categories" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Basic(B), Network(N), Compute(C) VNF Categories</p>

<p><strong>Targeted VNF Classes/Families </strong>for baseline measurements are described in <a href=https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter02.md#2.2>chapter 2.2</a>.

<a name="x.x.x"></a>
### Best Practices.
<ul>
<li>Standardized test methodology / flow, Test Plan, and Test Case Suites</li>
<li>Integration with Dovetail and OVP flow (code, docs, cert criteria, etc.)</li>
<li>Leveraging ONAP Network and Service Models, with identified VNF-specific parameters</li>
<li>Standardized certification criteria</li>
<li>Define CNTT ref arch as scenarios, and have all test cases for the ref arch be involved in OVP (could also be addressed in OVP as CNTT test)</li>
<li>Add test cases from operators, which operators already tested in their environment</li>
</ul>



<a name="x.x.x"></a>
### System Under Test (SUT) Pre-reqs
1. Test Specifications – per infra profile, specifications, and features/capabilities
2. Naming conventions
3. NFVi profiles and Flavours
4. Test User Guide
5. Scenarnio Descriptor File (SDF)


<a name="x.x.x"></a>
### Test Categories
<ol>
<li>On-Boarding (ONAP MANO, NFVi Agnostic)</li>
<li>Instantiation, Deletion, Recent Change (ONAP MANO, NFVi Agnostic)</li>
<li>VNF Functional Testing</li>
<li>Security Testing</li>
<li>Charging / Revenue Assurance Verification</li>
<li>MicroServices Support</li>
<li>Closed Loop Testing</li>
<li>VNF Coexistence (ETSI NFV-TST001 &ldquo;Noisy Neighbor&rdquo;)</li>
<li>VNF Interactions with Extended NFVi Topology</li>
<li>VNF Interactions with Complex NFVi (Akraino)</li>
<li>Scalability Testing</li>
<li>HA Testing</li>
<li>Fault Recovery Testing</li>
<li>PM/KPI/Service Assurance Testing</li>
</ol>

<a name="x.x.x"></a>
### Test Harness(es)
<ol>
<li>Standardized test methodology / flow</li>
<li>Working test bed reference design</li>
<li>Standardized Cloud-based facilities (storage, IAM, etc.)</li>
<li>Standard ONAP Network and Service Models, with identified VNF-specific parameters</li>
<li>Robot library to enable Data-Driven testing of On-Boarding, Instantiation, etc.</li>
<li>Sample VNF, CSAR and Robot Test Cases</li>
<li>Standardized base Test Plan and Test Case suite</li>
<li>Standardized certification criteria</li>
<li>Integration with Dovetail and OVP flow (code, docs, cert criteria, etc.)</li>
<li>Real, usable documentation</li>
<li>&ldquo;Just add Water&rdquo; deployment vehicle</li>
</ol>


<a name="x.x"></a>
## Test Results

**NOT MVP**

Test suites will be categorized as functional or performance based. Results reporting will be communicated as a boolean (pass/fail). The pass/fail determination for performance-based test cases will be made by comparing results against a baseline.
Example performance-based metrics include, but are not limited to: resource utilization, response times, latency, and sustained throughput per second (TPS).

<a name="x.x.x"></a>
### Measurements

**NOT MVP**



<a name="x.x.x"></a>
### Report Summary

**NOT MVP**

1. Pass/Fail
2. Measure Only (e.g. throughput analysis, baseline, transaction stats, etc)

<a name="x.x"></a>
## Future Planning

**NOT MVP**

This section will be used to plan for future offerings.



<a name="x.x.x"></a>
### Reports Dashboard

**NOT MVP**

Placeholder to document where results will be posted (e.g. Dovetail dashboards.)

<a name="x.x.x"></a>
### Automation Considerations

**NOT MVP**

Placholder to identify automation needs and tool chains.

<a name="x.x"></a>
## Recommendations

**NOT MVP**

Placholder to capture best practices.
-->