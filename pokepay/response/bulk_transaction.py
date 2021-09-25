# DO NOT EDIT: File is generated by code generator.

from pokepay_partner_python_sdk.pokepay.response.response import PokepayResponse


class BulkTransaction(PokepayResponse):
    def __init__(self, response, response_body):
        super().__init__(response, response_body)
        self.id = response_body['id']
        self.request_id = response_body['request_id']
        self.name = response_body['name']
        self.description = response_body['description']
        self.status = response_body['status']
        self.error = response_body['error']
        self.error_lineno = response_body['error_lineno']
        self.submitted_at = response_body['submitted_at']
        self.updated_at = response_body['updated_at']

    def id(self):
        return self.id

    def request_id(self):
        return self.request_id

    def name(self):
        return self.name

    def description(self):
        return self.description

    def status(self):
        return self.status

    def error(self):
        return self.error

    def error_lineno(self):
        return self.error_lineno

    def submitted_at(self):
        return self.submitted_at

    def updated_at(self):
        return self.updated_at

