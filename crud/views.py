from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
import os
import json

from .models import Posts

SOURCE_DIR = os.path.dirname(__file__)
source_file = os.path.join(SOURCE_DIR, 'fixtures/Export_DataFrame.json')


class Posts_list(ListView):
    model = Posts
    fields = '__all__'
    template_name = 'crud.html'


class Post_Update(UpdateView):
    model = Posts
    fields = ['post_title', 'is_posted', 'equipment_mode']
    template_name = 'crud_update.html'
    success_url = '/crud/'


def json_file(request):
    json_data = json.load(open(source_file, encoding='utf-8'))
    context = {
        'json_data': json_data,
    }

    return render(request, 'json_out.html', context)
