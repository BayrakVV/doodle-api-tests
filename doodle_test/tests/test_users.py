from doodle_test.utils.utils import get_entry_from_collection

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
    # Create new user
    users_api.create(body)
    # Get user by id (id field is automatically assigned to the user object after creation)
    response, response_body = users_api.get()

    assert response.status_code == 200
    assert response_body["name"] == name
    assert response_body["id"] == users_api.id


def test_users_get_all(users_api):
    # Create new user
    users_api.create(body)
    # Get all users
    response, response_body = users_api.get_all()
    # Extract previously created user from collection
    user = get_entry_from_collection(response_body, users_api.id)

    assert response.status_code == 200
    assert user["name"] == name
    assert user["id"] == users_api.id


def test_users_delete(users_api):
    # Create new user
    users_api.create(body)
    # Check that new user exists
    _, response_body = users_api.get_all()
    user = get_entry_from_collection(response_body, users_api.id)
    assert user["id"] == users_api.id

    # Delete user and check it
    response = users_api.delete()
    _, response_body = users_api.get_all()
    user = get_entry_from_collection(response_body, users_api.id)

    assert response.status_code == 200
    assert user == "Entry not found"

