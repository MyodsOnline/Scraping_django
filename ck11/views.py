from django.shortcuts import render

from .models import UIDMapping
from .utils.get_pbr_api import get_pbr_get_table_ck11


def date_view(request):
    return render(request, 'ck.html')


def get_pbr_data_view(request):
    if request.method == 'POST':
        date_end = request.POST.get('dateEnd')
        try:
            data = UIDMapping.objects.all()
            if not data:
                raise ValueError
        except (Exception, ValueError):
            data = None

        if date_end:
            data_list = get_pbr_get_table_ck11(date_end, data)
            context = {
                'data_list': data_list,
            }
            return render(request, 'pbr.html', context)
