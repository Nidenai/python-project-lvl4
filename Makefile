start:
	gunicorn task_manager.wsgi

export:
	export DJANGO_SETTINGS_MODULE=task_manager.settings

poetry:
	export PATH="$HOME/.local/bin:$PATH"

venv:
	source venv/bin/activate

req:
	pip freeze > requirements.txt


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


local_pre:
	python3 manage.py makemessages -l ru -i venv

local_launch:
	python3 manage.py compilemessages


data:
	python3 manage.py loaddata fixtures/users.json
	python3 manage.py loaddata fixtures/statuses.json
	python3 manage.py loaddata fixtures/labels.json
	python3 manage.py loaddata fixtures/tasks.json