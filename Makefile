install:
	poetry install

test:
	poetry run pytest hexlet_python_package tests

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build
