# Payment API Automation Suite

## Description
This suite validates the `/payment/` endpoint for a marketplace checkout. It covers:
- Schema validation
- Method clickability rules
- BNPL option eligibility rules
- Negative scenarios: missing fields, wrong types, non-200 status

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
##




Digipay Payment Automation
Overview

This project provides automated testing for Digipay's payment methods API.
It validates scenarios such as BNPL availability, required fields, clickability, wallet rules, and response statuses.

Features

Fetch payment methods for different cell numbers.

Validate API response status.

Ensure all required fields exist in the response.

Check clickability and wallet rules.

Test BNPL (Buy Now, Pay Later) scenarios: blocked, insufficient credit, non-active options, default invalid option.

Modular and reusable steps using Robot Framework keywords.

Installation
Prerequisites

Python 3.10+

Virtual environment (venv)

pip package manager

Setup
# Clone the repository
git clone <repository_url>
cd digipay_payment

# Create virtual environment
python -m venv .venv
# Activate venv (Windows)
.venv\Scripts\activate
# Activate venv (Linux/macOS)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Usage

Run Robot Framework tests using:

# From the project root
robot --pythonpath . -d results features


--pythonpath . ensures your custom libraries in steps/ and libs/ are discoverable.

Results are stored in the results/ folder (output.xml, log.html, report.html).

Project Structure
digipay_payment/
│
├─ features/                  # Robot Framework test cases
│   └─ payment_methods.robot
│
├─ steps/                     # Python Robot keywords
│   └─ payment_steps.py
│
├─ apis/                      # API client implementations
│   └─ payment_api.py
│
├─ libs/                      # Validation and helper libraries
│   └─ validation_library.py
│
├─ results/                   # Robot test outputs
├─ requirements.txt           # Python dependencies
└─ README.md

Running Tests

Set the API scenario using the API scenario is <scenario_name> keyword.

Fetch payment methods with I fetch payment methods for cell number <cell_number>.

Validate responses using response status should be <status>, all required fields must exist, clickability and wallet rules must pass, BNPL options must satisfy all rules.

Limitations

Tests depend on a running API at http://127.0.0.1:8080.

Some scenarios may fail if API responses are incomplete or malformed.

Only the payment_methods feature is currently implemented.

Contributing

Contributions are welcome! You can:

Add new test scenarios or features.

Improve validation logic in libs/validation_library.py.

Refactor keywords in steps/payment_steps.py for reusability.