[<< Back](../../ref_model)
# 9	Infrastructure Operations and Lifecycle Management
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [9.1 MVP Status.](#9.1)
* [9.2 Configuration and Lifecycle Management](#9.2)
* [9.3 Resource and Service Assurance](#9.3)
* [9.4 Capacity Management](#9.4)
* [9.5 Infrastructure Maintenance](#9.5)


The purpose of this chapter is to define the capabilities required of the infrastructure to ensure it is effectively supported, maintained and otherwise lifecycle-managed by Operations teams.  This includes requirements relating to the need to be able to maintain infrastructure services "in-service" without impacting the applications and VNFs, whilst minimising human labour. It shall also capture any exceptions and related assumptions.

<a name="9.1"></a>
## 9.1 MVP Status

This chapter is not MVP, and is not currently expected to be ready for the first deliverable draft.

<a name="9.2"></a>
## 9.2 Configuration and Lifecycle Management

This is a placeholder for Configuration and Lifecycle Management requirements. e.g.
- all configuration activities can be done via API (link to interfaces chapter?)
- desired state configuration
- declarative configuration management; embed the logic of performing LCM tasks (create, update, delete) into infra control plane components
- making orchestration closed-loops as small as possible
- etc.

<a name="9.3"></a>
## 9.3 Resource and Service Assurance

This is a placeholder for Resource and Service Assurance requirements. e.g.
- monitoring, logging and alerting of individual components/resources (e.g. a single host)
- monitoring, logging and alerting of an infrastructure service (e.g. NFVI in a region/location)
- ability to detect and deal with rogue workloads
- ability to detect and deal with defective components
- closing the loop with orchestration to perform healing activities based on events / configuration management input
- effective telemetry/event streams for enhanced decision making by assurance systems
- etc.

<a name="9.4"></a>
## 9.4 Capacity Management

This is a placeholder for Capacity Management requirements. e.g.
- effective telemetry and events to allow for data-driven decisions
- ability to include application metrics/events?
- etc.

<a name="9.5"></a>
## 9.5 Infrastructure Maintenance

This is a placeholder for Infrastructure Maintenance requirements. e.g.

- ability to drain hosts
- ability to update control plane before host agents etc.
- ability to 
