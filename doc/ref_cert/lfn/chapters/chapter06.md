[<< Back](../)

# 6. VNF Test Case Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 Assumptions](#6.2)
* [6.3 Developer Deliverables](#6.3)
* [6.4 Requirement Type](#6.4)
* [6.5 Interaction Type](#6.5)
* [6.6 Performance Profiles](#6.6)
* [6.7 VNF Class/Family and Characteristics](#6.7)
* [6.8 Measurement](#6.8)
* [6.9 VNF Test Cases](#6.9)

<a name="6.1"></a>
## 6.1 Introduction

> Scope of this chapter is to have a list of test cases needed (a detailed table of sort)

Network functions virtualization (NFV) and softwaredefined networking (SDN) offer service providers increased service agility, OpEx improvements, and back-office automation. Disaggregation, the approach of decoupling the various layers of the stack, from hardware, to NFVI/VIM software, to dataplane acceleration, SDN controllers, MANO components, and VNFs, enables multi-vendor deployments with best-of-breed options at each layer.

CNTT is defining the required architecture and model for NFVI along with VNF specification which will help to decouple the various commercial product layers and it is important to define and certify the VNF and NFVI.Therefore,in addition to verify general NFVI capabilities based on CNTT RM/RA/RI, it is also necessary to verify that VNFs can provide virtualization functions normally based on the CNTT-compatible NFVI. So the VNF testing should at least include: Compliance，verification，validation，Performance. With the improvement of specifications, the types of tests may continue to add in the future.

In this chapter, the scope and requirements of VNF test cases are defined as reference for VNF certification, which helps to perform the various compliance and verification (C&V) testing and submit results to LFN OVP certification portal.

<a name="6.2"></a>
## 6.2 Assumptions
Here lists the assumptions for VNF certification:
- NFVI is ready and it should be CNTT-compatible NFVI
- VNF template is ready to deploy and certificate
- VNF Test environment is ready, the test environment contains test functions and entities(NFVI, MANO, VNF Test Platform, VNF Test Tools) to enable controlling the test execution and collecting the test measurements.
- VNF Test Platform has been integrated with CICD chain
- VNF test result can be generated with OVP defined format

<a name="6.3"></a>
## 6.3 Developer Deliverables

This section define the developer Deliverables (artifacts),the following list the expectations and deliverables we expect from developers in order to achieve the VNF certification:
- VNF test cases scripts/programs
- VNF test cases configuration/profile
- VNF test tools

<a name="6.4"></a>
## 6.4 Requirement Type

- Describe the types of requirement:  Bare metal, API, etc

<a name="6.5"></a>
## 6.5 Interaction Type

- Descrive the types of Interactions: Extended Topology, Complex (Akraino), Functional, HA, Fault, Interoperability

<a name="6.6"></a>
## 6.6 Performance Profiles

- Descrie and provide a Table showing Performance Profiles

<a name="6.7"></a>
## 6.7 VNF Test Case Category
In order to Certificate the VNF, CNTT define the following four category testing which should be consistent with the VNF test category defined by OVP.

|  VNF Test Case Category   |  Category Definitions  |
| ----------------------- | ------------------|
|  Compliance testing|  compliance check based on TOSCA using ETSI SOL004 & SOL001；OpenStack HOT using ONAP VNFREQS；GSMA profile  |
|  Verification testing|  Perform on-boarding/ verification life cycle operation (from instantiation,configuration, update, termination) using MANO supporting CNTT compliant NFVi. |
| Validation Testing  |  Perform various VNF type specific functionality operations on CNTT RA & RM compliant NFVi |
|Performance testing| Perform various performance related testing and facilitate for benchmarking the VNF performance on different profile and scenarios.|

Note: The four category testing can be gradually supported.


<a name="6.8"></a>
## 6.8 Measurement

- Describe Assumptions:  Automatable, Integrated with CICD tool chain

<a name="6.3"></a>
## 6.3 Developer Deliverables

- Describe - Developer Deliverables (artifacts) - what kinds of expectations and deliverables do we expect from developers.

<a name="6.4"></a>
## 6.4 Requirement Type

- Describe the types of requirement:  Bare metal, API, etc

<a name="6.5"></a>
## 6.5 Interaction Type

- Descrive the types of Interactions: Extended Topology, Complex (Akraino), Functional, HA, Fault, Interoperability

<a name="6.6"></a>
## 6.6 Performance Profiles

- Descrie and provide a Table showing Performance Profiles

<a name="6.7"></a>
## 6.7 VNF Class/Family and Characteristics

- Describe and provide a Table of VNF Class/Family & Characteristics of Each

<a name="6.8"></a>
## 6.8 Measurement

> we need to a list of VNFs measurements we need to collect.

<a name="6.9"></a>
## 6.9 VNF Test Cases
> we need to have list of VNF test cases in here.

- Compliance test cases

- Verification test cases

- Validation Test cases

- Performance Test cases
