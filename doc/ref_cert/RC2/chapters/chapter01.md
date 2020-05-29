[<< Back](../)

# 1. Introduction
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents

* [1.1 Introduction](#1.1)
  * [1.1.1 Terminology](#1.1)
  * [1.1.2 Relation to other communities](#1.1)
* [1.2 Scope](#1.2)
* [1.3 Principles and Guidelines](#1.3)
  * [1.4.1 Overarching Objectives and Goals](#1.4.1)
* [1.4 Best Practices](#1.4)
* [1.5 Verification methodologies](#1.5)
*	[1.6 Assumptions & Dependencies](#1.6)
*	[1.7 Results Collation & Presentation](#1.7)
* [1.9 Resources & References](#1.9)

## Executive Summary

The Reference Conformance 2 (RC2) was established to ensure implementations of the Reference Architecture 2 (RA2), such as the Reference Implementation 2 (RI2), meet industry driven quality assurance standards for conformance, verification, and validation. For the purpose of this chapter, infrastructure and cloud native network function (CNF) testing will be performed to evaluate **Conformance** (i.e. adherence) to, and demonstrated proficiency with, all aspects of software delivery.  More specifically, Conformance includes:

 - Verified implementations of infrastructure and CNF match expected design requirements
 - Clearly stated guidelines for test, badging, and lifecycle management
 - Inclusion of Operational run-books for 3rd party supplier instantiation and validations
 - Evidence, through test results, confirming delivered code matches industrial requirements
 - Interoperability testing with Reference CNFs, ensuring integration stability and life-cycle management of the Reference CNF on the target implementation.

In summary, **Conformance** testing will be performed for **Verification** and **Validation** purposes, defined further as:

- **Verification** will be used to indicate conformance to design requirement specifications. Accomplished with Requirement Traceability and Manifest Reviews to ensure the Kubernetes infrastructure is delivered per implementation specifications.
- **Validations** is used to indicate that testing performed confirms the infrastructure and CNF meet the expected, or desired outcome, or behaviour.

**All Terms utilized throughout this chapter are intended to align with CVC definitions, and their use through CVC documentation, guidelines, and standards.**

<a name="1.1"></a>
## 1.1 Introduction

**Chapter Purpose**<br>
This chapter includes process flow, logistics, and requirements which must be satisfied to ensure Kubernetes infrastructure meets the design, feature, and capability expectations of the Reference Model (RM) and RA2. Upstream projects will define features/capabilities, test scenarios, and test cases which will be used to test for infrastructure verification purposes. Existing processes, communication mediums, and related technologies will be utilized where feasible.  Ultimately, test results of infrastructures will reduce the amount of time and cost it takes each operator to on-board and maintain vendor provided Kubernetes infrastructure and CNFs.

**Objective**<br>
Perform Kubernetes infrastructure and CNF Verification and Validations using CNTT RA2 to test code for compliance. Upstream projects will define features/capabilities, test scenarios, and test cases.

**Test Methodology**
- Verification test to make sure that the Kubernetes services have been deployed and configured correctly
- Manifest Verifications (Termed Compliance by CVC) will ensure the infrastructure is compliant, and delivered for testing, with hardware and software profile specifications defined by the RM and RA2
- Candidate CNF Validation will ensure interoperablity of CNF behaviour on the Kubernetes infrastructure.  Testing ensures CNFs can be spun up, modified, or removed, on the target infrastructure (aka Interoperability).  

<a name="1.1.1"></a>
### 1.1.1 Terminology

Terminology in this document will follow [CNTT Terminology](../../../tech/glossary.md).

<a name="1.2"></a>
## 1.2 Scope

This document covers the realisation aspects of conformance of both Kubernetes infrastructure and CNFs. The document will cover the following topics:

- Identify in details the Requirement of Test Cases (and mapping them to requirements from The Reference Model and the Kubernetes Based Reference Architecture).
- Analysis of existing community projects.
- Propose an E2E Framework for conformance of Kubernetes infrastructures and CNFs.
- Playbook of instructions, user manuals, steps of how to perform verification and conformance for both infrastructure and CNFs using the proposed E2E Framework.
- Gap analysis to identify where the Gaps are in the industry (tooling, test cases, process, etc).
- Identify development efforts needed to address any gaps identified.

**Not in Scope**
- Functional testing / validation of the application provided by the CNF is outside the scope of this work.
- ONAP is not used in the process flow for infrastructure verifications, or validations.
- Upgrades to CNFs, and the respective processes of verifying upgrade procedures and validating (testing) the success and compatibility of upgrades is not in scope.

<a name="1.3"></a>
## 1.3 Principles and Guidelines

The objectives of the Reference Conformance is to deliver a validated set of test cases to validate implementations against the reference architecture which satisfies infrastructure needs for CNF-developer teams.

These core principles will guide CFV verification deliverables:

<a name="1.3.1"></a>
### 1.3.1 Overarching Standards and Goals

1. Test Harnesses will be portable, or compatible, across all RAs/Distributions which already conform to standard interfaces and services.
2. Increase probability of CNFs.
3. Decrease operator onboarding time for both Kubernetes infrastructures and CNFs.

<a name="1.4"></a>
## 1.4 Best Practices

The following best practices have been adopted to ensure verification and validation procedures are repeatable with consistent quality in test results and RI conformances:

* Standardized test methodology / flow, Test Plan, and Test Case Suites
* Integration with upstream projects and flow (code, docs, cert criteria, etc.)
* Leverage Network and Service Models, with identified CNF-specific parameters
* Standardized conformance criteria
* Add test cases from operators, which operators already tested in their environment

<a name="1.5"></a>
## 1.5 Verification methodologies

Perform CNF interoperability verifications against an implementation of CNTT RA2. Upstream projects will define features/capabilities, test scenarios, and test cases to be executed via the OVP Ecosystem.

3rd Party test platforms may also be leveraged, if desired.

<a name="1.6"></a>
## 1.6 Assumptions & Dependencies

**Assumptions** Infrastructure and CNF testing will be considered **Testable** if the follow
qualifiers are present in a test execution, and subsequent result:
* Ability to perform Conformance, or Verification of Artifacts to ensure
  designs (RM/RA/RI) are delivered per specification
* Ability to Control (or manipulate), manifestations of RM/RA/RI for the
  purposes to adjust the test environment, and respective cases, scenarios, and
  apparatus, to support actual test validations
* Ability to monitor, measure, and report, Validations performed against a
  target, controlled system under test

In addition, respective Entrance criteria is a prerequisite which needs to be
satisfied for infrastructure and CNFs to be considered **Testable**.

**Dependencies** infrastructure and CNFs verification will rely upon test harnesses, test
tools, and test suites provided by upstream projects, including OPNFV and CNF conformance. 
These upstream projects will be reviewed
semi-annually to verify they are still healthy and active projects. Over time,
the projects representing the conformance process may change, but test parity
is required if new test suites are added in place of older, stale projects.

* infrastructure and CNF verifications will be performed against well defined instance types
  consisting of a HW and SW Profile, Configured Options, and Applied Extensions
  (See image.)

![Instance Type](../figures/RC_NFVI_VNF_Instance_Type_25Nov2019.jpg)
<p align="center"><b>Figure:</b> Instance Type</p>


**Infrastructure Instance Type:**
* Standard compute flavours to be tested are defined in RM
  [chapter 4.2.1](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter04.md#4.2.1)
* Performance profiles come in the form of Basic, Network Intensive, and
  Compute intensive. Refer to RM
  [chapter 2.3](https://github.com/cntt-n/CNTT/blob/master/doc/ref_model/chapters/chapter02.md#2.3)
  for details on these profiles.

<a name="1.7"></a>
## 1.7 Results Collation & Presentation

**Placeholder to document where results will be posted**

<a name="1.9"></a>
## 1.9 Resources & References

1. **OPNFV** https://www.opnfv.org/ - project and community that facilitates a cloud infrastructure, continuous integration (CI) with upstream projects, stand-alone testing toolsets, and a compliance and verification program for industry-wide testing and integration to accelerate the transformation of enterprise and service provider networks.<br>
2. **CVC** https://wiki.lfnetworking.org/display/LN/Compliance+and+Verification+Committee - members-driven committee within LF Networking that recommends policies and oversight for compliance and conformance program to the Governing Board of LF Networking (“Governing Board”).
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
1. **Verification/Validation/Conformance**: [https://users.ece.cmu.edu/~koopman/des_s99/verification/](https://users.ece.cmu.edu/~koopman/des_s99/verification/ )
1. _IOPS - I/O (Input/Output) operations per second_, by Vangie Beal.  Retrieved from https://www.webopedia.com/TERM/I/IOPS.html on 9/18/2019.
2. _The ultimate IOPS cheat sheet!_, by Bas van Kaam.  Retrieved from https://www.basvankaam.com/2014/07/29/the-ultimate-iops-cheat-sheet/ on 9/18/2019.
3. _An explanation of IOPS and latency_, by Dimitris Krekoukias.  Retrieved from http://recoverymonkey.org/2012/07/26/an-explanation-of-iops-and-latency/ on 9/18/2019.
