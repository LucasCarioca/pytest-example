.PHONY: test

run: .
	python3 src/main.py

test: .
	pytest -v -s
