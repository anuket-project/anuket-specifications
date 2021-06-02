[<< Back](../../kubernetes)

# 6. Special Interest Group level requirements
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 API Machinery Special Interest Group](#6.2)
* [6.3 Apps Special Interest Group](#6.3)
* [6.4 Auth Special Interest Group](#6.4)
* [6.5 CLI Special Interest Group](#6.5)
* [6.6 Cluster Lifecycle Special Interest Group](#6.6)
* [6.7 Instrumentation Special Interest Group](#6.7)
* [6.8 Network Special Interest Group](#6.8)
* [6.9 Node Special Interest Group](#6.9)
* [6.10 Scheduling Special Interest Group](#6.10)

<a name="6.1"></a>
## 6.1 Introduction

Kubernetes has defined
[Testing Special Interest Groups](https://github.com/kubernetes/community/blob/master/sig-testing/charter.md)
to make it easier for the community to write and run tests, and to contribute,
analyze and act upon test results. This chapter basically converts all the
requirements written in the previous chapters as mandatory Special Interest
Group Features. It enforces the overall requirements traceability to testing,
especially those offered for
[End-to-End Testing](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/e2e-tests.md)
The reference conformance, for its part, lists all regexes matching the
following Features tabs defined here.

<a name="6.2"></a>
## 6.2 [API Machinery Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-api-machinery)

| **Labels**                             | **Mandatory** |
|----------------------------------------|:-------------:|
| Conformance                            | X             |
| None                                   | X             |
| Feature:ComprehensiveNamespaceDraining | X             |
| Feature:CrossNamespacePodAffinity      |               |
| Feature:PodPriority                    | X             |
| Feature:ScopeSelectors                 | X             |
| Feature:StorageVersionAPI              |               |

<a name="6.3"></a>
## 6.3 [Apps Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-apps)

| **Labels**                   | **Mandatory** |
|------------------------------|:-------------:|
| Conformance                  | X             |
| None                         | X             |
| Feature:DaemonSetUpdateSurge |               |
| Feature:IndexedJob           |               |
| Feature:StatefulSet          |               |
| Feature:StatefulUpgrade      |               |
| Feature:SuspendJob           |               |
| Feature:TaintEviction        |               |
| Feature:TTLAfterFinished     | X             |

<a name="6.4"></a>
## 6.4 [Auth Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-auth)

| **Labels**                             | **Mandatory** |
|----------------------------------------|:-------------:|
| Conformance                            | X             |
| None                                   | X             |
| Feature:BoundServiceAccountTokenVolume |               |
| Feature:NodeAuthenticator              | X             |
| Feature:NodeAuthorizer                 | X             |
| Feature:PodSecurityPolicy              |               |
| NodeFeature:FSGroup                    | X             |

<a name="6.5"></a>
## 6.5 [CLI Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-cli)

| **Labels**  | **Mandatory** |
|-------------|:-------------:|
| Conformance | X             |
| None        | X             |

<a name="6.6"></a>
## 6.6 [Cluster Lifecycle Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-cluster-lifecycle)

| **Labels**              | **Mandatory** |
|-------------------------|:-------------:|
| Conformance             | X             |
| None                    | X             |
| Feature:BootstrapTokens | X             |

<a name="6.7"></a>
## 6.7 [Instrumentation Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-instrumentation)

| **Labels**                               | **Mandatory** |
|------------------------------------------|:-------------:|
| Conformance                              | X             |
| None                                     | X             |
| Feature:Elasticsearch                    |               |
| Feature:StackdriverAcceleratorMonitoring |               |
| Feature:StackdriverCustomMetrics         |               |
| Feature:StackdriverExternalMetrics       |               |
| Feature:StackdriverMetadataAgent         |               |
| Feature:StackdriverMonitoring            |               |

<a name="6.8"></a>
## 6.8 [Network Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-network)

| **Labels**                          | **Mandatory** |
|-------------------------------------|:-------------:|
| Conformance                         | X             |
| None                                | X             |
| Feature:Example                     |               |
| Feature:Ingress                     |               |
| Feature:IPv6DualStack               |               |
| Feature:kubemci                     |               |
| Feature:KubeProxyDaemonSetMigration |               |
| Feature:KubeProxyDaemonSetUpgrade   |               |
| Feature:NEG                         |               |
| Feature:NoSNAT                      | X             |
| Feature:Networking-IPv4             | X             |
| Feature:Networking-IPv6             |               |
| Feature:Networking-Performance      | X             |
| Feature:NetworkPolicy               |               |
| Feature:PerformanceDNS              | X             |
| Feature:SCTP                        |               |
| Feature:SCTPConnectivity            |               |

<a name="6.9"></a>
## 6.9 [Node Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-node)

| **Labels**                                | **Mandatory** |
|-------------------------------------------|:-------------:|
| Conformance                               | X             |
| None                                      | X             |
| Feature:Example                           | X             |
| Feature:ExperimentalResourceUsageTracking |               |
| Feature:GPUUpgrade                        |               |
| Feature:PodGarbageCollector               |               |
| Feature:RegularResourceUsageTracking      |               |
| Feature:ProbeTerminationGracePeriod       | X             |
| NodeFeature:DownwardAPIHugePages          |               |
| NodeFeature:PodReadinessGate              | X             |
| NodeFeature:RuntimeHandler                |               |
| NodeFeature:Sysctls                       | X             |


<a name="6.10"></a>
## 6.10 [Scheduling Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-scheduling)

| **Labels**                            | **Mandatory** |
|---------------------------------------|:-------------:|
| Conformance                           | X             |
| None                                  | X             |
| Feature:GPUDevicePlugin               |               |
| Feature:LocalStorageCapacityIsolation | X             |
| Feature:Recreate                      |               |
