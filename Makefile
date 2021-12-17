.DEFAULT_GOAL := all
isort = isort asgard tests
black = black -S -l 120 --target-version py38 asgard tests

.PHONY: install
install:
	pip install -U pip setuptools wheel
	pip install -U -e .[extra]
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
	pip install -r requirements.txt

.PHONY: install-dev
install-dev:
	if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

.PHONY: install-all
install-all: install install-dev

.PHONY: run
run:
	uvicorn asgard.main:app

.PHONY: format
format:
	$(isort)
	$(black)

.PHONY: lint
lint:
	flake8 asgard/ tests/
	$(isort) --check-only --df
	$(black) --check --diff

.PHONY: test
test:
	pytest --cov=asgard

.PHONY: testcov
testcov:
	pytest --cov=asgard
	@echo "building coverage html"
	@coverage html

.PHONY: all
all: lint testcov

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
	rm -rf dist
	python setup.py clean
