from django.shortcuts import render
from django.http import JsonResponse

from .forms import SelOffEls
from .models import BranchData, Vetv, Node
from .extraction_util.walk_dir import scan_basedir, get_SMZU_file
from .utils import data_scan, time_scan
from .svg_module.expotr_svg import return_svg_from_file


def main_page(request):
    mass_name_elem = ['mass_name_elem_1', 'mass_name_elem_2', 'mass_name_elem_3']
    mass_rastr_result = ['mass_rastr_result_1']
    context = {'form': SelOffEls(),
               'mass_name_elem': mass_name_elem,
               'mass_rastr_result': mass_rastr_result,
               'range_arr': range(9),
               'status_but': 'selected_settings',
               }

    return render(request, 'main.html', context=context)


def home_page(request):
    previous_page = request.META.get('HTTP_REFERER', None)
    context = {
        'title': 'Home page',
        'previous_page': previous_page
    }
    return render(request, 'home.html', context=context)


def mode_page(request):
    context = None
    return render(request, 'mode.html', context=context)


def ui_page(request):
    branches = BranchData.objects.all()
    date_list = scan_basedir()
    context = {
        'title': 'Ui page',
        'branches': branches,
        'date_list': date_list,
    }
    return render(request, 'ui.html', context=context)


def bars_page(request):
    branches = BranchData.objects.all()
    context = {
        'title': 'Bars page',
        'branches': branches,
    }
    return render(request, 'bars.html', context=context)


def base_page(request):
    try:
        svg_data = return_svg_from_file('new_svg.svg')
    except FileNotFoundError:
        svg_data = f'Source is empty'
    smzu_file_name = get_SMZU_file()

    context = {
        'title': 'Base page',
        'smzu_file_name': smzu_file_name,
        'svg_data': svg_data,
    }
    return render(request, 'base_index.html', context=context)


def process_data(request):
    results = []
    if request.method == 'POST':
        data = request.POST.get('set_data', '')
        if data:
            for item in data.split(','):
                item = item.strip()
                if '__' in item:
                    ip, iq = item.split('__')
                    vetv_data = Vetv.objects.filter(
                        start=ip.replace('ip_', ''),
                        end=iq.replace('iq_', '')).values()
                    results.extend(list(vetv_data))
                else:
                    node_data = Node.objects.filter(number=item.replace('ny_', '')).values()
                    results.extend(list(node_data))
        else:
            results.append('Nothing to change')

    return render(request, 'tеmpp.html', {'title': 'Base page', 'results': results})


def av_page(request):
    selected_name = request.GET.get('selected_name')
    try:
        branch = BranchData.objects.get(name=selected_name)
    except:
        branch = None
    return render(request, 'av.html', {'branch': branch})


def get_times(request):
    selected_date = request.GET.get('date')
    times = time_scan(selected_date)
    return JsonResponse({'times': times})


def index(request):
    dates = data_scan()
    return render(request, 'temp.html', {'dates': dates})
