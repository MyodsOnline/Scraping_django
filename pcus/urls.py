from django.urls import path

from .views import pcus_home


urlpatterns = [
    path('', pcus_home, name='pcus'),
]
