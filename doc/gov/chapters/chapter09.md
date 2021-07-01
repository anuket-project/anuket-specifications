# 9. Adoption
<p align="right"><img src="../figures/bogo_sdc.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [9.1 Introduction](#9.1)
  * [9.1.1 Background](#9.1.1)
  * [9.1.2 Field Trial Purpose](#9.1.2)
  * [9.1.3 Purpose of this Document Section](#9.1.3)  
* [9.2 Adoption Strategy](#9.3)
  * [9.2.1 Expectations from Operators](#9.3.1)
  * [9.2.2 Expectations from Vendors](#9.3.2)
  * [9.2.3 Expectations from Industry](#9.3.3)
* [9.3 Adoption Roadmaps](#9.4)
* [9.4 Transition Plan](#9.2)
  * [9.4.1 Conformance Levels](#9.2.1)
  * [9.4.2 Exception Types](#9.2.2)
  * [9.4.3 Transition Framework](#9.2.3)
* [9.5 Anuket CNTT Field Trial Approach](#9.5)

<a name="9.1"></a>
## 9.1 Introduction
It is vitally important for the success of the Anuket CNTT mission to have as many working Anuket CNTT compliant solutions, including infrastructure and VNF/CNF designs from the vendor community as possible. Obviously, there will be solutions that will not be able to be fully aligned with Anuket CNTT requirements, however, the intention is to make the Anuket CNTT reference architectures and implementations map to the real world so to make compliance attractive to the broader community. Therefore, a transition plan, an adoption strategy, and adoption roadmap needs to be agreed on within the Anuket CNTT community. The intention of this document is to detail the strategy for broader adoption in the larger telecom ecosystem. 

<a name="9.1.1"></a>
### 9.1.1 Background
The Cloud iNfrastructure Telco Taskforce (Anuket CNTT) is developing a set of cloud infrastructure specifications to be implemented within telcos to improve the cost effectiveness and speed of deployment of cloud network functions. As part of the specifications development, the organization has built a Reference Model (RM) on which Reference Implementation (RI) and Reference Conformance (RC) standards have been defined.  For Anuket CNTT to ensure value add to Telco industry operators, suppliers, and end user customers, it is running field tests to validate the feasibility, utility, and effectiveness of its methods (RI/RC standards).

<a name="9.1.2"></a>
### 9.1.2 Field Trial Purpose

In the truest form, adoption of a specification is an indication of it’s success within an industry. Specifications developed must be interactively tested in multiple environments or “trialed” to ensure they are practicable, functional, and operative. Without running trials to validate the Anuket CNTT approach, specifications may not provide intended value across a sufficient spectrum of participating entities to be widely adopted. The intentions of these field trials is as follows:

1)	Demostrate the partnership approach to validate Anuket CNTT community is adopting a consistent approach
2)	Validate the RI-1 specifications and RC-1 test suite, not VNFs or NFVI’s

<a name="9.1.3"></a>
### 9.1.3 Purpose of this Document Section
The purpose of this document is to define the goals/outcomes, expectations, and roles necessary to support the Anuket CNTT release trials. The document will define/discuss the following:

*	Purpose of field trials
*	Goals/desired outcomes of the field trials
*	Success indicators 
*	Intentions and expectations
*	Action plan
*	Resource requirements
*	Metrics definition

<a name="9.2"></a>
## 9.2 Adoption Strategy

<a name="9.3.1"></a>
### 9.2.1 Expectations from Operators

<a name="9.2.2"></a>
### 9.2.2 Expectations from Vendors

<a name="9.2.3"></a>
### 9.3.3 Expectations from Industry

<a name="9.3"></a>
## 9.3 Adoption Roadmap

<a name="9.4"></a>
## 9.4 Transition Plan

A Transition plan is needed to address technology components that do not presently conform to Anuket CNTT principles, and hence require explicit direction on how the situation will be treated in the present, as well as plans for the future.  The plans might be that the component will be added to the Anuket CNTT corpus in a future release, or remain outside of the main body, depending on the nature of the given technology or system.  For example, a technology might be propriatary to a specific vendor, yet has become a de facto standard  would not be part of the reference, but might be referred to due to its wildspread adoption by the industry.

The transition plan described here informs application designers on how the Reference Conformance, and ultimately the industry certification programs will manage and document exceptions encountered during the badging process. The actions taken might include flagging warnings and potential errors caused by the variance from the Anuket CNTT conformance levels, which could prevent issuance of a certification badge.

<a name="9.4.1"></a>
### 9.4.1 Conformance Levels

- **Fully Conformant**: VNFs/CNFs or Cloud Infrastructure designed and developed to be fully conformant to Anuket CNTT specifications with no use of any of the allowed Exceptions.
- **Conformant with Exceptions**: VNFs/CNFs or Cloud Infrastructure written and designed to be conformant to Anuket CNTT specifications with one or more of the allowed Exceptions used.

<a name="9.4.2"></a>
### 9.4.2 Exception Types

- **Technology Exceptions** : The use of specific technologies that are considered non conformant to Anuket CNTT principles (such as PCIe Direct Assignment, exposure of hardware features to VNFs/CNFs).
- **Version Exceptions**: Using versions of  Software components, APIs, or Hardware that are different from the specifications.

<a name="9.4.3"></a>
### 9.4.3 Transition Framework

#### NFVI Transition Plan Framework 

Exceptions will be clearly recorded in a given Reference Architecture's Appendix.  That document provides guidance to NFVI vendors of what Exceptions will be allowed in each Anuket CNTT release. **Figure 1** below demonstrates the concept.

- It is expected that over time, as technology matures, there will be a decreasing numbers of Exceptions allowed in Anuket CNTT releases.
- For each Anuket CNTT Release, the Cloud Infrastructure can be either Fully Conformant or Conformant with Exceptions.
  - **Fully Conformant**: Supports the Target Reference Architecture without any exceptions. There should be a technology choice in RA to support RM Exceptions (However, none of the Exceptions allowed in RA has been used).
  - **Conformant with Exceptions**: One or more of the allowed exceptions in RA are used.

<p align="center"><img src="../figures/nfvi_transition.png" alt="Transition" title="NFVI Transition Plan" width="70%"/></p>
<p align="center"><b>Figure 1:</b> Transition Plan for NFVI solutions within Anuket CNTT</p>

#### VNF/CNF Transition Plan Framework 

Exceptions will be clearly recorded in the appropriate specification Appendix which will service as guidance to VNF/CNF application vendors of what Exceptions will be allowed in each Anuket CNTT release. **Figure 2** below demonstrates the concept.

- It is expected that over time, as technology matures, there will be a decreasing numbers of Exceptions allowed in Anuket CNTT releases.
- For each Anuket CNTT Release, VNF/CNF can be either:
  - **Fully Conformant**: No Exception used.
  - **Conformant with Exception**: One or More of the allowed Exceptions in the Reference Model have been used.  

<p align="center"><img src="../figures/vnf_cnf_transition.png" alt="Transition" title="VNF/CNF Transition Plan" width="70%"/></p>
<p align="center"><b>Figure 2:</b> Transition Plan for VNFs/CNFs within Anuket CNTT</p>

<a name="9.5"></a>
## 9.5 Anuket CNTT Field Trial/ Approach

This portion of Chapter 9 is segmented into two subsections. Section 9.5.1 provides a summary and overview of the trials activities specifically targeted to potential trials participants. Section 9.5.2 addresses the overall Anuket CNTT approach to field trials as a method of ensuring consistency between releases.

<a name="9.5.1"></a>

### 9.5.1 Summary/Field Trials Participants Overview

Reference Implementation (RI-1) and Reference Conformance (RC-1) requirements are defined by the Reference Architecture (RA-1). To ensure that Telecom industry operators, suppliers, and end user customers will derive benefit for the effort, Anuket CNTT is running field tests to validate the feasibility, utility, and effectiveness of its requirements and methods (RI-1/RC-1).

<a name="9.5.1.1"></a>
#### 9.5.1.1 Field Trials Intentions

The field trials are viewed as a partnership of Anuket CNTT with participants to validate that the community is adopting a consistent approach. This is not a VI badging exercise. The trials will validate the RI-1 and the RC-1 test suite requirements and methods themselves, not VNFs or VI systems under test. 

<a name="9.5.1.2"></a>
#### 9.5.1.2 Expectations and Assumptions of Field Trials

Anuket CNTT expects to exit the trials with either validation of RI-1 and RC-1 or a set of actions to review and possibly modify the RI-1 or RC-1 to address any gaps identified.  By taking advantage of the community continuous improvement process, the lessons learned in the field trials will be applied to the badging processes to refine/define the criteria with the intention of making the badges meaningful and mutually beneficial to operators and suppliers. Performance testing is not included in the field trials.

<a name="9.5.1.3"></a>
#### 9.5.1.3 Pre-trials activities

Prior to the comencement of any field trials, the Anuket CNTT community will define an operational plan, secure resources, and provide all designated contact information required to support trial participants.  As the results of the trails may produce data and information that could be considered sensitive by participants, Anuket CNTT will establish standard data set requirements and secure collection methods to ensure participant privacy protection.

<a name="9.5.1.4"></a>
#### 9.5.1.4 Expectations of Trials Participants

Trials participants will be expected to commit to establishing an RA-1 compliant NFVI, in whatever manner best suited to the participant. The first step is for the participant to secure appropriate environment space from pre-existing space, newly built space or securing LaaS.  The environment can exist in any mix of participant owned, private or community hardware infrastructure.

Second, the participant will build/setup/configure the environment space using their preferred method. This can include the use of a cookbook, automated install, and/or build from RA-1/RI-1 requirements and specifications. Anuket CNTT [RI-1 Chapter 3](../ref-impl/cntt-ri/chapters/chapter03.md ) documentation provides the matching RI-1 requirements for the build.

<a name="9.5.1.5"></a>
#### 9.5.1.5 Expectation 2: Execute the RC-1 Test suite

Anuket CNTT will provide the participants with the community RC-1 Test suite, found at this Link: https://github.com/cntt-n/Anuket CNTT/blob/master/doc/ref_impl/cntt-ri/chapters/chapter04.md. The participants will execute test cases per instructions and record the quantitative results.

Test case suite should be executed successfully at least three (3) times, because this number represents the recommended number of test suite runs to eliminate false positives in results.  A triage process will be used to determine and manage root cause analysis of any failures encountered. If the failures are determined to be issues with the participant’s VI, Anuket CNTT will convey the issues to the RI work stream and make available SMEs to assist the participant in resolving the issues. When failures are deemed to be caused by an issue or gap in the RA/RI/RC, the community will work to determine the resolution, and modify the RA/RI/RC accordingly.

Once the test case suite execution is successful for 3 consecutive iterations, the participant will provide the data of all iterations (both successful and unsuccessful) to Anuket CNTT based on participant privacy expectations (See Expectation #4)

<a name="9.5.1.6"></a>
#### 9.5.1.6 Expectation #3: The Qualitative Survey

At the conclusion of the Test Case iterations, the participant will be asked to complete a qualitative survey of their experience. This survey will be used to measure the feasibility, utility, and effectiveness of the RI-1 specifications, installation/configuration methods and RC-1 Test case efficacy. The survey will be in an Agile User Story format. The Table below provides an example of the survey questions:

<p align="center"><img src="../figures/Table 1-1.png" alt="Qualitative Survey" title="Survey/Questionnaire example" width="85%"/></p>
<p align="center"><b>Table 1:</b> Survey/Questionnaire example</p>


<a name="9.5.1.7"></a>
#### 9.5.1.7 Expectation 4: Providing Trials Results

As a community, Anuket CNTT is concerned with the privacy of participant data. Anuket CNTT abides by the LFN anti-trust policies ( https://www.linuxfoundation.org/antitrust-policy/ ) and the LFN Privacy Policy ( https://www.linuxfoundation.org/privacy/ ). As discussed in the Pre-trials activity section of the document, data generated by the trials will be secured to protect participant privacy. Additionally, should participants have concerns regarding the data they generate from the trials, Anuket CNTT will either work with the participant to eliminate their concerns, honor instructions from the participant on limitations to the data use, or agree to exclude that participant’s data from the analysis.

<a name="9.5.1.8"></a>
#### 9.5.1.8 Conclusion: Final Deliverable - End-of-Trial Report

Upon completion of field trials, Anuket CNTT write an End of Trial Report which summarizes the overall conclusions based on the evaluation.  The report will include:

1.	Successes: What activities went well both generally and specifically? How did it compare to past or alternative results?
2.	Challenges: What did not go well overall? What impact could these challenges have on future community adoption?
3.	Discoveries: What are key discoveries/strategic learnings about any of the Anuket CNTT approaches or methods? Other?
4.	Decisions and Recommendations: Identification of the key decisions made and list of what corrective actions shall be taken. What shoud be changed, enhanced, maintained, or discontinued?
5.	Next Steps: Indication of proposed steps and activities to be undertaken by the community to further the objectives of the Anuket CNTT work group.

### 9.5.2 Anuket CNTT Field Trials Approach 

<a name="9.5.2.5"></a>
#### 9.5.2.5 Key Expectations and Assumptions

1)	Expectation: Through healthy feedback from suppliers, Anuket CNTT will exit the trial with either validation of VI-1 and RC-1 or a set of actions to close gaps.
2)	Expectation: Post trial and gap closure, the community will define a badging process that is mutually beneficial to operators and suppliers. 
3)	Assumption: Performance testing is not in field trial.

<a name="9.5.2.6"></a>
### 9.5.2.6 Overview: Stages of Field Trial

The following diagram the key components and flow of activities, actions, and deliverables to be undertaken during the trial. Details of each component are provided in this document.

<p align="center"><img src="../figures/field_trials.png" alt="Anuket CNTT Field Trial Approach" title="Field Trial Approach" width="85%"/></p>
<p align="center"><b>Figure 3:</b> Field Trial Approach</p>

<a name="9.5.2.7"></a>
#### Success Indicators

1) Agreement secured on the use of trials results data, including:
a.	Level of data detail required to validate the results
b.	Acceptable data values indicating valid results
c.	Level of data detail that will be published

2) VI-1 Labs are successfully deployed in all target environments
* Vendor (NFVI, VNF, VIM, 3rd Party)
*	Community (OPNFV)
*	LaaS (e.g. UNH)

3) Engaged vendors successfully configure their VI and run the RC-1 test suite and are able to provide expert feedback

4) Engaged vendors are able to validate that they can instantiate and run rudimentary validation of VNF functionality on more than one conformant cloud infrastructure (NFVI)

<a name="9.5.2.7"></a>
### 9.5.2.7 Initiation 

<a name="9.5.2.7.1"></a>
#### 9.5.2.7.1 Objectives of RI-1/RC-1 Trials

The object is to quantitively and qualitatively assess and evaluate the following Anuket CNTT requirements, methods, and support processes:
* RI-1 Specifications
*	VI-1 implementation support methods ( i.e. cookbooks, installation manuals, how to guides etc.)
* RC-1 Test Suite 
* TC Traceability
* Test Pass Criteria
* Benchmark Data
* Other criteria to be determined at commencment or during the execution of the trial

Overall, feedback from the trials and issues and gaps found shall be used to enhance and improve the Anuket CNTT approach. Enhancements to future releases will/shall be identified accordingly.

<a name="9.5.2.7.2"></a>
#### 9.5.2.7.2 Trial Participant Interaction with the Community

The focus of the field trials is on the test suites and Anuket CNTT methods, not on the systems under test. A process is being developed to identify issues and gaps and managing how they are reported.

Anuket CNTT will work very closely with field trial partners (NFVI vendors, VNF vendors, or system integrators) and agree on labs that will be used for the trial. Anuket CNTT will take all necessary measures to protect the intellectual property rights (IP rights) for all partners involved in those trials. All Reports and findings will be vetted carefully and only published after being approved by all parties concerned. No test results or records will be kept in any public records without the consent of the participants.

The targeted repositories for this information are:

Anuket CNTT GitHub

*  GitHub Code
  
*  GitHub Projects
  
*  GitHub Issues
  
OPNFV 

*  (Where?)

<a name="9.5.2.7.3"></a>
#### 9.5.2.7.3 Test Case Identification

Specific test cases for the field trials will be documented and provided to the participants based upon the Anuket CNTT RI-1 and RC-1 work streams requirements. The technical testing methods, procedures and documentation shall be provided by these work streams. 

<a name="9.5.2.7.4"></a>
#### 9.5.2.7.4 Vendor Solicitation/Commitment

Vendor members will be solicited for participation in the trials. The vendors will be required to commit fully to the assessment and evaluation  processes. As previously mentioned, additional discussion is needed to define what results data and at what level of detail is acceptable to be shared.

<a name="9.5.2.7.5"></a>
#### 9.5.2.7.5 Deliverable

The Initiate Field Trial Stage will deliver execution and assessment plans including: 

* A high-level check list of the tasks each participant will need to complete shall be provided.  
* The plan will contain all the key milestones and activities the participants will expected to perform. 

<a name="9.5.2.8"></a>
### 9.5.2.8 Execution Stage

<a name="9.5.2.8.1"></a>
#### 9.5.2.8.1 Objectives of the Execute Stage

The objective of Execute Stage is participants implementing field trials tasks and record/assess outcomes Anuket CNTT will assemble the Trials team to fully develop the action plan including resource assignments, materials requirements, and timelines. 

Activities include the deployment and configuration of VI and execution of the RC-1 test cases. Vendor community members that commit to the trials will build/setup/prep labs for the trials per the instructions:

1.	Secure appropriate environment space (pre-existing, new build, LaaS)

2.	VI per published RI-1 Specifications  

3.	RC-1 Test suite will be provided to the participants
   
4. Trial Participants ensure a complete understanding of the test suite actions and expected outcomes.

<a name="9.5.2.8.2"></a>
#### 9.5.2.8.2 Running the Field Trial

The field trial will run the Test Suite for 3 Iterations. For each iteration:

*	Vendor RC-1 test results are documented. Vendor provide feedback to Anuket CNTT
*	OPNVF RC-1 test results are documented. OPNFV provides feedback to Anuket CNTT 

The Community shall review Issues/Gaps during the evaluate stage and do one of the following:

*	Accept the Issue/Gap, and accordingly modify the RI/RC 
*	Not-Accept the Issue/Gap and document the condition of non-conformance while maintaining the privacy of participants

<a name="9.5.6.1"></a>
#### 9.5.6.1 Resources and Roles

Anuket CNTT will staff the plan by soliciting volunteers from the participants. The list below is suggested list of roles to be staffed:

*	Overall Field Trial Lead
*	Technical Field Trial Steering Lead 
*	Vendor lead from each supplier
*	SME(s) for RC1 supporting suppliers
*	SME(s) for RI1 supporting suppliers
*	OPNVF lead for RI1/RC1
*	Other support roles such as Governance, technical writers, etc.

The participants that volunteer for the roles will be expected to provide the appropriate amount of time to support the trials initiative.

<a name="9.5.2.8.4"></a>
#### 9.5.2.8.4 Deliverables

The deliverables of the execute stage will be: 

* Implemented Participant RA-1 Labs which have been tested.
* RC-1 Test cases are run.

<a name="9.5.2.9"></a>
### 9.5.2.9 Assessment

The Assess stage shall utilize data collected during the execute stage. Participants will assess their experience using the methods used by Anuket CNTT accordingly to quantitatively and or qualitatively measure:

#### Required Assessments

* VI Implementation methods and procedures (cookbook, etc) 
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

OPNFV will also assess their experience of the methods used by Anuket CNTT to assess the following operational areas:
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

* Feedback is provided from the participants on their outcomes to Anuket CNTT.
* Completed Questionnaire and test case results (Participant and OPNFV)

<a name="9.5.2.10"></a>
### 9.5.2.10 Evaluation Stage

Proving the ‘right’ value to the operator and vendor community is ultimately what will ensure adoption of Anuket CNTT requirements. These field trials are intended to verify and validate the requirements and  methods developed by Anuket CNTT so that adjustments can be made to ensure the intended value is being delivered. 

Anuket CNTT shall evaluate all feedback and test results to understand whether Anuket CNTT methods and measures are meeting intended objectives. If a method or measure is not meeting its intended purpose, it shall be identified as a gap or an issue for resolution. Determinations if and when adjustments or adaptations are needed shall be made to by the Anuket CNTT community.


<a name="9.5.2.10.1"></a>
#### 9.5.2.10.1 Deliverables

All identified gaps and issues shall be captured in the Anuket CNTT GitHub repository. Decisions and determinations will be captured and logged accordingly.
   
<a name="9.5.2.11"></a>
### 9.5.2.11 Closeout Stage

To close out the Field Trial, Anuket CNTT shall summarize its evaluation of the Field Trial and actions to be taken to address any adaption needed.

<a name="9.5.2.11.1"></a>
#### 9.5.2.11.1 Final Deliverable - End-of-Trial Report

Upon completion of field trials, Anuket CNTT shall develop an End of Trial Report which summarizes the overall conclusions based on the evaluation, to include:
   *	Successes - What went activities well both generally or specifically? How did it compare to the past or alternative results?   
   * Challenges - What didn’t go well overall? What impact could these challenges have to adoption?
   *	Discoveries - What are key discoveries/strategic learnings about any Anuket CNTT approaches or methods? Other?
   *	Decisions and Recommendations - Identification of key decisions made and list of what corrective actions shall be taken. What to enhance, maintain, or discontinue?
   *	Next Steps - Indication of proposed steps and activities to be undertaken by the community
