.PHONY: all
all: test npm-build docker-build

.PHONY: test
test:
	@npm install
	@CI=true npm test

.PHONY: npm-build
npm-build:
	@npm install
	@npm run build

.PHONY: docker-build
docker-build:
	@docker build . -t webtemplate-react:latest