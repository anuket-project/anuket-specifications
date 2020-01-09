# 9. Adoption
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [9.1 Introduction](#9.1)
* [9.2 Transition Plan](#9.2)
  * [9.2.1 Conformance Levels](#9.2.1)
  * [9.2.2 Exception Types](#9.2.2)
  * [9.2.3 Transition Framework](#9.2.3)
* [9.3 Adoption Strategy](#9.3)
  * [9.3.1 Expectations from Operators](#9.3.1)
  * [9.3.2 Expectations from Vendors](#9.3.2)
  * [9.3.3 Expectations from Industry](#9.3.3)
* [9.4 Adoption Roadmaps](#9.4)

<a name="9.1"></a>
## 9.1 Introduction

It is vitally important for CNTT to have working solution from infrastructure vendors and mature VNFs/CNFs designs from application vendors that is compliant to CNTT specifications. It is also understood that, in some areas, the industry might not have solutions that are fully aligned with CNTT requirements. 

Therefore, a transition plan, an adoption strategy, and adoption Roadmap is needed to be agreed on within the CNTT community. This document explains those elements in details. 

<a name="9.2"></a>
## 9.2 Transition Plan

A Transition plan comprised of one or more exceptions and/or transitions is required to address technology that does not presently conform to CNTT mandates, and hence requires explicit direction to prescribe how the situation will be treated in the present, as well as in the future.

The transition plan described here will inform application designers how RC and ultimately industry certification programs will react when encountering exceptions during the qualification process, including flagging warnings and potentially errors which could prevent issuance of a certification badge.

<a name="9.2.1"></a>
### 9.2.1 Conformance Levels

- **Fully Conformant**: VNFs/CNFs or NFVI are written and designed to be fully conformant to CNTT specification with no use of any of the allowed Exceptions.
- **Conformant with Exceptions**: VNFs/CNFs or NFVI are written and designed to be conformant to CNTT with one or more of the allowed Exceptions used.

<a name="9.2.2"></a>
### 9.2.2 Exception Types

- **Technology Exceptions** : Using specific technologies that are considered non conformant to CNTT principles (such as PCIe Direct Assignment, exposure of hardware features to VNFs/CNFs).
- **Version Exceptions**: Using Versions of  Software components, , APIs, or Hardware that are different from the one specified in the specification.

<a name="9.2.3"></a>
### 9.2.3 Transition Framework

Exceptions will be clearly recorded in the Reference Model Appendix which will act as a guidance to VNFs/CNFs of what Exceptions will be allowed on each CNTT release. **Figure 1** below demonstrate the concept.

- As technology matures, fewer and fewer Exceptions will be allowed in CNTT releases.
- For each CNTT Release, VNF/CNF can be either:
  - **Fully Conformant**: No Exception used.
  - **Conformant with Exception**: One or More of the allowed Exceptions in RM has been used.  


<p align="center"><img src="../figures/vnf_cnf_transition.png" alt="Transition" title="VNF/CNF Transition Plan" width="70%"/></p>
<p align="center"><b>Figure 1:</b> Transition Plan for VNFs/CNFs within CNTT</p>


<a name="9.3"></a>
## 9.3 Adoption Strategy

<a name="9.3.1"></a>
### 9.3.1 Expectations from Operators

<a name="9.3.2"></a>
### 9.3.2 Expectations from Vendors

<a name="9.3.3"></a>
### 9.3.3 Expectations from Industry

<a name="9.4"></a>
## 9.4 Adoption Roadmap
