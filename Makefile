start:
	gunicorn task_manager.wsgi

export:
	export DJANGO_SETTINGS_MODULE=task_manager.settings

poetry:
	export PATH="$HOME/.local/bin:$PATH"

venv:
	source project/bin/activate

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