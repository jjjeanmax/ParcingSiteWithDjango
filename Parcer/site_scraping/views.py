import json

from asgiref.sync import async_to_sync
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import UpdateView, CreateView, ListView
from django_tables2 import SingleTableView, LazyPaginator
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum


from .serializers import ExchangesSerializer, DataSerializer
from .tasks import *
from .models import *
from .tables import *


# TODO: для фронта использовать vue + axios / js + bootstrap

# вводим News в представление

def menu_view(request):
    template = loader.get_template('statement/menu.html')
    return HttpResponse(template.render({'': ''}, request))


class DataView(SingleTableView):
    model = DataSave
    table_class = DataTable
    paginator_class = LazyPaginator
    template_name = "statement/statement_template.html"


class ExchangesView(SingleTableView):
    model = Exchanges
    table_class = ExchangesTable
    paginator_class = LazyPaginator
    template_name = "statement/statement_template.html"


class RatesView(SingleTableView):
    model = Rates
    table_class = RatesTable
    paginator_class = LazyPaginator
    template_name = "statement/statement_template.html"
