[<< Back](../)

# 2. NFVI E2E C&V Framework Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction](#2.1)
* [2.2 Methodology](#2.2)
* [2.3 Certification Strategy & Vehicle](#2.3)
* [2.4 Profiles Reference](#2.4)
* [2.5 Compliance, Verification, and Certification](#2.5)
* [2.6 Entry & Exit Criteria](#2.6)
* [2.7 Frameworks](#2.7)

##Synopsis:
Ensure Reference Implementation (RI) of CNTT Reference Model (RM) and CNTT Reference Architecture (RA) meets industry driven quality assurance standards for compliance, verification and validation. The OPNFV Verified Program (OVP), by Linux Foundation Networking (LFN), overseen by the Compliance Verification Committee (CVC), will provide tracking and governance for RM/RA verification.

For the purposes of this chapter, NFVI+VNF testing will be performed for Verification, Validations, ultimately leading to Certifications indicating a measured performance of the adherence to, and demonstrated proficiency with, all aspects of software delivery including but no limited to planning, logistics for communication, and testing of installed, or implemented, NFVI. Similarily, VNFs will be checked for Compliance and Validations against the RM and RA requirements ensuring VNF instantiation, stability, and successful removal of the VNF from the implementation of the stated architecture. The additional VNF testing will verify that the developed VNF meets prescribed RM/RA infrastructure standards.

In summary, NFVI+VNF testing will be performed for Verification and Validation purposes.

Verification will be used to indicate conformance to design requirement specifications. Activities involved Reviews and Walk-Throughs to ensure the NFVI is delivered per implementation specifications.

Validations is used to indicate testing performed to confirm the actual output of a product meets the expected, or desired outcome, or behavior.

All Terms utilized throughout this chapter are intended to align with CVC definitions, and their use through CVC documentation, guidelines, and standards. This chapter will outline the Requirements, Process, and Automation, needed to deliver NFVI Certification.

<a name="2.1"></a>
## 2.1 Introduction
NFVI (Network Functions Virtualization Infrastructure) refers to the physical resources (compute, storage and network) on which virtual network functions (VNFs) are deployed. As such, the performance of a VNF depends on the underlying NFVI over which it is hosted. A certain VNF may perform good in one hardware and may perform worst in another. Thus, a need arises to certify NFVI that can help in onboarding VNFs onto a hardware with an acceptable level of VNF performance. Certain frameworks like [yardstick](https://github.com/opnfv/yardstick), [vsperf](https://github.com/opnfv/vswitchperf) etc. provide a set of tests that can be run on a hardware to obtain Key Performance Indicators (KPIs) which give a measurable output of the NFVI's performance. With these KPIs, a decision can be made on the VNFs that can offer an acceptable level of performance when on-boarded on the NFVI.

<a name="2.2"></a>
## 2.2 Methodology
The NFVI provided by hardware vendors is consumed or used by VNFs via APIs exposed by Virtualised Infrastructure Manager (VIM). The resources created by VIM on the NFVI use the underlying physical hardware (compute, storage and network) either directly or indirectly. CNTT recommends RA1/RA2 to be used as a reference architecture for NFVI certification. This  would provide a set of standard interaces to create resources on NFVI. Below step by step process illustrates the NFVI certification methodology:
* CNTT RA1/RA2 is deployed on NFVI that needs to be certified.
* A set of tests are run on NFVI to determine the NFVI readiness for certification process.
* Golden KPIs are taken as a reference.
* A set of tests are run on the target NFVI.
* KPIs obtained from the target NFVI are collected and submitted to certification portal.
* The NFVI KPIs are reviewed and compared with Golden KPIs to determine if the certification badge is to be provided to NFVI or not.
* Perform VNF interoperability verifications against an implementation of CNTT reference architecture, leveraging existing OPNFV Intake Process. Upstream projects will define features/capabilities, test scenarios, and test cases to augment existing OVP test harnesses to be executed via the OVP Ecosystem. Third-party test platforms may also be leveraged, if desired.

<p align="center"><img src="../figures/RC_CertificationMethodology.jpg" alt="Certification Methodology" title="Certification Methodology" width="100%"/></p>
<p align="center"><b>Figure:</b> Certification Methodology</p>

<a name="2.3"></a>
## 2.3 Certification Strategy & Vehicle
In order to begin the certification process, NFVI needs to be validated and expected to be in a required state. This state would be determined by running tests as described in Reference Implementation. Once the target NFVI passes these tests, it would become a candidate for NFVI certification. If NFVI fails the tests, it will not be move to next workflow for certification. NFVI+VNF validations consist of a three part process for Compliance, Validation, and Performance. Adherence to Security standards are equally important and addressed in [Chapter 7 of CNTT RM](../../../ref_model/chapters/chapter07.md).

The three part verificaiton process includes NFVI Manifest Validations, Emprical Baseline measurements against targeted VNF families, and Candidate VNF verifications. More specifically,
* NFVI Verification (Compliance): NFVI is the SUT, ensuring NFVI is compliant with specs of RM and RA accomplished with Manifest Validations (performed via Echo Tests)
* Empirical Validation with Reference VNF (Validation): NFVI is the SUT, ensuring NFVI runs with Golden VNFs and is instrumented to objectively validate resources through consumption and measurement
* Candidate VNF Certification (Validation & Performance): VNF is the SUT, ensuring VNFs operate with RM and RA leveraging VVP/CVP/VFNSDK Test Suites
* Security: Ensures NFVI+VNF is free from known security vulnerabilities, utilizing industry standard cyber security frameworks (Refer to CNTT Chapter 7 Security for additional test/verification details)
Validations are performed against an Infrastructure Profile Catalog, VNF performance profile, and targeted VNF class or family for baseline measurements.

The Infrastructure Profile Catalog contains the following attributes:

* Profile is a collection of (limited) options offered by the infrastructure to the VNF
  * Capabilities
  * Metrics
  * Compute flavors
  * Interface options
  * Storage extensions
  * Acceleration capabilities
* Profiles are offered to VNFs as an instance types with predefined compute flavors.
  * A particular set of options is an instance type
  * Compute flavors: S, M, L
* VNF performance profiles, for which NFVI validations will support and be verified against, are defined as basic, network intensive, and compute intensive. Details for each of these profiles can be found in chapter 2.3.
<p align="center"><img src="../figures/RC_NFVI_Profiles.jpg" alt="NFVI Profiles" title="NFVI Profiles" width="100%"/></p>
<p align="center"><b>Figure:</b> NFVI Profiles</p>
Targeted VNF Classes/Families for baseline measurements are described in chapter XXXX.

<a name="2.4"></a>
## 2.4 Profiles Reference 
Different vendors have different types of VNFs to serve different use-cases. A VNF like Broadband Network Gateway (BNG) would require high netorking throughout whereas a VNF like Mobility Management Entity (MME) woud require high computing performance. As such, BNG would require high KPI values for network throughput and MME would require high CPU performance KPIs like Index Score, Instructions Per Second (IPS) etc. The target NFVI to cater these needs woud have different characteristics. Depending on VNF's requirements, the NFVI can be categorised into below profiles:
* Basic (B) profile for standard computing
* Compute intensive (C) profile where predictable computing performance is expected and
* Network intensive (N) profile offerring low latency and high networking throughout
Similarly, different NFVI vendors may specialise in different hardware profiles and some may specialise in both VNFs and NFVI. To cater to different needs from multiple NFVI vendors, CNTT allows different types of NFVI certification based on their types of [profile](../../../ref_model/chapters/chapter02.md#2.3)
 * Certify Vendor NFVI Hardware solution: This allows for certification of only NFVI.
 * Certify Vendor NFVI Hardware and Software Solution: This allows for certification for NFVI running a particular VNF.

<a name="2.5"></a>
## 2.5 Compliance, Verification, and Certification
The below set of steps define the compliance, verification and certification process for NFVI
* Based on VNF's requirements, NFVI profile is selected - B, C, N
* NFVI readiness is checked for certification.
* The test VNFs are on-boarded using automation scripts on the NFVI.
* VNF on-boarding is validated by running functional tests to ensure that the on-boarding is successful.
* VNF performance tests are executed and NFVI KPIs are recorded during the tests.
* KPI comparison is run to compare NFVI KPIs with Golden KPIs, which serve as a reference for NFVI certification.
* If NFVI KPIs meet Golden KPIs, NFVI is certified and granted a certification badge.
* If NFVI KPIs do not meet Golden KPIs, no certification is provided.
<p align="center"><img src="../figures/RC_Ref_NFVI_Profiles.jpg.jpg" alt="Reference NFVI Profiles Implementation" title="Reference NFVI Profiles Implementation" width="100%"/></p>
<p align="center"><b>Figure:</b> Reference NFVI Profiles Implementation</p>

<a name="2.6"></a>
## 2.6 Entry & Exit Criteria
**Entry criteria**: Before entering into NFVI certification, NFVI needs to satisfy the following requirements as entry pass:
* Lab Requirements*: The NFVI lab needs to be setup according to RA1/RA2 as defined by CNTT and should be in the required state.

**Exit criteria**: NFVI certification testing should completed with following exit criteria:
* All mandatory test cases should pass.
* Test results collated, centralized, and normalized, with a final report generated showing status of the test scenario/case (e.g. Pass, Fail, Skip, Measurement Success/Fail, etc), along with traceability to a functional, or non-functional, requirement.

<a name="2.7"></a>
## 2.7 Frameworks
The NFVI certification framework deals with the process of testing NFVI in below three areas:
* Compliance: The NFVI needs to comply to CNTT RA1/RA2.
* Validation: Validation deals with the ability of NFVI to respond to Cloud APIs and interfaces.
* Performance: Performance deals with running tests on NFVI depending on the NFVI profile and collecting KPIs.

The NFVI KPIs are compared with Golden KPIs, which serve as a reference for NFVI certification. If NFVI KPIs meet Golden KPIs, NFVI is certified and granted a certification badge. If NFVI KPIs do not meet Golden KPIs, no certification badge is provided.
