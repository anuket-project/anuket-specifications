[<< Back](../)

# 2. Reference Implementation Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [2.1 Introduction](#2.1)
* [2.2 Reference Architecture Requirement](#2.2)
* [2.3 Reference Implementation Requirement](#2.3)
* [2.4 Typical Example for Reference Implementation](#2.3)

<a name="2.1"></a>、


## 2.1 Introduction


**must**: Requirements that are marked as _must_ are considered mandatory and must exist in the reference architecture and reflected in any implementation targeting this reference architecture. The same applies to _must not_.

**should**: Requirements that are marked as _should_ are expected to be fulfilled by the reference architecture but it is up to each service provider to accept an implementation targeting this reference architecture that is not reflecting on any of those requirements. The same applies to _should not_.
> RFC2119

**may**: Requirements that are marked as _may_ are considered optional. The same applies to _may not_.


<a name="2.2"></a>
## 2.2 Reference Architecture Requirement

This is the reference implementation for OpenStack based CNTT RA. Please refer to [CNTT Reference Architectures:OpenStack Based:Chapter 02 - Architecture Requirement](https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/openstack/chapters/chapter02.md) for the details of RA requirement

The implementation should follow all the requirement identified in the RA chapter.

<a name="2.3"></a>
## 2.3 Reference Implementation Requirement

The implementation **must** use open source software.

The implementation **may** use software version same or different from the main branch of upstream software

The implementation **must** use open source API as identified in the RA

The implementation **must** provide availability and resiliency according to requirement identified in the RA

The Implementation **must** be able to support VM for different profile, namely Base, Network Intensive, and Compute Intensive

The Implementation **must** support automatic deployment and configuration

The implementation **must** follow generic installer requirements identified in the following chapters when deploy

The implementation **must** be scalable in order to fix into lab testing as well as large scale field deployment

The implementation **must** provide detailed capabilities needed so as to verify test cases for Reference compliance

The implementation **must** be capable of acting as 'golden NFVi' and support VNFs under certification in OVP


<a name="2.4"></a>
## 2.4 Typical Example for Reference Implementation

The following figure explicitely shows a typical example for reference implementation based on OpenStack. Note that this is just an example, actual
deployment can be varied in multiple aspects, including the number of VIM-ctrl, SDN/no-SDN, the number of network nodes and storage nodes and 
leaf-spine/no leaf-spine. 


<p align="center"><img src="../figures/chp02_typical RI.PNG" alt="relationship" title="Document Types" width="100%"/></p>
<p align="center"><b>Figure 1-1:</b> A Typical Example for RI.</p>

For the purpose of reference implementation and verification, OPNFV based RI will include the following components:

1 foundation node: support for building and lifecycle managing an OpenStack cloud, act as jump server and Jenkins slave in OPNFV CI

3 control nodes: support for cloud control service identified in RA

N compute nodes: support for cloud workload service identified in RA. (N>=2)

Note that the number "N" can be defined according to the need for deployment or verification. It will be defined by actual work load that is going to run 
on the cloud. N need to be equal or larger than 2 so as to fit into the requirement for resiliency.

 
