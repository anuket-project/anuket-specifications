[<< Back](../)

# 8. Gap analysis and Development
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [8.1 Introduction](#8.1)
* [8.2 Openstack Release Comparisons](#8.2)
* [8.3 Automation Gaps](#8.3)
* [8.4 Test Case Gaps](#8.4)
* [8.5 Framework Gaps](#8.5)

<a name="8.1"></a>
## 8.1 Introduction

- Describe the purpose of this chapter, which includes, but not limited to:
- Test Case Gaps (analysis)
-	Automation Gaps
-	OpenStack release Comparisons (Train, Ussuri, etc)

<a name="8.2"></a>
## 8.2 Openstack Release Comparisons

- Provide details, preferably in table format, comparing OpenStack releases based
  on Train baseline for Anuket CNTT RI-1 (e.g. Train, Ussuri, etc)

<a name="8.3"></a>
## 8.3 Automation Gaps

At the time of writing,
[the yaml file](https://git.opnfv.org/releng/tree/jjb/airship/cntt.yaml)
configuring all RI Jenkins jobs are postprocessed by hand which requires lots
of skills especially about
[Jenkins job builder](https://docs.openstack.org/infra/jenkins-job-builder/).
The RI Cookbook will be deeply simplified if the deployment scripts are
delivered in a new
[Xtesting](https://xtesting.readthedocs.io/en/latest/)-based container as
proposed in
[new RI deployment container](https://github.com/cntt-n/Anuket CNTT/issues/828).
In addition to avoid configuring the jumphost, it will allow generating the
Jenkins jobs via a simple yaml file and
[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting).

<a name="8.4"></a>
## 8.4 Test Case Gaps

OPNFV has developed many test cases in the different
[OPNFV test projects](https://wiki.opnfv.org/display/testing/TestPerf) which
can quickly improve RC. As highlighted in OPNFV Marketing Goals for 2020 and
listed in
[RC Test case integration requirements](chapter02.md),
porting all the existing testcases to Xtesting will unify the test case
execution and simplify the test integration as required by RC. Here are all the
related issues:
- [port YardStick testcases to Xtesting](https://github.com/cntt-n/Anuket CNTT/issues/509)
- [port Bottlenecks to Xtesting](https://github.com/cntt-n/Anuket CNTT/issues/511)
- [port StorPerf testcases to Xtesting](https://github.com/cntt-n/Anuket CNTT/issues/673)
- [port NFVbench testcases to Xtesting](https://github.com/cntt-n/Anuket CNTT/issues/865)

Here are the possible new test cases which could be integrated in the existing
OPNFV projects to improve RC:

| issues                                                                                            | requirements      |
|---------------------------------------------------------------------------------------------------|-------------------|
| [update and integrate heat-tempest-plugin in Functest](https://github.com/cntt-n/Anuket CNTT/issues/483) | Heat API testing  |
| [integrate KloudBuster in Functest](https://github.com/cntt-n/Anuket CNTT/issues/508)                    | disk benchmarking |
| [add tempest-stress in Functest](https://github.com/cntt-n/Anuket CNTT/issues/916)                       | stress testing    |

<a name="8.5"></a>
## 8.5 Framework Gaps

As proposed in [port VTP test cases to Xtesting](https://github.com/cntt-n/Anuket CNTT/issues/917),
VTP selected in
[VNF E2E C&V Framework ](chapter05.md)
requires small adaptations to fully fulfill the current
[RC Test case integration requirements](chapter02.md).
It seems trivial changes as VTP proposed a REST API but will ensure that both
NFVI and VNF testing can be executed in the same CI toolchain very easily.
