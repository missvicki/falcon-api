import falcon

from api import resources

application = falcon.App()

transactions = resources.Resource()

application.add_route('/transactions/all/{merchantId}/{currency}', transactions)
application.add_route('/transactions/all/{merchantId}/{currency}/{start_date}', transactions)
application.add_route('/transactions/all/{merchantId}/{currency}/{start_date}/{end_date}', transactions)
