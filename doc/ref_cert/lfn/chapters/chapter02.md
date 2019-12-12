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

Describe the purpose.. 

- Define E2E Framework Requirements, process and automation for NFVI Certification
- Ensure Platform Stability, Operability, & Performance for target RAs

<a name="2.2"></a>
## 2.2 Methodology

Define the approach to NFVI testing, and Frameworks needed...

<a name="2.3"></a>
## 2.3 Certification Strategy & Vehicle

Define and illustrate the certification strategy and vehicle for NFVI..

<a name="2.4"></a>
## 2.4 Profiles Reference 

Define the profiles used, why they're important, and what is being certified..

<a name="2.5"></a>
## 2.5 Compliance, Verification, and Certification

Define the framework and process for NFVI certification..

<a name="2.6"></a>
## 2.6 Entry & Exit Criteria
**Entry criteria**: Before entering into NFVI certification, NFVI needs to satisfy the following requirements as entry pass:
* Lab Requirements*: The NFVI lab needs to be setup according to RA1/RA2 as defined by CNTT.

**Exit criteria**: NFVI certification testing should completed with following exit criteria:
* All mandatory test cases should pass.
* A report to be generated with test summary along with test results and statistics in HTML, JSON, XML etc. format.

<a name="2.7"></a>
## 2.7 Frameworks

List out the various frameworks requirements needed for certifications
