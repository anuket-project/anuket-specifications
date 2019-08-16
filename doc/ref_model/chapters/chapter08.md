[<< Back](../../ref_model)
# 8 Compliance, Verification, and Certification
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction.](#8.1)
* [8.2 Principals and Guidelines](#8.2)

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

<b><u>Overarching Objectives and Goals</u></b><br>
1. Deliver certified reference architecture which matches VNF-developer specifications<br>
2. All accomplished with augmentation to the current OVP ecosystem.<br>
3. Certified VNFs will on-board and function first shot<br>

<b><u>Verification Methodologies</u></b><br>
1. Engineering package validations will be performed against targeted infrastructure/architecture<br>
2. Configuration settings/features/capabilities will be baseline<br> 
3. Test runs using reference model VNFs will validate RA chosen by the VNF-supplier meets developer needs<br>
4. Verification decisions will be based on data

<b><u>Governance</u></b><br>
1. Certification badges will be presented by the CVC<br>
2. CVC will maintain requirements for certification<br>




<a name="8.3"></a>
## 8.3 Recommendations

<a name="8.4"></a>
## 8.4 Compliance, Verification, and Certification process and life cycle

<a name="8.4.1"></a>
### 8.4.1 NFVI reference architectures

<a name="8.4.2"></a>
### 8.4.2 Test suites

---

<a name="Terms and Definitions"></a>
## Terms and Definitions

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
