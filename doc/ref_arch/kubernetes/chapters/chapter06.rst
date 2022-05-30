API and Feature Testing requirements
====================================

Introduction
------------

The CNCF has defined a
`Testing Special Interest Group <https://github.com/kubernetes/community/blob/master/sig-testing/charter.md>`__ to make
it easier for the community to write and run tests, and to contribute, analyse and act upon test results.
This chapter maps the requirements written in the previous chapters as mandatory Special Interest Group Features. It
enforces the overall requirements traceability to testing, especially those offered for
`End-to-End Testing <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-testing/
e2e-tests.md>`__.
The Anuket Reference Conformance (RC2) testing then matches the following Features tabs defined here.

Kubernetes feature gate policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Feature gates <https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/>`__ are a set of
key-value pairs that describe Kubernetes features. The components of the control plane of Kubernetes Clusters can be
run with different Feature Gate settings.

A feature can be in Alpha, Beta or GA stage:

- Alpha features are disabled by default, may be buggy, and support may be dropped
- Beta features are enabled by default, are well tested, and support will not be dropped (although breaking API
  changes may happen)
- GA features are stable, always enabled and cannot be disabled.

The policy for RA2 to include Kubernetes features as mandatory is:

   Only features that are either in Beta or GA stage can be made mandatory, subject to RA2 requirements.

A list of feature gates is available
`here <https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-gates>`__.

Kubernetes API policy
~~~~~~~~~~~~~~~~~~~~~

The `Kubernetes API <https://kubernetes.io/docs/reference/using-api/>`__ supports all operations and communications
between components, and external user commands.
Everything in the Kubernetes platform is treated as an API object.
Different API versions indicate different levels of stability and support. An API can have Alpha, Beta or Stable
versions. The version of APIs that are backed by a feature will match the stage of the feature itself (i.e. Alpha, Beta
or GA/Stable).

The policy for RA2 to include Kubernetes APIs as mandatory is:

   Only APIs that are either in Beta or Stable stage can be made mandatory, subject to RA2 requirements.

The Kubernetes API reference is available `here <https://kubernetes.io/docs/reference/kubernetes-api/>`__.

The list of `API groups <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/
#-strong-api-groups-strong->`__ that are mandatory is:

============================ ========================
Group                        Version
============================ ========================
admissionregistration.k8s.io v1
apiextensions.k8s.io         v1
apiregistration.k8s.io       v1
apps                         v1
authentication.k8s.io        v1
authorization.k8s.io         v1
autoscaling                  v1, v2, v2beta2, v2beta1
batch                        v1, v1beta1
certificates.k8s.io          v1
coordination.k8s.io          v1
core                         v1
discovery.k8s.io             v1, v1beta1
events.k8s.io                v1, v1beta1
flowcontrol.apiserver.k8s.io v1beta2, v1beta1
internal.apiserver.k8s.io    v1alpha1
networking.k8s.io            v1
node.k8s.io                  v1, v1beta1, v1alpha1
policy                       v1, v1beta1
rbac.authorization.k8s.io    v1
scheduling.k8s.io            v1
storage.k8s.io               v1, v1beta1, v1alpha1
============================ ========================

`API Machinery Special Interest Group <https://github.com/kubernetes/community/tree/master/sig-api-machinery>`__
----------------------------------------------------------------------------------------------------------------

+----------------------------------------+-------------+--------------------------------------------------------------+
| **Labels**                             |**Mandatory**| **Description**                                              |
+========================================+=============+==============================================================+
| Conformance                            | X           | Kubernetes conformance test                                  |
+----------------------------------------+-------------+--------------------------------------------------------------+
| None                                   | X           | Kubernetes mainstream features                               |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:ComprehensiveNamespaceDraining | X           | Namespaces should always delete fast (ALL of 100 namespaces  |
|                                        |             | in 150 seconds)                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:`CrossNamespacePodAffinity <ht |             | Should verify ResourceQuota with cross namespace pod         |
| tps://kubernetes.io/docs/concepts/sche |             | affinity scope using scope-selectors                         |
| duling-eviction/assign-pod-node/#names |             |                                                              |
| pace-selector>`__                      |             |                                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:`PodPriority <https://kubernet | X           | Verify ResourceQuota's priority class scope against a pod    |
| es.io/docs/concepts/configuration/pod- |             | with different priority class                                |
| priority-preemption/>`__               |             |                                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:ScopeSelectors                 | X           | Verify ResourceQuota with terminating scopes through scope   |
|                                        |             | selectors                                                    |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:`StorageVersionAPI <https://ku |             |                                                              |
| bernetes.io/docs/reference/generated/k |             |                                                              |
| ubernetes-api/v1.23/#storageversion-v1 |             |                                                              |
| alpha1-internal-apiserver-k8s-io>`__   |             |                                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+

