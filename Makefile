
.PHONY: docker-build
docker-build:
	docker build -t doodle_test .

.PHONY: docker-start
docker-start: docker-build
	docker run -it --rm \
			--network=qa-backend-challenge_qa-challenge \
			-v $$(pwd)/:/test/ \
			doodle_test sh

.PHONY: docker-run-test
docker-run-test:
	python3 -m pytest -lvv --url='http://qa-challenge:8080' test/doodle_test/tests/$(test)

.PHONY: run-test
run-test:
	python3 -m pytest -lvv doodle_test/tests/$(test) --alluredir=/tmp/allure_results --clean-alluredir
