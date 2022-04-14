from doodle_test.utils.utils import get_entry

name = "test_user"
body = {
    "name": name
}


def test_users_post(users_api):
    response, response_body = users_api.create(body)

    assert response.status_code == 201
    assert response_body["name"] == name
    assert response_body["id"] == users_api.id


def test_users_get_by_id(users_api):
    users_api.create(body)
    response, response_body = users_api.get()

    assert response.status_code == 200
    assert response_body["name"] == name
    assert response_body["id"] == users_api.id


def test_users_get_all(users_api):
    users_api.create(body)
    response, response_body = users_api.get_all()
    user = get_entry(response_body, users_api.id)

    assert response.status_code == 200
    assert user["name"] == name
    assert user["id"] == users_api.id


def test_users_delete(users_api):
    users_api.create(body)
    _, response_body = users_api.get_all()
    user = get_entry(response_body, users_api.id)

    assert user["name"] == name
    assert user["id"] == users_api.id

    response = users_api.delete()
    _, response_body = users_api.get_all()
    user = get_entry(response_body, users_api.id)

    assert response.status_code == 200
    assert user == "Record not found"

