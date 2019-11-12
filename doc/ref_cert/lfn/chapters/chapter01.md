[<< Back](../)

# 1. Introduction
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [1.1 Introduction](#1.1)
* [1.2 Terminology](#1.2)
* [1.3 Resources](#1.3)

<a name="1.1"></a>
## 1.1 Introduction

<a name="1.2"></a>
## 1.2 Terminology

Below are some of the terminology used throughout the document:

<table>
  <tr><th>Term</th><th>Description</th></tr>
  <tr><td>AZ</td><td>AZ	Availability Zone</td></tr>
    <tr><td>Certfications</td><td>include a measured performance of the adherence to, and demonstrated proficiency with, all aspects of software delivery including but no limited to planning, development (of which there are no code developed/delivered), and logistics for communications.</td></tr>
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

<a name="1.3"></a>
## 1.3 Resources
 
1. **OPNFV** https://www.opnfv.org/ - project and community that facilitates a common NFVI, continuous integration (CI) with upstream projects, stand-alone testing toolsets, and a compliance and verification program for industry-wide testing and integration to accelerate the transformation of enterprise and service provider networks.<br>
2. **CVC** https://wiki.lfnetworking.org/display/LN/Compliance+and+Verification+Committee - members-driven committee within LF Networking that recommends policies and oversight for compliance and certification program to the Governing Board of LF Networking (“Governing Board”).
3. **Conducting OVP Testing with Dovetail** https://docs.opnfv.org/en/stable-danube/submodules/dovetail/docs/testing/user/userguide/testing_guide.html
4. **Dovetail**
   1. Framework https://wiki.opnfv.org/display/dovetail/Dovetail+Test+Case+Requirements
   2. Test Plan: https://wiki.opnfv.org/display/dovetail/Dovetail+%28Danube%29+Documentation+for+Review?preview=/11698759/11698757/User%20Guide.pdf
   3. TCs:
      1. https://wiki.opnfv.org/display/dovetail/Dovetail+%28Danube%29+Documentation+for+Review
      2. Called by functest (repo): https://github.com/opnfv/dovetail/tree/master/etc/testcase
      3. Per OVP release in the release notes:
        1. https://docs.opnfv.org/en/stable-fraser/submodules/dovetail/docs/release/release-notes/index.html
       2. https://docs.opnfv.org/en/stable-danube/submodules/dovetail/docs/release/release-notes/index.html
5. **Overall documentation** is on docs.opnfv.org for the corresponding Fraser and Danube releases
   1. https://docs.opnfv.org/en/stable-fraser/testing/testing-user.html (Fraser)
   2. https://docs.opnfv.org/en/stable-fraser/testing/testing-dev.html (Fraser)
6. **OPNFV Verification Program** is an open source, community-led compliance and verification program to demonstrate the readiness and availability of commercial NFV products and services, including NFVI and VNFs, using OPNFV and ONAP components (https://www.lfnetworking.org/OVP/).
1. **OVP Whitepaper**: https://www.lfnetworking.org/resources/2019/04/03/ovp:-opnfv-verification-program/
1. **What is Verification And Validation In Software Testing**: [https://www.softwaretestingmaterial.com/verification-and-validation/](https://www.softwaretestingmaterial.com/verification-and-validation/)
1. **Verification vs Validation**: [http://softwaretestingfundamentals.com/verification-vs-validation/ ](http://softwaretestingfundamentals.com/verification-vs-validation/  )
1. **Verification/Validation/Certification**: [https://users.ece.cmu.edu/~koopman/des_s99/verification/](https://users.ece.cmu.edu/~koopman/des_s99/verification/ )