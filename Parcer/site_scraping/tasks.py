# scraping/tasks.py
# скрапинг

import json

from celery import shared_task

from .models import Exchanges, Rates

from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile

url = 'http://api.bestchange.ru/info.zip'
extract_to = "code"
json_list = ''
STATUS_FILE_PATH = "code/bm_rates.dat"


@shared_task
def download_and_unzip(url=url, extract_to=extract_to):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)


@shared_task
def read_status():
    fh = open(STATUS_FILE_PATH)
    status_raw = fh.read()
    pattern = [line.strip() for line in status_raw.split("\n")]
    pairs = [line.split(";", 1) for line in pattern if line != '']
    with open('code/rates.json', 'w', encoding='utf-8') as f:
        json.dump(pairs, f, indent=4)


@shared_task(serializer='json')
def save_function():
    article_list = []
    with open('code/rates.json', 'r') as fp:
        data = json.load(fp)
        for i in range(len(data)):
            id_given_currency = data[i][0]
            l_data = data[i][1].split(';')
            id_received_currency = l_data[0]
            rate_given_exchange = l_data[1]
            rate_received_exchange = l_data[2]
            received_currency_reserve = l_data[3]
            reviews = l_data[4]
            minimum_exchange_amount = l_data[6]
            maximum_exchange_amount = l_data[7]
            city = l_data[8]
            exchanges = l_data[9]
    try:
        article = {
            'ID отдаваемой валюты': id_given_currency,
            'ID получаемой валюты': id_received_currency,
            'Курс отдаю': rate_given_exchange,
            'Курс получаю': rate_received_exchange,
            'Резерв получаемой валюты': received_currency_reserve,
            'Отзывы': reviews,
            'Минимальная сумма обмена': minimum_exchange_amount,
            'Максимальная сумма обмена': maximum_exchange_amount,
            'город': city,
            'ID обменного пункта': exchanges

        }
        # добавляем "article_list" с каждым объектом "article"
        article_list.append(article)
        print('Finished scraping the articles')

    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

    new_count = 0

    for article in article_list:
        try:
            rates = Rates(
                rate_given_exchange=article['Курс отдаю'],
                rate_received_exchange=article['Курс отдаю'],
                received_currency_reserve=article['Курс получаю'],
                reviews=article['Отзывы'],
                id_given_currency=article['ID отдаваемой валюты'],
                id_received_currency=article['ID получаемой валюты'],
                minimum_exchange_amount=article['Минимальная сумма обмена'],
                maximum_exchange_amount=article['Максимальная сумма обмена'],
                city=article['город'],
                exchanges=article['ID обменного пункта'],
            )
            rates.save()
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break

    return print('finished')
