# Contribution

## Table of Contents
* [Permission levels](#permissions)
* [Labels](#labels)
* [Issues & Labels](#issues)
* [Pull Requests](#prs)
* [Pull Requests Approval Process](#approvals)
* [Idle Pull Requests Policy](#idle)
* [Unresolved Pull Requests Policy](#unresolved)

This document is an extension to the generic [Anuket Project Operations and Procedures](https://wiki.anuket.io/display/HOME/Anuket+Project+Operations+and+Procedures) and describes contribution rules to the Anuket specifications, that are the set of documents maintained in this repository. 

<a name="permissions"></a>
### Permission levels

There are different permissions (levels) available for contributing into the Anuket specifications:
- **Outside Collaborators**: This includes general public. 
  - Outside collaborators can create issues and add comments to issues and Pull Requests.
- **Read, Triage, Write, and Maintain** Permissions, which are explained in [here](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization), will be assigned as follows:
  - **Read** will be assigned to those who want to create issues, join the discussions, receive notifications, and provide feedback.
  - **Triage** will be assigned to active contributors who create issues, pull requests and review them.
  - **Writes** will be assigned to sub-project Co-Leads to allow them to manage issues and pull request, approve them and be auto requested for review.
  - **Maintain** will be assigned to sub-project Leads to allow them to merge PRs into the repository.

<a name="labels"></a>
### Labels

Every Issue and PR should be tagged with one or more of the following labels to indicate their status and for the automation pipelines to apply the correct Anuket processes.

  - **Backlog**: The Issue will be addressed in future releases..
  - **Major/Minor**: The Issue or PR concerns a major or minor change.. 
  - **WIP**: The PR is still under development, no reviews/approvals are expected yet.
     - PRs can also be created as "Draft" to indicate that the PR is in progress.
  - **Returned**: The issue/PR has been sent back to author (e.g. more information needed, not a high priority, no longer valid, etc). Only WSL or TSL can tag an issue/PR as Returned.
  - **Idle**: This label will be **automatically** applied (by a GitHub work flow or by WSL/TS Leads) to both issues/PRs to indicate that no activity has been observed on the issue/PR for some determined time frame. This triggers an action to close the issue/PR.
  - **Unresolved**: This label will be **automatically** applied to PRs to indicate that no consensus has been reached on the PR. This triggers an action to resolve the PR by the TSC.
  - **Forced**: This label will be **automatically** applied to PRs to indicate that the PR has been merged without following the default process (due to reasons identified below)

<a name="issues"></a>
### Issues

- Title needs to be in the following format [SPx Chx] (if applicable).
  - SPx: The name of the sub-project it is targeting.
  - Chx: The name of the chapter it is targeting (if applicable).
- Upon Creation, Issues must be correctly set with the correct **Project Name**. 
  - Project Name = Sub-project name.
- Issues must be correctly set with the right labels and Milestone by the sub-project lead.
  - Relevant Milestone for the upcoming release (M1 - M6).
- Contributors can assign an unassigned issue to themselves if they would like to work on them
- Sub-project leads have the responsibility to assign stalling or priority issues to individuals to address them.
- Sub-project leads may label an issue as "**Returned**" to request further information or to decide not to work on it.

<a name="prs"></a>
### Pull Requests

- Minor editorial change PRs can be raised without a corresponding Issue, but must be labelled as "Minor". Otherwise, PRs must only be created when there is an issue present and a decision to create a PR is made. 
- A PR must reference the issue it is resolving in the description field.
   - using GitHub predefined keyword "Fixes Issue#" will automatically close the issue which the PR is resolving when it is merged.
- A PR for an issue must only be created by the contributor assigned to the issue (either by self assignment or by the respective sub-project lead).
- Only the person assigned ("assignee") to a PR may edit it. The normal process is for others to make suggests in "Comments" but not directly edit a PR unless the assignee has granted another contributor permission to contribute directly to the PR.
- A PR is recommended to only create/modify content within the scope of a single chapter in a single sub-project if possible.
- A PR should only add/change content related to the issue associated with the PR.
- Comments/sub-Conversations within a PR may only be marked Resolved by:
  - A) The originator of the sub-conversation. 
  - B) The relevant sub-project lead or 
  - C) An automated timeout of 1 week when there has been no additional comments after an update is posted to resolve the sub-thread. 
  - **The person responding to a sub-conversation shall not mark it as Resolved**.
- All changes to an existing PRs shall be made through subsequent commits. 
  - **Do not modify an existing commit, create separate commits under the same PR**.
  - After major changes to a PR reapproval is needed from all previous approvers
  - PRs will be merged using "Squash and Merge" to enforce a linear commit history.

<a name="approvals"></a>
### Pull Requests Approval Process

- Once a PR is created, it needs to get the following approvals before it is merged into master.
  - From at least three of contributors for that sub-project
    - Approvers should be distributed equally among operators and vendors.
  - From sub-project lead (to make sure consensus is reached).
  - Sub-project lead can request additional approvals reviews.
    - Recommendation is to use 4 approvals for complex PRs.
  - 2 business days waiting period should be applied before Final approval.
- The selection of which contributor to approve a PR is made by the sub-project lead and should take those factors into consideration:
  - Contributor needs to be actively discussing the PR to be selected for approval.
- PRs will be merged automatically online by the sub-project lead or other committers of the sub-projetc once consensus is reached and all approvals are received. 
  - Sub-projects should have an agreed set of committers who are trusted with merging rights to the sub-projects. [CODEOWNERS](CODEOWNERS) file should contain all the committers of the sub-projects including the sub-project lead.
- The person creating the PR cannot be an approver and should not be the person performing the merge.
- If a PR affects more than one sub-project or areas outside of the scope of the sub-projects the following approvals are needed:
  - From the sub-project leads of the affected sub-projects or if the PR affects no sub-projects at least 3 contributors active in 3 different sub-projects of Anuket specifications

<p align="right"><img src="artefacts/figures/pr-approval-process.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 1:</b> PR Approval Process</p>

<a name="idle"></a>
### Idle Pull Requests Policy

Pull Requests will be automatically labled as "**Idle**" when:
- No engagement/activity (content, reviews, conversations) from author, reviewers and sub-project contributors on non-merge ready PRs for 15 calendar days.
  - Personal holidays or public holidays will not be counted.
- One or more identified Reviewers (including WSL) are not providing feedback/resolutions or approving the Pull Request for more than 15 calender days.

Any Pull Requests that are labeled as "Idle" will be discussed during Technical Steering Meeting to take a decision on, such as:
- Close the PR and label it as "**Returned**".
- "**Force**" Merging of the PR without having full reviewers approvals due to their inactivity.

<a name="unresolved"></a>
### Unresolved Pull Requests Policy

Pull Requests will be automatically labled as "**Unresolved**" (by GitHub automation flow or a similar automation mechanism) when no consensus is reached during approval process.

Any Pull Requests that are labeled as "**Unresolved**" will be discussed during Technical Steering Comitee Meeting to take a decision on it by:
- Finding Common Grounds to come to consensus.
- Follow Governance Procedures to get consensus via voting mechanisms.


<!--
* [Contribution Guidelines](https://github.com/cntt-n/CNTT/wiki/Contribution-Guidelines)
* [Approval Process](https://github.com/cntt-n/CNTT/wiki/Approval-Process) 
-->
  
