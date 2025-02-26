from django.urls import path

from .views import srdk_home_page

app_name = 'srdk'
urlpatterns = [
    path('', srdk_home_page, name='srdkhome'),
]
