from django.db import models
from transliterate import slugify


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='City')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.name} | {self.slug}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    language = models.CharField(max_length=50, verbose_name='Code language')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Code language'
        verbose_name_plural = 'Code languages'

    def __str__(self):
        return self.language

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.language))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Job title')
    company = models.CharField(max_length=250, verbose_name='Company')
    description = models.TextField(verbose_name='Vacancy description')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='City')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Language')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Adding timestamp')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.title
