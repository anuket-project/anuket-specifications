[<< Back](../../ref_model)
# Appendix A - Guidelines For VNF Vendors
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [A.1 Goals](#A.1)
* [A.2 Intro and Terminology](#A.2)
* [A.3 VNF Maturity Levels](#A.3)
* [A.4 Links](#A.4)
* [A.5 Miscellaneous](#A.5)

<a name="A.1"></a>
## A.1 Goals
This Appendix has two goals:
1. Provide guidance to VNF or more generally Application vendors on how to consume CNTT Reference Model and Architectures
2. Provide usable definitions of maturity levels for VNF software architecture between Physical-to-Virtual migration and “Cloud Native”.

The goal is not to be prescriptive on how to re-architect existing or architect new applications but rather staying within scope of focusing on interface and interaction between applications and platform.

<a name="A.2"></a>
## A.2 Intro and Terminology
(Summary status and trends of ETSI NFV and Cloud. Decoupling application from platform. Terminology used/introduced.)

<a name="A.3"></a>
## A.3 VNF Maturity Levels
(And how they map to CNTT RAs)

<a name="A.4"></a>
## A.4 Links


<a name="A.5"></a>
## A.5 Miscellaneous
### A.5.1 VNF Network Monitoring Capabilities - UseCase.
Network Monitoring capabilities exposed by NFVI Platform are used for the passive observation of VNF-specific traffic traversing the NFVI when:
* Performance issues and/or packet drops reported in VNF
* Determining performance bottle necks at VNF level
* Doing anomaly detection and network forensics

<b>Note: It is responsibility of NFVI Platform to expose such capabilities (like vTAP) to have visibility into VNF traffic. 
 NFVI must expose capability to created virtual interface having mirrored traffic from monitored VNF. This port can be attached to Monitoring VNF so that all traffic from Monitored VNF would be available for troubleshooting/debugging purpose.</b>

