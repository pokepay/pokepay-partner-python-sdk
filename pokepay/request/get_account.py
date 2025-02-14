# DO NOT EDIT: File is generated by code generator.

from pokepay.request.request import PokepayRequest
from pokepay.response.account_detail import AccountDetail


class GetAccount(PokepayRequest):
    def __init__(self, account_id):
        self.path = "/accounts" + "/" + account_id
        self.method = "GET"
        self.body_params = {}
        
        if 'start' in self.body_params:
            self.body_params['from'] = self.body_params.pop('start')
        self.response_class = AccountDetail
