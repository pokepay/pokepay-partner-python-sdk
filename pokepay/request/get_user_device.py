# DO NOT EDIT: File is generated by code generator.

from pokepay.request.request import PokepayRequest
from pokepay.response.user_device import UserDevice


class GetUserDevice(PokepayRequest):
    def __init__(self, user_device_id):
        self.path = "/user-devices" + "/" + user_device_id
        self.method = "GET"
        self.body_params = {}
        
        if 'start' in self.body_params:
            self.body_params['from'] = self.body_params.pop('start')
        self.response_class = UserDevice
