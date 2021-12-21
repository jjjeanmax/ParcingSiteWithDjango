import json

from .models import *


#
#
# @shared_task(serializer='json',bind=True, acks_late=True)
# def scrap_rates():
#     rates_list = []
#     try:
#         with open('code/rates.json', 'r') as rt:
#             data_rt = json.load(rt)
#             for i in range(len(data_rt)):
#                 r_data = data_rt[i][1].split(';')
#                 rate_given_exchange = r_data[1]
#                 rate_received_exchange = r_data[2]
#                 reviews = r_data[4]
#                 exchanges = r_data[9]
#
#         rates = {
#             'Курс отдаю': rate_given_exchange,
#             'Курс получаю': rate_received_exchange,
#             'Отзывы': reviews,
#             'Обменного пункта': exchanges
#
#         }
#
#         # добавляем "rates_list и exchanges_list" с каждым объектом "rates exch"
#         rates_list.append(rates)
#         print('Finished scraping ')
#         return save_rates(rates_list)
#
#     except Exception as e:
#         print('The scraping job failed. See exception:')
#         print(e)
#
#
# @shared_task(serializer='json',bind=True, acks_late=True)
# def save_rates(rates_list):
#     print('Rate Starting')
#     new_count = 0
#
#     for rates in rates_list:
#         try:
#             rates = Rates(
#                 rate_given_exchange=rates['Курс отдаю'],
#                 rate_received_exchange=rates['Курс получаю'],
#                 reviews=rates['Отзывы'],
#             )
#             rates.save()
#             new_count += 1
#             exchanges = Exchanges.objects.values('name_exchange_office')
#             rates.exchanges.add(list(exchanges)[1])
#         except Exception as e:
#             print('failed at rates is none')
#             print(e)
#             break
#
#     return print('finished')


# def get_queryset():
#     data_dict = {}
#     qs_exch = Exchanges.objects.values("name_exchange_office", "reserve")
#     qs_rate = Rates.objects.values("rate_given_exchange", "rate_received_exchange", "reviews")
#
#     for val in qs_exch:
#         data_dict["name_exchange_office"] = val['name_exchange_office']
#         data_dict["reserve"] = val['reserve']
#     for qs in qs_rate:
#         data_dict["rate_given_exchange"] = qs['rate_given_exchange']
#         data_dict["rate_received_exchange"] = qs['rate_received_exchange']
#         data_dict["reviews"] = qs['reviews']
#         data_dict["total_exchanger_given"] = Rates.objects.values('exchanges__name_exchange_office').order_by(
#             "rate_given_exchange").count()
#         data_dict["total_exchanger_received"] = Rates.objects.values(
#             'exchanges__name_exchange_office').order_by(
#             "rate_received_exchange").count()
#         data_dict["sum_reserve_given"] = Rates.objects.values('exchanges__name_exchange_office').order_by(
#             "exchanges__id_exchange_office").aggregate(Sum('exchanges__reserve'))
#         data_dict["sum_reserve_received"] = Rates.objects.values(
#             'exchanges__name_exchange_office').order_by("rate_received_exchange").aggregate(
#             Sum('exchanges__reserve'))
#     return data_dict




# @shared_task
# def save_rates(rates_list):
#     print('Starting Rates')
#     new_count = 0
#     for rat in rates_list:
#         try:
#             rates = Rates(
#                 rate_given_exchange=rat['Курс отдаю'],
#                 rate_received_exchange=rat['Курс получаю'],
#                 reviews=rat['Отзывы'],
#             )
#             rates.save()
#             qs = Exchanges.objects.all()
#
#             new_count += 1
#         except Exception as e:
#             print('failed at exchanges is none')
#             print(e)
#             break
#
#     return print('finished')
#
#
# @shared_task(serializer='json')
# def save_function():
#     article_list = []
#     with open('code/bm_rates.dat.json', 'r') as fp:
#         data = json.load(fp)
#         for i in range(len(data)):
#             r_data = data[i][1].split(';')
#             rate_given_exchange = r_data[1]
#             rate_received_exchange = r_data[2]
#             reviews = r_data[4]
#             exchanges = r_data[9]
#
#     try:
#         rates = {
#             'Курс отдаю': rate_given_exchange,
#             'Курс получаю': rate_received_exchange,
#             'Отзывы': reviews,
#             'Обменного пункта': exchanges
#
#         }
#         # добавляем "article_list" с каждым объектом "article"
#         article_list.append(rates)
#         print('Finished scraping the articles')
#
#     except Exception as e:
#         print('The scraping job failed. See exception:')
#         print(e)
#
#     new_count = 0
#
#     for article in article_list:
#         try:
#             rates = Rates(
#                 rate_given_exchange=article['Курс отдаю'],
#                 rate_received_exchange=article['Курс отдаю'],
#                 received_currency_reserve=article['Курс получаю'],
#                 reviews=article['Отзывы'],
#                 exchanges=article['ID обменного пункта'],
#             )
#             rates.save()
#             new_count += 1
#         except Exception as e:
#             print('failed at latest_article is none')
#             print(e)
#             break
#
#     return print('finished')

