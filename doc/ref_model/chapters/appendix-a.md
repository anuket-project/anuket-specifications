[<< Back](../../ref_model)
# Appendix A - Guidelines
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [A.1 Guidelines for VNF Vendors](#A.1)
* [A.2 Guidelines for CNF Vendors](#A.2)
* [A.3 VNF Generations Details](#A.3)
* [A.4 CNF Generations Details](#A.4)
* [A.5 Technical Exceptions](#A.5)
* [A.6 Miscellaneous](#A.6)

<a name="A.1"></a>
## A.1 Guidelines for VNF Vendors

<a name="A.2"></a>
## A.2 Guidelines for CNF Vendors

<a name="A.3"></a>
## A.3 VNF Transitional Generations

VNF Generation are defined by [Adoption Governance WS](../../../doc/gov/chapters/chapter08.md#842-vnf-transition-generations)

| VNF Generation | Exception List | Notes |
|------------|----------------|-------|
| Gen1 |  |  | 
| Gen2 |  |  | 
| Gen3 |  |  | 
| Gen4 |  |  | 

<a name="A.4"></a>
## A.4 CNF Transitional Generations

CNF Generation are defined by [Adoption Governance WS](../../../doc/gov/chapters/chapter08.md#844-cnf-transition-generations)

| CNF Generation | Exception List | Notes |
|------------|----------------|-------|
| Gen1 |  |  | 
| Gen2 |  |  | 
| Gen3 |  |  | 
| Gen4 |  |  | 

<a name="A.5"></a>
## A.5 Technical Exceptions

This will be covered in: https://github.com/cntt-n/CNTT/pull/760


<a name="A.6"></a>
## A.6 Miscellaneous
### A.6.1 VNF Network Monitoring Capabilities - UseCase.
Network Monitoring capabilities exposed by NFVI Platform are used for the passive observation of VNF-specific traffic traversing the NFVI when:
* Performance issues and/or packet drops reported in VNF
* Determining performance bottle necks at VNF level
* Doing anomaly detection and network forensics

**Note:** It is responsibility of NFVI Platform to expose capability to create virtual interface having mirrored traffic from monitored VNF. This port can be attached to Monitoring VNF so that all traffic from Monitored VNF would be available for troubleshooting/debugging purpose.