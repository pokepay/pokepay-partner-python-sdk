# DO NOT EDIT: File is generated by code generator.

from pokepay.response.response import PokepayResponse


class UserDevice(PokepayResponse):
    def __init__(self, response, response_body):
        super().__init__(response, response_body)
        self.id = response_body['id']
        self.user = response_body['user']
        self.is_active = response_body['is_active']
        self.metadata = response_body['metadata']

    def id(self):
        return self.id

    def user(self):
        return self.user

    def is_active(self):
        return self.is_active

    def metadata(self):
        return self.metadata

