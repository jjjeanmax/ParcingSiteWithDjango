import json
import os

from celery import shared_task
from django.db.models import Sum, FloatField, Count, F
from django.db.models.functions import Cast

from Parcer.settings.base import API

from .models import Exchanges, Rates, DataSave, Currencies

from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

# TODO: use redis caches instated of this directory
extract_to = "code"


@shared_task
def download_and_unzip(url=API, extract_to=extract_to):
    try:
        http_response = urlopen(url)
        zipfile = ZipFile(BytesIO(http_response.read()))
        zipfile.extractall(path=extract_to)
        entries = os.listdir(extract_to)
        for entry in entries:
            if entry.endswith(".dat"):
                file_path = f"{extract_to}/{entry}"
                fh = open(file_path, encoding="ISO-8859-1")
                status_raw = fh.read()
                pattern = [line.strip() for line in status_raw.split("\n")]
                pairs = [line.split(";", 1) for line in pattern if line != '']
                with open(f'{file_path}.json', 'w', encoding='utf-8') as f:
                    json.dump(pairs, f, indent=4)
    except OSError:
        pass


@shared_task
def scrap_exchanges():
    try:
        with open('code/bm_exch.dat.json', 'r', ) as ex:
            data_exh = json.load(ex)
            for item in data_exh:
                Exchanges.objects.update_or_create(id_exchange_office=item[0],
                                                   name_exchange_office=item[1].split(";")[0],
                                                   WMBL=item[1].split(";")[2],
                                                   reserve=item[1].split(";")[3]
                                                   )
    except Exception as e:
        print("exchanges failed")
        print(e)
        pass


@shared_task
def get_exchanges_current():
    scrap_exchanges.delay()


@shared_task
def scrap_currencies():
    try:
        with open('code/bm_cy.dat.json', 'r', encoding="utf-8") as ex:
            data_cur = json.load(ex)
            for item in data_cur:
                Currencies.objects.update_or_create(id_currency=item[0],
                                                    name_currency=item[1].split(";")[1],
                                                    )
    except Exception as e:
        print("currencies failed")
        print(e)
        pass


@shared_task
def get_currencies_current():
    scrap_currencies.delay()


@shared_task
def scrap_rates():
    try:
        with open('code/bm_rates.dat.json', 'r', encoding="utf-8") as rt:
            data_rt = json.load(rt)
            for item in data_rt:
                exchanges = Exchanges.objects.filter(id_exchange_office=item[1].split(';')[1]).first()
                id_name_receive = Currencies.objects.filter(id_currency=item[1].split(';')[0]).first()
                id_name_given = Currencies.objects.filter(id_currency=item[0]).first()

                name_receive = Currencies.objects.values('name_currency', 'id_currency').filter(
                    id_currency=item[1].split(';')[0]).first()
                name_given = Currencies.objects.values('name_currency', 'id_currency').filter(
                    id_currency=item[0]).first()

                Rates.objects.update_or_create(rate_given_exchange=item[1].split(';')[2],
                                               rate_received_exchange=item[1].split(';')[3],
                                               reviews=item[1].split(';')[5],
                                               exchanges=exchanges,
                                               name_rate_given_exchange=name_given['name_currency'],
                                               name_rate_received_exchange=name_receive['name_currency'],
                                               id_rate_received_exchange=id_name_receive,
                                               id_rate_given_exchange=id_name_given
                                               )
    except Exception as e:
        print("rates failed")
        print(e)


@shared_task
def get_rate_current():
    scrap_rates.delay()


@shared_task
def get_queryset():
    q = Rates.objects.values("exchanges__name_exchange_office",
                             "rate_received_exchange",
                             "rate_given_exchange",
                             "reviews", "exchanges__reserve",
                             "name_rate_received_exchange",
                             "name_rate_given_exchange").annotate(dcount=Count('exchanges__name_exchange_office'),
                                                                  dsum=Sum(Cast('exchanges__reserve',
                                                                                output_field=FloatField())))

    try:
        for data_dict in q:
            DataSave.objects.update_or_create(name_exchange_office=data_dict['exchanges__name_exchange_office'],
                                              reserve=data_dict['exchanges__reserve'],
                                              rate_given_exchange=data_dict['rate_given_exchange'],
                                              rate_received_exchange=data_dict['rate_received_exchange'],
                                              reviews=data_dict['reviews'],
                                              name_rate_received_exchange=data_dict['name_rate_received_exchange'],
                                              name_rate_given_exchange=data_dict['name_rate_given_exchange'],
                                              total_exchanger=data_dict['dcount'],
                                              sum_reserve=data_dict['dsum'],
                                              )
        print("save")

    except Exception as e:
        print("dataaa failed")
        print(e)
        pass


@shared_task
def get_data():
    get_queryset.delay()
