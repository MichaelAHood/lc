check:
	poetry run ruff check . --ignore E501 && poetry run black --check .

test:
	poetry run pytest 
