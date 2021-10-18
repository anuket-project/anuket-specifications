# Introduction

![Scope](../figures/bogo_ifo.png)

## Executive Summary

The Reference Conformance for the Kubernetes-based workstream (RC2) was established to ensure implementations of the Anuket Reference Architecture 2 (RA2), such as the Reference Implementation 2 (RI2), meet functional and performance requirements specified in RA2 and the Anuket Reference Model (RM). Cloud infrastructure and workload verification and validation will be utilised to evaluate **Conformance** (i.e. adherence) to the RA2 and RM requirements. Conformance scope includes:

 - Test cases, with traceability to requirements, to validate that the cloud infrastructure implementation meets the expected capabilities specified in RA-2 and that the workloads consume compliant cloud infrastructure resources
 - Verify, with requirements traceability, that the installation cookbooks (manifests) of RI-2 are in conformance with the RA-2 specifications (for example, software versions, plugins, and configurations)
 - Guidelines for processes, environments, and tools for enabling conformance testing

In summary, **Conformance** testing will be performed as part of cloud infrastructure and workload lifecycle testing which includes **Verification** and **Validation**, defined further as:

- **Verification** is performed using reviews (e.g., manifests) to ensure that the cloud infrastructure or workload is delivered as per implementation specifications.
- **Validation** confirms the infrastructure or workload meet the expected or desired behaviour by means of automated testing.

**All Terms utilized throughout this chapter are intended to align with LFN Complinace and Verification Committee (CVC) definitions, and their use through CVC documentation, guidelines, and standards.**

## Introduction

**Document Purpose**

This chapter includes tracability from requirements to test cases and a test case execution framework to ensure Kubernetes infrastructure meets the design, feature, and capability expectations of the Reference Model (RM) and RA2. Ultimately, RC2 will reduce the amount of time and cost it takes each operator to on-board and maintain cloud infrastructure and CNFs.

## RC2 End User Requirements

Telcom service providers / operators are the primary intended audience for RC2 results. Specifically those selecting infrastructure and network function technologies to use in their network. The RC2 result artefact(s) should be clear and provide confidence to the service provider that the test results meet the requirements *they have.*

Vendors/Developers are a secondary audience. They should be able to clearly see the mapping from a specific test result (pass or fail) to the requirement.

### Operator/SP Test Result Requirements
* Clickable links from test cases to requirements
* Pass, Fail, or Skipped for every test
* Reason for failures
* Reason for skipping
* Format supporting clickable links (eg. HTML)
* Provide a stable set of point-in-time requirements and tests to achieve conformance
* Testing tools allow users to select between validation of mandatory and optional requirements
* Enable clear tracability with versioning to know which requirements have and haven’t been covered and track changes over time
* Tests must be available to run locally
* Testing tools must produce machine-readable result formats

### Vendor Test Result Requirements
* Clear mapping between requirements and test results
* Enable clear tracability to know which requirements have and haven’t been covered and track changes over time
* Failures should provide additional content to inform the user where or how the requirement was violated without having to read the test
* Expected preconditions and environment requirements for any test tooling must be defined

## Scope

This document covers aspects of conformance for both Kubernetes based cloud infrastructure and workloads. The document will cover the following topics:

- Identify in detail the requirements of test-cases (mapped from RA2 and RM)
- Test criteria that shows a certain capability or feature of the system-under-test exists and behaves as expected
- An E2E framework for conformance of Kubernetes infrastructures and workloads, including specification for conformance test infrastructure (lab environment and tools)
- Analysis to identify where the gaps are in the industry for implementing conformance test objectives (tooling, methods, process, etc)

**Not in Scope**
- Functional testing / validation of the application provided by the workload is outside the scope of this work
- Testing to confirm anything not in RM or RA2 requirements
- VNFM/NFVO, like ONAP, is not used in the process flow for infrastructure verifications or validations
- Upgrades to workloads, and the respective processes of verifying upgrade procedures and validating (testing) the success and compatibility of upgrades is not in scope

## Guidelines

The objectives of the Reference Conformance for cloud infrastrucute is to verify implementations against the reference architecture which satisfies infrastructure needs for workloads. The objectives of the Reference Conformance for workloads is to verify workload implementations consume resources and behave as expected against the reference architecture.

These guidlines will drive RC2 deliverables:

- RC2 requirements are completely derived from RM and RA2 which specify infrastructure capabilities including compute, memory, storage, resource capabilities, performance optimization capabilities, and monitoring capabilities.

- Requirements in the RM and RAs that are performance related may not have minimum perfromance criteria identified but where feasible will have tests with metrics to show relevant capabilities are present and working as expected.

- Must/shall conformance criteria are testable as pass/fail and/or reporting of quantitative test results. This will ensure infrastructures and workloads meet minimum thresholds of functional operability and/or performance behavior. This is the focus of RC2 since it is what will drive a commercially significant badging program.

- Should/may conformance criteria, which may or may not be testable, provide recommendations or best-practices for functional operability and/or performance behavior. These criteria and associated tests can be very useful for developing, evaluating or deploying a cloud infrastructure but are not critical to a commercially significant badging program.

## Conformance Methodologies

The RC2 test suite will provide validation to ensure workloads can interoperate with the RA2 conformant infrastructure. Upstream projects will define features/capabilities, test scenarios, and test cases to be executed. 3rd Party test platforms may also be leveraged if desired.

**Dependencies** infrastructure and workload validation will rely upon test harnesses, test tools, and test suites provided by upstream projects, including OPNFV and CNF conformance. These upstream projects will be reviewed semi-annually to verify they are still healthy and active projects. Over time, the projects representing the conformance process may change, but test parity is required if new test suites are added in place of older, stale projects.

## Reading Guide and Usage

RC2 focuses on testing of Kubernetes based cloud infrastructure thus the chapter structure is designed to facilitate this by matching test cases to requirements and building test cookbooks. If you are looking for requirements or the reasons behind them, please refer to the RA2. Chapters 2 and 3 cover Kubernetes infrastructure conformance while 4 and 5 cover CNF conformance.

Chapter 2 takes the requirements from the RA2 and matches them to upstream test cases. This will cover how specific test cases map to requirements and the overall coverage of requirements with test cases. Chatper 3 outlines how these test cases can be integrated together into an automated toolchain to test conformance of the Kubernetes infrastructure.

Similarly, Chapter 4 maps test cases map to requirements for CNFs and Chapter 5 builds a testing cookbook. Chapter 6 encompasses any gaps in the Reference Conformance 2.
