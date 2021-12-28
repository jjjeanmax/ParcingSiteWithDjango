from django.db import models


class Exchanges(models.Model):
    id_exchange_office = models.CharField(max_length=100, verbose_name="ID обменного пункта", null=False, blank=False)
    name_exchange_office = models.CharField(max_length=100, verbose_name="Название обменного пункта", null=False,
                                            blank=False)
    WMBL = models.CharField(max_length=100, null=False, blank=False)
    reserve = models.CharField(max_length=100, verbose_name="резерв", null=False, blank=False)

    def __str__(self):
        return self.name_exchange_office

    class Meta:
        verbose_name = "Ссписок обменных пунктов"
        verbose_name_plural = "Списки обменных пунктов"


class Currencies(models.Model):
    id_currency = models.CharField(max_length=100, verbose_name="ID валюты", null=False, blank=False)
    name_currency = models.CharField(max_length=100, verbose_name="Название валюты", null=False, blank=False)

    def __str__(self):
        return self.id_currency

    class Meta:
        verbose_name = "Список валют в формате"
        verbose_name_plural = "Списки валют в формате"


class Rates(models.Model):
    name_rate_received_exchange = models.CharField(max_length=100, verbose_name="Получаемой валюты", null=False, blank=False)
    name_rate_given_exchange = models.CharField(max_length=100, verbose_name="Отдаваемой валюты", null=False, blank=False)
    rate_given_exchange = models.CharField(max_length=100, verbose_name="Курс отдаю", null=False, blank=False)
    rate_received_exchange = models.CharField(max_length=100, verbose_name="Курс получаю", null=False, blank=False)
    reviews = models.CharField(max_length=255, verbose_name="Отзывы", null=False, blank=False)
    exchanges = models.ForeignKey(Exchanges, on_delete=models.PROTECT, verbose_name="Обменный пунк", null=False,
                                  blank=False)
    id_rate_received_exchange = models.ForeignKey(Currencies, verbose_name="ID пПолучаемой валюты",
                                                  related_name="currency_received", on_delete=models.PROTECT,
                                                  null=False, blank=False)
    id_rate_given_exchange = models.ForeignKey(Currencies, verbose_name="ID отдаваемой валюты",
                                               related_name="currency_given", on_delete=models.PROTECT,
                                               null=False, blank=False)

    def __str__(self):
        return f" {self.exchanges}"

    class Meta:
        verbose_name = "Список курсов обмена"
        verbose_name_plural = "Списки курсов обмена"


class DataSave(models.Model):
    name_exchange_office = models.CharField(max_length=100,
                                            verbose_name=" Обменник", null=False, blank=False)
    name_rate_received_exchange = models.CharField(max_length=100, verbose_name="Получаемой валюты", null=False,
                                                   blank=False)
    name_rate_given_exchange = models.CharField(max_length=100, verbose_name="Отдаваемой валюты", null=False,
                                                blank=False)
    rate_given_exchange = models.CharField(max_length=100, verbose_name="Курс отдаю", null=False, blank=False)
    rate_received_exchange = models.CharField(max_length=100, verbose_name="Курс получаю", null=False)
    reserve = models.CharField(verbose_name="резерв", max_length=100, null=False, blank=False)
    reviews = models.CharField(max_length=255, verbose_name="Отзывы", null=False, blank=False)
    total_exchanger = models.CharField(max_length=100, verbose_name=" количество обменников ", null=False, blank=False,
                                       default=0)
    sum_reserve = models.CharField(max_length=100, verbose_name="суммарный резерв со всех обменников ", null=False,
                                   blank=False, default=0)

    def __str__(self):
        return self.name_exchange_office

    class Meta:
        verbose_name = "Нужные Данных"
        verbose_name_plural = "Нужных Данных"
