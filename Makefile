.PHONY: help format lint mypy test test-all vulncheck

help:
	@echo "format    - Format python code with isort and black"
	@echo "lint      - Check style with pylint"
	@echo "mypy      - Run the static type checker"
	@echo "test      - Run tests suite with python"
	@echo "test-all  - Run lint, and test coverage"
	@echo "vulncheck - Check for packages vulnerabilities with pipenv"

format:
	isort -rc --apply ghibli tests ./**.py
	black ghibli tests

lint:
	isort -rc -c ghibli tests ./**.py
	black --check ghibli tests
	pylint tests --rcfile=tests/.pylintrc
	pylint ghibli ./**.py --rcfile=ghibli/.pylintrc

mypy:
	mypy ghibli tests

test:
	coverage run -m unittest discover -v -s ./tests
	coverage report
	coverage html
	coverage xml

test-all: lint mypy test

vulncheck:
	pipenv check
