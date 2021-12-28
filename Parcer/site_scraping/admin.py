from django.contrib import admin

from .models import *


@admin.register(DataSave)
class AdminData(admin.ModelAdmin):
    list_display = ['name_exchange_office', 'rate_given_exchange', 'rate_received_exchange',
                    'reserve', 'reviews', 'total_exchanger',
                    'sum_reserve', ]


@admin.register(Rates)
class AdminRates(admin.ModelAdmin):
    list_display = ("rate_given_exchange", "rate_received_exchange", "reviews", "exchanges")

    def exchanges(self, obj):
        return "\n".join([a.name_exchange_office for a in obj.exchanges_set.all()])


@admin.register(Exchanges)
class AdminExchanges(admin.ModelAdmin):
    list_display = ("id_exchange_office", "name_exchange_office", "WMBL", "reserve")
