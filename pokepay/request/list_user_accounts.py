# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.request.request import PokepayRequest
from pokepay_partner_python_sdk.pokepay.response.paginated_account_details import PaginatedAccountDetails


class ListUserAccounts(PokepayRequest):
    def __init__(self, user_id):
        self.path = "/users" + "/" + user_id + "/accounts"
        self.method = "GET"
        self.body_params = {}
        
        self.response_class = PaginatedAccountDetails
