from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Message author')
    title = models.CharField(max_length=200, verbose_name='Message title')
    text = models.TextField(verbose_name='Message text', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/%Y', verbose_name='Message image', blank=True)
    link = models.URLField(verbose_name='Message URL', blank=True)
    active = models.BooleanField(default=True, verbose_name='Is active')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
