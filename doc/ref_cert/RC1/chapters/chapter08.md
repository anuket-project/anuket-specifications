# Gap analysis and Development

![Scope](../figures/bogo_ifo.png)

## Introduction

- Describe the purpose of this chapter, which includes, but not limited to:
- Test Case Gaps (analysis)
-	Automation Gaps
-	OpenStack release Comparisons

## Openstack Release Comparisons

- Provide details, preferably in table format, comparing OpenStack releases based
  on Wallaby baseline for RI-1

## Automation Gaps

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

## Test Case Gaps

Anuket has developed many test cases in the different
[test projects](https://wiki.opnfv.org/display/testing/TestPerf) which
can quickly improve RC. As listed in
[RC Test case integration requirements](chapter02.md),
porting all the existing testcases to Xtesting will unify the test case
execution and simplify the test integration as required by RC. Here are all the
related issues:

- [port VinePerf to Xtesting](https://github.com/cntt-n/CNTT/issues/511)
- [port NFVbench testcases to Xtesting](https://github.com/cntt-n/CNTT/issues/865)

Here are the possible new test cases which could be integrated in the existing
Anuket projects to improve RC:

| issues                                                                                            | requirements      |
|---------------------------------------------------------------------------------------------------|-------------------|
| [integrate KloudBuster in Functest](https://github.com/cntt-n/CNTT/issues/508)                    | disk benchmarking |
| [add tempest-stress in Functest](https://github.com/cntt-n/CNTT/issues/916)                       | stress testing    |

## Framework Gaps

As proposed in [port VTP test cases to Xtesting](https://github.com/cntt-n/CNTT/issues/917),
VTP selected in
[VNF E2E C&V Framework ](chapter05.md)
requires small adaptations to fully fulfill the current
[RC Test case integration requirements](chapter02.md).
It seems trivial changes as VTP proposed a REST API but will ensure that both
NFVI and VNF testing can be executed in the same CI toolchain very easily.
