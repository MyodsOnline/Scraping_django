from django.shortcuts import render


def home(request):
    context = {
        'title': 'HomePage',
        'name': 'zvk_page',
    }
    return render(request, 'zvk.html', context)
