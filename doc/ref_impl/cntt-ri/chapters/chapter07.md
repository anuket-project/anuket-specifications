[<< Back](../)

# 7. Integration
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [7.1 Introduction](#7.1)
* [7.2 Pre-requisites](#7.2)
* [7.3 Requirements Gathering](#7.3)
* [7.4 Access and Connectivity](#7.4)
* [7.5 Available Installers](#7.5)
* [7.6 Deployment Installer & Install Steps](#7.6)
* [7.7 Deployment Validations](#7.7)
* [7.8 CICD Tool Chain (use of, process, and scripts)](#7.8)
* [7.9 Jenkins Setup & Job Creation](#7.9)
* [7.10 Compliance Validation (steps, process)](#7.10)

<a name="7.1"></a>
## 7.1 Introduction

The purpose of this chapter is to establish an operational run-book containing sequences and steps explaining, with enough detail, how to install a Reference Implementation (RI).

The term Run-Book is synonymous with "Cookbook", and either term will be used interchangeably to indicate that if a user follows the steps or procedures in the "book", the expected result will be an RI identical to the lab utilized by CNTT for the instantiation and certification of RI-1.

It is assumed that the reader of this chapter has the skill set to install Common NFVI on their own labs.

*   Covers installers, automation, etc.
*   Integration of installers and components.

<a name="7.2"></a>
## 7.2 Prerequisites

The following are pre-requisites to be completed in advance of software deployments:

1.  Bare-metal validations: confirming delivery, rack, stack, of env and that env is "ready" for software deployments (e.g. BIOS, firmware, boot order, health, disk config, port / socket validations, MAC/NIC status, etc)

Need some details from pod 15:

- [ ] What servers/models are present
- [ ] What firmware is loaded
- [ ] BIOS settings that are not factory default - is HT on, what VT extensions?
- [ ] How many NICs are present per server?
- [ ] How many switches and how are they cabled?
- [ ] Does Airship configure disks and boot order or must this be done ahead of time?


<a name="7.3"></a>
## 7.3 Requirements Gathering

Requirements gathering processes and steps:

1.  RA Requirements Gathering process
2.  Infra Requirements and Selection Process

<a name="7.4"></a>
## 7.4 Access & Connectivity

Logical steps for lab access and connectivity.

Sample steps provided mimic those utilized for POD10 test lab access.

This RI leverages OPNFV Pharos pod 15, which is hosted by Intel and requires VPN access.  Requests for VPN access must
go through the OPNFV Infra Project.  Once on the VPN, only the DMZ network is reachable.  In order to gain access to
any of the other networks, the Foundation node (jump host) must be used.

<a name="7.5"></a>
## 7.5 Available Installers

### 7.5.1 Airship

#### 7.5.1.1 Descriptor File Preparations

Reference steps describing the use, creation, and implementation of descriptor files.  This is where the Airship Manifest
files need to be documented:

- Profiles
- Hardware
  - Server
  - Device Aliases
  - Disk Aliases
- Nodes
- Networks
- Software
- PKI-Catalog
- Secrets
- Actions

#### 7.5.1.2 Deployment Installer & Install Steps

### 7.5.2 Future Installers

At this point, the RI is based on Airship, but can be extended to employ any other OpenStack distribution.

<a name="7.6"></a>
## 7.6 Deployment Installer & Install Steps

Steps and procedures for installing and setting up the RI.
Start pulling in content from: https://wiki.opnfv.org/display/AIR/Airship+Installer+Deployment+Guide

<a name="7.7"></a>
## 7.7 Deployment Validations

Details explaining:
- Validation Tests Run
- Expected outputs
- Explanation of Pass/Fail
- Disposition, or next steps, based on test results (e.g. handling of failures, handoff to next tier with passing results)

Description of the Functest suite and what is selected for validation testing.  Need to document the line between "validation of install" and "reference certification."  It has been stated that these might be one and the same, however deployment validation could be a simple smoke test prior to starting a full run.

<a name="7.8"></a>
## 7.8 CICD Tool Chain (use of, process, and scripts)]

Placeholder to describe the CICD tool chain used in RI validations.

Include flow diagram.

<a name="7.9"></a>
## 7.9 Jenkins Setup & Job Creation

Placeholder to describe the process, access, steps, instance, etc, information for the setup of Jenkins, the jobs required for validation, and the results dashboard.

<a name="7.10"></a>
## 7.10 Compliance Validation (steps, process)

Placholder to describe the purpose, steps, and process, using the Jenkins Jobs, Tool Chain, and Test Case requirements mapping to perform validations.