`Apps Special Interest Group <https://github.com/kubernetes/community/tree/master/sig-apps>`__
----------------------------------------------------------------------------------------------

+----------------------------------------+-------------+--------------------------------------------------------------+
| **Labels**                             |**Mandatory**| **Description**                                              |
+========================================+=============+==============================================================+
| Conformance                            | X           | Kubernetes conformance test                                  |
+----------------------------------------+-------------+--------------------------------------------------------------+
| None                                   | X           | Kubernetes mainstream features                               |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:`DaemonSetUpdateSurge <https:/ |             | Daemon set should surge pods onto nodes when spec was        |
| /kubernetes.io/docs/reference/generate |             | updated and update strategy is RollingUpdate                 |
| d/kubernetes-api/v1.23/#rollingupdated |             |                                                              |
| aemonset-v1-apps>`__                   |             |                                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:`IndexedJob <https://kubernete |             | Should create pods for an Indexed job with completion        |
| s.io/docs/concepts/workloads/controlle |             | indexes                                                      |
| rs/job/>`__                            |             |                                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:`StatefulSet <https://kubernet |             | Should creating a working zookeeper cluster                  |
| es.io/docs/concepts/workloads/controll |             |                                                              |
| ers/statefulset/>`__                   |             |                                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:StatefulUpgrade                |             | Stateful upgrade should maintain a functioning cluster       |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:`SuspendJob <https://kubernete |             | Should not create pods when created in suspend state         |
| s.io/docs/concepts/workloads/controlle |             |                                                              |
| rs/job/>`__                            |             |                                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:`TaintEviction <https://kubern |             | All pods on the unreachable node should be marked as         |
| etes.io/docs/concepts/scheduling-evict |             | NotReady upon the node turn NotReady AND all pods should be  |
| ion/taint-and-toleration/#taint-based- |             | evicted after eviction timeout passes                        |
| evictions>`__                          |             |                                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+
| Feature:`TTLAfterFinished <https://kub | X           | Job should be deleted once it finishes after TTL seconds     |
| ernetes.io/docs/concepts/workloads/con |             |                                                              |
| trollers/ttlafterfinished/>`__         |             |                                                              |
+----------------------------------------+-------------+--------------------------------------------------------------+

`Auth Special Interest Group <https://github.com/kubernetes/community/tree/master/sig-auth>`__
----------------------------------------------------------------------------------------------

+-----------------------------------------+-------------+-------------------------------------------------------------+
| **Labels**                              |**Mandatory**| **Description**                                             |
+=========================================+=============+=============================================================+
| Conformance                             | X           | Kubernetes conformance test                                 |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| None                                    | X           | Kubernetes mainstream features                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:`BoundServiceAccountTokenVolume |             | ServiceAccount admission controller migration master        |
| <https://github.com/kubernetes/enhancem |             | upgrade should maintain a functioning cluster               |
| ents/blob/master/keps/sig-auth/1205-bou |             |                                                             |
| nd-service-account-tokens/README.md>`__ |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:NodeAuthenticator               | X           | The kubelet's main port 10250 should reject requests with   |
|                                         |             | no credentials                                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:NodeAuthorizer                  | X           | Setting existing and non-existent attributes should exit    |
|                                         |             | with the Forbidden error, not a NotFound error              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:PodSecurityPolicy               |             | Should enforce the restricted policy.PodSecurityPolicy      |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| NodeFeature:FSGroup                     | X           | ServiceAccounts should set ownership and permission when    |
|                                         |             | RunAsUser or FsGroup is present                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+

`Cluster Lifecycle Special Interest Group <https://github.com/kubernetes/community/tree/master/sig-cluster-lifecycle>`__
------------------------------------------------------------------------------------------------------------------------

