from doodle_test.utils.utils import get_entry_from_collection

user_name = "test_user"
slot_start_at = "2022-04-13T15:00:00Z"
slot_end_at = "2022-04-13T15:30:00Z"
meeting_title = "test_meeting"
users_body = {
    "name": user_name
}
slots_body = {
    "startAt": slot_start_at,
    "endAt": slot_end_at
}


def test_meetings_post(users_api, slots_api, meetings_api):
    # Prepare data for meetings POST request
    users_api.create(users_body)
    slots_api.create(slots_body)
    user_id = users_api.id
    slot_id = slots_api.id

    # Build meetings POST request body
    meetings_body = {
        "slotId": slot_id,
        "title": meeting_title,
        "participants": [
            {
                "id": user_id
            }
        ]
    }

    # Send request
    response, response_body = meetings_api.create(meetings_body)

    assert response.status_code == 201
    assert response_body["id"] == meetings_api.id
    # assert response_body["slotId"] == slot_id BUG: there is no slotId in the response
    assert response_body["title"] == meeting_title
    assert response_body["startAt"] == slot_start_at
    assert response_body["endAt"] == slot_end_at
    assert response_body["participants"][0]["id"] == user_id
    assert response_body["participants"][0]["name"] == user_name


def test_meetings_get_by_id(users_api, slots_api, meetings_api):
    # Prepare new meeting
    users_api.create(users_body)
    slots_api.create(slots_body)
    user_id = users_api.id
    slot_id = slots_api.id
    meetings_body = {
        "slotId": slot_id,
        "title": meeting_title,
        "participants": [
            {
                "id": user_id
            }
        ]
    }
    meetings_api.create(meetings_body)

    # Get meeting by id (id field is automatically assigned to the meeting object after creation)
    response, response_body = meetings_api.get()

    assert response.status_code == 200
    assert response_body["id"] == meetings_api.id
    # assert response_body["slotId"] == slot_id BUG: there is no slotId in the response
    assert response_body["title"] == meeting_title
    assert response_body["startAt"] == slot_start_at
    assert response_body["endAt"] == slot_end_at
    assert response_body["participants"][0]["id"] == user_id
    assert response_body["participants"][0]["name"] == user_name


def test_meetings_get_all(users_api, slots_api, meetings_api):
    # Prepare new meeting
    users_api.create(users_body)
    slots_api.create(slots_body)
    user_id = users_api.id
    slot_id = slots_api.id
    meetings_body = {
        "slotId": slot_id,
        "title": meeting_title,
        "participants": [
            {
                "id": user_id
            }
        ]
    }
    meetings_api.create(meetings_body)

    # Get all meetings
    response, response_body = meetings_api.get_all()

    # Extract previously created meeting from collection
    meeting = get_entry_from_collection(response_body, meetings_api.id)

    assert response.status_code == 200
    assert meeting["id"] == meetings_api.id
    # assert response_body["slotId"] == slot_id BUG: there is no slotId in the response
    assert meeting["title"] == meeting_title
    assert meeting["startAt"] == slot_start_at
    assert meeting["endAt"] == slot_end_at
    assert meeting["participants"][0]["id"] == user_id
    assert meeting["participants"][0]["name"] == user_name


def test_meetings_delete(users_api, slots_api, meetings_api):
    # Prepare new meeting
    users_api.create(users_body)
    slots_api.create(slots_body)
    user_id = users_api.id
    slot_id = slots_api.id
    meetings_body = {
        "slotId": slot_id,
        "title": meeting_title,
        "participants": [
            {
                "id": user_id
            }
        ]
    }
    meetings_api.create(meetings_body)

    # Check that new meeting exists
    _, response_body = meetings_api.get_all()
    meeting = get_entry_from_collection(response_body, meetings_api.id)
    assert meeting["id"] == meetings_api.id

    # Delete previously created meeting and check it
    response = meetings_api.delete()
    _, response_body = meetings_api.get_all()
    meeting = get_entry_from_collection(response_body, meetings_api.id)

    assert response.status_code == 200
    assert meeting == "Entry not found"
