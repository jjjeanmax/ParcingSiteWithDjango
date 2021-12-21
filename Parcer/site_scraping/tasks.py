import json
import os

from celery import shared_task
from django.db.models import Sum, FloatField, F, Count
from django.db.models.functions import Cast

from .models import Exchanges, Rates, DataSave

from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

api = 'http://api.bestchange.ru/info.zip'
extract_to = "code"

json_list = ''
RATES_FILE_PATH = "code/bm_rates.dat"
Exchanges_FILE_PATH = "code/bm_exch.dat"


@shared_task
def download_and_unzip(url=api, extract_to=extract_to):
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
    q = Exchanges.objects.values("name_exchange_office").annotate(dcount=Count('name_exchange_office')).order_by()
    for i in range(len(q)):
        print(q[i])
    try:

        qs = Rates.objects.values("rate_given_exchange", "rate_received_exchange", "reviews",
                                  NameExchangeOffice=F('exchanges__name_exchange_office'),
                                  Reserve=F("exchanges__reserve"),
                                  TotalExchangerGiven=Count(F('exchanges__name_exchange_office')),
                                  SumReserveGiven=Sum((Cast('exchanges__reserve', output_field=FloatField())))
                                  ).order_by()
        for data_dict in qs:
            DataSave.objects.update_or_create(name_exchange_office=data_dict['NameExchangeOffice'],
                                              reserve=data_dict['Reserve'],
                                              rate_given_exchange=data_dict['rate_given_exchange'],
                                              rate_received_exchange=data_dict['rate_received_exchange'],
                                              reviews=data_dict['reviews'],
                                              total_exchanger_given=data_dict['TotalExchangerGiven'],
                                              total_exchanger_received=data_dict['TotalExchangerGiven'],
                                              sum_reserve_given=data_dict['SumReserveGiven'],
                                              sum_reserve_received=(data_dict['SumReserveGiven']),

                                              )
        print("save")

    except Exception as e:
        print("dataaa failed")
        print(e)
        pass


@shared_task
def get_data():
    get_queryset.delay()
