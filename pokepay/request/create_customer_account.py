# DO NOT EDIT: File is generated by code generator.

from pokepay.request.request import PokepayRequest
from pokepay.response.account_with_user import AccountWithUser


class CreateCustomerAccount(PokepayRequest):
    def __init__(self, message):
        self.path = "/accounts" + "/customers"
        self.method = "POST"
        self.body_params = {"private_money_id": private_money_id}
        self.response_class = AccountWithUser
