# StorageForAll
https://t.me/StorageForAllBot
@StorageForAllBot

Это телеграм бот для администрирования сотрудничества между заказчиками и складами

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте БД командой `python manage.py migrate`
- Запустите бота `py main.py`

## Администрирование
- Запустите сервер для администрирования командой `python manage.py runserver`
- Перейдите по адресу http://127.0.0.1:8000/admin
- Используйте данные для авторизации (Username: "admin", Password: "PHPadmin")
- Далее следуйте указаниям бота

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` папке venv `manage.py` и 
запишите туда данные в таком формате: 
```python
SECRET_KEY = 'secret key for Django'
DEBUG = False
BOT_TOKEN = 6277504232:AAGya9EHaLsRzb4CwyGot6z5NYRm1eMfXGY
DJANGO_SETTINGS_MODULE = 'warehouse.settings'
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
 