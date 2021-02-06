.PHONY: all
all: test docker-build

.PHONY: test
test:
	@python3 -m venv ci-env
	@( \
       `. ci-env/bin/activate`; \
       pip install -r requirements.txt; \
	   python3 -m pytest; \
    )

.PHONY: docker-build
docker-build:
	@docker build . -t webtemplate-flask:latest