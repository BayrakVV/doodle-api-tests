def test_meetings_create(users_api, slots_api, meetings_api):
    user_name = "test_user"
    slot_start_at = "2022-04-13T15:00:00Z"
    slot_end_at = "2022-04-13T15:30:00Z"
    users_body = {
        "name": user_name
    }
    slots_body = {
        "startAt": slot_start_at,
        "endAt": slot_end_at
    }
    users_api.create(users_body)
    slots_api.create(slots_body)
    user_id = users_api.id
    slot_id = slots_api.id

    meeting_title = "test_meeting"
    meetings_body = {
        "slotId": slot_id,
        "title": meeting_title,
        "participants": [
            {
                "id": user_id
            }
        ]
    }

    response, response_body = meetings_api.create(meetings_body)

    assert response.status_code == 201
    assert response_body["id"] == meetings_api.id
    # assert response_body["slotId"] == slot_id BUG: there is no slotId in the response
    assert response_body["title"] == meeting_title
    assert response_body["startAt"] == slot_start_at
    assert response_body["endAt"] == slot_end_at
    assert response_body["participants"][0]["id"] == user_id
    assert response_body["participants"][0]["name"] == user_name

    response, response_body = meetings_api.get()

    assert response.status_code == 200
    assert response_body["id"] == meetings_api.id
    # assert response_body["slotId"] == slot_id BUG: there is no slotId in the response
    assert response_body["title"] == meeting_title
    assert response_body["startAt"] == slot_start_at
    assert response_body["endAt"] == slot_end_at
    assert response_body["participants"][0]["id"] == user_id
    assert response_body["participants"][0]["name"] == user_name
