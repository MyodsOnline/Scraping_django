from django.shortcuts import render
from django.http import HttpResponse

from .models import City, Language


def main(request):
    cities = City.objects.all()
    context = {
        'title': 'It works',
        'cities_list': cities,
    }
    return render(request, 'scrap.html', context)
