from django.urls import path

from .views import date_view, get_pbr_data_view, svg_data_view

app_name = 'ck11'

urlpatterns = [
    path('', date_view, name='ck_home'),
    path('result/', get_pbr_data_view, name='ck_result'),
    path('svg/', svg_data_view, name='svg'),
]
