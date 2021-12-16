from django.shortcuts import render
from django.views import generic

from .models import Exchanges


# вводим News в представление

class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'

    # назначаем список объектов "Infos" объекту "articles"
    # передаем объекты "News", как набор запросов для представления списка
    def get_queryset(self):
        return Exchanges.objects.all()
