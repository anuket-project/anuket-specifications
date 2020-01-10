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
- VNF test cases model/scripts/programs
- VNF test cases configuration/profile
- VNF test tools

<a name="6.4"></a>
## 6.4 Requirement Type

VNF test cases are used to verify whether the virtualization network functions can be deployed on the CNTT-compatible NFVI and provide normal functions and meet performance, security and other requirements.

By running these VNF test cases and analysis the test results, can be used for VNF compliance, verfication,validation and performance certification and help on CNTT-compatible NFVI validation and performance certification.

All the VNF test cases should be supported and run by VNF E2E certification and verification Framework and generate outputs, logs to identify whether the test passed or failed.

CNTT defines the following four category testing which should be consistent with the VNF test category defined by OVP.

|  VNF Test Case Category   | Requirement Number  | Type (Measurement/Boolean)  |Definition/Description   |
| ------------ | ------------ | ------------ | ------------ |
|  Compliance | VNF.COMPreq.001  |  Boolean (i.e. Pass/Fail) |  Test case “must”perform a platform check against the Open Stack requirements and VNF package structure and syntax requirements  | 
|  Verification |  VNF.VERIFYreq.001 |  Boolean (i.e. Pass/Fail) | Test case “must” perform on-boarding/ verification life cycle operation validation  |
|  Validation | VNF.VALIDreq.001  |  Boolean (i.e. Pass/Fail) | Test case “must” perform API validation tests to verify operability  |
|  Performance  | VNF.PERFreq.001  | Measurement  | Test case “must” execute various performance related testing and facilitate for benchmarking the VNF performance on different profile and scenarios  |

Note: The four category testing can be gradually supported and in the future, will also cover secutiry and other test category.


<a name="6.5"></a>
## 6.5 Interaction Type

- Descrive the types of Interactions: Extended Topology, Complex (Akraino), Functional, HA, Fault, Interoperability

<a name="6.6"></a>
## 6.6 Performance Profiles

Performance profiles are not in the scope of current release, and in future it
would need to align with *chapter RM-4* defined measurements.

<a name="6.7"></a>
## 6.7 VNF Class/Family and Characteristics

- Describe and provide a Table of VNF Class/Family & Characteristics of Each

The communication network usually consists of three parts: access network, transmission network/bearer network and core network.
Following are some examples of network elements for each type of network

|  Network Type               | Network Elements  |
| ----------------------- | ------------------|
| Access Network |  Including mobile access network, wireless access network, wired access network  |
|  Transport network & Bearer network|  Including Trunk Optical Transport Network，Metro transport network，IP backbone network, etc. |
| Core Network  |Circuit domain, including MSC / VLR, GMSC, MGW, NPMSC, HLR / AUC, NPHLR, HSS，etc；Packet domain devices, including MME, SAE GW, EPC CG, EPC DNS, PCC，etc；Core network equipment for IoT private network，including PGW/GGSN、PCRF、HSS/HLR，etc；5G core network element，including AMF、SMF、UPF、UDM/UDR/AUSF、PCF、NSSF、NRF、SMSF，etc|

In addition to the above network elements, there are some other data communication network element, including FW, DNS, Router, GW, etc|

According to the current level of the entire network virtualization, the core network already has many VNFs, and also includes some datacom-type(data communication) VNFs.

We can also classify VNFs based on the level of VNF operation：

a) VNFs that operate at Layer 2 or Layer 3 and are primarily involved in switching or routing packets at these layers. Examples include vRouter, vBNG, vCE device, or vSwitch.

b) VNFs that operate at Layer 4 through Layer 7 and are involved in forwarding, dropping, filtering or redirecting packets at Layer 4 through 7. Examples include vFirewall, vADC, vIDS/vIPS, or vWAN Accelerator.

c) VNFs that are involved in the dataplane forwarding through the evolved packet core.

<a name="6.8"></a>
## 6.8 Measurement

As part of certification testing, following measurement would help for evaluating
the badging:

* VNF type defined as part of *Chapter RM-02* and its profile used for testing.
* Test cases and their test results including the test case outputs, logs
* VNF model type (TOSCA/HOT)
* Test case pass/failed
* Different NFVi profiles used and LAB reference identifier
* Test owner (point of contact)

<a name="6.9"></a>
## 6.9 VNF Test Cases

### Compliance test cases
 Currently, there VNFs can be packaged as HEAT templates or in a CSAR file using TOSCA and OVP has supported the VNF compliance test cases(compliance check based on TOSCA using ETSI SOL004 & SOL001；OpenStack HOT using ONAP VNFREQS；GSMA profile), all the OVP supported test case can be found in the following two link:

|  Test Cases |   Link|
| ------------ | ------------ |
|  Heat Test Cases | https://onap.readthedocs.io/en/latest/submodules/vnfrqts/testcases.git/docs/Appendix.html#list-of-requirements-with-associated-tests |
| Tosca Test Cases | https://onap.readthedocs.io/en/latest/submodules/vnfsdk/model.git/docs/files/csar-validation.html|

Above compliance test cases defination can be found https://github.com/onap/vnfsdk-validation/tree/master/csarvalidation/src/main/resources/open-cli-schema

 In order to adapt CNTT specification, more compliance test case will be added here.

### Verification test cases
In general， the VNF Manager, in collaboration with the NFV Orchestrator, the VIM and the EM, is responsible for managing a VNF's lifecycle. The lifecycle phases are listed below：
  • VNF on-boarding, it refers to VNF package onboarding to service/resouce Orchestrator
  • VNF instantiation, once the VNF is instantiated,  its associated VNFCs have been successfully instantiated and have been allocated necessary NFVI resources
  • VNF scaling/updating, it means the VNF can scale or update by allocating more or less NFVI resources
  • VNF termination, any NFVI resources consumed by the VNF can be cleaned up and released.

 OVP has also supported the lifecycle test case:https://wiki.lfnetworking.org/display/LN/VNF+Validation+Minimum+Viable+Product?src=contextnavpagetreemode


### Validation Test cases
From the current situation of operators, there are usually corresponding functional test specifications for each types of VNFs. Therefore, different types of VNFs have different functional test cases. Normally, functional tests for VNFs require the cooperation of surrounding VNFs. Or use the instruments to simulate the functions of surrounding VNFs for testing.
Therefore, different test cases need to be defined according to different types of VNFs

### Performance Test cases
This is the same as what described in validation test cases，the performance test cases need to be defined according to different types of VNFs.
Combined with the classification of VNF, according to the protocol level that VNF operates, it can include:
  • VNF data plane benchmarking, like forwarding Performance Benchmarking,Long duration traffic testing, low misrouting and so on.
  • VNF control plane benchmarking, like throughput
  • VNF user plane benchmarking, like Packet Loss,Latency, Packet Delay

 ETSI spec has also defined the testing method http://www.etsi.org/deliver/etsi_gs/NFV-TST/001_099/001/01.01.01_60/gs_nfv-tst001v010101p.pdf
