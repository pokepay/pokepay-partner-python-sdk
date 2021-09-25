# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.request.request import PokepayRequest
from pokepay_partner_python_sdk.pokepay.response.user import User


class CreateShop(PokepayRequest):
    def __init__(self, shop_name, **rest_args):
        self.path = "/shops"
        self.method = "POST"
        self.body_params = {"shop_name": shop_name}
        self.body_params.update(rest_args)
        self.response_class = User
