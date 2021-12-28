import django_tables2 as tables

from .tasks import *
from .models import *


class DataTable(tables.Table):
    class Meta:
        model = DataSave
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id",)


class RatesTable(tables.Table):
    class Meta:
        model = Rates
        template_name = "django_tables2/bootstrap.html"
        exclude = (
            "id", "minimum_exchange_amount", "maximum_exchange_amount", "id_given_currency", "id_received_currency")


class ExchangesTable(tables.Table):
    class Meta:
        model = Exchanges
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", "WMBL",)
