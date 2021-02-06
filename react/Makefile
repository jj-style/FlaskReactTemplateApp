.PHONY: all
all: test build

.PHONY: test
test:
	@npm install
	@CI=true npm test

.PHONY: build
build:
	@npm install
	@npm run build