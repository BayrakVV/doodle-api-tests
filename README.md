# Doodle test challenge
This is the solution for Doodle interview code challenge, an example of API test automation

## Getting Started

### Dependencies
To run tests you need:
- Docker Desktop installed (or Docker Engine for Linux)
- [Doddle's backend application](https://github.com/DoodleScheduling/qa-backend-challenge)
- Python >= 3.8 if you want to play with tests
- [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline) suitable for your environment if you want to see test report sample 

### Setup
- Clone Doddle's backend application to your machine an launch it
- Clone this repository

## How to run tests

### Inside Docker container
- To build a Docker image run in the root project directory:
>$ docker build -t doodle_test .
- Then start the container:
>$ docker run -it --rm --network=qa-backend-challenge_qa-challenge -v $(pwd)/:/test/ doodle_test sh
- Now inside the container shell you can run all tests:
>$ python3 -m pytest -lvv --url='http://qa-challenge:8080' test/doodle_test/tests/
- Or some specific one:
>$ python3 -m pytest -lvv --url='http://qa-challenge:8080' test/doodle_test/tests/test_users.py::test_users_post

### In the terminal on your host (if you have python3.8 or higher installed)
- Create new virtual environment: 
>$ python3 -m venv <path_to_your_venvs>/doodle_venv
- Activate your virtual environment:
>$ source <path_to_your_venvs>/doodle_venv/bin/activate
- To install required python dependencies in the project root directory run:
>$ pip3 install -r requirements.txt
- To run all tests in the project root directory run:
>$ python3 -m pytest -lvv doodle_test/tests/ --alluredir=/tmp/allure_results --clean-alluredir
- Run specific test:
>$ python3 -m pytest -lvv doodle_test/tests/test_users.py::test_users_post --alluredir=/tmp/allure_results --clean-alluredir
- To get Allure report (will be opened in your default browser):
>$ allure serve /tmp/allure_results
