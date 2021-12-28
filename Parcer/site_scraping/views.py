from django.shortcuts import render
from django_tables2 import SingleTableView, LazyPaginator
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator

from rest_framework.views import APIView

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
    filterset_class = DataSave


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


class GetTotalOfficeView(APIView):

    @staticmethod
    def get(request):
        qs = Exchanges.objects.values('name_exchange_office').distinct()
        total = len(qs)

        qs_reserve = Exchanges.objects.values('name_exchange_office').annotate(
            dsum=Sum(Cast('reserve', output_field=FloatField())))

        summ = sum(q['dsum'] for q in qs_reserve)

        q = Rates.objects.values("exchanges__name_exchange_office"
                                 , "rate_received_exchange",
                                 "rate_given_exchange",
                                 "reviews",
                                 "exchanges__reserve", "name_rate_received_exchange", "name_rate_given_exchange")
        data = list(q)
        paginator = Paginator(data, 13)
        page = request.GET.get('page')
        d = paginator.get_page(page)
        return render(request, 'statement/table.html', {"d": d, 'total': total, 'summ': summ})