# @shared_task(bind=True, serializer='json')
# def to_save(self, qs, dat_dict, el=None):
#     for k, v in dat_dict.items():
#         data = qs(el, k=v)
#         data.save()


# @shared_task
# def get_queryset():
#     data_dict = {}
#     qs_exch = Exchanges.objects.values("name_exchange_office", "reserve")
#     qs_rate = Rates.objects.values("rate_given_exchange", "rate_received_exchange", "reviews")
#
#     for val in qs_exch:
#         data_dict["name_exchange_office"] = val['name_exchange_office']
#         data_dict["reserve"] = val['reserve']
#     for qs in qs_rate:
#         data_dict["rate_given_exchange"] = qs['rate_given_exchange']
#         data_dict["rate_received_exchange"] = qs['rate_received_exchange']
#         data_dict["reviews"] = qs['reviews']
#         data_dict["total_exchanger_given"] = Rates.objects.values('exchanges__name_exchange_office').order_by(
#             "rate_given_exchange").count()
#         data_dict["total_exchanger_received"] = Rates.objects.values(
#             'exchanges__name_exchange_office').order_by(
#             "rate_received_exchange").count()
#         data_dict["sum_reserve_given"] = Rates.objects.values('exchanges__name_exchange_office').order_by(
#             "exchanges__id_exchange_office").aggregate(Sum('exchanges__reserve'))
#         data_dict["sum_reserve_received"] = Rates.objects.values(
#             'exchanges__name_exchange_office').order_by("rate_received_exchange").aggregate(
#             Sum('exchanges__reserve'))
#     return data_dict





#

# class UpdateDataView(ListView, CreateView):
#     model = DataSave
#     fields = '__all__'
#     # serializer_class = DataSerializer
#     context_object_name = 'data'
#     template_name = "statement/base2.html"
#
#     def get_queryset(self):
#         data = DataSave.objects.all()
#         if len(data) == 0:
#             data_dict = {}
#             qs_exch = Exchanges.objects.values("name_exchange_office", "reserve")
#             qs_rate = Rates.objects.values("rate_given_exchange", "rate_received_exchange", "reviews")
#
#             for val in qs_exch:
#                 data_dict["name_exchange_office"] = val['name_exchange_office']
#                 data_dict["reserve"] = val['reserve']
#             for qs in qs_rate:
#                 data_dict["rate_given_exchange"] = qs['rate_given_exchange']
#                 data_dict["rate_received_exchange"] = qs['rate_received_exchange']
#                 data_dict["reviews"] = qs['reviews']
#                 data_dict["total_exchanger_given"] = Rates.objects.values('exchanges__name_exchange_office').order_by(
#                     "rate_given_exchange").count()
#                 data_dict["total_exchanger_received"] = Rates.objects.values(
#                     'exchanges__name_exchange_office').order_by(
#                     "rate_received_exchange").count()
#                 data_dict["sum_reserve_given"] = Rates.objects.values('exchanges__name_exchange_office').order_by(
#                     "exchanges__id_exchange_office").aggregate(Sum('exchanges__reserve'))
#                 data_dict["sum_reserve_received"] = Rates.objects.values(
#                     'exchanges__name_exchange_office').order_by("rate_received_exchange").aggregate(
#                     Sum('exchanges__reserve'))
#                 print(len(data_dict))
#
#                 # data = async_to_sync(serialize('json', to_save.apply_async((DataSave, data_dict,))))
#                 # serializer_context = {
#                 #     'request': data_dict,
#                 # }
#                 # serializer = DataSerializer(data_dict, context=serializer_context, data=data_dict)
#                 # return Response({'announce': data})
#         return HttpResponseRedirect('index')
#
#
# class UpdateExchangesView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'myApp/announce_detail.html'
#
#     @staticmethod
#     def put(request):
#         try:
#             with open('code/bm_exch.dat.json', 'r', ) as ex:
#                 data_exh = json.load(ex)
#
#                 for i in range(len(data_exh)):
#                     id_exchange_office = data_exh[i][0]
#                     e_data = data_exh[i][1].split(';')
#                     name_exchange_office = e_data[0]
#                     WMBL = e_data[2]
#                     reserve = e_data[3]
#                     exch = {
#                         " id_exchange_office": id_exchange_office,
#                         "name_exchange_office": name_exchange_office,
#                         "WMBL": WMBL,
#                         "reserve": reserve
#
#                     }
#                     print(exch)
#                     try:
#                         data = async_to_sync(serialize('json', to_save.apply_async((Exchanges, exch,))))
#
#                         return HttpResponse(data=data, content_type="application/json")
#                     except Exception as e:
#                         print(e)
#                         return Response('failed', status=404)
#
#         except Exception as e:
#             print('The scraping job failed. See exception:')
#             print(e)
#             return Response('failed', status=503)
#
#
# class UpdateRatesView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'myApp/announce_detail.html'
#
#     @staticmethod
#     def put(request):
#         try:
#             with open('code/bm_rates.dat.json', 'r', ) as rt:
#                 data_rt = json.load(rt)
#
#                 for i in range(len(data_rt)):
#                     r_data = data_rt[i][1].split(';')
#                     rate_given_exchange = r_data[2]
#                     rate_received_exchange = r_data[3]
#                     reviews = r_data[5]
#                     exchanges = r_data[1]
#                     rat = {
#                         'Курс отдаю': rate_given_exchange,
#                         'Курс получаю': rate_received_exchange,
#                         'Отзывы': reviews,
#                     }
#                     try:
#                         exchange = Exchanges.objects.filter(id_exchange_office=exchanges).first()
#
#                         data = async_to_sync(serialize('json', to_save.apply_async((Rates, rat, exchange))))
#
#                         return HttpResponse(data=data, content_type="application/json")
#                     except Exception as e:
#                         print(e)
#                         return Response('failed', status=404)
#         except Exception as e:
#             print('The scraping job failed. See exception:')
#             print(e)
#             return Response('failed', status=503)



