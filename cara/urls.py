from django.urls import path

from .views import main_page, mode_page, home_page, ui_page, av_page

app_name = 'cara'
urlpatterns = [
    path('', home_page, name='carahome'),
    path('main/', main_page, name='main_page'),
    path('mode/', mode_page, name='mode_page'),
    path('ui/', ui_page, name='ui_page'),
    path('av/', av_page, name='av_page'),
]
