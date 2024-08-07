from django.urls import path

from .views import main_page, mode_page, home_page, ui_page, av_page, get_times, index
from .extraction_util.walk_dir import get_fetch_response

app_name = 'cara'
urlpatterns = [
    path('', home_page, name='carahome'),
    path('main/', main_page, name='main_page'),
    path('mode/', mode_page, name='mode_page'),
    path('ui/', ui_page, name='ui_page'),
    path('av/', av_page, name='av_page'),
    path('time/', index, name='time'),
    path('get_times/', get_times, name='get_times'),
    path('copy_file/', get_fetch_response, name='copy_file'),
]
