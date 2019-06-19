[<< Back](../../ref_model)
# 6	Reference NFVI HW profiles and configurations
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

The support of a variety of different workload types, each with different (sometimes conflicting) compute, storage and network characteristics, including accelerations and optimizations, drives the need to aggregate these characteristics as a hardware host profile. A host profile is essentially a “personality” assigned to a compute host (physical server, also known as (aka) compute host, host, node or pServer). The host profile contains a specification (yaml file) on how the host should be configured including the underlay networking and storage.

This chapter defines a simplified host and host profile model and the host profile configuration parameters associated with the different hardware profile types shown in **Figure 6-1**.

