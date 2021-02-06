.PHONY: all
all: pre-reqs lint test docker-build

.PHONY: pre-reqs
pre-reqs: requirements.txt
	python -m pip install --upgrade pip
	pip install flake8 pytest
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

.PHONY: lint
lint: pre-reqs
	# stop the build if there are Python syntax errors or undefined names
	flake8 app --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 app --count --exit-zero --max-line-length=127 --statistics

.PHONY: test
test: pre-reqs
	@pytest

.PHONY: docker-build
docker-build:
	@docker build . -t webtemplate-flask:latest