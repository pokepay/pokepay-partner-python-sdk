# DO NOT EDIT: File is generated by code generator.

from pokepay.request.request import PokepayRequest
from pokepay.response.transaction_detail import TransactionDetail


class CreateExchangeTransaction(PokepayRequest):
    def __init__(self, user_id, sender_private_money_id, receiver_private_money_id, amount, **rest_args):
        self.path = "/transactions" + "/exchange"
        self.method = "POST"
        self.body_params = {"user_id": user_id,
                            "sender_private_money_id": sender_private_money_id,
                            "receiver_private_money_id": receiver_private_money_id,
                            "amount": amount}
        self.body_params.update(rest_args)
        if 'start' in self.body_params:
            self.body_params['from'] = self.body_params.pop('start')
        self.response_class = TransactionDetail
