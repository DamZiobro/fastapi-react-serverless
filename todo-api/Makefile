deps:
	@poetry --version &> /dev/null || (echo -e "ERROR: please install poetry" && false)
	poetry config virtualenvs.in-project true
	poetry install
	touch $@

run: deps
	poetry run uvicorn api.main:app --reload

clean:
	rm -rf deps .venv

format: deps ## format code according to PEP-8 style
	poetry run isort .
	poetry run black --preview .

lint: deps ## check wehther code is formatted according to PEP-8 style
	poetry run flake8 .
	poetry run isort --check-only .
	poetry run black --preview --check .

