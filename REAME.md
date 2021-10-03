# Transaction API with Falcon

How to run:
- `gunicorn --reload transaction:application --timeout 600`
- `curl -XGET localhost:8000/transactions/all/merchantId/currency/`
