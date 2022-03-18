from django.shortcuts import render


def pcus_home(request):
    content = {'header': 'Fingrid Orders'}
    return render(request, 'pcus.html', content)