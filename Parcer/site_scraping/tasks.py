import json
import os

from celery import shared_task
from django.db.models import Sum, FloatField, Count, F
from django.db.models.functions import Cast

from Parcer.settings.base import API

from .models import Exchanges, Rates, DataSave

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
def scrap_rates():
    try:
        with open('code/bm_rates.dat.json', 'r', ) as rt:
            data_rt = json.load(rt)
            for item in data_rt:
                exchanges = Exchanges.objects.filter(id_exchange_office=item[1].split(';')[1]).first()
                Rates.objects.update_or_create(rate_given_exchange=item[1].split(';')[2],
                                               rate_received_exchange=item[1].split(';')[3],
                                               reviews=item[1].split(';')[5],
                                               exchanges=exchanges
                                               )
    except Exception as e:
        print("rates failed")
        print(e)


@shared_task
def get_rate_current():
    scrap_rates.delay()


@shared_task
def get_queryset():
    qs = Exchanges.objects.values('name_exchange_office').annotate(dcount=Count('name_exchange_office'),
                                                                   dsum=Sum(Cast('reserve',
                                                                                 output_field=FloatField()))).order_by()
    print(qs)
    q = Rates.objects.values("exchanges__name_exchange_office",
                             "rate_received_exchange",
                             "rate_given_exchange",
                             "reviews", "exchanges__reserve").annotate(dcount=Count('exchanges__name_exchange_office'),
                                                                       dsum=Sum(Cast('exchanges__reserve',
                                                                                     output_field=FloatField())))

    try:
        for data_dict in q:
            DataSave.objects.update_or_create(name_exchange_office=data_dict['exchanges__name_exchange_office'],
                                              reserve=data_dict['exchanges__reserve'],
                                              rate_given_exchange=data_dict['rate_given_exchange'],
                                              reviews=data_dict['reviews'],
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
