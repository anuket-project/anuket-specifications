[<< Back](../)

# 7. Integration
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [7.1 Introduction](#7.1)
* [7.2 Pre-requisites](#7.2)
* [7.3 Requirements Gathering](#7.3)
* [7.4 Access and Connectivity](#7.4)
* [7.5 Descriptor File Preparations](#7.5)
* [7.6 Deployment Installer & Install Steps](#7.6)
* [7.7 Deployment Validations](#7.7)
* [7.8 Development Validations](#7.8)
* [7.9 CICD Tool Chain (use of, process, and scripts)](#7.9)
* [7.10 Jenkins Setup & Job Creation](#7.10)
* [7.11 Compliance Validation (steps, process)](#7.11)

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

<a name="7.3"></a>
## 7.3 Requirements Gathering

Requirements gathering processes and steps:

1.  RA Requirements Gathering process
2.  Infra Requirements and Selection Process

<a name="7.4"></a>
## 7.4 Access & Connectivity

Logical steps for lab access and connectivity.

Sample steps provided mimic those utilized for POD10 test lab access.

<a name="7.5"></a>
## 7.5 Descriptor File Preparations

Reference steps describing the use, creation, and implementation of descriptor files.

e.g. Descriptor file &/or Manifest creation (data elements, use/implementation, etc

<a name="7.6"></a>
## 7.6 Deployment Installer & Install Steps

Steps and precedures for installing and setting up the RI.

<a name="7.7"></a>
## 7.7 Deployment Validations

Details explaining:
- Validation Tests Run
- Expected outpus
- Explanation of Pass/Fail
- Disposition, or next steps, based on test results (e.g. handling of failures, handoff to next tier with passing results)

<a name="7.8"></a>

## 7.8 Development Validations

CNTT RI jobs must verify all patches before merge as defined in the best open
source practices (see
[OpenStack Gates](https://docs.openstack.org/infra/system-config/devstack-gate.html)
or [Functest Gates](https://build.opnfv.org/ci/view/functest/job/functest-hunter-gate/142/))
to achieve the stability needed by CNTT. Then the deployment validations
previously detailed must be also applied for every patch proposed in RI and
all changes published in [Gerrit](https://gerrit.opnfv.org/) must be
automatically voted -1 by Jenkins in case of failures.

Only the following test cases must pass as a temporarily bypass in
[RI gates](https://build.opnfv.org/ci/view/airship/job/airship-latest-gate/) to
allow merging the next patches. At the time writing, CNTT RI is not compliant
with [RA1 Core OpenStack Services APIs]({{ "/doc/ref_arch/openstack/chapters/chapter05.html" | relative_url }})
and then a part of the containers selected in [RC1 TC Requirements]({{ "/doc/ref_cert/lfn/chapters/chapter09.html" | relative_url }})
cannot be executed successfully.

| container                               | test case         | criteria (Jenkins) |
|-----------------------------------------|-------------------|:------------------:|
| opnfv/functest-healthcheck:hunter       | connection_check  | Success            |
| opnfv/functest-healthcheck:hunter       | tenantnetwork1    | Success            |
| opnfv/functest-healthcheck:hunter       | tenantnetwork2    | Success            |
| opnfv/functest-healthcheck:hunter       | vmready1          | Success            |
| opnfv/functest-healthcheck:hunter       | vmready2          | Success            |
| opnfv/functest-healthcheck:hunter       | singlevm1         | Success            |
| opnfv/functest-healthcheck:hunter       | singlevm2         | Success            |
| opnfv/functest-healthcheck:hunter       | vping_ssh         | Success            |
| opnfv/functest-healthcheck:hunter       | vping_userdata    | Success            |
| opnfv/functest-healthcheck:hunter       | cinder_test       | Success            |
| opnfv/functest-healthcheck:hunter       | odl               | Success            |
| opnfv/functest-smoke:hunter             | tempest_scenario  | Success            |
| opnfv/functest-smoke:hunter             | neutron_trunk     | Success            |
| opnfv/functest-smoke:hunter             | networking-bgpvpn | Success            |
| opnfv/functest-smoke:hunter             | networking-sfc    | Success            |
| opnfv/functest-smoke:hunter             | barbican          | Success            |
| opnfv/functest-benchmarking-cntt:hunter | vmtp              | Success            |
| opnfv/functest-benchmarking-cntt:hunter | shaker            | Success            |
| opnfv/functest-vnf:hunter               | cloudify          | Success            |
| opnfv/functest-vnf:hunter               | vyos_vrouter      | Success            |
| opnfv/functest-vnf:hunter               | juju_epc          | Success            |

All OPNFV test cases part of RI development validation must follow the same
principles to prevent falsy testing and then to avoid blocking the RI gates.
It's worth mentioning that Functest already part of RI development validation
conform to these best practices by running all test cases vs SUTs
[currently CNTT compliant](https://build.opnfv.org/ci/view/functest/job/functest-hunter-gate/142/).

## 7.9 CICD Tool Chain (use of, process, and scripts)]

Placeholder to describe the CICD tool chain used in RI validations.  

Include flow diagram.

<a name="7.9"></a>
## 7.10 Jenkins Setup & Job Creation

Placeholder to describe the process, access, steps, instance, etc, information for the setup of Jenkins, the jobs required for validation, and the results dashboard.

<a name="7.10"></a>
## 7.11 Compliance Validation (steps, process)

Placholder to describe the purpose, steps, and process, using the Jenkins Jobs, Tool Chain, and Test Case requirements mapping to perform validations.  
