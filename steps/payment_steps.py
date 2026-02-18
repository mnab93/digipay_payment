from robot.api.deco import keyword
from apis.payment_api import PaymentAPI
from libs.validation_library import (
    validate_bnpl_options,
    validate_clickability,
    validate_required_fields,
    validate_status
)

class PaymentSteps:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        # مقدار پیش‌فرض Base URL از Variable فایل یا hardcode
        self.base_url = "http://127.0.0.1:8080"
        self.api = None
        self.scenario = None
        self.response = None

    @keyword("the API scenario is")
    def set_api_scenario(self, scenario_name):
        self.scenario = scenario_name
        self.api = PaymentAPI(self.base_url, scenario_name)

    @keyword("I fetch payment methods for cell number")
    def fetch_payment_methods(self, cell):
        if not self.api:
            raise RuntimeError("API scenario not set. Use 'the API scenario is' first.")
        self.response = self.api.fetch_payment_methods(cell)

    @keyword("response status should be")
    def response_status_should_be(self, expected_status=200):
        validate_status(self.response, expected_status)

    @keyword("all required fields must exist")
    def all_required_fields_must_exist(self):
        validate_required_fields(self.response)

    @keyword("clickability and wallet rules must pass")
    def clickability_and_wallet_rules_must_pass(self):
        validate_clickability(self.response)

    @keyword("BNPL options must satisfy all rules")
    def bnpl_options_must_satisfy_all_rules(self):
        validate_bnpl_options(self.response)