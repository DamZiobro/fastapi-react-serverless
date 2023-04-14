deps:
	@poetry --version &> /dev/null || (echo -e "ERROR: please install poetry" && false)
	poetry config virtualenvs.in-project true
	poetry install
	touch $@

run: deps
	poetry run uvicorn api.main:app --reload

clean:
	rm -rf deps .venv
