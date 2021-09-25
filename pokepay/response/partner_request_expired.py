# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.response.response import PokepayResponse


class PartnerRequestExpired(PokepayResponse):
    def __init__(self, response, response_body):
        super().__init__(response, response_body)
        self.type = response_body['type']
        self.message = response_body['message']

    def type(self):
        return self.type

    def message(self):
        return self.message

