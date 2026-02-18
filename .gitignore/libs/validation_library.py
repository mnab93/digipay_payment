def validate_status(response, expected_status):
    if response.get("status") != expected_status:
        raise AssertionError(f"Expected status {expected_status}, got {response.get('status')}")

def validate_required_fields(response):
    methods = response.get("payment_methods", [])
    for method in methods:
        for field in ["id", "type", "title", "is_clickable"]:
            if field not in method:
                raise AssertionError(f"Missing required field '{field}' in method {method.get('id', 'unknown')}")

def validate_clickability(response):
    for method in response.get("payment_methods", []):
        if method["type"] != "wallet" and method.get("is_wallet", False):
            raise AssertionError(f"Rule R3 violated: non-wallet method marked as wallet (method id {method['id']})")
        if not isinstance(method["is_clickable"], bool):
            raise AssertionError(f"is_clickable must be boolean (method id {method['id']})")

def validate_bnpl_options(response):
    for method in response.get("payment_methods", []):
        if method["type"] == "bnpl" and method.get("is_clickable", False):
            options = method.get("options", [])
            if options is None:
                raise AssertionError(f"Rule R4 violated: BNPL method {method['id']} missing options array")
            eligible = [o for o in options if o.get("is_active") and o.get("credit", 0) > 0]
            if eligible and sum(1 for o in eligible if o.get("is_default")) != 1:
                raise AssertionError(f"Rule R6 violated: BNPL method {method['id']} has invalid default option")
            for o in options:
                if o.get("price_type") not in ["CASH_PRICE", "CREDIT_PRICE"]:
                    raise AssertionError(f"Rule R7 violated: option {o.get('source_id')} invalid price_type")
