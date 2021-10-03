# Transaction API with Falcon

Get started
- git clone this repo
- Install a virtual env `python3 -m virtualenv venv`
- Activate the environment

How to run:
- `cd app`
- `gunicorn --reload transaction:application --timeout 600`
- `curl -XGET localhost:8000/transactions/all/merchantId/currency`

To run tests:
- `export PYTHONPATH=. pytest`
- `cd app` and then run `pytest tests`

