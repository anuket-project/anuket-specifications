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

Test Case Gaps
--------------

Anuket has developed many test cases in the different `test
projects <https://wiki.opnfv.org/display/testing/TestPerf>`__ which can
quickly improve RC. As listed in
:ref:`ref_cert/RC1/chapters/chapter02:nfvi conformance requirements`,
porting all the existing testcases to Xtesting will unify the test case
execution and simplify the test integration as required by RC. Here are all the
related issues:

-  `port VinePerf to
   Xtesting <https://github.com/cntt-n/CNTT/issues/511>`__
-  `port NFVbench testcases to
   Xtesting <https://github.com/cntt-n/CNTT/issues/865>`__

Here are the possible new test cases which could be integrated in the
existing Anuket projects to improve RC:

.. list-table:: Possible new test cases
   :widths: auto

   * - Issues
     - Requirements
   * - `integrate KloudBuster in Functest
       <https://github.com/cntt-n/CNTT/issues/508>`__
     - disk benchmarking
   * - `add tempest-stress in Functest
       <https://github.com/cntt-n/CNTT/issues/916>`__
     - stress testing

Framework Gaps
--------------

As proposed in `port VTP test cases to
Xtesting <https://github.com/cntt-n/CNTT/issues/917>`__, VTP selected in
:ref:`ref_cert/RC1/chapters/chapter05:vnf testing framework requirements`
requires small adaptations to fully fulfill the current
:ref:`ref_cert/RC1/chapters/chapter02:nfvi conformance requirements`.
It seems trivial changes as VTP proposed a REST API but will ensure that both
NFVI and VNF testing can be executed in the same CI toolchain very easily.
