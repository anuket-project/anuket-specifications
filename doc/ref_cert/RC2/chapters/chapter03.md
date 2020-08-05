[<< Back](../)

# 3. Kubernetes Test Cases and Traceability to CNTT Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [3.1 Introduction](#3.1)
* [3.2 Selection Criteria](#3.2)
* [3.3 Traceability Matrix](#3.3)
  * [3.3.1 K8s Architecture Requirements](#3.3.1)
  * [3.3.2 Infrastructure](#3.3.2)
  * [3.3.3 Interfaces & APIs](#3.3.3)
  * [3.3.4 Dashboard](#3.3.4)
  * [3.3.5 K8s API benchmarking](#3.3.5)
  * [3.3.6 Dataplane Benchmarking](#3.3.6)
  * [3.3.7 K8s Workload onboarding and testing](#3.3.7)
  * [3.3.8 Tenants](#3.3.8)
  * [3.3.9 LCM](#3.3.9)
  * [3.3.10 Assurance](#3.3.10)
  * [3.3.11 Security](#3.3.11)
  * [3.3.12 Resilience](#3.3.12)
  * [3.3.13 Bare-metal validations](#3.3.13)
* [3.4 Test Cases Traceability to Requirements](#3.4)
  * [3.4.1 Test Cases Traceability](#3.4.1)



<a name="3.1"></a>
## 3.1 Introduction

The scope of this chapter is to identify and list down test cases based on requirements defined in [Reference Architecture-1 (RA-2)](../../../ref_arch/kubernetes/README.md). This will serve as traceability between test cases and requirements.

Note that each requirement may have one or more test cases associated with it.

Priority for tests:

**must**: Test Cases that are marked as must are considered mandatory and must pass successfully.

**should**: Test Cases that are marked as should are expected to be fulfilled by platform but it is up to each service provider to accept an platform targeting reference architecture that is not reflecting on any of those requirements. The same applies to should not.

**may**: Test cases that are marked as may are considered optional. The same applies to may not.

<a name="3.2"></a>
## 3.2 Selection Criteria
Test cases and their dependencies must be open source. The test cases (or test suite with the test case) as well as the environment needed to run the test should be reproducible by any party following publicly available documentation.

Examples initiatives (having testing tools, test suites, etc) with test cases which could be used include K8s Conformance, K8s e2e, Sonobuoy, OPNFV FuncTest, CNF Conformance.


<a name="3.3"></a>
## 3.3 Traceability Matrix

The following is a Requirements Traceability Matrix (RTM) mapping Test Case, and/or Test Case Coverage, to RM and RA requirements -- configuration, deployment, runtime.


> [TBD Needs update] The RTM contains RM configuration requirements listed “per profile”, followed by RA requirements.  Requirements fall into 8 domains: general(gen), infrastructure(inf), VIM(vim), Interface & API(int), Tenants(tnt), LCM(lcm), Assurance(asr), Security(sec).

>[TBD NEEDS UPDATE] For detailed information on RM & RA Platform and Workload requirements, please refer to  ...




<a name="3.3.1"></a>
### 3.3.1 Kubernetes Architecture Requirements

This section focuses on the test case covering requirements in [RA-2 Chapter 2.3](https://cntt-n.github.io/CNTT/doc/ref_arch/kubernetes/chapters/chapter02.html#2.3) for the K8s architecture. 




| RM/RA Ref | Category | Sub-Category | Type (functional, performance) | High-level test definition | Test name and project | Priority | 
|---|---|---|---|---|---|---|
| req.gen.cnt.01 | General | Cloud nativeness | Functional | | | | Must | 
| req.gen.cnt.02 | General | Cloud nativeness | Functional | | | | Must | 




