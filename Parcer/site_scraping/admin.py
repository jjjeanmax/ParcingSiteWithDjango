from django.contrib import admin

from .models import Rates


@admin.register(Rates)
class AdminRates(admin.ModelAdmin):
    list_display = ['id_given_currency', 'id_received_currency', 'rate_given_exchange', 'rate_received_exchange',
                    'received_currency_reserve', 'reviews', 'minimum_exchange_amount', 'maximum_exchange_amount',
                    'city', 'exchanges']
