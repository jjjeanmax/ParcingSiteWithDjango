from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', views.menu_view, name='index'),
    # path('data/', views.data_view, name='da'),
    # path('exchanges/', views.exhanges_view, name='exchange'),

    re_path('^data/?$', views.DataView.as_view(), name="data"),

    re_path('^exchanges/?$', views.ExchangesView.as_view(), name="exchanges_view"),

    re_path('^rates/?$', views.RatesView.as_view(), name="rates_view"),

]
