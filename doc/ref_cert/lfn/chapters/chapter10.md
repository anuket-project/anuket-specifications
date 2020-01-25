[<< Back](../)

# 10. Gap analysis and Development
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [10.1 Introduction](#11.1)
* [10.2 Openstack Release Comparisons](#11.2)
* [10.3 Automation Gaps](#11.3)
* [10.4 Test Case Gaps](#11.4)
* [10.5 Framework Gaps](#11.5)

<a name="10.1"></a>
## 10.1 Introduction

- Describe the purpose of this chapter, which includes, but not limited to:
- Test Case Gaps (analysis)
-	Automation Gaps
-	Open Stack release Comparisons (Ocata, Pike, Queens, Stein, etc)

<a name="10.2"></a>
## 10.2 Openstack Release Comparisons

- Provide detail, perhaps in table format, comparing Openstack releases based on Pike baseline for CNTT RI-1 (e.g. Ocata, Pike, Queens, Stein, etc)

<a name="10.3"></a>
## 10.3 Automation Gaps

At the time of writing,
[the yaml file](https://git.opnfv.org/releng/tree/jjb/airship/cntt.yaml)
configuring all RI Jenkins jobs are postprocessed by hand which requires lots
of skills especially about
[Jenkins job builder](https://docs.openstack.org/infra/jenkins-job-builder/).
The RI Cookbook will be deeply simplified if the deployment scripts are
delivered in a new
[Xtesting](https://xtesting.readthedocs.io/en/latest/)-based container as
proposed in
[new RI deployment container](https://github.com/cntt-n/CNTT/issues/828).
In addition to avoid configuring the jumphost, it will allow generating the
Jenkins jobs via a simple yaml file and
[Xtesting CI](https://galaxy.ansible.com/collivier/xtesting).

<a name="10.4"></a>
## 10.4 Test Case Gaps

OPNFV has developed many test cases in the different
[OPNFV test projects](https://wiki.opnfv.org/display/testing/TestPerf) which
can quickly improve RC. As highlighted in OPNFV Marketing Goals for 2020 and
listed in
[RC Test case integration requirements]({{ "/doc/ref_cert/lfn/chapters/chapter02.html" | relative_url }}),
porting all the existing testcases to Xtesting will unify the test case
execution and simplify the test integration as required by RC. Here are all the
related issues:
- [port YardStick testcases to Xtesting](https://github.com/cntt-n/CNTT/issues/509)
- [port Bottlenecks to Xtesting](https://github.com/cntt-n/CNTT/issues/511)
- [port StorPerf testcases to Xtesting](https://github.com/cntt-n/CNTT/issues/673)
- [port NFVbench testcases to Xtesting](https://github.com/cntt-n/CNTT/issues/865)

Here are the possible new test cases which could be integrated in the existing
OPNFV projects to improve RC:

| issues                                                                                            | requirements      |
|---------------------------------------------------------------------------------------------------|-------------------|
| [update and integrate heat-tempest-plugin in Functest](https://github.com/cntt-n/CNTT/issues/483) | Heat API testing  |
| [integrate KloudBuster in Functest](https://github.com/cntt-n/CNTT/issues/508)                    | disk benchmarking |
| [add tempest-stress in Functest](https://github.com/cntt-n/CNTT/issues/916)                       | stress testing    |

<a name="10.5"></a>
## 10.5 Framework Gaps

As proposed in [port VTP test cases to Xtesting](https://github.com/cntt-n/CNTT/issues/917),
VTP selected in
[VNF E2E C&V Framework ]({{ "/doc/ref_cert/lfn/chapters/chapter05.html" | relative_url }})
requires small adaptations to fully fulfill the current
[RC Test case integration requirements]({{ "/doc/ref_cert/lfn/chapters/chapter02.html" | relative_url }}).
It seems trivial changes as VTP proposed a REST API but will ensure that both
NFVI and VNF testing can be executed in the same CI toolchain very easily.
