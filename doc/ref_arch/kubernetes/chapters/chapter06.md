[<< Back](../../kubernetes)

# 6. API and Feature Testing requirements

<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents <!-- omit in toc -->

- [6. API and Feature Testing requirements](#6-api-and-feature-testing-requirements)
  - [6.1 Introduction](#61-introduction)
    - [6.1.1 Kubernetes feature gate policy](#611-kubernetes-feature-gate-policy)
    - [6.1.2 Kubernetes API policy](#612-kubernetes-api-policy)
  - [6.2 API Machinery Special Interest Group](#62-api-machinery-special-interest-group)
  - [6.3 Apps Special Interest Group](#63-apps-special-interest-group)
  - [6.4 Auth Special Interest Group](#64-auth-special-interest-group)
  - [6.5 Cluster Lifecycle Special Interest Group](#65-cluster-lifecycle-special-interest-group)
  - [6.6 Instrumentation Special Interest Group](#66-instrumentation-special-interest-group)
  - [6.7 Network Special Interest Group](#67-network-special-interest-group)
  - [6.8 Node Special Interest Group](#68-node-special-interest-group)
  - [6.9 Scheduling Special Interest Group](#69-scheduling-special-interest-group)
  - [6.10 Storage Special Interest Group](#610-storage-special-interest-group)

## 6.1 Introduction

The CNCF has defined a
[Testing Special Interest Group](https://github.com/kubernetes/community/blob/master/sig-testing/charter.md) to make it easier for the community to write and run tests, and to contribute, analyse and act upon test results.
This chapter maps the requirements written in the previous chapters as mandatory Special Interest Group Features. It enforces the overall requirements traceability to testing, especially those offered for [End-to-End Testing](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/e2e-tests.md).
The Anuket Reference Conformance (RC2) testing then matches the following Features tabs defined here.

### 6.1.1 Kubernetes feature gate policy

[Feature gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) are a set of key-value pairs that describe Kubernetes features. The components of the control plane of Kubernetes Clusters can be run with different Feature Gate settings.

A feature can be in Alpha, Beta or GA stage:

- Alpha features are disabled by default, may be buggy, and support may be dropped
- Beta features are enabled by default, are well tested, and support will not be dropped (although breaking API changes may happen)
- GA features are stable, always enabled and cannot be disabled.

The policy for RA2 to include Kubernetes features as mandatory is:

> Only features that are either in Beta or GA stage can be made mandatory, subject to RA2 requirements.

A list of feature gates is available [here](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-gates).

### 6.1.2 Kubernetes API policy

The [Kubernetes API](https://kubernetes.io/docs/reference/using-api/) supports all operations and communications between components, and external user commands.
Everything in the Kubernetes platform is treated as an API object.
Different API versions indicate different levels of stability and support. An API can have Alpha, Beta or Stable versions. The version of APIs that are backed by a feature will match the stage of the feature itself (i.e. Alpha, Beta or GA/Stable).

The policy for RA2 to include Kubernetes APIs as mandatory is:

> Only APIs that are either in Beta or Stable stage can be made mandatory, subject to RA2 requirements.

The Kubernetes API reference is available [here](https://kubernetes.io/docs/reference/kubernetes-api/).

The list of [API groups](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#-strong-api-groups-strong-) that are mandatory is:

| Group                        | Version              |
|------------------------------|----------------------|
| admissionregistration.k8s.io | v1                   |
| apiextensions.k8s.io         | v1                   |
| apiregistration.k8s.io       | v1                   |
| apps                         | v1                   |
| authentication.k8s.io        | v1                   |
| authorization.k8s.io         | v1                   |
| autoscaling                  | v1, v2beta2, v2beta1 |
| batch                        | v1                   |
| certificates.k8s.io          | v1                   |
| coordination.k8s.io          | v1                   |
| core                         | v1                   |
| discovery.k8s.io             | v1                   |
| events.k8s.io                | v1                   |
| flowcontrol.apiserver.k8s.io | v1beta1              |
| networking.k8s.io            | v1                   |
| node.k8s.io                  | v1                   |
| policy                       | v1                   |
| rbac.authorization.k8s.io    | v1                   |
| scheduling.k8s.io            | v1                   |
| storage.k8s.io               | v1                   |

## 6.2 [API Machinery Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-api-machinery)

| **Labels**                             | **Mandatory** | **Description** |
|----------------------------------------|:-------------:|:----------------|
| Conformance                            | X             | Kubernetes conformance test |
| None                                   | X             | Kubernetes mainstream features |
| Feature:ComprehensiveNamespaceDraining | X             | Namespaces should always delete fast (ALL of 100 namespaces in 150 seconds) |
| Feature:[CrossNamespacePodAffinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#namespace-selector)|               | Should verify ResourceQuota with cross namespace pod affinity scope using scope-selectors |
| Feature:[PodPriority](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/)| X             | Verify ResourceQuota's priority class scope against a pod with different priority class |
| Feature:ScopeSelectors                 | X             | Verify ResourceQuota with terminating scopes through scope selectors |
| Feature:[StorageVersionAPI](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.21/#storageversion-v1alpha1-internal-apiserver-k8s-io)|               |

## 6.3 [Apps Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-apps)

| **Labels**                   | **Mandatory** | **Description** |
|------------------------------|:-------------:|:----------------|
| Conformance                  | X             | Kubernetes conformance test |
| None                         | X             | Kubernetes mainstream features |
| Feature:[DaemonSetUpdateSurge](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.21/#rollingupdatedaemonset-v1-apps) |               | Daemon set should surge pods onto nodes when spec was updated and update strategy is RollingUpdate |
| Feature:[IndexedJob](https://kubernetes.io/docs/concepts/workloads/controllers/job/)          |               | Should create pods for an Indexed job with completion indexes |
| Feature:[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)          |               | Should creating a working zookeeper cluster |
| Feature:StatefulUpgrade      |               | Stateful upgrade should maintain a functioning cluster |
| Feature:[SuspendJob](https://kubernetes.io/docs/concepts/workloads/controllers/job/)|               | Should not create pods when created in suspend state |
| Feature:[TaintEviction](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#taint-based-evictions)|               | All pods on the unreachable node should be marked as NotReady upon the node turn NotReady AND all pods should be evicted after eviction timeout passes |
| Feature:[TTLAfterFinished](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/)| X             | Job should be deleted once it finishes after TTL seconds |

## 6.4 [Auth Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-auth)

| **Labels**                             | **Mandatory** | **Description** |
|----------------------------------------|:-------------:|:----------------|
| Conformance                            | X             | Kubernetes conformance test |
| None                                   | X             | Kubernetes mainstream features |
| Feature:[BoundServiceAccountTokenVolume](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md)|               | ServiceAccount admission controller migration master upgrade should maintain a functioning cluster |
| Feature:NodeAuthenticator              | X             | The kubelet's main port 10250 should reject requests with no credentials |
| Feature:NodeAuthorizer                 | X             | Setting existing and non-existent attributes should exit with the Forbidden error, not a NotFound error |
| Feature:PodSecurityPolicy              |               | Should enforce the restricted policy.PodSecurityPolicy |
| NodeFeature:FSGroup                    | X             | ServiceAccounts should set ownership and permission when RunAsUser or FsGroup is present |

## 6.5 [Cluster Lifecycle Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-cluster-lifecycle)

| **Labels**              | **Mandatory** | **Description** |
|-------------------------|:-------------:|:----------------|
| Conformance             | X             | Kubernetes conformance test |
| None                    | X             | Kubernetes mainstream features |
| Feature:BootstrapTokens | X             | Should delete the token secret when the secret expired |

## 6.6 [Instrumentation Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-instrumentation)

| **Labels**                               | **Mandatory** | **Description** |
|------------------------------------------|:-------------:|:----------------|
| Conformance                              | X             | Kubernetes conformance test |
| None                                     | X             | Kubernetes mainstream features |
| Feature:Elasticsearch                    |               | Should check that the Kibana logging instance is alive |
| Feature:StackdriverAcceleratorMonitoring |               | Stackdriver Monitoring should have accelerator metrics |
| Feature:StackdriverCustomMetrics         |               | Stackdriver Monitoring should run Custom Metrics - Stackdriver Adapter for new resource model |
| Feature:StackdriverExternalMetrics       |               | Stackdriver Monitoring should run Custom Metrics - Stackdriver Adapter for external metrics |
| Feature:StackdriverMetadataAgent         |               | Stackdriver Monitoring should run Stackdriver Metadata Agent |
| Feature:StackdriverMonitoring            |               | |

## 6.7 [Network Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-network)

| **Labels**                          | **Mandatory** | **Description** |
|-------------------------------------|:-------------:|:----------------|
| Conformance                         | X             | Kubernetes conformance test |
| None                                | X             | Kubernetes mainstream features |
| Feature:Example                     |               | Should create pod that uses DNS |
| Feature:Ingress                     |               | Should prevent Ingress creation if more than 1 IngressClass marked as default |
| Feature:[IPv6DualStack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/)|               | IPv4/IPv6 dual-stack networking enables the allocation of both IPv4 and IPv6 addresses to Pods and Services. IPv4/IPv6 dual-stack networking is enabled by default for your Kubernetes cluster starting in 1.21, allowing the simultaneous assignment of both IPv4 and IPv6 addresses. |
| Feature:kubemci                     |               | Should create ingress with pre-shared certificate |
| Feature:KubeProxyDaemonSetMigration |               | Upgrade kube-proxy from static pods to a DaemonSet should maintain a functioning cluster |
| Feature:KubeProxyDaemonSetUpgrade   |               | Upgrade kube-proxy from static pods to a DaemonSet should maintain a functioning cluster |
| Feature:NEG                         |               | Should sync endpoints to NEG |
| Feature:NoSNAT                      | X             | Should be able to send traffic between Pods without SNAT |
| Feature:Networking-IPv4             | X             | Networking should provide Internet connection for containers |
| Feature:Networking-IPv6             |               | Networking should provide Internet connection for containers |
| Feature:Networking-Performance      | X             | run iperf2 |
| Feature:NetworkPolicy               |               | NetworkPolicy between server and client should enforce policy to allow traffic only from a different namespace, based on NamespaceSelector |
| Feature:PerformanceDNS              |               | Should answer DNS query for maximum number of services per cluster |
| Feature:SCTP                        |               | should allow creating a basic SCTP service with pod and endpoints |
| Feature:SCTPConnectivity            |               | Pods should function for intra-pod communication: sctp |

## 6.8 [Node Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-node)

| **Labels**                                | **Mandatory** | **Description** |
|-------------------------------------------|:-------------:|:----------------|
| Conformance                               | X             | Kubernetes conformance test |
| None                                      | X             | Kubernetes mainstream features |
| Feature:Example                           | X             | Liveness pods should be automatically restarted |
| Feature:ExperimentalResourceUsageTracking |               | Resource tracking for 100 pods per node |
| Feature:GPUUpgrade                        |               | Master upgrade should NOT disrupt GPU Pod |
| Feature:PodGarbageCollector               |               | Should handle the creation of 1000 pods |
| Feature:RegularResourceUsageTracking      |               | Resource tracking for 0 pods per node |
| Feature:[ProbeTerminationGracePeriod](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#probe-level-terminationgraceperiodseconds)| X             | Probing container should override timeoutGracePeriodSeconds when LivenessProbe field is set |
| NodeFeature:[DownwardAPIHugePages](https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information)|               | Downward API tests for huge pages should provide container's limits.hugepages-pagesize; and requests.hugepages-pagesize& as env vars |
| NodeFeature:[PodReadinessGate](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-readiness-gate)| X             | Pods should support pod readiness gates |
| NodeFeature:RuntimeHandler                |               | RuntimeClass should run a Pod requesting a RuntimeClass with a configured handler |
| NodeFeature:[Sysctls](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/)| X             | Should not launch unsafe, but not explicitly enabled sysctls on the node |

## 6.9 [Scheduling Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-scheduling)

| **Labels**                            | **Mandatory** | **Description** |
|---------------------------------------|:-------------:|:----------------|
| Conformance                           | X             | Kubernetes conformance test |
| None                                  | X             | Kubernetes mainstream features |
| Feature:GPUDevicePlugin               |               | Run Nvidia GPU Device Plugin tests |
| Feature:[LocalStorageCapacityIsolation](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) | X             | Validates local ephemeral storage resource limits of pods that are allowed to run |
| Feature:Recreate                      |               | Run Nvidia GPU Device Plugin tests with a recreation |

## 6.10 [Storage Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-storage)

| **Labels**                            | **Mandatory** | **Description**                |
|---------------------------------------|:-------------:|:-------------------------------|
| Conformance                           | X             | Kubernetes conformance test    |
| None                                  | X             | Kubernetes mainstream features |
| Feature:ExpandInUsePersistentVolumes  |               |                                |
| Feature:Flexvolumes                   |               |                                |
| Feature:GKELocalSSD                   |               |                                |
| Feature:VolumeSnapshotDataSource      |               |                                |
| Feature:Volumes                       | X             |                                |
| Feature:vsphere                       |               |                                |
| Feature:Windows                       |               |                                |
| NodeFeature:EphemeralStorage          | X             |                                |
| NodeFeature:FSGroup                   | X             |                                |
