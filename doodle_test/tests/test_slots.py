from doodle_test.utils.utils import get_entry_from_collection

start_at = "2022-04-13T15:00:00Z"
end_at = "2022-04-13T15:30:00Z"
body = {
    "startAt": start_at,
    "endAt": end_at
}


def test_slots_post(slots_api):
    response, response_body = slots_api.create(body)

    assert response.status_code == 201
    assert response_body["startAt"] == start_at
    assert response_body["endAt"] == end_at
    assert response_body["id"] == slots_api.id


def test_slots_get_by_id(slots_api):
    # Create new slot
    slots_api.create(body)

    # Get slot by id (id field is automatically assigned to the slot object after creation)
    response, response_body = slots_api.get()

    assert response.status_code == 200
    assert response_body["startAt"] == start_at
    assert response_body["endAt"] == end_at
    assert response_body["id"] == slots_api.id


def test_slots_get_all(slots_api):
    # Create new slot
    slots_api.create(body)
    # Get all slots
    response, response_body = slots_api.get_all()
    # Extract previously created slot from collection
    slot = get_entry_from_collection(response_body, slots_api.id)

    assert response.status_code == 200
    assert slot["startAt"] == start_at
    assert slot["endAt"] == end_at
    assert slot["id"] == slots_api.id


def test_slots_delete(slots_api):
    # Create new slot
    slots_api.create(body)
    # Check that new slot exists
    _, response_body = slots_api.get_all()
    slot = get_entry_from_collection(response_body, slots_api.id)
    assert slot["id"] == slots_api.id

    # Delete slot and check it
    response = slots_api.delete()
    _, response_body = slots_api.get_all()
    user = get_entry_from_collection(response_body, slots_api.id)

    assert response.status_code == 200
    assert user == "Entry not found"

