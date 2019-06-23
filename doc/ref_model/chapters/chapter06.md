[<< Back](../../ref_model)
# 6	Reference NFVI HW profiles and configurations
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1	Basic NFVI reference SW profile and configuration.](#6.1)
* [6.2 Network intensive NFVI reference SW profile and configuration.](#6.2)
* [6.3 Compute intensive NFVI reference SW profile and configuration.](#6.3)

The support of a variety of different workload types, each with different (sometimes conflicting) compute, storage and network characteristics, including accelerations and optimizations, drives the need to aggregate these characteristics as a hardware host profile. A host profile is essentially a “personality” assigned to a compute host (physical server, also known as (aka) compute host, host, node or pServer). The host profile contains a specification (yaml file) on how the host should be configured including the underlay networking and storage.

This chapter defines a simplified host and host profile model and the host profile configuration parameters associated with the different hardware profile types shown in **Figure 6-1**.

<p align="center"><img src="../figures/ch06_ref_nfvi_hw_profiles.PNG" alt="ref_hw_profiles" title="Reference HW Profiles" width="65%"/></p>
<p align="center"><b>Figure 6-1:</b> Reference NFVI hardware profiles.</p>

## 6.1	Hardware Profile Model
The host profile model and configuration parameters will be utilized in the reference architecture to define different hardware profiles.

A software flavour series (see Chapters 4 and 5) defines the characteristics of Virtual Machines (VMs or vServers) that will be deployed on hosts assigned a host-profile. A many to many relationship exists between software flavour series and host profiles. A given host can only be assigned a single host profile; a host profile can be assigned to multiple hosts. Different Cloud Service Providers (CSP) may utilize different naming standards for their host profiles. 

The following naming convention is utilized in this document:

`<host profile name>:: <”hp”><numeral host profile sequence #>`

When a software flavour series is associated with a host profile then a qualified name can be used as specified below. For example, for software flavor series “ns” (network intensive with SR-IOV) the above host profile name would be “ns-hp1”.

`<qualified host profile>:: <software flavor series><”-“><”hp”><numeral host profile sequence #>`

The following model depicts the essential characteristics of a host that are of interest in specifying a host profile. The host (physical server) is composed of compute, network and storage resources. The compute resources are composed of physical CPUs (aka CPU sockets or sockets) and memory (RAM). The network resources and storage resources are similarly modelled. 

