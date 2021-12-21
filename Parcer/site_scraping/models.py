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
        verbose_name = "список обменных пунктов"
        verbose_name_plural = "список обменных пунктов"
        unique_together = ['id_exchange_office', 'name_exchange_office', 'WMBL', 'reserve']


class Rates(models.Model):
    rate_given_exchange = models.CharField(max_length=100, verbose_name="Курс отдаю", null=False, blank=False)
    rate_received_exchange = models.CharField(max_length=100, verbose_name="Курс получаю", null=False, blank=False)
    reviews = models.CharField(max_length=255, verbose_name="Отзывы", null=False, blank=False)
    exchanges = models.ForeignKey(Exchanges, on_delete=models.PROTECT, verbose_name="Обменного пунк", null=False,
                                  blank=False)

    def __str__(self):
        return f" {self.exchanges}"

    class Meta:
        verbose_name = " список курсов обмена"
        verbose_name_plural = " список курсов обмена"
        unique_together = ['rate_given_exchange', 'rate_received_exchange', 'reviews', 'exchanges']


class ExchangesRates(models.Model):
    rates = models.ForeignKey(Rates, on_delete=models.CASCADE, verbose_name="Kурс обмена")
    exchanges = models.ForeignKey(Exchanges, on_delete=models.CASCADE, verbose_name="Oбменных пунктов")


class DataSave(models.Model):
    name_exchange_office = models.CharField(max_length=100,
                                            verbose_name=" Обменник", null=False, blank=False)
    rate_given_exchange = models.CharField(max_length=100, verbose_name="Курс отдаю", null=False, blank=False)
    rate_received_exchange = models.CharField(max_length=100, verbose_name="Курс получаю", null=False)
    reserve = models.CharField(verbose_name="резерв", max_length=100, null=False, blank=False)
    reviews = models.CharField(max_length=255, verbose_name="Отзывы", null=False, blank=False)
    total_exchanger_given = models.CharField(max_length=100, verbose_name=" количество обменников отдаю", null=False, blank=False,
                                                default=0)
    total_exchanger_received = models.CharField(max_length=100, verbose_name=" количество обменников получаю", null=False,
                                                   blank=False, default=0)
    sum_reserve_given = models.CharField(max_length=100, verbose_name="суммарный резерв со всех обменников отдаю", null=False,
                                            blank=False, default=0)
    sum_reserve_received = models.CharField(max_length=100, verbose_name="суммарный резерв со всех обменников получаю")

    def __str__(self):
        return self.name_exchange_office

    class Meta:
        verbose_name = "Нужные Данных"
        verbose_name_plural = "Нужные Данных"

