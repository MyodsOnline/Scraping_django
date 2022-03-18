from django.shortcuts import render

from .models import Zvk


def home(request):
    zvk = Zvk.objects.all()
    context = {
        'title': 'HomePage',
        'zvk': zvk
    }
    return render(request, 'zvk.html', context)
