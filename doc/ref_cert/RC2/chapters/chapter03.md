[<< Back](../)

# 3. Kubernetes Test Cases and Traceability to CNTT Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Introduction

All of the requirements for RC2 have been defined in the Reference Model (RM) and Reference Architecture (RA2). The scope of this chapter is to identify and list down test cases based on these requirements. Users of this chapter will be able to use it to determine which test cases they must run in order to test compliance with the requirements. This will enable traceability between the test cases and requirements. They should be able to clearly see which requirements are covered by which tests and the mapping from a specific test result (pass or fail) to a requirement. Each requirement may have one or more test case associated with it.

### Goals
- Clear mapping between requirements and test cases
- Provide a stable set of point-in-time requirements and tests to achieve conformance
- Enable clear traceability of the coverage of requirements across consecutive releases of this document
- Clickable links from test cases to requirements
- One or more tests for every MUST requirement
- A set of test cases to serve as a template for Cloud Native OVP

### Non-Goals
- Defining any requirements
- Providing coverage for non-testable requirements

### Definitions
*must*: Test Cases that are marked as must are considered mandatory and must pass successfully

*should*: Test Cases that are marked as should are expected to be fulfilled by the cloud infrastructure but it is up to each service provider whether to accept a cloud infrastructure that is not fulfilling any of these requirements. The same applies to should not.

*may*: Test cases that are marked as may are considered optional. The same applies to may not.

## Traceability Matrix

### Kubernetes API benchmarking

[Rally](https://github.com/openstack/rally) and is tool and framework that
allows to perform Kubernetes API benchmarking.

[Functest Kubernetes Benchmarking](https://git.opnfv.org/functest-kubernetes/tree/docker/benchmarking/testcases.yaml?h=stable%2Fkali)
proposed a Rally-based test case,
[xrally_kubernetes_full](http://artifacts.opnfv.org/functest-kubernetes/LCY61RV15EX7/functest-kubernetes-opnfv-functest-kubernetes-benchmarking-kali-xrally_kubernetes_full-run-4/xrally_kubernetes_full/xrally_kubernetes_full.html),
which iterates 10 times the mainline
[xrally-kubernetes](https://github.com/xrally/xrally-kubernetes) scenarios.

At the time of writing, no KPI is defined in
[Kubernetes based Reference Architecture](../../../ref_arch/kubernetes/chapters/chapter02.md)
which would have asked for an update of the default SLA (maximum failure rate
of 0%) proposed in
[Functest Kubernetes Benchmarking](https://git.opnfv.org/functest-kubernetes/tree/docker/benchmarking/testcases.yaml?h=stable%2Fkali)

[Functest xrally_kubernetes_full](http://artifacts.opnfv.org/functest-kubernetes/LCY61RV15EX7/functest-kubernetes-opnfv-functest-kubernetes-benchmarking-kali-xrally_kubernetes_full-run-4/xrally_kubernetes_full/xrally_kubernetes_full.html):

| Scenarios                                                          | Iterations |
|--------------------------------------------------------------------|:----------:|
| Kubernetes.create_and_delete_deployment                            | 10         |
| Kubernetes.create_and_delete_job                                   | 10         |
| Kubernetes.create_and_delete_namespace                             | 10         |
| Kubernetes.create_and_delete_pod                                   | 10         |
| Kubernetes.create_and_delete_pod_with_configmap_volume             | 10         |
| Kubernetes.create_and_delete_pod_with_configmap_volume [2]         | 10         |
| Kubernetes.create_and_delete_pod_with_emptydir_volume              | 10         |
| Kubernetes.create_and_delete_pod_with_emptydir_volume [2]          | 10         |
| Kubernetes.create_and_delete_pod_with_hostpath_volume              | 10         |
| Kubernetes.create_and_delete_pod_with_secret_volume                | 10         |
| Kubernetes.create_and_delete_pod_with_secret_volume [2]            | 10         |
| Kubernetes.create_and_delete_replicaset                            | 10         |
| Kubernetes.create_and_delete_replication_controller                | 10         |
| Kubernetes.create_and_delete_statefulset                           | 10         |
| Kubernetes.create_check_and_delete_pod_with_cluster_ip_service     | 10         |
| Kubernetes.create_check_and_delete_pod_with_cluster_ip_service [2] | 10         |
| Kubernetes.create_check_and_delete_pod_with_node_port_service      | 10         |
| Kubernetes.create_rollout_and_delete_deployment                    | 10         |
| Kubernetes.create_scale_and_delete_replicaset                      | 10         |
| Kubernetes.create_scale_and_delete_replication_controller          | 10         |
| Kubernetes.create_scale_and_delete_statefulset                     | 10         |
| Kubernetes.list_namespaces                                         | 10         |

The following software versions are considered to verify Kubernetes v1.18
(latest stable release) selected by CNTT:

| software                | version     |
|-------------------------|-------------|
| Functest                | kali        |
| xrally-kubernetes       | 1.1.1.dev12 |

## Test Cases Traceability to Requirements

The following test case must pass as they are for Reference Conformance:

| container                                   | test case              | criteria | requirements                |
|---------------------------------------------|------------------------|:--------:|-----------------------------|
| opnfv/functest-kubernetes-benchmarking:kali | xrally_kubernetes_full | PASS     | Kubernetes API benchmarking |
