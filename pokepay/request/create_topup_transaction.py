# DO NOT EDIT: File is generated by code generator.

from pokepay.request.request import PokepayRequest
from pokepay.response.transaction_detail import TransactionDetail


class CreateTopupTransaction(PokepayRequest):
    def __init__(self, shop_id, customer_id, private_money_id, **rest_args):
        self.path = "/transactions" + "/topup"
        self.method = "POST"
        self.body_params = {"shop_id": shop_id,
                            "customer_id": customer_id,
                            "private_money_id": private_money_id}
        self.body_params.update(rest_args)
        self.response_class = TransactionDetail
