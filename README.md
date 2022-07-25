## Описание проекта
 
Перед вами приложение менеджера задач.
Для использования необходима регистрация и авторизация.
Задачам можно присваивать метки и статусы, а так же другого пользователя, которому адресована задача.
Задачи можно фильтровать.


## [Страница проекта](https://afternoon-citadel-86375.herokuapp.com/)

[![Actions Status](https://github.com/Nidenai/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/Nidenai/python-project-lvl4/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/845c9ad13166925bdb85/maintainability)](https://codeclimate.com/github/Nidenai/python-project-lvl4/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/845c9ad13166925bdb85/test_coverage)](https://codeclimate.com/github/Nidenai/python-project-lvl4/test_coverage)

[![Linter](https://github.com/Nidenai/python-project-lvl4/workflows/linter/badge.svg)](https://github.com/Nidenai/python-project-lvl4/linter)

[![Tests](https://github.com/Nidenai/python-project-lvl4/workflows/tests/badge.svg)](https://github.com/Nidenai/python-project-lvl4/tests)


## Инсталляция приложения

1. Необходимо установить [python3](https://www.python.org/downloads/)

2. Необходимо установить [poetry](https://python-poetry.org/).

3. Установите приложение командной: 
`git clone https://github.com/Nidenai/python-project-lvl4.git`

4. Затем установите все библиотеки из файла командой:
`pip install -r requirements.txt`

5. После этого, необходимо создать файл `.env` и добавить туда следующие переменные:
* `SECRET_KEY`
* `DATABASE_ENGINE`
* `DATABASE_NAME`
* `ROLL_KEY`
* `DEBUG`

6. Затем можно запустить приложение командой `make start`
