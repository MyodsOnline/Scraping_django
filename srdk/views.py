from django.shortcuts import render
from datetime import datetime
import pandas as pd


def srdk_home_page(request):
    data = datetime.now()
    context = {
        'data': data,
    }
    return render(request, 'srdk.html', context=context)
