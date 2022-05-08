# ParcingSiteWithDjango

Web site parsing bestchange

> Bestchange - a cryptocurrency site that is updated every 10-20s.
>
> Bestchange API - An API that contains some data from the Bestchange website
> ie the data from this api is updated every 10-20s.
>
> Task: extract the necessary data from the Bestchange API and upload it to a table

## Requirements
* Python 3+;
* PostgreSQL 11+;
* Redis;
* celery
* PIP modules (see requirements.txt).

## Configuration file
When deploying, copy the `configs.json.example` file to the `configs.json` file in the directory
`Parcer/Parcer/settings/`.

Example `configs.json` file `Parcer/Parcer/settings/configs.json.example`.

## Start

1. Create and activate virtual environment:

    `python -m venv venv`

2. Install packages:

    `pip install -r requirements.txt`

3. Run migrations:

    `python manage.py migrate`

4. Create superuser:

    `python manage.py createsuperuser`

4. Create config file:

    `configs.json`

6. Start django server:
    
    `$ python manage.py runserver`


7. Run celery:

    `$ celery -A Parcer worker -l info`


8. Run celery beat:

    `$ celery -A Parcer beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`
