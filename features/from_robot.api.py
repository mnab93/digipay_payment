from robot.api.deco import keyword
from apis.payment_api import PaymentAPI
from libs.validation_library import validate_bnpl_options, validate_clickability, validate_required_fields, validate_status

class PaymentSteps:

    def __init__(self, base_url):
        self.api = PaymentAPI(base_url)
        self.response = None

    @keyword("I fetch payment methods for cell number")
    def fetch_payment_methods(self, cell):
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