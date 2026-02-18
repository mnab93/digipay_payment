from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_PATH = os.path.join("testdata", "sample_responses")

scenario_map = {
    "1": "happy_path.json",
    "2": "bnpl_blocked.json",
    "3": "insufficient_credit.json",
    "4": "non_active_option.json",
    "5": "default_option_invalid.json",
    "6": "missing_required_field.json",
    "7": "wrong_type.json",
    "8": "non_success.json"
}

@app.route("/payment/", methods=["GET"])
def payment():
    cell = request.args.get("CellNumber")
    scenario_digit = cell[-1] if cell else "1"
    filename = scenario_map.get(scenario_digit, "non_success.json")
    filepath = os.path.join(DATA_PATH, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=8080)
