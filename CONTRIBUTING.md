# Contribution

## Table of Contents
* [Labels](#labels)
* [Issues & Labels](#issues)
* [Pull Requests](#prs)
* [Pull Requests Approval Process](#approvals)
* [Idle Pull Requests Policy](#idle)
* [Unresolved Pull Requests Policy](#unresolved)

<a name="labels"></a>
### Labels
Following labels should be correctly used for all issues and PRs to indicate the status of them and to assist automation pipelines to correctly apply CNTT processes.

  - **Roadmap Item**: This label applies to both issues and PRs to indicate that the issue/PR is for a roadmap item for an upcoming release.
  - **Fix needed**: This label applies to both issues and PRs to indicate that the issue/PR is to fix an existing bug.
  - **Backlog**: This label applies to issues only to indicate that the issue is to be added to a backlog of features for future releases (to be considered during technical steering meeting).
  - **Workstream Name**: This label applies to both issues and PRs to indicate which project the issue/PR is targeting.
  - **Chapter Number**: This label applies to PRs (and optionally to issues) to indicate which chapter the PR is targeting.
  - **General**: This label applies to both issues and PRs to indicate that this issue/PR is not corresponding to any particular chapter/file.
  - **Major/Minor**: This label applies to both issues and PRs to indicate if the issue/PR is addressing a major or minor change. 
  - **WIP**: This label applies to PRs to indicate that this PR is still being developed and no reviews/approvals are expected.
  - **Enhancement**: This label applies to both issues and PRs to indicate that the issue/Pr is proposing an Enhancement.
  - **Returned**: This label applies to both issues and PRs to indicate that the issue/PR has been sent back to authoer (e.g. more information needed, not a high priority, no longer valid, etc).
  - **Idle**: This label will be **automatically** applied (by a GitHub work flow or by TSC Leads) to both issues/PRs to indicate that no activity has been observed on the issue/PR for some determined time frame. This triggers an action to close the issue/PR.
  - **Unresolved**: This label will be **automatically** applied to PRs to indicate that no consensus has been reached on the PR. This triggers an action to resolve the PR by the TSC.
  - **Forced**: This label will be **automatically** applied to PRs to indicate that the PR has been merged without following the default process (due to reasons identified below)

<a name="issues"></a>
### Issues

- All issues must be clearly titled, described, and tagged with the right labels when created.
  - Title needs to be in the following format [WSx Chx].
    - WSx: The name of the work stream it is targeting.
    - Chx: The name of the chapter it is targeting (if applicable).
- Issues should be correctly set with the correct Project and Milestone.
  - Milestone = the upcoming release related to the issue/PR.
  - Project = Work stream.
- Workstream Leads has the sole responsibility to assign issues to individuals to address them.
- **self assignment** are NOT recommended. Contributors may ask WSL (via comment or others) to get the issue assigned to them if they would like to work on it.
  - This is to make sure items are worked based on priorities and right reasoning.
- WSL may label an issue as "**Returned**" to request further information or to decide not to work on it.

<a name="prs"></a>
### Pull Requests
- PRs must only be created when there is an issue present and a decision to create a PR is made. A PR must reference the issue it is resolving into the description field.
  - using GitHub predefined keyword "**Fixes Issue#**" will automatically close the issue which the PR is resolving when it is merged.
- A PR for an issues must only be created by the contributor assigned to the issue by the respective WSL.
- One person only is allowed to edit a given PR unless given permission to other contributor to contribute directly into the PR.
- A PR is recommended to only create/modify content within the scope of a single workstream.
- A PR should only add/change content related to the issue associated with the PR.
- Comments/sub-Conversations within a PR may only be marked Resolved by:
  - A) The originator of the sub-conversation. 
  - B) The relevant WSL or 
  - C) An automated timeout of 48hrs when there has been no additional comments after an update is posted to resolve the sub-thread. 
  - **The person responding to a sub-conversation shall not mark it as Resolved**.
- Explicitly communicate all changes to existing PRs shall be made through subsequent commits. 
  - **Do not modify an existing commit, create separate commits under the same PR**.
  - PRs will be merged using "Squash and Merge" to enforce a linear commit history.

<a name="approvals"></a>
### Pull Requests Approval Process

- Once a PR is created, it needs to get the following approvals before it is merged into master.
  - From at least one of contributor for that workstream
    - Approvers should be distributed equally among operators and vendors.
  - From WSL (to make sure consensus is reached).
  - WSL can request additional approvals reviews.
    - Recommendation is to use 4 approvals for complex PRs.
  - 2 business days cool off period should be applied before Final approval.
  - Final Approval by TSL (to make sure process is followed)
- Only One approval will be counted per each organization for a given PR.
- The selection of which contributor to approve a PR is made by the WSL and should take those factors into consideration:
  - Contributor needs to be actively discussing the PR to be selected for approval.
- PRs will be merged automatically online by the TSL once consensus is reached and all approvals are received. 
- If WSL is the person who is creating the PR, They need to request an alternate approver, preferably from the co-lead or from the contributors list.

<p align="right"><img src="artefacts//figures/approval_process.png" alt="scope" title="Scope" width="100%"/></p>
<p align="center"><b>Figure 1:</b> Approval Process</p>

<a name="idle"></a>
### Idle Pull Requests Policy

Pull Requests will be automatically labled as "**Idle**" when:
- No engagement/activity (content, reviews, conversations) from author, reviewers and workstream contributors on non-merge ready PRs for 15 calendar days.
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
  
