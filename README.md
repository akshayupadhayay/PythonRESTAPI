# PythonRESTAPI

![GitHub contributors](https://img.shields.io/github/contributors/akshayupadhayay/PythonRESTAPI?color=green)
![coverage](https://img.shields.io/badge/coverage-90%25-green)
![GitHub repo size](https://img.shields.io/github/repo-size/akshayupadhayay/PythonRESTAPI)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/akshayupadhayay/PythonRESTAPI?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/akshayupadhayay/PythonRESTAPI?color=yellow)
![GitHub forks](https://img.shields.io/github/forks/akshayupadhayay/PythonRESTAPI?style=social)

### Task 1

### Solution

**`1 -`** Before team can start working on test strategy, we need to write a long and detailed interface specification (the contract) and Implement the providing service according to the defined contract. Throughout this stage the QA can utilize the agile environment and discuss the complexities around the contract with the development team from both producer/consumers perspective.
Meanwhile QA can initiate by introducing Test pyramid framework (below in picture) to work upon the test strategy and later derive a detailed test plan from it. Drawing the guidelines from the framework the tests around API should be at least 20-30% of all tests.

<code><img height="300" src="https://github.com/akshayupadhayay/APITestStrategy/blob/master/testingpyramid.png"></code>


***We should start with Functional Testing, i.e., to ensure the API functions correctly as:***

- `to ensure that the implementation/REST contract is working correctly as expected and no bugs are found specially if it’s a customer-facing public API. Also, to make sure that endpoints are correctly named, that resources and their types correctly reflect the object model, that there is no missing functionality or duplicate functionality, and that relationships between resources are reflected in the API correctly.`

- `to ensure that the implementation is working as specified according to the requirements specification (which later on becomes our API documentation).`


**`2 -`** ***Once we have validated the API contract, it’s time to define test scenarios based on:***

- `Positive testing – with/without parameters`

- `Negative testing – valid/invalid inputs`

- `Security and Authorization testing – check authorized/unauthorized calls`

- `Performance testing – API response time and latency`

- `Load testing – determine system limits under load`

- `Stress testing – graceful failure under stress`

- `Integration testing – communication between APIs`


***From this QA can derive test actions per API request like:***

- `Verify correct HTTP status code`

- `Verify response payload`

- `Verify response headers`

- `Verify correct application state`

- `Verify basic performance sanity`

**`3 -`** ***A QA needs to define:***

- `What to test?`

- `How to test?`

- `And the test coverage as per business requirements`

It’s best to use common test design approaches (divide into submodules, boundary value analysis, equivalence partitioning, state transition testing, etc.)

***Once we know which endpoints your web service provides:***

- `Each collection endpoint needs to be tested`

- `At least one single resource endpoint needs to be tested for each resource type`

The API calls should be defined based on endpoints over Http methods like GET/POST/PUT/DELETE etc.
We can utilize Python <a href="https://github.com/psf/requests">Requests</a> HTTP library and pytest framework to write tests around our API under test.

Depending on the format of response payload, for example if JSON, we can utilize the built-in JSON decoder which comes with request library or use <a href="https://docs.python.org/3/library/json.html#module-json">JSON library</a> to load and dump (Deserialize and Serialize the obj) and extract meaningful value from the response Header and Body.

***So, using Request library and pytest, the automation tests can be built around the API as:***

- `Check HTTP status codes for all responses`

- `Check if the value of the response content type header correctly identifies that the response body is in JSON format`

- `Extract required information from the header, which in case is a dictionary (key-value pair)`

- `Check response Body is not empty and break response to write test around it using Asserts.`


**Note:** QA can utilize open source reporting tools inside the unit tests upon success/failure to extract the information from the response and report the cumulative metrics to the dashboard for stakeholders. Always report the latency, response time, timestamps, response size, content type and many more meaningful information extracted from the responses. This in turn helps the team not to dig the databases to get a collective insight of the responses at any later stage.








