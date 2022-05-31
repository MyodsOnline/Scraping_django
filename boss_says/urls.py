from django.urls import path

from .views import BossSays, BossSaysMessage, BossSaysAuthor, BossSaysTag, Search

urlpatterns = [
    path('', BossSays.as_view(), name='boss_says'),
    path('message/<str:slug>/', BossSaysMessage.as_view(), name='boss_says_message'),
    path('author/<str:slug>/', BossSaysAuthor.as_view(), name='boss_says_author'),
    path('tag/<str:slug>/', BossSaysTag.as_view(), name='boss_says_tag'),
    path('search/', Search.as_view(), name='search'),
    # path('author/<int:pk>', BossNameSays.as_view(), name='boss_name_says'),
]
