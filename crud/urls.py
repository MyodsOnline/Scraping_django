from django.urls import path

from .views import Posts_list, Post_Update

urlpatterns = [
    path('', Posts_list.as_view(), name='posts-list'),
    path('post/<slug:pk>', Post_Update.as_view(), name='post-update'),
]
