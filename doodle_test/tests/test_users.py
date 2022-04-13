def test_users_create(users_api):
    name = "test_user"
    body = {"name": name}
    response, response_body = users_api.create(body)

    assert response.status_code == 201
    assert "id", "name" in response_body
    assert response_body["name"] == name

    response, response_body = users_api.get()

    assert response.status_code == 200
    assert response_body["name"] == name

    # response, response_body = users_api.get_collection(page_size=200)
    # assert response.status_code == 200
    # assert "piu" in response_body["items"][0]["name"]
