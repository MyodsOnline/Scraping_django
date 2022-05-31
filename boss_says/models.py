from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class MessageAuthor(models.Model):
    boss_name = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Boss name')
    slug = models.SlugField(max_length=30, unique=True, verbose_name='Boss slug')

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('boss_says_author', kwargs={'slug': self.slug})


class MessageTag(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Message tag')
    slug = models.SlugField(max_length=30, unique=True, verbose_name='Tag slug')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('boss_says_tag', kwargs={'slug': self.slug})


class Message(models.Model):
    author = models.ForeignKey(MessageAuthor, on_delete=models.CASCADE, verbose_name='Message author')
    title = models.CharField(max_length=200, verbose_name='Message title')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Message slug')
    text = models.TextField(verbose_name='Message text', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    updated = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(MessageTag, blank=True, related_name='messages', verbose_name='meg tag')
    image = models.ImageField(upload_to='media/%Y/images', verbose_name='Message image', blank=True)
    file = models.FileField(upload_to='media/%Y/images', verbose_name='Message image', blank=True)
    link = models.URLField(verbose_name='Message URL', blank=True)
    active = models.BooleanField(default=True, verbose_name='Is active')

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('boss_says_message', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
