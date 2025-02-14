# DO NOT EDIT: File is generated by code generator.

from pokepay.request.request import PokepayRequest
from pokepay.response.transaction_detail import TransactionDetail


class CreateBankTopupTransaction(PokepayRequest):
    def __init__(self, user_device_id, private_money_id, amount, bank_id, request_id, **rest_args):
        self.path = "/user-devices" + "/" + user_device_id + "/banks" + "/topup"
        self.method = "POST"
        self.body_params = {"private_money_id": private_money_id,
                            "amount": amount,
                            "bank_id": bank_id,
                            "request_id": request_id}
        self.body_params.update(rest_args)
        if 'start' in self.body_params:
            self.body_params['from'] = self.body_params.pop('start')
        self.response_class = TransactionDetail
