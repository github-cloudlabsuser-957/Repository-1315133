

PROMPT_BDD_SCENARIOS = """
    Write BDD TEST SCENARIOS for given BUSINESS REQUIREMENT DOCUMENT
    and
    also please include a USER JOURNEY in all these scenarios
    and
    include all the POSITIVE and NEGATIVE scenarios 
    and 
    also use tables if required for a data to be supplied in this particular bdd scenario.
    
follow below instructions while generating the response:

each scenario can be describe using below format
        <b>{scenario}{number}</b>
        <li>{User Journey}</li>
        <li>{Positive Scenarios}</li>
        <li>{Negative Scenarios}</li>
        
    
    BUSINESS REQUIREMENT DOCUMENT is here - 
"""

PROMPT_TEST_CASES = """
    Write Positive and Negative TEST CASES for below given User Stories along with Acceptance Criteria 
    where
    each user story starts with "'As an" and having acceptance criteria starts with "Given"
    and
    each user story should suggest scenarios
    and
    please generate 5 Test Cases for each acceptance criteria starts with "Given", 
    and
    each test case should contain all important components - Test case ID, Test steps, Test case Description, Test scenario and Expected Result 
    and 
    Avoid test case repetition
    and 
    Use continues sequence numbers for all the test cases.
  .
        
follow below instructions while generating the response:

each test case can be describe using below format
        <b>{Test case ID}</b>
        <li>{Test Case Description}</li>
        <li>{Test Steps}</li>
        <li>{Test cases}</li>
        <li>{Expected Result}</li>

    User Stories along with Acceptance Criteria is here - 
"""

PROMPT_TEST_SCRIPTS = """
    Write selenium scripts in python for the test cases 
    where
    each testcases starts with "'Test Case" or "'TC'".
    Test cases is here  - 
"""

PROMPT_TEST_SCRIPTS2 = """
    Write selenium scripts in python and c# for the test cases 
    where
    each testcases starts with "'Test Case" or "'TC'".
    User Stories along with Test cases is here - 
"""
