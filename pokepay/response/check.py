# DO NOT EDIT: File is generated by code generator.

from pokepay.response.response import PokepayResponse


class Check(PokepayResponse):
    def __init__(self, response, response_body):
        super().__init__(response, response_body)
        self.id = response_body['id']
        self.created_at = response_body['created_at']
        self.amount = response_body['amount']
        self.money_amount = response_body['money_amount']
        self.point_amount = response_body['point_amount']
        self.description = response_body['description']
        self.user = response_body['user']
        self.is_onetime = response_body['is_onetime']
        self.is_disabled = response_body['is_disabled']
        self.expires_at = response_body['expires_at']
        self.last_used_at = response_body['last_used_at']
        self.private_money = response_body['private_money']
        self.usage_limit = response_body['usage_limit']
        self.usage_count = response_body['usage_count']
        self.point_expires_at = response_body['point_expires_at']
        self.point_expires_in_days = response_body['point_expires_in_days']
        self.token = response_body['token']

    def id(self):
        return self.id

    def created_at(self):
        return self.created_at

    def amount(self):
        return self.amount

    def money_amount(self):
        return self.money_amount

    def point_amount(self):
        return self.point_amount

    def description(self):
        return self.description

    def user(self):
        return self.user

    def is_onetime(self):
        return self.is_onetime

    def is_disabled(self):
        return self.is_disabled

    def expires_at(self):
        return self.expires_at

    def last_used_at(self):
        return self.last_used_at

    def private_money(self):
        return self.private_money

    def usage_limit(self):
        return self.usage_limit

    def usage_count(self):
        return self.usage_count

    def point_expires_at(self):
        return self.point_expires_at

    def point_expires_in_days(self):
        return self.point_expires_in_days

    def token(self):
        return self.token

