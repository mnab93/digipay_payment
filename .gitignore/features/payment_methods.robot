*** Settings ***
Library  steps/payment_steps.py  ${BASE_URL}  
Library  Collections    
Library  OperatingSystem
Library  RequestsLibrary 
Library  BuiltIn
Library  String  

*** Variables ***
${BASE_URL}    http://127.0.0.1:8080



*** Test Cases ***

S1 Happy Path
    Given the API scenario is    happy_path
    When I fetch payment methods for cell number    09100000000
    Then response status should be    200
    And required fields must exist
    And method clickability rules must pass
    And BNPL option rules must pass

S2 BNPL Blocked
    Given the API scenario is    bnpl_blocked
    When I fetch payment methods for cell number    09000000000
    Then BNPL must not be selectable

S3 Insufficient Credit
    Given the API scenario is    insufficient_credit
    When I fetch payment methods for cell number    09000000001
    Then option eligibility rule R5 must fail

S4 Non Active Option
    Given the API scenario is    non_active_option
    When I fetch payment methods for cell number    09000000002
    Then option eligibility rule R5 must fail

S5 Default Option Invalid
    Given the API scenario is    default_option_invalid
    When I fetch payment methods for cell number    09000000003
    Then default rule R6 must fail

S6 Missing Required Field
    Given the API scenario is    missing_required_field
    When I fetch payment methods for cell number    09000000004
    Then required field validation must fail

S7 Wrong Type
    Given the API scenario is    wrong_type
    When I fetch payment methods for cell number    09000000005
    Then type validation must fail

S8 Non Success
    Given the API scenario is    non_success
    When I fetch payment methods for cell number    0900000006
    Then fail fast due to non success status
