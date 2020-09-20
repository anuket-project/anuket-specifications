[<< Back](../)

# 2. Kubernetes Test Cases and Requirements Traceability
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

### Kubernetes API testing

The primary objectives of the
[e2e tests](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/e2e-tests.md)
are to ensure a consistent and reliable behavior of the Kubernetes code base,
and to catch hard-to-test bugs before users do, when unit and integration tests
are insufficient. They are partially selected for the
[Software Conformance Certification program](https://github.com/cncf/k8s-conformance)
run by the Kubernetes community (under the aegis of the CNCF).

CNTT shares the same goal to give end users the confidence that when they use
a certified product they can rely on a high level of common functionality.
Then CNTT RC2 starts with
[the test case list](https://git.opnfv.org/functest-kubernetes/tree/docker/smoke/testcases.yaml?h=stable/kali#n23)
defined by [K8s Conformance](https://github.com/cncf/k8s-conformance) which is
expected to grow according to the ongoing requirement traceability:
- focus: \[Conformance\]
- skip: \[Disruptive\]|NoExecuteTaintManager

[Rally](https://github.com/openstack/rally) and is tool and framework that
allows to perform Kubernetes API testing by iterating once the mainline
[xrally-kubernetes](https://github.com/xrally/xrally-kubernetes) scenarios:

[Functest xrally_kubernetes](http://artifacts.opnfv.org/functest-kubernetes/HTJLR3AVHUN6/functest-kubernetes-opnfv-functest-kubernetes-smoke-kali-xrally_kubernetes-run-153/xrally_kubernetes/xrally_kubernetes.html):

| Scenarios                                                          |
|--------------------------------------------------------------------|
| Kubernetes.create_and_delete_deployment                            |
| Kubernetes.create_and_delete_job                                   |
| Kubernetes.create_and_delete_namespace                             |
| Kubernetes.create_and_delete_pod                                   |
| Kubernetes.create_and_delete_pod_with_configmap_volume             |
| Kubernetes.create_and_delete_pod_with_configmap_volume [2]         |
| Kubernetes.create_and_delete_pod_with_emptydir_volume              |
| Kubernetes.create_and_delete_pod_with_emptydir_volume [2]          |
| Kubernetes.create_and_delete_pod_with_hostpath_volume              |
| Kubernetes.create_and_delete_pod_with_secret_volume                |
| Kubernetes.create_and_delete_pod_with_secret_volume [2]            |
| Kubernetes.create_and_delete_replicaset                            |
| Kubernetes.create_and_delete_replication_controller                |
| Kubernetes.create_and_delete_statefulset                           |
| Kubernetes.create_check_and_delete_pod_with_cluster_ip_service     |
| Kubernetes.create_check_and_delete_pod_with_cluster_ip_service [2] |
| Kubernetes.create_check_and_delete_pod_with_node_port_service      |
| Kubernetes.create_rollout_and_delete_deployment                    |
| Kubernetes.create_scale_and_delete_replicaset                      |
| Kubernetes.create_scale_and_delete_replication_controller          |
| Kubernetes.create_scale_and_delete_statefulset                     |
| Kubernetes.list_namespaces                                         |

The following software versions are considered to verify Kubernetes v1.19
(latest stable release) selected by CNTT:

| software                | version     |
|-------------------------|-------------|
| Functest                | kali        |
| Kubernetes              | v1.19       |
| xrally-kubernetes       | 1.1.1.dev12 |

### Kubernetes API benchmarking

[Rally](https://github.com/openstack/rally) is a tool and framework that
performs Kubernetes API benchmarking.

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

The following software versions are considered to benchmark Kubernetes v1.19
(latest stable release) selected by CNTT:

| software                | version     |
|-------------------------|-------------|
| Functest                | kali        |
| xrally-kubernetes       | 1.1.1.dev12 |

### Security testing

There are a couple of opensource tools that help securing the Kubernetes stack.
Amongst them,
[Functest Kubernetes Security](https://git.opnfv.org/functest-kubernetes/tree/docker/security/testcases.yaml?h=stable%2Fkali)
offers two test cases based on
[kube-hunter](https://github.com/aquasecurity/kube-hunter) and
[kube-bench](https://github.com/aquasecurity/kube-bench).

[kube-hunter](https://github.com/aquasecurity/kube-hunter) hunts for security
weaknesses in Kubernetes clusters and
[kube-bench](https://github.com/aquasecurity/kube-bench) checks
whether Kubernetes is deployed securely by running the checks documented in the
[CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/).

[kube-hunter](https://github.com/aquasecurity/kube-hunter) classifies all
vulnerabilities as low, medium, and high. In context of this conformance suite,
only the high vulnerabilities lead to a test case failure. Then all low and
medium vulnerabilities are only printed for information.

Here are the
[vulnerability categories](https://github.com/aquasecurity/kube-hunter/blob/v0.3.1/kube_hunter/core/events/types.py)
tagged as high by
[kube-hunter](https://github.com/aquasecurity/kube-hunter):
- RemoteCodeExec
- IdentityTheft
- PrivilegeEscalation

At the time of writing, none of the  Center for Internet Security (CIS) rules
are defined as mandatory (e.g. sec.std.001: The Cloud Operator **should**
comply with Center for Internet Security CIS Controls) else it would have
required an update of the default kube-bench behavior (all failures and
warnings are only printed) as integrated in
[Functest Kubernetes Security](https://git.opnfv.org/functest-kubernetes/tree/docker/security/testcases.yaml?h=stable%2Fkali).

The following software versions are considered to verify Kubernetes v1.19
(latest stable release) selected by CNTT:

| software                | version     |
|-------------------------|-------------|
| Functest                | kali        |
| kube-hunter             | 0.3.1       |
| kube-bench              | 0.3.1       |

### Opensource CNF onboarding and testing

Running opensource containerized network functions (CNF) is a key technical
solution to ensure that the platforms meet Network Functions Virtualization
requirements.

Functest CNF offers 2 test cases which automatically onboard and test
[Clearwater IMS](https://github.com/Metaswitch/clearwater-docker)
via kubecltl and Helm. It's worth mentioning that this CNF is covered by the
upstream tests (see
[clearwater-live-test](https://github.com/Metaswitch/clearwater-live-test)).

The following software versions are considered to verify Kubernetes v1.19
(latest stable release) selected by CNTT:

| software                | version     |
|-------------------------|-------------|
| Functest                | kali        |
| clearwater              | release-130 |
| Helm                    | v3.3.1      |

## Test Cases Traceability to Requirements

The following test case must pass as they are for Reference Conformance:

| container                                   | test case              | criteria | requirements                          |
|---------------------------------------------|------------------------|:--------:|---------------------------------------|
| opnfv/functest-kubernetes-smoke:kali        | k8s_conformance        | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-smoke:kali        | xrally_kubernetes      | PASS     | Kubernetes API testing                |
| opnfv/functest-kubernetes-security:kali     | kube_hunter            | PASS     | Security testing                      |
| opnfv/functest-kubernetes-security:kali     | kube_bench_master      | PASS     | Security testing                      |
| opnfv/functest-kubernetes-security:kali     | kube_bench_node        | PASS     | Security testing                      |
| opnfv/functest-kubernetes-benchmarking:kali | xrally_kubernetes_full | PASS     | Kubernetes API benchmarking           |
| opnfv/functest-kubernetes-cnf:kali          | k8s_vims               | PASS     | Opensource CNF onboarding and testing |
| opnfv/functest-kubernetes-cnf:kali          | helm_vims              | PASS     | Opensource CNF onboarding and testing |
