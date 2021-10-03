# Transaction API with Falcon

How to run:
- `gunicorn --reload transaction:application --timeout 600`
- `curl -XGET localhost:8000/transactions/all/merchantId/currency`

To run tests:
- `export PYTHONPATH=. pytest`
- cd into the app folder and then run `pytest tests`

