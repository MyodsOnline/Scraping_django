from django.shortcuts import render
from .models import Message
from django.views.generic import ListView, DetailView


class BossSays(ListView):
    model = Message
    template_name = 'boss_says/boss_says.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Boss_says'
        return content


class BossSaysMessage(DetailView):
    model = Message


class BossSaysAuthor(ListView):
    template_name = 'boss_says/message_author.html'

    def get_queryset(self):
        return Message.objects.filter(author__slug=self.kwargs['slug'])


class BossSaysTag(ListView):
    pass


class Search(ListView):
    template_name = 'boss_says/search.html'

    def get_queryset(self):
        return Message.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        return content
