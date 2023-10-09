Gaps, Innovation, and Development
=================================


The purpose of this chapter is to identify the gaps between what is
required for automated deployment of VNFs on Cloud Infrastructure
frameworks and the framework offered by OpenStack. Once gaps are
identified, the next step will be to propose a plan to address these
gaps. The most obvious way to address the gaps will be to propose a set
of APIs in the upstream OpenStack community

The Gap
-------

Autoscaling
~~~~~~~~~~~

With regards to resource autoscaling
(gen.scl.01
:ref:`chapters/chapter02:general recommendations`) it is
recommended that the NFVO/VNFM manages the policy and triggers a
scale-up or scale-down action based on application telemetry, event, AI,
or ML etc. While the use of telemetry and alarming system can trigger a
scaling operation based on resource utilisation, without application
context this may not provide the granularity or reaction time required
by the application. It is therefore suggested that an OpenStack scaling
operation is called using an appropriate autoscaling web-hook by the
NFVO/VNFM.

For more information on auto-scaling with Heat please see the OpenStack
document "Autoscaling with heat :cite:p:`autosc_ra1`".
Please note that the OpenStack Senlin service is still under development
with major architectural changes made in the OpenStack Ussuri release.

Please note: physical compute node autoscaling is out of scope.

.. bibliography::
   :cited:
