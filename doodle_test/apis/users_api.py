from doodle_test.apis.base_api import BaseApi


class UsersApi(BaseApi):
    def __init__(self, base_address):
        super().__init__(
            base_address,
            api_path="users"
        )