#
# @shared_task()
# def save_exchanges(exchanges_list):
#     print('Starting Exchanges')
#     new_count = 0
#     for exch in exchanges_list:
#         print(exch)
#         try:
#             exchange = Exchanges(
#                 id_exchange_office=exch['ID обменного пункта'],
#                 name_exchange_office=exch['Название обменного пункта'],
#                 WMBL=exch['WMBL'],
#                 reserve=exch['резерв'],
#             )
#             qs = Exchanges.objects.all()
#             filt = []
#             for q in qs :
#                 if q not in filt:
#                     exchange.save()
#                     filt.append(q)
#                     new_count += 1
#         except Exception as e:
#             print('failed at exchanges is none')
#             print(e)
#             break
#
#     return print('finished')





# def data_view(request):
#     template = loader.get_template('statement/statement_template.html')
#     context = get_queryset()
#     return HttpResponse(template.render(context, request))
#
#
# def exhanges_view(request):
#     template = loader.get_template('statement/statement_template.html')
#     context = scrap_exchanges()
#     return HttpResponse(template.render(context, request))


# re_path('^dat/?$', views.HomePageView.as_view(),
#         name="home"
#              ""),
# re_path('^ex/?$', views.UpdateExchangesView.as_view(),
#         name="ex"),
# re_path('^rt/?$', views.UpdateRatesView.as_view(),
#         name="rt"),


#
# class DaTable(tables.Table):
#     class Meta:
#         model = DataSave
#         template_name = "django_tables2/bootstrap.html"
#         exclude = ("id", "WMBL",)

#
# def sav_ex():
#     try:
#         exch = scrap_exchanges()
#
#         exchange = Exchanges(
#             id_exchange_office=exch['ID обменного пункта'],
#             name_exchange_office=exch['Название обменного пункта'],
#             WMBL=exch['WMBL'],
#             reserve=exch['резерв'],
#         )
#         exchange.save()
#         return Exchanges
#     except Exception:
#         pass
#
#
# sav_ex()
#
#
# def sav_rat():
#     try:
#         rat = scrap_rates()
#         exchanges = rat['Обменного пунк']
#         exchange = Exchanges.objects.filter(id_exchange_office=exchanges).first()
#         rates = Rates(
#             rate_given_exchange=rat['Курс отдаю'],
#             rate_received_exchange=rat['Курс получаю'],
#             reviews=rat['Отзывы'],
#             exchanges=exchange
#         )
#         rates.save(force_insert=True)
#         return Rates
#     except Exception:
#         pass
#
#
# sav_rat()
#
#
# def saver():
#     try:
#         a = get_queryset()
#         print(a['total_exchanger_given'])
#
#         rates = DataSave(name_exchange_office=a['name_exchange_office'],
#                          reserve=a['reserve'],
#                          rate_given_exchange=a['rate_given_exchange'],
#                          rate_received_exchange=a['rate_received_exchange'],
#                          reviews=a['reviews'],
#                          total_exchanger_given=a['total_exchanger_given'],
#                          total_exchanger_received=a['total_exchanger_received'],
#                          sum_reserve_given=a['sum_reserve_given']['exchanges__reserve__sum'],
#                          sum_reserve_received=a['sum_reserve_received']['exchanges__reserve__sum'],
#
#                          )
#         rates.save()
#         return DataSave
#     except Exception:
#         pass
#
#
# saver()