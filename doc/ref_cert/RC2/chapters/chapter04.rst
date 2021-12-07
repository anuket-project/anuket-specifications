CNF Test Cases and Requirements Traceability
============================================

.. figure:: ../figures/bogo_ifo.png
   :alt: Scope

   Scope

Introduction
------------

The scope of this chapter is to identify and list test cases based on
requirements defined in `Reference Architecture-2
(RA-2) <https://github.com/cntt-n/CNTT/blob/master/doc//ref_arch/kubernetes/README.md>`__.
This will serve as traceability between test cases and requirements for
Kubernetes platform interoperability.

Note that each requirement may have one or more test cases associated
with it.

Selection Criteria
------------------

Test cases, tools and their dependencies must be open source. The test
cases (or test suite with the test case) as well as the environment
needed to run the test should be reproducible by any party following
publicly available documentation.

Examples of initiatives (having testing tools, test suites, etc) with
test cases which could be used include K8s Conformance, K8s e2e,
Sonobuoy, Anuket Functest, CNF Conformance.

Traceability Matrix
-------------------

The following is a Requirements Traceability Matrix (RTM) mapping Test
Case, and/or Test Case Coverage, to RM and RA requirements –
configuration, deployment, runtime.

Test Case Traceability to RA2 Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section focuses on the test cases covering the requirements in
`RA-2 Chapter 4.9
<https://github.com/cntt-n/CNTT/blob/master/doc/ref_arch/kubernetes/chapters/chapter04.md>`__
for Kubernetes workloads.

=========== ========================== ===================== ========
RM/RA Ref   High-level test definition Test name and project Priority
=========== ========================== ===================== ========
ra2.app.001                                                  Must
ra2.app.002                                                  Must
ra2.app.003                                                  Must
ra2.app.004                                                  Must
ra2.app.005                                                  Must
ra2.app.006                                                  Must
ra2.app.007                                                  Must
=========== ========================== ===================== ========
