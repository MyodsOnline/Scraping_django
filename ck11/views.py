from django.shortcuts import render, redirect
from .models
import UIDMapping
from .utils.expotr_svg import return_svg_from_file
from .utils.get_pbr_api import get_pbr_get_table_ck11, get_local_uid_list


def date_view(request):
    return render(request, 'ck.html')


def get_pbr_data_view(request):
    if request.method == 'POST':
        date_end = request.POST.get('dateEnd')
        try:
            data = []
            get_objects = UIDMapping.objects.all()
            for el in get_objects:
                data.append(el.uid)
        except (Exception, ValueError):
            data = get_local_uid_list()

        if date_end:
            data_list, description = get_pbr_get_table_ck11(date_end, data)
            context = {
                'data_list': data_list,
                'description': description
            }
            return render(request, 'pbr.html', context)

          
def svg_data_view(request):
    try:
        svg_data = return_svg_from_file('output.svg')
    except FileNotFoundError:
        svg_data = f'Source is empty'
    context = {
        'svg_data': svg_data,
    }
    return render(request, 'svg.html', context)
