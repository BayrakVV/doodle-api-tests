import json

import requests


def handle_response(request):
    response = request
    if not response:
        raise Exception("Response is empty")
    response_body = None
    if response.text:
        response_body = json.loads(response.text)
    return response, response_body


class BaseApi(object):
    def __init__(self, base_address, api_path=None):
        self.headers = {"Accept": "*/*"}
        self.base_address = base_address
        self.api_path = api_path
        self.ids = []
        self.url = f"{self.base_address}/{self.api_path}"

    def create(self, payload):
        request = requests.post(
            url=self.url,
            headers=self.headers,
            json=payload
        )
        response, response_body = handle_response(request)
        self.ids.append(response_body["id"])
        return response, response_body

    def get_all(self, page="", page_size="20000"):
        request = requests.get(
            url=f"{self.url}?page={page}&page_size={page_size}",
            headers=self.headers
        )
        response, response_body = handle_response(request)
        return response, response_body

    def get(self, entity_id):
        request = requests.get(
            url=f"{self.url}/{entity_id}",
            headers=self.headers
        )
        response, response_body = handle_response(request)
        return response, response_body

    def delete(self, entity_id):
        response = requests.delete(
            url=f"{self.url}/{entity_id}",
            headers=self.headers
        )
        return response

    def clean_up(self):
        for i in self.ids:
            requests.delete(
                url=f"{self.url}/{i}",
                headers=self.headers
            )
