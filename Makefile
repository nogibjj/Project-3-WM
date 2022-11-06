install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv spotify_db.py

format:
	black *.py

lint:
	pylint --disable=R,C spotify_db.py

all: install lint test

# each line is a command