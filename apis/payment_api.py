import requests

class PaymentAPI:

    def __init__(self, base_url, scenario):
        self.base_url = base_url
        self.scenario = scenario

    def fetch_payment_methods(self, cell_number):
        response = requests.get(
            f"{self.base_url}/payment/",
            params={
                "CellNumber": cell_number,
                "scenario": self.scenario
            }
        )

        try:
            body = response.json()
        except ValueError:
            body = None

        return {
            "status_code": response.status_code,
            "body": body,
            "raw_text": response.text
        }
