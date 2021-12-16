from django.db import models


class Infos(models.Model):
    updated = models.DateTimeField()


class Cities(models.Model):
    id_city = models.CharField(verbose_name="ID города", max_length=100)
    name_city = models.CharField(verbose_name="Название города", max_length=255)

    def __str__(self):
        return self.id_city

    class Meta:
        verbose_name = "список городов"


class Exchanges(models.Model):
    id_exchange_office = models.CharField(max_length=100, verbose_name="ID обменного пункта")
    name_exchange_office = models.CharField(max_length=100, verbose_name="Название обменного пункта")
    WMBL = models.CharField(max_length=100)
    reserve = models.CharField(verbose_name="резерв", max_length=100)

    def __str__(self):
        return self.id_exchange_office

    class Meta:
        verbose_name = "список обменных пунктов"


class Rates(models.Model):
    id_given_currency = models.CharField(max_length=100, verbose_name="ID отдаваемой валюты")
    id_received_currency = models.CharField(max_length=100, verbose_name="ID получаемой валюты")
    rate_given_exchange = models.CharField(max_length=100, verbose_name="Курс отдаю")
    rate_received_exchange = models.CharField(max_length=100, verbose_name="Курс получаю")
    received_currency_reserve = models.CharField(max_length=100, verbose_name="Резерв получаемой валюты")
    reviews = models.CharField(max_length=255, verbose_name="Отзывы")
    minimum_exchange_amount = models.CharField(max_length=100, verbose_name="Минимальная сумма обмена")
    maximum_exchange_amount = models.CharField(max_length=100, verbose_name="Максимальная сумма обмена")
    city = models.CharField(max_length=100,verbose_name=" ID города")
    exchanges = models.CharField(max_length=100,verbose_name=" ID обменного пункта")

    def __str__(self):
        return f"отдать: {self.rate_given_exchange} и получить: {self.rate_received_exchange}"

    class Meta:
        verbose_name = " список курсов обмена"


class CodeCurrencies(models.Model):
    id_code = models.CharField(max_length=100)
    name_code = models.CharField(max_length=100)


class Currencies(models.Model):
    id_currency = models.CharField(max_length=100, verbose_name="ID валюты")
    position_currency_in_table = models.CharField(max_length=100,
                                                  verbose_name="Позиция валюты в табличном списке на сайте")
    name_values = models.CharField(max_length=100, verbose_name="Название валюты")
    display_in_tables_of_exchanger = models.CharField(max_length=100,
                                                      verbose_name=" Отображение в таблице обменников по направлению")
    id_code_currencies = models.ForeignKey(CodeCurrencies, on_delete=models.PROTECT)

    def __str__(self):
        return self.id_currency

    class Meta:
        verbose_name = "список валют"

