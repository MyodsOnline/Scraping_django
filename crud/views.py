from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from .models import Posts


class Posts_list(ListView):
    model = Posts
    fields = '__all__'
    template_name = 'crud.html'


class Post_Update(UpdateView):
    model = Posts
    fields = ['post_title', 'is_posted', 'equipment_mode']
    template_name = 'crud_update.html'
    success_url = '/crud/'
