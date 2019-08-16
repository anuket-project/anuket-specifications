[<< Back](../../ref_model)
# 8 Compliance, Verification, and Certification
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction.](#8.1)
* [8.2 Principals and Guidelines.](#8.2)
  * [8.2.1 NFVI reference architectures.](#8.2.1)
  * [8.2.2 Test suites.](#8.2.2)
* [8.3 Terms and Resources.](#8.3)
  * [8.3.1 Resources.](#8.3.1)
  * [8.3.2 Terms.](#8.3.2)
  * [8.3.3 Test Plans | Suites | Cases.](#8.3.3)
* [8.4 Compliance, Verification, and Certification process and life cycle.](#8.4)
  * [8.4.1 NFVI reference architectures.](#8.4.1)
  * [8.4.2 Test suites.](#8.4.2)
* [8.3	Recommendations.](#8.3)

## Synopsis

Ensure Reference Model and Reference Architecture infrastructure meets industry driven quality assurance standards for compliance, verification and certification.  The OPNFV Verified Program (OVP), by Linux Foundation Networking (LFN), in partnership with the Compliance Verification Committee (CVC), will provide tracking and governance for RM/RA verification.

<a name="8.1"></a>
## 8.1 Introduction

This document includes process flow, logistics, and requirements which much be satisfied to ensure common infrastructure meets design, features, and capability expectations of VNF supplier teams to deliver NFV promoting the use and scalability of SDN capabilities.  This chapter captures the core fundamentals and steps needed to certify VNFs on target NFVi frameworks and architectures which drives more work into the community, resulting in pre-certified VNFs on core capabilities ultimately reducing the amount of time and cost it takes each operator to on-board and maintain vendor provided VNFs.

<p align="center"><img src="../figures/ch10_ref_model_lfn.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 8-1:</b> CNTT relation to LFN OVP</p>

<a name="8.2"></a>
## 8.2 Principals and Guidelines

The objectives of the verification program are to deliver certified reference architecture which matches VNF-developer specifications, levering the OVP ecosystem as the vehicle for deliverying validated NFV.

These core principals will guide NFV verification deliverables: 

<a name="8.2.1"></a>
### 8.2.1 Overarching Objectives and Goals

1. Deliver certified reference architecture which matches VNF-developer specifications<br>
2. All accomplished with augmentation to the current OVP ecosystem.<br>
3. Certified VNFs will on-board and function first shot<br>

<a name="8.2.2"></a>
### 8.2.2 Verification Methodologies
1. Engineering package validations will be performed against targeted infrastructure/architecture<br>
2. Configuration settings/features/capabilities will be baseline<br> 
3. Test runs using reference model VNFs will validate RA chosen by the VNF-supplier meets developer needs<br>
4. Verification decisions will be based on data

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

------

<a name="8.4"></a>
## 8.4 Compliance, Verification, and Certification process and life cycle

<a name="8.4.1"></a>
### 8.4.1 NFVI reference architectures

<a name="8.4.2"></a>
### 8.4.2 Test suites

<a name="8.5"></a>
## 8.5 Recommendations

-----

<a name="Lifecycle and Process Flow"></a>
## Lifecycle and Process Flow

<a name="Current OVP/CVC Process"></a>
## Current OVP/CVC Process

<a name="CNTT/NFVI Certification Approach"></a>
## CNTT/NFVI Certification Approach

<a name="Quality Assurance"></a>
## Quality Assurance

<a name="Automation Considerations"></a>
## Automations Considerations

<a name="Results Reporting"></a>
## Results Reporting

Test suites will be categorized as functional or performance based. Results reporting will be communicated as a boolean (pass/fail). The pass/fail determination for performance-based test cases will be made by comparing results against a baseline.
Example performance-based metrics include, but are not limited to: resource utilization, response times, latency, and sustained throughput per second (TPS).

<a name="Future Planning Efforts"></a>
## Future Planning Efforts
This section will be used to plan for future offerings.
1. Performance
2. Dashboard
3. etc
