# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.request.request import PokepayRequest
from pokepay_partner_python_sdk.pokepay.response.paginated_transaction import PaginatedTransaction


class ListCustomerTransactions(PokepayRequest):
    def __init__(self, private_money_id, **rest_args):
        self.path = "/customers" + "/transactions"
        self.method = "GET"
        self.body_params = {"private_money_id": private_money_id}
        self.body_params.update(rest_args)
        self.response_class = PaginatedTransaction
