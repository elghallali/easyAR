install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=lib tests/test_*.py

format:
	black *.py lib/*.py tests/test_*.py

lint:
	pylint --rcfile=.pylintrc *.py lib/*.py tests/test_*.py

run:
	python main.py

all: install lint test