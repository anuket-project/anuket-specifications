[<< Back](../../kubernetes)

# 6. Special Interest Group level requirements
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [6.1 Introduction](#6.1)
* [6.2 API Machinery Special Interest Group](#6.2)

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
