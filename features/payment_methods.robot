*** Settings ***

Library    steps.payment_steps.PaymentSteps
Library    Collections
Library    OperatingSystem
Library    RequestsLibrary
Library    BuiltIn
Library    String

*** Test Cases ***

S1 Happy Path
    the API scenario is    happy_path
    I fetch payment methods for cell number    09100000000
    response status should be    200
    all required fields must exist
    clickability and wallet rules must pass
    BNPL options must satisfy all rules

S2 BNPL Blocked
    the API scenario is    bnpl_blocked
    I fetch payment methods for cell number    09000000000
    BNPL options must satisfy all rules

S3 Insufficient Credit
    the API scenario is    insufficient_credit
    I fetch payment methods for cell number    09000000001
    BNPL options must satisfy all rules

S4 Non Active Option
    the API scenario is    non_active_option
    I fetch payment methods for cell number    09000000002
    BNPL options must satisfy all rules

S5 Default Option Invalid
    the API scenario is    default_option_invalid
    I fetch payment methods for cell number    09000000003
    BNPL options must satisfy all rules

S6 Missing Required Field
    the API scenario is    missing_required_field
    I fetch payment methods for cell number    09000000004
    all required fields must exist

S7 Wrong Type
    the API scenario is    wrong_type
    I fetch payment methods for cell number    09000000005
    all required fields must exist

S8 Non Success
    the API scenario is    non_success
    I fetch payment methods for cell number    09000000006
    response status should be    500
