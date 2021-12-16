from django.contrib import admin
from django.urls import path

from site_scraping.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),  # homepage
]
