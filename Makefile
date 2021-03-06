start:
	gunicorn task_manager.wsgi

export:
	export DJANGO_SETTINGS_MODULE=task_manager.settings

poetry:
	export PATH="$HOME/.local/bin:$PATH"

activate:
	cd ..
	source django-venv/bin/activate
	cd python-project-lvl4

req:
	pip freeze > requirements.txt

local_pre:
	python3 manage.py makemessages -l ru -i test_venv

local_launch:
	python3 manage.py compilemessages

data:
	python3 manage.py loaddata fixtures/users.json
	python3 manage.py loaddata fixtures/statuses.json
	python3 manage.py loaddata fixtures/labels.json
	python3 manage.py loaddata fixtures/tasks.json

lint:
	poetry run flake8

test:
	python3 manage.py test

coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

all:
	make install
	make build
	make publish
	make package-install