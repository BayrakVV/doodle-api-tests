import requests

from doodle_test.apis.base_api import BaseApi, handle_response


class CalendarsApi(BaseApi):
    def __init__(self, base_address):
        super().__init__(
            base_address,
            api_path="meetings"
        )

    def get_calendar(self, month):
        request = requests.get(
            url=f"{self.base_address}/calendars?month={month}",
            headers=self.headers
        )
        response, response_body = handle_response(request)
        return response, response_body
