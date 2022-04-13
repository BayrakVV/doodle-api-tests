def test_slots_create(slots_api):
    start_at = "2022-04-13T15:00:00Z"
    end_at = "2022-04-13T15:30:00Z"
    body = {
        "startAt": start_at,
        "endAt": end_at
    }
    response, response_body = slots_api.create(body)

    assert response.status_code == 201
    assert response_body["startAt"] == start_at
    assert response_body["endAt"] == end_at
    assert response_body["id"] == slots_api.id

    response, response_body = slots_api.get()

    assert response.status_code == 200
    assert response_body["startAt"] == start_at
    assert response_body["endAt"] == end_at
    assert response_body["id"] == slots_api.id
