# DO NOT EDIT: File is generated by code generator.

from pokepay.request.request import PokepayRequest
from pokepay.response.campaign import Campaign


class CreateCampaign(PokepayRequest):
    def __init__(self, name, private_money_id, starts_at, ends_at, priority, event, **rest_args):
        self.path = "/campaigns"
        self.method = "POST"
        self.body_params = {"name": name,
                            "private_money_id": private_money_id,
                            "starts_at": starts_at,
                            "ends_at": ends_at,
                            "priority": priority,
                            "event": event}
        self.body_params.update(rest_args)
        self.response_class = Campaign
