import requests

class PaymentAPI:

    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_payment_methods(self, cell_number):
        response = requests.get(
            f"{self.base_url}/payment/",
            params={"CellNumber": cell_number}
        )
        return response.json()

