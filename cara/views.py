from django.shortcuts import render

from .forms import SelOffEls
from .models import BranchData

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
    context = {
        'title': 'Home page',
    }
    return render(request, 'home.html', context=context)


def mode_page(request):
    context = None
    return render(request, 'mode.html', context=context)


def ui_page(request):
    branches = BranchData.objects.all()
    context = {
        'title': 'Ui page',
        'branches': branches,
    }
    return render(request, 'ui.html', context=context)


def av_page(request):
    selected_name = request.GET.get('selected_name')
    return render(request, 'av.html', {'selected_name': selected_name})

