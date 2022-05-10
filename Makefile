start:
	gunicorn task_manager.wsgi

export:
	export DJANGO_SETTINGS_MODULE=task_manager.settings

poetry:
	export PATH="$HOME/.local/bin:$PATH"