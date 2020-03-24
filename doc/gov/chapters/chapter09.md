# 9. Adoption
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [9.1 Introduction](#9.1)
* [9.2 Transition Plan](#9.2)
  * [9.2.1 Conformance Levels](#9.2.1)
  * [9.2.2 Exception Types](#9.2.2)
  * [9.2.3 Transition Framework](#9.2.3)
* [9.3 Adoption Strategy](#9.3)
  * [9.3.1 Expectations from Operators](#9.3.1)
  * [9.3.2 Expectations from Vendors](#9.3.2)
  * [9.3.3 Expectations from Industry](#9.3.3)
* [9.4 Adoption Roadmaps](#9.4)
* [9.5 CNTT Field Trial Approach] (#9.5) 
<a name="9.1"></a>
## 9.1 Introduction

It is vitally important for CNTT to have working solution from infrastructure vendors and mature VNFs/CNFs designs from application vendors that is compliant to CNTT specifications. It is also understood that, in some areas, the industry might not have solutions that are fully aligned with CNTT requirements. 

Therefore, a transition plan, an adoption strategy, and adoption Roadmap is needed to be agreed on within the CNTT community. This document explains those elements in details. 

<a name="9.2"></a>
## 9.2 Transition Plan

A Transition plan comprised of one or more exceptions and/or transitions is required to address technology that does not presently conform to CNTT mandates, and hence requires explicit direction to prescribe how the situation will be treated in the present, as well as in the future.

The transition plan described here will inform application designers how RC and ultimately industry certification programs will react when encountering exceptions during the qualification process, including flagging warnings and potentially errors which could prevent issuance of a certification badge.

<a name="9.2.1"></a>
### 9.2.1 Conformance Levels

- **Fully Conformant**: VNFs/CNFs or NFVI are written and designed to be fully conformant to CNTT specification with no use of any of the allowed Exceptions.
- **Conformant with Exceptions**: VNFs/CNFs or NFVI are written and designed to be conformant to CNTT with one or more of the allowed Exceptions used.

<a name="9.2.2"></a>
### 9.2.2 Exception Types

- **Technology Exceptions** : Using specific technologies that are considered non conformant to CNTT principles (such as PCIe Direct Assignment, exposure of hardware features to VNFs/CNFs).
- **Version Exceptions**: Using Versions of  Software components, , APIs, or Hardware that are different from the one specified in the specification.

<a name="9.2.3"></a>
### 9.2.3 Transition Framework

#### VNF/CNF Transition Plan Framework 

Exceptions will be clearly recorded in the appropriate specification Appendix which will act as a guidance to VNFs/CNFs vendors of what Exceptions will be allowed in each CNTT release. **Figure 1** below demonstrate the concept.

- As technology matures, fewer and fewer Exceptions will be allowed in CNTT releases.
- For each CNTT Release, VNF/CNF can be either:
  - **Fully Conformant**: No Exception used.
  - **Conformant with Exception**: One or More of the allowed Exceptions in RM has been used.  


<p align="center"><img src="../figures/vnf_cnf_transition.png" alt="Transition" title="VNF/CNF Transition Plan" width="70%"/></p>
<p align="center"><b>Figure 1:</b> Transition Plan for VNFs/CNFs within CNTT</p>

#### NFVI Transition Plan Framework 

Exceptions will be clearly recorded in Reference Architectures' Appendices which will act as a guidance to NFVI vendors of what Exceptions will be allowed in each CNTT release. **Figure 2** below demonstrate the concept.

- As technology matures, fewer and fewer Exceptions will be allowed in CNTT releases.
- For each CNTT Release, VNF/CNF can be either:
  - **Fully Conformant**: Support the Target Reference Architecture without any exceptions. There should be a technology choice in RA to support RM Exceptions (However, none of the Exceptions allowed in RA has been used).
  - **Conformant with Exceptions**: One or more of the allowed exceptions in RA are used.

<p align="center"><img src="../figures/nfvi_transition.png" alt="Transition" title="NFVI Transition Plan" width="70%"/></p>
<p align="center"><b>Figure 2:</b> Transition Plan for NFVI solutions within CNTT</p>

<a name="9.3"></a>
## 9.3 Adoption Strategy

<a name="9.3.1"></a>
### 9.3.1 Expectations from Operators

<a name="9.3.2"></a>
### 9.3.2 Expectations from Vendors

<a name="9.3.3"></a>
### 9.3.3 Expectations from Industry

<a name="9.4"></a>
## 9.4 Adoption Roadmap

<a name="9.5"></a>
## 9.5 CNTT Field Trial/ Approach

This portion of Chapter 9 is segmented into two subsections. Section 9.5.1 provides a summary and overview of the trials activities specifically targeted to potential trials participants. Section 9.5.2 addresses the overall approach of CNTT to field trials as a method of ensuring consistency between releases.

<a name="9.5.1"></a>

### 9.5.1 Summary/Field Trials Participants Overview

CNTT has built a Reference Architecture (RA-1) on which Reference Implementation (RI-1) and Reference Conformance (RC-1) requirements have been defined. To ensure value add to Telco industry operators, suppliers, and end user customers, it is running field tests to validate the feasibility, utility, and effectiveness of its requirements and methods (RI-1/RC-1).

<a name="9.5.1.1"></a>
#### 9.5.1.1 Intents of Field Trials

This is a partnership of CNTT with participants to validate the community is adopting a consistent approach. This is not a VI badging exercise. The trials will validate the RI-1 and the RC-1 test suite requirements and methods themselves, not VNFs or VI systems under test. 

<a name="9.5.1.2"></a>
#### 9.5.1.2 Expectations and Assumptions of Field Trials

CNTT expects to exit the trial with either validation of RI-1 and RC-1 or a set of actions to close gaps. Through the community continuous improvement process, badging processes mutually beneficial to operators and suppliers will be defined/refined. CNTT assumes that performance testing is not included in the field trial.

<a name="9.5.1.3"></a>
#### 9.5.1.3 Pre-trials activities

Prior to the beginning of field trials, the CNTT community will define an operational plan, secure resources, and provide all designated contact information required to support the trial participants.  As the results of the trails may produce data and information that could be considered sensitive by participants, CNTT will establish standard data set requirements and secure collection methods to ensure participant privacy protection.

<a name="9.5.1.4"></a>
#### 9.5.1.4 Expectations of Trials Participants

Trials participants will be expected to commit to establishing an RA-1 compliant NFVi through means that are most appropriate for the participant. 

First, the participant will secure appropriate environment space from pre-existing space, newly built space or securing LaaS.  The environment can exist in private or community hardware infrastructure.

Second, the participant will build/setup/configure the environment space via their preferred method. This can include the use of a cookbook, automated install, and/or build from RA-1/RI-1 requirements and specifications. CNTT RI-1 Chapter 3 (https://github.com/cntt-n/CNTT/blob/master/doc/ref_impl/cntt-ri/chapters/chapter03.md ) documentation provides the matching RI-1 requirements for the build.

<a name="9.5.1.5"></a>
#### 9.5.1.5 Expectation 2: Execute the RC-1 Test suite

CNTT will provide the participants with the community RC-1 Test suite, found at this Link: https://github.com/cntt-n/CNTT/blob/master/doc/ref_impl/cntt-ri/chapters/chapter04.md. The participants will execute test cases per instructions and record the quantitative results.

Test case suite should be executed successfully at least 3 times. Three times represents the recommended number of test suite runs to eliminate false positives in results.  A triage process will be used to determine and manage root cause analysis of failures. If the failures are determined to be issues with the participant’s RI, CNTT will convey the issues to the RI and make available SMEs to assist the participant in resolving the issues. When failures are deemed to be caused by an issue or gap in the RA/RI/RC, the community will work to determine the resolution, and modify the RA/RI/RC accordingly.

Once the test case suite execution is successful for 3 consecutive iterations, the participant will provide the data of all iterations (both successful and unsuccessful) to CNTT based on participant privacy expectations (See Expectation #4)

<a name="9.5.1.6"></a>
#### 9.5.1.6 Expectation #3: The Qualitative Survey

At the conclusion of Test Case iterations, the participant will be asked to complete a qualitative survey of their experience. This survey will be used to measure the feasibility, utility, and effectiveness of the RI-1 specifications, installation/configuration methods and RC-1 Test case efficacy. The survey will use an Agile User Story format. The Table below provides an example of the survey questions:

<p align="center"><img src="../figures/Table 1.png" alt="Qualitative Survey" title="Survey/Questionnaire example" width="85%"/></p>
<p align="center"><b>Table 1:</b> Survey/Questionnaire example</p>


<a name="9.5.1.7"></a>
#### 9.5.1.7 Expectation 4: Providing Trials Results

As a community, CNTT is concerned with the privacy of the participant data. CNTT subscribes to the LFN anti-trust policies ( https://www.linuxfoundation.org/antitrust-policy/ ) and the LFN Privacy Policy ( https://www.linuxfoundation.org/privacy/ ). As discussed in the Pre-trials activity section of the document, data generated by the trials will be secured to protect participant privacy. Additionally, should participants have concerns regarding the data they generate from the trials, CNTT will either work with the participant to eliminate their concerns, honor instructions from the participant on the data use, or agree to exclude that participant’s data from the analysis.

<a name="9.5.1.8"></a>
#### 9.5.1.8 Conclusion: Final Deliverable - End-of-Trial Report

Upon completion of field trials, CNTT shall develop an End of Trial Report which summarizes the overall conclusions based on the evaluation, to include:

1.	Successes: What went activities went well generally or specifically? How did it compare to the past or alternative results?
2.	Challenges: What didn’t go well overall? What impact could these challenges have on adoption?
3.	Discoveries: What are key discoveries/strategic learnings about any CNTT approaches or methods? Other?
4.	Decisions and Recommendations: Identification of key decisions made and list of what corrective actions shall be taken? What to enhance, maintain, or discontinue?
5.	Next Steps: Indication of proposed steps and activities to be undertaken by the community

### 9.5.2 CNTT Field Trials Approach 

### 9.5.2.1 Background
The Common NVFI Telco Taskforce (CNTT) is building a set of infrastructure standards to be implemented within telcos to improve cost effectiveness and speed of delivery of Virtual Network Functions. As part of the standards development, the organization has built a Reference Model (RM) on which Reference Implementation (RI) and Reference Conformance (RC) standards have been defined.  For CNTT to ensure value add to Telco industry operators, suppliers, and end user customers, it is running field tests to validate the feasibility, utility, and effectiveness of its methods (RI/RC standards).

<a name="9.5.2.2"></a>
### 9.5.2.2 Purpose of this Document Section

The purpose of this document is to define the goals/outcomes, expectations, and roles necessary to support the CNTT release trials. The document will define/discuss the following:

*	Purpose of field trials
*	Goals/desired outcomes of the field trials
*	Success indicators 
*	Intentions and expectations
*	Action plan
*	Resource requirements
*	Metrics definition

<a name="9.5.2.3"></a>
### 9.5.2.3 Field Trial Purpose

In the truest form, adoption of a standard is an indication of it’s success within an industry. Standards developed must be interactively tested in multiple environments or “trialed” to ensure they are practicable, functional, and operative. Without running trials to validate the CNTT approach, standards may not provide intended value across a sufficient spectrum of participating entities to be widely adopted. 

<a name="9.5.2.4"></a>
#### 9.5.2.4 Intents

1)	This is a partnership approach to validate CNTT community is adopting a consistent approach
2)	Validate RI-1 specifications and RC-1 test suite, not VNFs or NFVI’s in the trial

<a name="9.5.2.5"></a>
#### 9.5.2.5 Key Expectations and Assumptions

1)	Expectation: Through healthy feedback from suppliers, CNTT will exit the trial with either validation of VI-1 and RC-1 or a set of actions to close gaps.
2)	Expectation: Post trial and gap closure, the community will define a badging process that is mutually beneficial to operators and suppliers. 
3)	Assumption: Performance testing is not in field trial.

<a name="9.5.2.6"></a>
### 9.5.2.6 Overview: Stages of Field Trial

The following diagram the key components and flow of activities, actions, and deliverables to be undertaken during the trial. Details of each component are provided in this document.

<p align="center"><img src="../figures/field_trials.png" alt="CNTT Field Trial Approach" title="Field Trial Approach" width="85%"/></p>
<p align="center"><b>Figure 3:</b> Field Trial Approach</p>

<a name="9.5.2.7"></a>
#### Success Indicators

1) Agreement secured on the use of trials results data, including:
a.	Detail level of data required to validate
b.	Acceptable data values indicating valid results
c.	Detail level of data that will be published

2) VI-1 Labs are successfully stood up in all target environments
* Vendor (NFVI, VNF, VIM, 3rd Party)
*	Community (OPNFV)
*	LaaS (e.g. UNH)

3) Engaged vendors successfully configure their cloud infrastructure per RI-1 and run the RC-1 test suite and are able to provide expert feedback

4) Engaged vendors are able to validate that they can instantiate and run rudimentary validation of VNF functionality on more than one conformant cloud infrastructure (NFVI)

<a name="9.5.2.7"></a>
### 9.5.2.7 Initiation 

<a name="9.5.2.7.1"></a>
#### 9.5.2.7.1 Objectives of RI-1/RC-1 Trials

The object is to quantitively and qualitatively assess and evaluate the following CNTT requirements, methods, and support processes:
* RI-1 Specifications
*	VI-1 implementation support methods ( i.e. cookbooks, installation manuals, how to guides etc.)
* RC-1 Test Suite 
* TC Traceability
* Test Pass Criteria
* Benchmark Data
 * Other?

Overall, feedback from the trials and issues and gaps found shall be used to enhance and improve the CNTT approach. Enhancements to future releases will/shall be identified accordingly.

<a name="9.5.2.7.2"></a>
#### 9.5.2.7.2 Trial Participant Interaction with the Community

The focus of the field trials is on the test suites and CNTT methods, not on the systems under test. A process is being developed to identify issues and gaps and managing how they are reported.

CNTT will work very closely with field trial partners (NFVI vendors, VNF vendors, or system integrators) and agree on labs that will be used for the trial. CNTT will take all necessary measures to protect the intellectual property rights (IP rights) for all partners involved in those trials. All Reports and findings will be vetted carefully and only published after being approved by all parties concerned. No test results or records will be kept in any public records without the consent of the participants.

The targeted repositories for this information are:

CNTT GitHub

*  GitHub Code
  
*  GitHub Projects
  
*  GitHub Issues
  
OPNFV 

*  (Where?)

<a name="9.5.2.7.3"></a>
#### 9.5.2.7.3 Test Case Identification

Specific test cases for the field trials will be documented and provided to the participants based upon the CNTT RI-1 and RC-1 work streams requirements. The technical testing methods, procedures and documentation shall be provided by these work streams. 

<a name="9.5.2.7.4"></a>
#### 9.5.2.7.4 Vendor Solicitation/Commitment

Vendor members will be solicited for participation in the trials. The vendors will be required to commit fully to the assessment and evaluation  processes. As previously mentioned, additional discussion is needed to define what results data and at what level is acceptable to be shared.

<a name="9.5.2.7.5"></a>
#### 9.5.2.7.5 Deliverable

The Initiate Field Trial Stage will deliver execution and assessment plans including: 

* A high-level check list of the tasks each participant will need to complete shall be provided.  
* The plan will contain all the key milestones and activities the participants will expected to perform. 

<a name="9.5.2.8"></a>
### 9.5.2.8 Execution Stage

<a name="9.5.2.8.1"></a>
#### 9.5.2.8.1 Objectives of the Execute Stage

The objective of Execute Stage is participants implementing field trials tasks and record/assess outcomes CNTT will assemble the Trials team to fully develop the action plan including resource assignments, materials requirements, and timelines. 

Activities include the deployment and configuration of VI-1 and execution of the RC-1 test cases. Vendor community members that commit to the trials will build/setup/prep labs for the trials per the instructions:

1.	Secure appropriate environment space (pre-existing, new build, LaaS)

2.	VI-1 per published RI-1 Specifications  

3.	RC-1 Test suite will be provided to the participants
   
4. Trial Participants ensure a complete understanding of the test suite actions and expected outcomes.

<a name="9.5.2.8.2"></a>
#### 9.5.2.8.2 Running the Field Trial

The field trial will run the Test Suite for 3 Iterations. For each iteration:

*	Vendor RC-1 test results are documented. Vendor provide feedback to CNTT
*	OPNVF RC-1 test results are documented. OPNFV provides feedback to CNTT 

The Community shall review Issues/Gaps during the evaluate stage and do one of the following:

*	Accept the Issue/Gap, and accordingly modify the RI/RC 
*	Not-Accept the Issue/Gap and document the condition while maintaining the privacy of participants

<a name="9.5.6.1"></a>
#### 9.5.6.1 Resources and Roles

CNTT will staff the plan by soliciting volunteers from the participants. The list below is suggested list of roles to be staffed:

*	Overall Field Trial Lead
*	Technical Field Trial Steering Lead 
*	Vendor lead from each supplier
*	SME(s) for RC1 supporting suppliers
*	SME(s) for RI1 supporting suppliers
*	OPNVF lead for RI1/RC1
*	Other support roles such as Governance, technical writers, etc.

The participants that volunteer for the roles will be expected to provide the appropriate level of time to support the trials initiative.

<a name="9.5.2.8.4"></a>
#### 9.5.2.8.4 Deliverables

The deliverables of the execute stage will be: 

* Implemented Participant RA-1 Labs which have been tested.
* RC-1 Test cases are run.

<a name="9.5.2.9"></a>
### 9.5.2.9 Assessment

The Assess stage shall utilize data collected during the execute stage. Participants will assess their experience using the methods used by CNTT accordingly to quantitatively and or qualitatively measure:

#### Required Assessments

* VI-1 Implementation methods and procedures (cookbook, etc) 
* RI-1 Specifications
*	RC-1 Test Suite 
*	TC Traceability
*	Test Pass Criteria
*	Benchmark Data
*	Other?

#### Optional (Pre-Launch Trials only)

##### NF Instantiation

   *	Smoke test the level of verification and validation
   *	Non-functional
   *	Stand up with only key operations working

OPNFV will also assess their experience of the methods used by CNTT to assess the following operational areas:
1.	Mechanism for Reporting Issues / Receiving Status
2.	Results Collation and Presentation, 
3.	Support Availability
   *	SME (Human)
   *	Materials 
4.	Release Notes
5.	Other?

<a name="9.5.2.9.1"></a>
#### 9.5.2.9.1 Measuring Outcomes

<a name="9.5.2.9.2"></a>
#### 9.5.2.9.2 Qualitative Outcomes

Participants and project teams will be provided a questionnaire based upon a set of User stories related to the field trail. Questionnaire responses will be used in the Evaluate phase.

<a name="9.5.2.9.3"></a>
#### 9.5.2.9.3 Quantitative Outcomes

Technical outcomes i.e. technical test results will be collected and managed by RI-1/RC-1 work streams based upon participants privacy preferences.

<a name="9.5.2.9.4"></a>
#### 9.5.2.9.4 Deliverables

* Feedback is provided from the participants on their outcomes to CNTT.
* Completed Questionnaire and test case results (Participant and OPNFV)

<a name="9.5.2.10"></a>
### 9.5.2.10 Evaluation Stage

Proving the ‘right’ value to the operator and vendor community is ultimately what will ensure adoption of CNTT requirements. These field trials are intended to verify and validate the requirements and  methods developed by CNTT so that adjustments can be made to ensure the intended value is being delivered. 

CNTT shall evaluate all feedback and test results to understand whether CNTT methods and measures are meeting intended purposes. If a method or measure is not meeting its intended purpose, it shall be identified as a gap or an issue for resolution. Determinations if and when adjustments or adaptations are needed shall be made to by CNTT community.


<a name="9.5.2.10.1"></a>
#### 9.5.2.10.1 Deliverables

All identified gaps and issues shall be captured in the CNTT GitHub repository. Decisions and determinations will be captured and logged accordingly.
   
<a name="9.5.2.11"></a>
### 9.5.2.11 Close Stage

To close out the Field Trial, CNTT shall summarize its evaluation of the Field Trial and actions to be taken to address any adaption needed.

<a name="9.5.2.11.1"></a>
#### 9.5.2.11.1 Final Deliverable - End-of-Trial Report

Upon completion of field trials, CNTT shall develop an End of Trial Report which summarizes the overall conclusions based on the evaluation, to include:
   *	Successes - What went activities well generally or specifically? How did it compare to the past or alternative results?   
   * Challenges - What didn’t go well overall? What impact could these challenges have to adoption?
   *	Discoveries - What are key discoveries/strategic learnings about any CNTT approaches or methods? Other?
   *	Decisions and Recommendations - Identification of key decisions made and list of what corrective actions shall be taken? What to enhance, maintain, or discontinue?
   *	Next Steps - Indication of proposed steps and activities to be undertaken by the community
