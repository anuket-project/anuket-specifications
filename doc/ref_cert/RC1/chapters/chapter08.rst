Gap analysis and Development
============================

Introduction
------------

-  Describe the purpose of this chapter, which includes, but not limited
   to:
-  Test Case Gaps (analysis)
-  Automation Gaps
-  OpenStack release Comparisons

Openstack Release Comparisons
-----------------------------

-  Provide details, preferably in table format, comparing OpenStack
   releases based on Wallaby baseline for RI-1

Automation Gaps
---------------

At the time of writing, `the yaml
file <https://git.opnfv.org/releng/tree/jjb/airship/cntt.yaml>`__
configuring all RI Jenkins jobs are postprocessed by hand which requires
lots of skills especially about `Jenkins job
builder <https://docs.openstack.org/infra/jenkins-job-builder/>`__. The
RI Cookbook will be deeply simplified if the deployment scripts are
delivered in a new
`Xtesting <https://xtesting.readthedocs.io/en/latest/>`__-based
container as proposed in `new RI deployment
container <https://github.com/cntt-n/CNTT/issues/828>`__. In addition to
avoid configuring the jumphost, it will allow generating the Jenkins
jobs via a simple yaml file and `Xtesting
CI <https://galaxy.ansible.com/collivier/xtesting>`__.

Test Case Gaps
--------------

Anuket has developed many test cases in the different `test
projects <https://wiki.opnfv.org/display/testing/TestPerf>`__ which can
quickly improve RC. As listed in `RC Test case integration
requirements <https://cntt.readthedocs.io/en/latest/ref_cert/RC1/chapters/chapter02.html>`__,
porting all the existing testcases to Xtesting will unify the test case
execution and simplify the test integration as required by RC. Here are all the
related issues:

-  `port VinePerf to
   Xtesting <https://github.com/cntt-n/CNTT/issues/511>`__
-  `port NFVbench testcases to
   Xtesting <https://github.com/cntt-n/CNTT/issues/865>`__

Here are the possible new test cases which could be integrated in the
existing Anuket projects to improve RC:

+-------------------------------------------------+-------------------+
| issues                                          | requirements      |
+=================================================+===================+
| `integrate KloudBuster in                       | disk benchmarking |
| Functest                                        |                   |
| <https://github.com/cntt-n/CNTT/issues/508>`__  |                   |
+-------------------------------------------------+-------------------+
| `add tempest-stress in                          | stress testing    |
| Functest                                        |                   |
| <https://github.com/cntt-n/CNTT/issues/916>`__  |                   |
+-------------------------------------------------+-------------------+

Framework Gaps
--------------

As proposed in `port VTP test cases to
Xtesting <https://github.com/cntt-n/CNTT/issues/917>`__, VTP selected in
`VNF E2E C&V Framework <https://cntt.readthedocs.io/en/latest/ref_cert/RC1/chapters/chapter05.html>`__
requires small adaptations to fully fulfill the current `RC Test case
integration requirements <https://cntt.readthedocs.io/en/latest/ref_cert/RC1/chapters/chapter02.html>`__.
It seems trivial changes as VTP proposed a REST API but will ensure that both
NFVI and VNF testing can be executed in the same CI toolchain very easily.
