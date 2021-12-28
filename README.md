# ParcingSiteWithDjango

Парсинг web сайта bestchange

> Bestchange - криптовалютный сайт, который каждый 10-20с обновляется.
> 
> API Bestchange - Апи , который содержит некие данные из сайта Bestchange 
> т.е данные из этого апи обновляются каждый 10-20с.
> 
> Задача: извлечь из API Bestchange нужные данные и выгрузить в таблицу

## Требования
* Python 3+;
* PostgreSQL 11+;
* Redis;
* Celery
* PIP модули (см. requirements.txt).

## Конфигурационный файл
При развертывание скопировать файл `configs.json.example` в файл `configs.json` в директории 
`Parcer/Parcer/settings/`.

Пример `configs.json` файла `Parcer/Parcer/settings/configs.json.example`.

## Старт

1. Создать и активировать виртуальное окружение:

    `python -m venv venv`


2. Установить пакеты:

    `pip install -r requirements.txt`


3. Выполнить команду для выполнения миграций :

    `python manage.py migrate`


4. Создать статичные файлы: 

    `python manage.py collectstatic`


5. Создать суперпользователя:

    `python manage.py createsuperuser`


6. Запустить сервер:

    `$ python manage.py runserver`


7. Запустить celery:

    `$ celery -A Parcer worker -l info`


8. Запустить celery beat:

    `$ celery -A Parcer beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`