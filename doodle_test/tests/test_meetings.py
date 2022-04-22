import pytest

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


@pytest.fixture()
def prepare_meeting(users_api, slots_api, meetings_api):
    # Prepare data for meetings POST request
    _, response_body = users_api.create(users_body)
    user_id = response_body["id"]
    _, response_body = slots_api.create(slots_body)
    slot_id = response_body["id"]

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

    return user_id, response, response_body, meetings_api


def test_meetings_post(prepare_meeting):
    # Prepare new meeting
    user_id, response, response_body, _ = prepare_meeting

    assert response.status_code == 201
    # assert response_body["slotId"] == slot_id BUG: there is no slotId in the response
    assert response_body["title"] == meeting_title
    assert response_body["startAt"] == slot_start_at
    assert response_body["endAt"] == slot_end_at
    assert response_body["participants"][0]["id"] == user_id
    assert response_body["participants"][0]["name"] == user_name


def test_meetings_get_by_id(prepare_meeting):
    # Prepare new meeting
    user_id, _, response_body, meetings_api = prepare_meeting
    meeting_id = response_body["id"]

    # Get meeting by id
    response, response_body = meetings_api.get(meeting_id)

    assert response.status_code == 200
    # assert response_body["slotId"] == slot_id BUG: there is no slotId in the response
    assert response_body["title"] == meeting_title
    assert response_body["startAt"] == slot_start_at
    assert response_body["endAt"] == slot_end_at
    assert response_body["participants"][0]["id"] == user_id
    assert response_body["participants"][0]["name"] == user_name


def test_meetings_get_all(prepare_meeting):
    # Prepare new meeting
    user_id, _, response_body, meetings_api = prepare_meeting
    meeting_id = response_body["id"]

    # Get all meetings
    response, response_body = meetings_api.get_all()

    # Extract previously created meeting from collection
    meeting = get_entry_from_collection(response_body, meeting_id)

    assert response.status_code == 200
    # assert response_body["slotId"] == slot_id BUG: there is no slotId in the response
    assert meeting["title"] == meeting_title
    assert meeting["startAt"] == slot_start_at
    assert meeting["endAt"] == slot_end_at
    assert meeting["participants"][0]["id"] == user_id
    assert meeting["participants"][0]["name"] == user_name


def test_meetings_delete(prepare_meeting):
    # Prepare new meeting
    _, _, response_body, meetings_api = prepare_meeting
    meeting_id = response_body["id"]

    # Check that new meeting exists
    _, response_body = meetings_api.get_all()
    meeting = get_entry_from_collection(response_body, meeting_id)
    assert meeting["title"] == meeting_title

    # Delete previously created meeting and check it
    response = meetings_api.delete(meeting_id)
    _, response_body = meetings_api.get_all()
    meeting = get_entry_from_collection(response_body, meeting_id)

    assert response.status_code == 200
    assert meeting == "Entry not found"
