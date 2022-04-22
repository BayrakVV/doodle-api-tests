import allure

from doodle_test.utils.utils import get_entry_from_collection

user_name = "test_user"
body = {
    "name": user_name
}


def test_users_post(users_api):
    with allure.step("Create new user"):
        response, response_body = users_api.create(body)

    with allure.step("Check response"):
        assert response.status_code == 201
        assert response_body["name"] == user_name


def test_users_get_by_id(users_api):
    with allure.step("Create new user"):
        _, response_body = users_api.create(body)
        user_id = response_body["id"]

    with allure.step("Get user by id"):
        response, response_body = users_api.get(user_id)

    with allure.step("Check response"):
        assert response.status_code == 200
        assert response_body["name"] == user_name


def test_users_get_all(users_api):
    with allure.step("Create new user"):
        _, response_body = users_api.create(body)
        user_id = response_body["id"]

    with allure.step("Get all users"):
        response, response_body = users_api.get_all()

    with allure.step("Extract previously created user from collection"):
        user = get_entry_from_collection(response_body, user_id)

    with allure.step("Check response"):
        assert response.status_code == 200
        assert user["name"] == user_name


def test_users_delete(users_api):
    with allure.step("Create new user"):
        _, response_body = users_api.create(body)
        user_id = response_body["id"]

    with allure.step("Check that new user exists"):
        _, response_body = users_api.get_all()
        user = get_entry_from_collection(response_body, user_id)
        assert user["name"] == user_name

    with allure.step("Delete user and check it"):
        response = users_api.delete(user_id)
        _, response_body = users_api.get_all()
        user = get_entry_from_collection(response_body, user_id)

        assert response.status_code == 200
        assert user == "Entry not found"