+-----------------------------------------+-------------+-------------------------------------------------------------+
| **Labels**                              |**Mandatory**| **Description**                                             |
+=========================================+=============+=============================================================+
| Conformance                             | X           | Kubernetes conformance test                                 |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| None                                    | X           | Kubernetes mainstream features                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:BootstrapTokens                 | X           | Should delete the token secret when the secret expired      |
+-----------------------------------------+-------------+-------------------------------------------------------------+

`Instrumentation Special Interest Group <https://github.com/kubernetes/community/tree/master/sig-instrumentation>`__
--------------------------------------------------------------------------------------------------------------------

+-----------------------------------------+-------------+-------------------------------------------------------------+
| **Labels**                              |**Mandatory**| **Description**                                             |
+=========================================+=============+=============================================================+
| Conformance                             | X           | Kubernetes conformance test                                 |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| None                                    | X           | Kubernetes mainstream features                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Elasticsearch                   |             | Should check that the Kibana logging instance is alive      |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:                                |             | Stackdriver Monitoring should have accelerator metrics      |
| StackdriverAcceleratorMonitoring        |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:StackdriverCustomMetrics        |             | Stackdriver Monitoring should run Custom Metrics -          |
|                                         |             | Stackdriver Adapter for new resource model                  |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:StackdriverExternalMetrics      |             | Stackdriver Monitoring should run Custom Metrics -          |
|                                         |             | Stackdriver Adapter for external metrics                    |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:StackdriverMetadataAgent        |             | Stackdriver Monitoring should run Stackdriver Metadata      |
|                                         |             | Agent                                                       |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:StackdriverMonitoring           |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+

`Network Special Interest Group <https://github.com/kubernetes/community/tree/master/sig-network>`__
----------------------------------------------------------------------------------------------------

+-----------------------------------------+-------------+-------------------------------------------------------------+
| **Labels**                              |**Mandatory**| **Description**                                             |
+=========================================+=============+=============================================================+
| Conformance                             | X           | Kubernetes conformance test                                 |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| None                                    | X           | Kubernetes mainstream features                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Example                         |             | Should create pod that uses DNS                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Ingress                         |             | Should prevent Ingress creation if more than 1 IngressClass |
|                                         |             | marked as default                                           |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:`IPv6DualStack <https://kuberne |             | IPv4/IPv6 dual-stack networking enables the allocation of   |
| tes.io/docs/concepts/services-networkin |             | both IPv4 and IPv6 addresses to Pods and Services.          |
| g/dual-stack/>`__                       |             | IPv4/IPv6 dual-stack networking is enabled by default for   |
|                                         |             | your Kubernetes cluster starting in 1.21, allowing the      |
|                                         |             | simultaneous assignment of both IPv4 and IPv6 addresses.    |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:kubemci                         |             | Should create ingress with pre-shared certificate           |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:KubeProxyDaemonSetMigration     |             | Upgrade kube-proxy from static pods to a DaemonSet should   |
|                                         |             | maintain a functioning cluster                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:KubeProxyDaemonSetUpgrade       |             | Upgrade kube-proxy from static pods to a DaemonSet should   |
|                                         |             | maintain a functioning cluster                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:NEG                             |             | Should sync endpoints to NEG                                |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:NoSNAT                          | X           | Should be able to send traffic between Pods without SNAT    |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Networking-IPv4                 | X           | Networking should provide Internet connection for           |
|                                         |             | containers                                                  |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Networking-IPv6                 |             | Networking should provide Internet connection for           |
|                                         |             | containers                                                  |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Networking-Performance          | X           | run iperf2                                                  |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:NetworkPolicy                   |             | NetworkPolicy between server and client should enforce      |
|                                         |             | policy to allow traffic only from a different namespace,    |
|                                         |             | based on NamespaceSelector                                  |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:PerformanceDNS                  |             | Should answer DNS query for maximum number of services per  |
|                                         |             | cluster                                                     |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:SCTP                            |             | should allow creating a basic SCTP service with pod and     |
|                                         |             | endpoints                                                   |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:SCTPConnectivity                |             | Pods should function for intra-pod communication: sctp      |
+-----------------------------------------+-------------+-------------------------------------------------------------+

