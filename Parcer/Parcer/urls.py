from django.contrib import admin
from django.urls import path, include

from Parcer.yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('site_scraping.urls')),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui'),
]
