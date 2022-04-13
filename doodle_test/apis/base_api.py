import json

import requests


class BaseApi(object):
    def __init__(self, base_address, api_path=None):
        self.headers = {"Accept": "*/*"}
        self.base_address = base_address
        self.api_path = api_path
        self.id = None
        self.url = f"{self.base_address}/{self.api_path}"

    def request(self, request):
        response = request
        if not response:
            raise Exception("Response is empty")
        response_body = None
        if response.text:
            response_body = json.loads(response.text)
        return response, response_body

    def create(self, payload):
        request = requests.post(
            url=self.url,
            headers=self.headers,
            json=payload
        )
        response, response_body = self.request(request)
        self.id = response_body["id"]
        return response, response_body

    def get_collection(self, page="", page_size=""):
        request = requests.get(
            url=f"{self.url}?page={page}&page_size={page_size}",
            headers=self.headers
        )
        response, response_body = self.request(request)
        return response, response_body

    def get(self):
        request = requests.get(
            url=f'{self.url}/{self.id}',
            headers=self.headers
        )
        response, response_body = self.request(request)
        return response, response_body

    def delete(self):
        request = requests.delete(
            url=f'{self.url}/{self.id}',
            headers=self.headers
        )
        response, response_body = self.request(request)
        return response, response_body
