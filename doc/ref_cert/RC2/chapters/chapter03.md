[<< Back](../)

# 3. Kubernetes Test Cases and Traceability to CNTT Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Introduction

All of the requirements for RC2 have been defined in the Reference Model (RM) and Reference Architecture (RA2). The scope of this chapter is to identify and list down test cases based on these requirements. Users of this chapter will be able to use it to determine which test cases they must run in order to test compliance with the requirements. This will enable traceability between the test cases and requirements. They should be able to clearly see which requirements are covered by which tests and the mapping from a specific test result (pass or fail) to a requirement. Each requirement may have one or more test case associated with it.

### Goals
- Clear mapping between requirements and test results
- Provide a stable set of point-in-time requirements and tests to achieve conformance
- Enable clear tracability with versioning to know which requirements have and haven't been covered and track changes over time
- Clickable links from test cases to requirements
- One or more tests for every MUST requirement

### Non-Goals
- Defining any requirements
- Providing coverage for non-testable requirements

### Definitions
*must*: Test Cases that are marked as must are considered mandatory and must pass successfully

*should*: Test Cases that are marked as should are expected to be fulfilled by the cloud infrastructure but it is up to each service provider whether to accept a cloud infrastructure that is not reflecting on any of those requirements. The same applies to should not.

*may*: Test cases that are marked as may are considered optional. The same applies to may not.
