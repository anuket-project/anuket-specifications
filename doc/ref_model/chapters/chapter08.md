[<< Back](../../ref_model)
# 8 Compliance, Verification, and Certification
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction.](#8.1)
* [8.2 Principles and Guidelines.](#8.2)
  * [8.2.1 Overarching Objectives and Goals.](#8.2.1)
  * [8.2.2 Verification Methodologies.](#8.2.2)
  * [8.2.3 Governance.](#8.2.3)  
* [8.3 Terms and Resources.](#8.3)
  * [8.3.1 Terms.](#8.3.1)
  * [8.3.2 Resources.](#8.3.2)
  * [8.3.3 Test Plans | Suites | Cases.](#8.3.3)
* [8.4 Lifecycle and Process Flow.](#8.4)
  * [8.4.1 Project Mgmt.](#8.4.1)
  * [8.4.2 OPNFV Iterations & Communications.](#8.4.2)
  * [8.4.3 Onboarding RA and Supplier VNF.](#8.4.3)
  * [8.4.4 SLAs and Issue Resolution](#8.4.4)
  * [8.4.5 RA Verification.](#8.4.5)
* [8.5 Current OVP and CVC Process.](#8.5)
  * [8.5.1 Process (CVC)](#8.5.1)
  * [8.5.2 Test Framework and Supported Test Cases.](#8.5.2)
  * [8.5.3 ONAP - VNF Testing and Certification.](#8.5.3)
* [8.6 CNTT/NFVI Compliance, Verification, and Certification Strategy.](#8.6)
  * [8.6.1 Methodology.](#8.6.1)
  * [8.6.2 OVP/CVC Certification Strategy & Vehicle.](#8.6.2)
  * [8.6.3 Best Practices.](#8.6.3)
  * [8.6.4 NFVI Profiles reference implementations.](#8.6.4)
  * [8.6.5 Vendor supplied NFVI solutions.](#8.6.5)
  * [8.6.6 NFVI Compliance, Verification, and Certification.](#8.6.6)
  * [8.6.7 VNF Compliance, Validation, and Certification.](#8.6.7)
* [8.7 Quality Assurance.](#8.7)
  * [8.7.1 Dependencies, Recommendations, Assumptions.](#8.7.1)
  * [8.7.2 System Under Test (SUT) Pre-reqs.](#8.7.2)
  * [8.7.3 Entrance & Exit Criteria.](#8.7.3)
  * [8.7.4 Test Frameworks.](#8.7.4)
  * [8.7.5 Test Categories.](#8.7.5)
  * [8.7.6 Test Harness(es).](#8.7.6)
  * [8.7.7 Test Tools.](#8.7.7)
* [8.8 Test Results.](#8.8)
  * [8.8.1 Metrics.](#8.8.1)
  * [8.8.2 Report Summary.](#8.8.2)
* [8.9 Future Planning.](#8.9)
  * [8.9.1 Performance and Resiliency Testing.](#8.9.1)
  * [8.9.2 Reports Dashboard.](#8.9.2)
  * [8.9.3 Automation Considerations.](#8.9.3)
* [8.10 Recommendations.](#8.10)

## Synopsis

Ensure Reference Model and Reference Architecture infrastructure meets industry driven quality assurance standards for compliance, verification and certification.  The OPNFV Verified Program (OVP), by Linux Foundation Networking (LFN), in partnership with the Compliance Verification Committee (CVC), will provide tracking and governance for RM/RA verification.

<a name="8.1"></a>
## 8.1 Introduction

This document includes process flow, logistics, and requirements which much be satisfied to ensure common infrastructure meets design, features, and capability expectations of VNF supplier teams to deliver NFV promoting the use and scalability of SDN capabilities.  This chapter captures the core fundamentals and steps needed to certify VNFs on target NFVi frameworks and architectures which drives more work into the community, resulting in pre-certified VNFs on core capabilities ultimately reducing the amount of time and cost it takes each operator to on-board and maintain vendor provided VNFs.

<p align="center"><img src="../figures/ch10_ref_model_lfn.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 8-1:</b> CNTT relation to LFN OVP</p>

<a name="8.2"></a>
## 8.2 Principles and Guidelines

The objectives of the verification program are to deliver certified reference architecture which matches VNF-developer specifications, levering the OVP ecosystem as the vehicle for deliverying validated NFV.

These core principles will guide NFV verification deliverables: 

<a name="8.2.1"></a>
### 8.2.1 Overarching Objectives and Goals

1. Deliver certified reference architecture which matches VNF-developer specifications<br>
2. All accomplished with augmentation to the current OVP ecosystem.<br>
3. Certified VNFs will on-board and function first shot<br>

<a name="8.2.2"></a>
### 8.2.2 Verification Methodologies
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
<li>Verification decisions will be based on data6. Test harness is &ldquo;compatible&rdquo;, or &ldquo;conforms&rdquo; to testing against standard interfaces and services</li>
<li>VNF functionality easily tested w/ addition of Supplier Apparatus</li>
<li>Leverage test harnesses from existing open source projects where practical, and applicable.&nbsp;</li>
</ol>

<a name="8.2.3"></a>
### 8.2.3 Governance
1. Certification badges will be presented by the CVC<br>
2. CVC will maintain requirements for certification<br>

<a name="8.3"></a>
## 8.3 Terms and Resources

<a name="8.3.1"></a>
### 8.3.1 Terms

<table>
  <tr><th>Term</th><th>Description</th></tr>
  <tr><td>AZ</td><td>AZ	Availability Zone</td></tr>
  <tr><td>CPE</td><td>Customer Premises Equipment</td></tr>
  <tr><td>CVC</td><td>Compliance and Verification Committee</td></tr>
  <tr><td>ETSI</td><td>European Telecommunications Standards Institute</td></tr>
  <tr><td>ETSI NFV-TST</td><td>ETSI - Network Functions Virtualisation - Test</td></tr>
  <tr><td>ETSI NFV-IFA</td><td>ETSI - Network Functions Virtualisation - Infrastructure</td></tr>
  <tr><td>GB</td><td>Gigabit</td></tr>
  <tr><td>HW</td><td>Hardware</td></tr>
<tr><td>IMS</td>	<td>IP Multimedia Subsystem</td></tr>
<tr><td>I/O</td>	<td>Input/Output</td></tr>
<tr><td>MB</td>	<td>Megabit</td></tr>
<tr><td>NFV</td>	<td>Network Function Virtualization</td></tr>
<tr><td>NFVI</td>	<td>NFV Infrastructure</td></tr>
<tr><td>NUMA</td>	<td>Non-Unified Memory Access</td></tr>
<tr><td>OPNFV</td>	<td>Open Platform for NFV</td></tr>
<tr><td>RAM</td><td>Random Access Memory</td></tr>
<tr><td>SDN</td>	<td>Software Defined Networking</td></tr>
<tr><td>SD-WAN</td>	<td>Software Defined Wide Area Network</td></tr>
<tr><td>SLA</td>	<td>Service Level Agreement</td></tr>
<tr><td>SUT</td>	<td>System Under Test</td></tr>
<tr><td>SW</td>	<td>Software</td></tr>
<tr><td>vCPU</td>	<td>Virtual CPU (Central Processing Unit)</td></tr>
<tr><td>vNIC</td>	<td>Virtual NIC (Network Interface Card)</td></tr>
<tr><td>vRouter</td>	<td>Virtual Router</td></tr>
<tr><td>vSwitch</td>	<td>Virtual Switch</td></tr>
<tr><td>VIM</td>	<td>Virtual Infrastructure Manager</td></tr>
<tr><td>VNF</td>	<td>Virtualised Network Function</td></tr>
<tr><td>VNF-C</td>	<td>VNF Component (can be hosted on a VM, Container, etc)</td></tr>
<tr><td>VNFM</td>	<td>VNF Manager</td></tr>
</table>

<a name="8.3.2"></a>
### 8.3.2 Resources
1. OPNFV https://www.opnfv.org/ - project and community that facilitates a common NFVI, continuous integration (CI) with upstream projects, stand-alone testing toolsets, and a compliance and verification program for industry-wide testing and integration to accelerate the transformation of enterprise and service provider networks.<br>
2. CVC https://wiki.lfnetworking.org/display/LN/Compliance+and+Verification+Committee - members-driven committee within LF Networking that recommends policies and oversight for compliance and certification program to the Governing Board of LF Networking (“Governing Board”).

<a name="8.3.3"></a>
### 8.3.3 Test Plans | Suites | Cases
1. 

<a name="8.4"></a>
## 8.4 Lifecycle and Process Flow

<a name="8.4.1"></a>
### 8.4.1 Project Mgmt
How certifications are requested, processed, managed, what lab(s) is used, life cycle management

<a name="8.4.2"></a>
### 8.4.2 OPNFV Iterations & Communications
OPNNV Iterations with the CNTT (mgmt and communication of)

<a name="8.4.3"></a>
### 8.4.3 Onboarding RA and Supplier VNF
Onboarding (for OVP certification) 

<a name="8.4.4"></a>
### 8.4.4 SLAs and Issue Resolution
Expectations for acknowlegment and turn-round from onboarding, verifications, and issue resolution.

<a name="8.4.5"></a>
### 8.4.5 RA Verification
Process flow for RA (Infra) Validation and Verfiication

<a name="8.5"></a>
## 8.5 Current OVP and CVC Process

<a name="8.5.1"></a>
### 8.5.1 Process (CVC)

<a name="8.5.2"></a>
### 8.5.2 Test Framework and Supported Test Cases
1. OPNFV – NFVi Testing and Certification
	1. Test framework, test result database and Web UI
		1. Dovetail project
2. Test tools, test cases and test execution
	1. API testing (FuncTest)
	2. Performance and HA (Yardstick)
	3. Load testing (Bottleneck)

<a name="8.5.3"></a>
### 8.5.3 ONAP - VNF Testing and Certification
1. VNF Validation/Packaging Compliance (HEAT and TOSCA/CSAR/VFD)
2. Web front-end integrated with OPNFV Dovetail Web UI
3. Future plan: testing of VNF lifecycle, VNF functions, VNF performance

<a name="8.6"></a>
## 8.6 CNTT/NFVI Compliance, Verification, and Certification Strategy

<a name="8.6.1"></a>
### 8.6.1 Methodology.

Perform VNF certifications using CNTT reference architecture, leveraging existing OPNFV Intake Process. Upstream projects
will define features/capabilities, test scenarios, and test cases to augment existing OVP test harnesses to be executed via the OVP Ecosystem.

3rd Party test platforms may also be leveraged, if desired.

<p align="center"><img src="../figures/ch8_certifying_methodlogy.jpg" alt="Certification Methodology" title="Certification Methodology" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Certification Methodology</p>

<a name="8.6.2"></a>
### 8.6.2 OVP/CVC Certification Strategy & Vehicle.
<ul>
<li><strong>NFVI Certification (</strong><em>Compliance</em><strong>):</strong> NFVI is the SUT, ensuring NFVI is compliant with specs of Ref Model and Ref Architecture accomplished with&nbsp;<strong>Manifest Validations</strong> (performed via Echo Tests)&nbsp;</li>
<li><strong>Empirical Validation with Reference VNF (</strong><em>Validation</em><strong>):</strong> NFVI is the SUT, ensuring NFVI runs with Golden VNFs and is instrumented to objectively validate resources through consumption and measurement</li>
<li><strong>Candidate VNF Certification (</strong><em>Validation &amp; Performance</em><strong>):</strong> VNF is the SUT, ensuring VNFs operate with Ref Model and Ref Arch leveraging VVP/CVP/CVC Test Suites</li>
<li><strong>Security</strong>: Ensures VNF is free from known security vulnerabilities, utilizing industry standard cyber security frameworks</li>
	
<a name="8.6.3"></a>
### 8.6.3 Best Practices.
<ul>
<li>Standardized test methodology / flow, Test Plan, and Test Case Suites</li>
<li>Integration with Dovetail and OVP flow (code, docs, cert criteria, etc.)</li>
<li>Leveraging ONAP Network and Service Models, with identified VNF-specific parameters</li>
<li>Standardized certification criteria</li>
</ul>

<a name="8.6.4"></a>
### 8.6.4 NFVI Profiles reference implementations.

For compliance, verification, and certification, of NFVI solutions provided for a given NFVI Profile, it is required to have a reference implementation of each profile so it can be used for compliance, validation, and certification.

Those reference implementations need to reflect on their corresponding profiles and deliver all metrics and capabilities promised. They need to use open source components. Figure below shows the various reference implementations required for each profile, they are:

- NFVI SW Reference implementation.
- NFVI HW Reference implementation.
- VNF reference implementation.

<p align="center"><img src="../figures/ch8_NFVI_ref_profiles_impementations.jpg" alt="NFVI RI Profiles" title="NFVI RI Profiles" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Reference NFVI Profiles Implementation</p>

<a name="8.6.5"></a>
### 8.6.5 Vendor supplied NFVI solutions.

Infrastructure Abstraction and Profiling allows NFVI SW vendors to provide solutions that are suitable for a given profile (as demonstrated in Figure below). Having NFVI solutions tailored towards a given profile makes it easier to verify, certify and test that solution against that profile using the reference implementation of the profile mentioned previously.

<p align="center"><img src="../figures/ch8_NFVI_vendor_supplied_sw_solutions.jpg" alt="NFVI Vendor SW Solutions" title="NFVI Vendor SW Solutions" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Vendor Supplied NFVI SW Solutions</p>

Similarly, Infrastructure Abstraction and Profiling allows NFVI HW vendors to provide solutions that are suitable for a given profile (as demonstrated in Figure below). Having NFVI hardware solutions tailored towards a given profile makes it easier to verify, certify and test that hardware solution against that profile using the reference implementation of the profile mentioned previously.

<p align="center"><img src="../figures/ch8_NFVI_vendor_supplied_hw_solutions.jpg" alt="NFVI Vendor HW Solutions" title="NFVI Vendor HW Solutions" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Vendor Supplied NFVI HW Solutions</p>

<a name="8.6.6"></a>
### 8.6.6 NFVI Compliance, Verification, and Certification.

Infrastructure abstraction and profiling makes it easier for a given NFVI SW solutions to be validated, certified and tested against the profile it is intended for.

Having a deterministic NFVI metrics and capabilities expected for a given profile, allows NFVI SW solutions to be characterised, validated, and verified against those metrics and capabilities, and therefore report the results in a standard format. This will allow operators to understand in depth the details and the differentiation a given solution can provide against other options.

Figure below demonstrates how a given NFVI SW solution can be validated and certified against a given profile by using a reference HW implementation and a reference NFVI implementation.

<p align="center"><img src="../figures/ch8_NFVI_certifying_vendor_sw_solutions.jpg" alt="Certifying NFVI Vendor SW Solutions" title="Certifying NFVI Vendor SW Solutions" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Certifying Vendor NFVI SW Solutions</p>

Similarly, to characterise, validate, and certify NFVI HW solution against a given profile, both NFVI SW reference implementation and a VNF reference implementation are needed as demonstrated as in Figure below.

<p align="center"><img src="../figures/ch8_NFVI_certifying_vendor_hw_solutions.jpg" alt="Certifying NFVI Vendor HW Solutions" title="Certifying NFVI Vendor HW Solutions" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Certifying Vendor NFVI HW Solutions</p>

Finally, NFVI vendors can characterise, validate, and certify an entire NFVI platform (both SW & HW) against a given profile by using a VNF reference implementation as shown in Figure below.

<p align="center"><img src="../figures/ch8_NFVI_certifying_vendor_swhw_solutions.jpg" alt="Certifying NFVI Vendor SW/HW Solutions" title="Certifying NFVI Vendor SW/HW Solutions" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Certifying Vendor NFVI SW/HW Solutions</p>

<a name="8.6.7"></a>
### 8.6.7 VNF Compliance, Validation, and Certification.

Standardising on Infrastructure profiles allows VNFs to be characterised, validated, and certified against a given profile by using reference NFVI implementations as demonstrated in Figure below. Where VNFs are using multiple profiles (different VNF-C written against different profiles), multiple Reference NFVI implementations should be used.

<p align="center"><img src="../figures/ch8_certifying_vendor_supplied_vnfs.jpg" alt="Certifying Vendor Supplied VNFs" title="Certifying Vendor Supplied VNFs" width="100%"/></p>
<p align="center"><b>Figure:</b> Figure: Certifying Vendor Supplied VNFs</p>

<a name="8.7"></a>
## 8.7 Quality Assurance

<a name="8.7.1"></a>
### 8.7.1 Dependencies, Recommendations, Assumptions

<a name="8.7.2"></a>
### 8.7.2 System Under Test (SUT) Pre-reqs
1. Test Specifications – per infra profile, specifications, and features/capabilities
2. Naming conventions
3. NFVi profiles and Flavors
4. Test User Guide

<a name="8.7.3"></a>
### 8.7.3 Entrance & Exit Criteria
<p><strong>OPNFV Entrance Criteria includes <em>D</em></strong><strong><em>emonstration of Reference Architecture Implementation,&nbsp;</em></strong><strong><em>and Delivery of the following:</em></strong></p>
<ol>
<li><u><strong>Design &amp; Requirements</strong></u>
<ul>
<li>Design, Configuration, Features, SLAs, and Capability documentation complete</li>
<li>Users stories / Adherence to CNTT Model principles and guidelines</li>
<li>Chosen Reference Architecture Matches a Reference Architecture from the product catalog<u></u></li>
</ul>
</li>
<li><u><strong>Environment</strong></u>
<ol>
<li>Lab / Flavor, component s/w rev levels specified, with confirmation of compatibility with external systems</li>
<li>Tenant needs identified</li>
<li>All connectivity, network, image, VMs, delivered with successful pairwise tests</li>
<li>Lab instrumented for proper monitoring<u></u></li>
</ol>
</li>
<li><u><strong>Planning &amp; Delivery</strong></u>
<ul>
<li>Kickoff / Acceptance Criteria reviews performed</li>
<li>Delivery commitments, timelines, and cadence accepted</li>
<li>Confirm backward compat. across software/flavor rev levels<u></u></li>
</ul>
</li>
<li><u><strong>Data / VNFs / Security</strong></u>
<ul>
<li>Images, Heat Templates, Preload Sheets available</li>
<li>Images uploaded to tenant space</li>
<li>External system test data needs identified</li>
<li>Owners (NFVI, VNF, PTL, etc) documented</li>
<li>Security Compliance Satisfied (see Ch. 8 &ndash; scans, vulnerabilities)<u></u></li>
</ul>
</li>
<li><u><strong>Test Case Contributions</strong></u>
<ul>
<li>VNF Developer/Supplier validations to be performed documented and supplied</li>
<li>NFVi validations to be performed supplied (e.g. echo, manifest)</li>
<li>Test to ensure users are added and have correct privileges for the tenant</li>
<li>Test to ensure quota against submitted request for the respective tenant</li>
<li>Test to ensure custom flavors against submitted request for respective tenants</li>
</ul>
</li>
</ol>

<br><p><strong>OPNFV Exit Criteria includes <em>D</em></strong><strong><em>emonstration of Compliance, Verification, Performance, and Validaiton, of Reference Architecture Implementation, and&nbsp;</em></strong><strong><em>Delivery of the following:</em></strong></p>
<ol>
<li><u><strong>CERTIFICATION TENANTS (via OVP Ecosystem)</strong></u>
<ol>
<li>All Test Cases have a status of &ldquo;Passed&rdquo;, &ldquo;Failed&rdquo;, &ldquo;N/A&rdquo; or &ldquo;Out-scoped&rdquo;.</li>
<li>All Severity 1 and Severity 2 issues are resolved.</li>
<li>All Issues have been Resolved or the Project/Component Team has voted unanimously for a Conditional Certification.</li>
<li>Known defects, or issues, are clearly documented and furnished to Telco providers with certification notes.</li>
<li>Certification Notification(s) issued.<u></u></li>
</ol>
</li>
<li><u><strong>OPERATIONAL CONSIDERATIONS (TELCO PERSPECTIVE)</strong></u>
<ol>
<li>Orchestration capabilities verified to be working as expected</li>
<li>Fabric setup/configuration validations successfully passed</li>
<li>Openstack API endpoint is reachable and working for that zone</li>
<li>Compute zones and cinder types verified</li>
<li>Standard images verified to exist (and usable)</li>
<li>Network object created (and working, as in IPs are bindable and usable)</li>
<li>Resolver overlay/DNS traffic/port 53 overlay on gateway is working properly</li>
<li>Designate is working, domain preferably created, and maybe test A record created/verified to be resolvable</li>
<li>Standard NTP servers are working and verified (using tenant's CIDR source IP)</li>
<li>NFVI/VNF is tested at steady state and high load</li>
<li>Continuously monitored to ensure SLAs are met and used as feedback to load/perf tests<u></u></li>
</ol>
</li>
<li><u><strong>END USER CONSIDERATIONS (TELCO PERSPECTIVE)</strong></u>
<ol>
<li>Component redundancy to ensure graceful updates without disruption of services</li>
<li>Thin provisioning storage should handle actual full quota usage cases</li>
<li>Load balancing should support elasticity</li>
<li>SRIOV Network configuration via SDN must be aware of all VMs on a host (and their network config)</li>
<li>Auto-healing databases (any component related db) when out of sync</li>
<li>Obvious, but, supports all required network functionality (all protocols, service chaining, VLAN trunking, QoS marking, probe/mirror, etc)</li>
<li>Supports NFV migration</li>
<li>Supports snapshots and backups of large volumes</li>
<li>Pre-check or audit failures during NFV deployment should allow follow-up mitigation, when possible, rather than killing deployment and rolling back</li>
</ol>
</li>
</ol>

<a name="8.7.4"></a>
### 8.7.4 Test Frameworks
1. Dovtail
2. Yardstick
3. Bottlenecks

<a name="8.7.5"></a>
### 8.7.5 Test Categories
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

<a name="8.7.6"></a>
### 8.7.6 Test Harness(es)
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

<a name="8.7.7"></a>
### 8.7.7 Test Tools
1. AQuA

<a name="8.8"></a>
## 8.8 Test Results

Test suites will be categorized as functional or performance based. Results reporting will be communicated as a boolean (pass/fail). The pass/fail determination for performance-based test cases will be made by comparing results against a baseline.
Example performance-based metrics include, but are not limited to: resource utilization, response times, latency, and sustained throughput per second (TPS).

<a name="8.8.1"></a>
### 8.8.1 Metrics
Metrics/Measurements and respective certification(s).
e.g. OVP Testing Ecosystem badge (with link to certification with posted results)

<a name="8.8.2"></a>
### 8.8.2 Report Summary
1. Pass/Fail
2. Measure Only (e.g. throughput analysis, baseline, transaction stats, etc)

<a name="8.9"></a>
## 8.9 Future Planning

This section will be used to plan for future offerings.

<a name="8.9.1"></a>
### 8.9.1 Performance and Resiliency Testing

<a name="8.9.2"></a>
### 8.9.2 Reports Dashboard

<a name="8.9.3"></a>
### 8.9.3 Automation Considerations

<a name="8.10"></a>
## 8.10 Recommendations

-----

<< Work space.  Ideas, Drafts, Work in progress. >>
