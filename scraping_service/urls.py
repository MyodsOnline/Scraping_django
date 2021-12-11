from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('scrap/', include('scraping.urls')),
    path('crud/', include('crud.urls')),
]
