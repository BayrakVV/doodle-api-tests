user_name = "test_user"
first_slot_start_at = "2022-04-13T15:00:00Z"
first_slot_end_at = "2022-04-13T15:30:00Z"
second_slot_start_at = "2022-04-15T12:00:00Z"
second_slot_end_at = "2022-04-15T13:00:00Z"
meeting_title = "test_meeting"
users_body = {
    "name": user_name
}
first_slot_body = {
    "startAt": first_slot_start_at,
    "endAt": first_slot_end_at
}
second_slot_body = {
    "startAt": second_slot_start_at,
    "endAt": second_slot_end_at
}


def test_calendars_get(users_api, slots_api, meetings_api, calendars_api):
    # Prepare user, slots and meeting
    _, response_body = users_api.create(users_body)
    user_id = response_body["id"]
    _, response_body = slots_api.create(first_slot_body)
    first_slot_id = response_body["id"]
    _, response_body = slots_api.create(second_slot_body)
    second_slot_id = response_body["id"]
    meetings_body = {
        "slotId": first_slot_id,
        "title": meeting_title,
        "participants": [
            {
                "id": user_id
            }
        ]
    }
    _, response_body = meetings_api.create(meetings_body)
    meetings_id = response_body["id"]

    # Get calendar
    response, response_body = calendars_api.get_calendar("2022-04")

    assert response.status_code == 200
    assert response_body["days"]["13"]["slots"] == []
    assert response_body["days"]["13"]["meetings"][0]["id"] == meetings_id
    assert response_body["days"]["13"]["meetings"][0]["title"] == meeting_title
    assert response_body["days"]["13"]["meetings"][0]["startAt"] == first_slot_start_at
    assert response_body["days"]["13"]["meetings"][0]["endAt"] == first_slot_end_at
    assert response_body["days"]["13"]["meetings"][0]["participants"][0]["id"] == user_id
    assert response_body["days"]["13"]["meetings"][0]["participants"][0]["name"] == user_name
    assert response_body["days"]["15"]["slots"][0]["id"] == second_slot_id
    assert response_body["days"]["15"]["slots"][0]["startAt"] == second_slot_start_at
    assert response_body["days"]["15"]["slots"][0]["endAt"] == second_slot_end_at
    assert response_body["days"]["15"]["meetings"] == []
    assert response_body["slotsBefore"] == 10000
    assert response_body["slotsAfter"] == 0
    assert response_body["meetingsBefore"] == 0
    assert response_body["meetingsAfter"] == 0
