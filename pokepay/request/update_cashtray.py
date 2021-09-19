# DO NOT EDIT: File is generated by code generator.

from pokepay.request.request import PokepayRequest
from pokepay.response.cashtray import Cashtray


class UpdateCashtray(PokepayRequest):
    def __init__(self, message):
        self.path = "/cashtrays" + "/" + cashtray_id
        self.method = "PATCH"
        self.body_params = {}
        self.response_class = Cashtray
