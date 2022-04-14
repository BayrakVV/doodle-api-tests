# Doodle test challenge
This is the solution for Doodle interview code challenge, an example of API test automation

## Getting Started

### Dependencies
To run tests you need:
- Docker Desktop installed (or Docker Engine for Linux)
- [Doddle's backend application](https://github.com/DoodleScheduling/qa-backend-challenge)
- Python >= 3.8 if you want to play with tests

### Setup
- Clone Doddle's backend application to your machine an launch it
- Clone this repository

## How to run tests

### Run tests inside Docker container
- To build a Docker image run in the root project directory:
>$ docker build -t doodle_test .
- Then start the container:
>$ docker run -it --rm --network=qa-backend-challenge_qa-challenge -v $(pwd)/:/test/ doodle_test sh
- Now inside the container shell you can run all tests:
>$ python3 -m pytest -lvv --url='http://qa-challenge:8080' test/doodle_test/tests/
- Or some specific one:
>$ python3 -m pytest -lvv --url='http://qa-challenge:8080' test/doodle_test/tests/test_users.py::test_users_post

### Run tests in the terminal (if you have python3.8 or higher installed)
- Create new virtual environment: 
>$ python3 -m venv <path_to_your_venvs>/doodle_venv
- Activate your virtual environment:
>$ source <path_to_your_venvs>/doodle_venv/bin/activate
- To install required python dependencies in the project root directory run:
>$ pip3 install -r requirements.txt
- To run all tests in the project root directory run:
>$ python3 -m pytest -lvv --url='http://qa-challenge:8080' test/doodle_test/tests/
- Run specific test:
>$ python3 -m pytest -lvv --url='http://qa-challenge:8080' test/doodle_test/tests/test_users.py::test_users_post
