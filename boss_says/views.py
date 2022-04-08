from django.shortcuts import render

def let_boss_say(request):
    context = {
        'title': 'Boss_says',
    }
    return render(request, 'boss_says.html', context)
