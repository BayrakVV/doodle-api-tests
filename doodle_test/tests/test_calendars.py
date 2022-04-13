def test_calendars(calendars_api):
    response, response_body = calendars_api.get_calendar("2022-04")
    assert response.status_code == 200
    assert response_body["days"] == {}

