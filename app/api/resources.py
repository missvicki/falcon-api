import json

import falcon

from datetime import datetime

class Resource:

    def on_get(self, req, resp, merchantId=None, currency=None, start_date=None, end_date=None):

        data = {
          "transactions":[
            {
              "merchantId": "1234567890",
              "currency": "GBP",
              "datetime": "2021-08-22T00:00:00Z",
              "amount":97,
              "name":"Ilias"
            },
            {
              "merchantId": "1234567891",
              "currency": "GBP",
              "datetime": "2021-08-20T00:00:00Z",
              "amount":99,
              "name":"Catherine"
            },
            {
              "merchantId": "1234567890",
              "currency": "GBP",
              "datetime": "2021-08-20T00:00:00Z",
              "amount":90,
              "name":"Jim"
            },
            {
              "merchantId": "1234567890",
              "currency": "GBP",
              "datetime": "2021-08-20T00:00:00Z",
              "amount":72,
              "name":"Alex"
            }
          ]
        }


        # Create a JSON representation of the resource
        if merchantId and currency and not end_date and not start_date:
          trans = list(filter(lambda x: x['merchantId'] == merchantId and x['currency'] == currency, data['transactions']))
          result = {
            "valueTransactions": {"amount": sum(x['amount'] for x in trans), "currency": currency},
            "volumeTransactions": len(trans)
          }
          resp.text = json.dumps(result)

        if merchantId and currency and not end_date and start_date:
          startDate = datetime.strptime(start_date,"%Y-%m-%d").strftime("%Y-%m-%dT%H:%M:%SZ")
          trans = list(filter(lambda x: x['merchantId'] == merchantId and x['currency'] == currency and x['datetime'] >= start_date, data['transactions']))
          result = {
            "valueTransactions": {"amount": sum(x['amount'] for x in trans), "currency": currency},
            "volumeTransactions": len(trans)
          }
          resp.text = json.dumps(result)
        
        if merchantId and currency and end_date and start_date:
          startDate = datetime.strptime(start_date,"%Y-%m-%d").strftime("%Y-%m-%dT%H:%M:%SZ")
          endDate = datetime.strptime(end_date,"%Y-%m-%d").strftime("%Y-%m-%dT%H:%M:%SZ")
          trans = list(filter(lambda x: x['merchantId'] == merchantId and x['currency'] == currency and 
            x['datetime'] >= startDate and x['datetime'] <= endDate, data['transactions']))
          result = {
            "valueTransactions": {"amount": sum(x['amount'] for x in trans), "currency": currency},
            "volumeTransactions": len(trans)
          }
          resp.text = json.dumps(result)
        
        resp.status = falcon.HTTP_200
