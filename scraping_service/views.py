from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().strftime('%H:%M %Y.%m.%d')
    context = {
        'title': 'HomePage',
        'date': date,
        'name': 'Кузнецов Андрей',
    }
    return render(request, 'index.html', context)
