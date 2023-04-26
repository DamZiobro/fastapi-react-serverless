CODE_DIRS=api
TEST_DIRS=tests

deps: ## install dependencies
	@poetry --version &> /dev/null || (echo -e "ERROR: please install poetry" && false)
	poetry config virtualenvs.in-project true
	poetry install
	touch $@

run: deps ## run project in localhost web server
	poetry run uvicorn api.main:app --reload

clean: ## clean project - remove all temporary files and venv dependencies
	rm -rf deps .venv **/__pycache__

format: deps ## format code according to PEP-8 style
	poetry run isort $(CODE_DIRS) $(TEST_DIRS)
	poetry run black --preview $(CODE_DIRS) $(TEST_DIRS)

lint: deps ## check wehther code is formatted according to PEP-8 style
	poetry run flake8 $(CODE_DIRS) $(TEST_DIRS)
	poetry run isort --check-only $(CODE_DIRS) $(TEST_DIRS)
	poetry run black --check $(CODE_DIRS) $(TEST_DIRS)

unit-tests: deps ## run unit tests
	poetry run pytest -s -vv $(TEST_FILE)

cov: deps ## run unit tests and should code coverage
	poetry run pytest -s -vv --cov=$(CODE_DIRS) $(TEST_FILE)

cov-html: deps ## run unit tests and generate HTML report showing code coverage
	poetry run coverage html

checks: lint cov ## run all code checks
