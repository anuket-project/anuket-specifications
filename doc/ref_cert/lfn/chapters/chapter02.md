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

<a name="2.1"></a>
## 2.1 Introduction
NFVI (Network Functions Virtualization Infrastructure) refers to the physical resources (compute, storage and network) on which virtual network functions (VNFs) are deployed. As such, the performance of a VNF depends on the underlying NFVI over which it is hosted. A certain VNF may perform good in one hardware and may perform worst in another. Thus, a need arises to certify NFVI that can help in onboarding VNFs onto a hardware with an acceptable level of VNF performance. Certain frameworks like [yardstick](https://github.com/opnfv/yardstick), [vsperf](https://github.com/opnfv/vswitchperf) etc. provide a set of tests that can be run on a hardware to obtain Key Performance Indicators (KPIs) which give a measurable output of the NFVI's performance. With these KPIs, a decision can be made on the VNFs that can offer an acceptable level of performance when on-boarded on the NFVI.

<a name="2.2"></a>
## 2.2 Methodology
The NFVI provided by hardware vendors is consumed or used by VNFs via APIs exposed by Virtualised Infrastructure Manager (VIM). The resources created by VIM on the NFVI use the underlying physical hardware (compute, storage and network) either directly or indirectly. CNTT recommends RA1/RA2 to be used as a reference architecture for NFVI certification. This  would provide a set of standard interaces to create resources on NFVI. Below step by step process illustrates the NFVI certification methodology:
* CNTT RA1/RA2 is deployed on NFVI that needs to be certified.
* A set of tests are run on NFVI to determine the NFVI readiness for certification process,
* Golden KPIs are taken as a reference.
* A set of tests are run on the target NFVI.
* KPIs obtained from the target NFVI are collected and submitted to certification portal.
* The NFVI KPIs are reviewed and compared with Golden KPIs to determine if the certification badge is to be provided to NFVI or not.

<a name="2.3"></a>
## 2.3 Certification Strategy & Vehicle
In order to begin the certification process, NFVI needs to be validated and expected to be in a required state. This state would be determined by running tests as described in Reference Implementation. Once the target NFVI passes these tests, it would become a candidate for NFVI certification. If NFVI fails the tests, it will not be move to next workflow for certification.

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
