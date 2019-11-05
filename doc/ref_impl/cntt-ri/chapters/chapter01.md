[<< Back](../)

# 1. Overview
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [1.1 Introduction.](#1.1)
  * [1.1.1 About Reference Implementation.](#1.1.1)
  * [1.1.2 Relationship with other communities.](#1.1.2)
* [1.2 Terminology.](#1.2)
* [1.3 Scope.](#1.3)
* [1.4 Roadmap.](#1.4)


<a name="1.1"></a>
## 1.1 Introduction



<a name="1.1.1"></a>
### 1.1.1 About Reference Implementation

This document includes the requirement and deployment details of the the first reference implementation for CNTT. This first reference implementation
 follows the requirement and architecture design of the [OpenStack Based Reference Architecture](../../../ref_arch/openstack/chapters). This document
 will includes the detailed requirement of RI for CNTT, NFVi configurations according to the requirement of RA and each different flavor of VNF, Lab 
 requirements for RI deployment and velidation and installer requirement. This reference implementation will fully reveal the capabilities and features
 defined in CNTT RM and RA, and thus will be utilized as 'golden NFVi' in the Reference Compliance of CNTT.
 
 In order to promote quick deployment of RI and not re-invent wheels, the CNTT community works closly with OPNFV, utilizing and evolving OPNFV CI 
 pipeline and installer automation and testing automation capabilities. Detailed collaboration and contribution to OPNFV will be concluded in the 
 following sessions.

<a name="1.1.2"></a>
### 1.1.2 Relationship with other communities

1. Relationship with OPNFV

Current collaboration with OPNFV includes:

1) OPNFV CIRV project. 

This project is the 'landing' place for CNTT in OPNFV. It is responsible for driving activities of CNTT within OPNFV, working with multiple projects,
including Airship, Functest, Dovetail, and ext.. The project team is working closely with the CNTT RI WSs. 

Detailed infomation of this project can be found here: 
https://wiki.opnfv.org/pages/viewpage.action?pageId=47284396


2) OPNFV Infra WG.

The CNTT RI WSs work closely with the OPNFV Infra WG for the requirement of Labs and Installers. The detailed requirements explained in 
[Chapter 4](ref_impl/cntt-ri/chapters/chapter04.md) and [Chapter 5](ref_impl/cntt-ri/chapters/chapter05.md) of this document are discussed and 
reviewed with the Infra WG, and will be used as guideline for detailed development work in Infra WG.

3) OPNFV Testing WG.

The CNTT RI WSs works with the Testing WG for minifest testing for the Reference implementation.

4) Airship Project.

The Airship Project will be used as the intaller for the first RI.

2. Relationship with OVP

This RI will act as 'golden NFVi' for the test of VNFs within OVP.

<p align="center"><img src="../figures/ch01_relationship.png" alt="relationship" title="Document Types" width="100%"/></p>
<p align="center"><b>Figure 1-1:</b> CNTT-RI Relationship with other communities.</p>


<a name="1.2"></a>
## 1.2 Terminology

Terminology in this document will follow [CNTT Terminology](ref_model/chapters/glossary.md).


<a name="1.3"></a>
## 1.3 Scope

<p align="center"><img src="../figures/ch01_scope.png" alt="scope" title="Document Types" width="100%"/></p>
<p align="center"><b>Figure 1-2:</b> CNTT-RI Scope.</p>

<a name="1.4"></a>
## 1.4 Roadmap

This document is planned to release on Jan. 2020, while the first of RI code (including installers, minifest test cases, automation CI) will follow the release 
routin of OPNFV Release J.

