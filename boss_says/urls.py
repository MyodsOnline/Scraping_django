from django.urls import path

from .views import let_boss_say

urlpatterns = [
    path('', let_boss_say, name='boss_says')
]
