import falcon
from falcon import testing
import pytest
import json
import msgpack


from app.transaction import application


@pytest.fixture
def client():
    return testing.TestClient(application)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_list_transactions(client):
    data = {
            "transactions":[
                {
                "merchantId": "9078",
                "currency": "GBP",
                "datetime": "2021-08-22T00:00:00Z",
                "amount":97,
                "name":"Ilias"
                },
                {
                "merchantId": "9078",
                "currency": "GBP",
                "datetime": "2021-08-20T00:00:00Z",
                "amount":99,
                "name":"Catherine"
                }
            ]
    }
    response = client.simulate_request(method='GET', path='/transactions/all/9078/GBP/2021-08-01', body=json.dumps(data))
    assert response.status == falcon.HTTP_OK