from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    context = {
        'title': 'HomePage',
        'date': date,
        'name': '%username%',
    }
    return render(request, 'index.html', context)
