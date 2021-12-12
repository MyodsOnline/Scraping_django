from django.shortcuts import render
from django.http import HttpResponse

from .models import City, Language, Vacancy


def main(request):
    cities_list = City.objects.all()
    lang_list = Language.objects.all()
    job_list = Vacancy.objects.all()
    context = {
        'title': 'It works',
        'cities_list': cities_list,
        'lang_list': lang_list,
        'job_list': job_list,
    }
    return render(request, 'scrap.html', context)
