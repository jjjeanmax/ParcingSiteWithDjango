from rest_framework import serializers

from .models import *


class ExchangesSerializer(serializers.ModelSerializer):
    id_exchange_office = serializers.CharField(required=True)
    name_exchange_office = serializers.CharField(required=True)
    WMBL = serializers.CharField(required=True)
    reserve = serializers.CharField(required=True)

    class Meta:
        model = Exchanges

        fields = [
            'id_exchange_office',
            'name_exchange_office',
            'WMBL',
            'reserve',

        ]


class RatesSerializer(serializers.ModelSerializer):
    rate_given_exchange = serializers.CharField(required=True)
    rate_received_exchange = serializers.CharField(required=True)
    reviews = serializers.CharField(required=True)
    exchanges = serializers.CharField(required=True)

    class Meta:
        model = Rates
        fields = [
            'rate_given_exchange',
            'rate_received_exchange',
            'reviews',
            'exchanges',

        ]


class DataSerializer(serializers.ModelSerializer):
    name_exchange_office = serializers.CharField(required=True)
    reserve = serializers.CharField(required=True)
    rate_given_exchange = serializers.CharField(required=True)
    rate_received_exchange = serializers.CharField(required=True)
    reviews = serializers.CharField(required=True)
    total_exchanger_given = serializers.IntegerField(required=True)
    total_exchanger_received = serializers.IntegerField(required=True)
    sum_reserve_given = serializers.IntegerField(required=True)
    sum_reserve_received = serializers.IntegerField(required=True)

    class Meta:
        model = DataSave

        fields = [
            'name_exchange_office',
            'rate_given_exchange',
            'rate_received_exchange',
            'reviews',
            'reserve',
            'sum_reserve_received',
            'sum_reserve_given',
            'total_exchanger_received',
            'total_exchanger_given'

        ]
