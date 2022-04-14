import pytest

from doodle_test.apis.calendars_api import CalendarsApi
from doodle_test.apis.meetings_api import MeetingsApi
from doodle_test.apis.slots_api import SlotsApi
from doodle_test.apis.users_api import UsersApi


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost:8080")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def users_api(base_url):
    users_object = UsersApi(base_url)
    yield users_object
    users_object.clean_up()


@pytest.fixture()
def slots_api(base_url):
    slots_object = SlotsApi(base_url)
    yield slots_object
    slots_object.clean_up()


@pytest.fixture()
def meetings_api(base_url):
    meetings_object = MeetingsApi(base_url)
    yield meetings_object
    meetings_object.clean_up()


@pytest.fixture()
def calendars_api(base_url):
    calendars_object = CalendarsApi(base_url)
    return calendars_object
