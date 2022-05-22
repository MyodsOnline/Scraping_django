from django.shortcuts import render
from .models import Message


def let_boss_say(request):
    messages = Message.objects.all()
    context = {
        'title': 'Boss_says',
        'messages': messages
    }
    return render(request, 'boss_says/boss_says.html', context)
