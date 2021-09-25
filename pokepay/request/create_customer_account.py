# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.request.request import PokepayRequest
from pokepay_partner_python_sdk.pokepay.response.account_with_user import AccountWithUser


class CreateCustomerAccount(PokepayRequest):
    def __init__(self, private_money_id, **rest_args):
        self.path = "/accounts" + "/customers"
        self.method = "POST"
        self.body_params = {"private_money_id": private_money_id}
        self.body_params.update(rest_args)
        self.response_class = AccountWithUser
