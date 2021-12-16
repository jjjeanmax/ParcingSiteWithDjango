# Generated by Django 3.2.10 on 2021-12-16 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_city', models.CharField(max_length=100, verbose_name='ID города')),
                ('name_city', models.CharField(max_length=255, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'список городов',
            },
        ),
        migrations.CreateModel(
            name='CodeCurrencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(max_length=100)),
                ('name_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exchanges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_exchange_office', models.CharField(max_length=100, verbose_name='ID обменного пункта')),
                ('name_exchange_office', models.CharField(max_length=100, verbose_name='Название обменного пункта')),
                ('WMBL', models.CharField(max_length=100)),
                ('reserve', models.CharField(max_length=100, verbose_name='резерв')),
            ],
            options={
                'verbose_name': 'список обменных пунктов',
            },
        ),
        migrations.CreateModel(
            name='Infos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_given_currency', models.CharField(max_length=100, verbose_name='ID отдаваемой валюты')),
                ('id_received_currency', models.CharField(max_length=100, verbose_name='ID получаемой валюты')),
                ('rate_given_exchange', models.CharField(max_length=100, verbose_name='Курс отдаю')),
                ('rate_received_exchange', models.CharField(max_length=100, verbose_name='Курс получаю')),
                ('received_currency_reserve', models.CharField(max_length=100, verbose_name='Резерв получаемой валюты')),
                ('reviews', models.CharField(max_length=255, verbose_name='Отзывы')),
                ('minimum_exchange_amount', models.CharField(max_length=100, verbose_name='Минимальная сумма обмена')),
                ('maximum_exchange_amount', models.CharField(max_length=100, verbose_name='Максимальная сумма обмена')),
                ('city', models.CharField(max_length=100, verbose_name=' ID города')),
                ('exchanges', models.CharField(max_length=100, verbose_name=' ID обменного пункта')),
            ],
            options={
                'verbose_name': ' список курсов обмена',
            },
        ),
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_currency', models.CharField(max_length=100, verbose_name='ID валюты')),
                ('position_currency_in_table', models.CharField(max_length=100, verbose_name='Позиция валюты в табличном списке на сайте')),
                ('name_values', models.CharField(max_length=100, verbose_name='Название валюты')),
                ('display_in_tables_of_exchanger', models.CharField(max_length=100, verbose_name=' Отображение в таблице обменников по направлению')),
                ('id_code_currencies', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_scraping.codecurrencies')),
            ],
            options={
                'verbose_name': 'список валют',
            },
        ),
    ]