`Node Special Interest Group <https://github.com/kubernetes/community/tree/master/sig-node>`__
----------------------------------------------------------------------------------------------

+-----------------------------------------+-------------+-------------------------------------------------------------+
| **Labels**                              |**Mandatory**| **Description**                                             |
+=========================================+=============+=============================================================+
| Conformance                             | X           | Kubernetes conformance test                                 |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| None                                    | X           | Kubernetes mainstream features                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Example                         | X           | Liveness pods should be automatically restarted             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:                                |             | Resource tracking for 100 pods per node                     |
| ExperimentalResourceUsageTracking       |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:GPUUpgrade                      |             | Master upgrade should NOT disrupt GPU Pod                   |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:PodGarbageCollector             |             | Should handle the creation of 1000 pods                     |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:RegularResourceUsageTracking    |             | Resource tracking for 0 pods per node                       |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:`ProbeTerminationGracePeriod <h | X           | Probing container should override timeoutGracePeriodSeconds |
| ttps://kubernetes.io/docs/tasks/configu |             | when LivenessProbe field is set                             |
| re-pod-container/configure-liveness-rea |             |                                                             |
| diness-startup-probes/#probe-level-term |             |                                                             |
| inationgraceperiodseconds>`__           |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| NodeFeature:`DownwardAPIHugePages <http |             | Downward API tests for huge pages should provide            |
| s://kubernetes.io/docs/tasks/inject-dat |             | container's limits.hugepages-pagesize; and                  |
| a-application/downward-api-volume-expos |             | requests.hugepages-pagesize& as env vars                    |
| e-pod-information>`__                   |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| NodeFeature:`PodReadinessGate <https:// | X           | Pods should support pod readiness gates                     |
| kubernetes.io/docs/concepts/workloads/p |             |                                                             |
| ods/pod-lifecycle/#pod-readiness-gat    |             |                                                             |
| e>`__                                   |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| NodeFeature:RuntimeHandler              |             | RuntimeClass should run a Pod requesting a RuntimeClass     |
|                                         |             | with a configured handler                                   |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| NodeFeature:`Sysctls <https://kubernete | X           | Should not launch unsafe, but not explicitly enabled        |
| s.io/docs/tasks/administer-cluster/sysc |             | sysctls on the node                                         |
| tl-cluster/>`__                         |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+

`Scheduling Special Interest Group <https://github.com/kubernetes/community/tree/master/sig-scheduling>`__
----------------------------------------------------------------------------------------------------------

+-----------------------------------------+-------------+-------------------------------------------------------------+
| **Labels**                              |**Mandatory**| **Description**                                             |
+=========================================+=============+=============================================================+
| Conformance                             | X           | Kubernetes conformance test                                 |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| None                                    | X           | Kubernetes mainstream features                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:GPUDevicePlugin                 |             | Run Nvidia GPU Device Plugin tests                          |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:`LocalStorageCapacityIsolation  | X           | Validates local ephemeral storage resource limits of pods   |
| <https://kubernetes.io/docs/concepts/co |             | that are allowed to run                                     |
| nfiguration/manage-resources-container  |             |                                                             |
| s/>`__                                  |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Recreate                        |             | Run Nvidia GPU Device Plugin tests with a recreation        |
+-----------------------------------------+-------------+-------------------------------------------------------------+

`Storage Special Interest Group <https://github.com/kubernetes/community/tree/master/sig-storage>`__
----------------------------------------------------------------------------------------------------

+-----------------------------------------+-------------+-------------------------------------------------------------+
| **Labels**                              |**Mandatory**| **Description**                                             |
+=========================================+=============+=============================================================+
| Conformance                             | X           | Kubernetes conformance test                                 |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| None                                    | X           | Kubernetes mainstream features                              |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:ExpandInUsePersistentVolumes    |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Flexvolumes                     |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:GKELocalSSD                     |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:VolumeSnapshotDataSource        |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Volumes                         | X           |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:vsphere                         |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| Feature:Windows                         |             |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| NodeFeature:EphemeralStorage            | X           |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+
| NodeFeature:FSGroup                     | X           |                                                             |
+-----------------------------------------+-------------+-------------------------------------------------------------+

