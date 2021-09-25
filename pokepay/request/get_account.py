# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.request.request import PokepayRequest
from pokepay_partner_python_sdk.pokepay.response.account_detail import AccountDetail


class GetAccount(PokepayRequest):
    def __init__(self, account_id):
        self.path = "/accounts" + "/" + account_id
        self.method = "GET"
        self.body_params = {}
        
        self.response_class = AccountDetail
