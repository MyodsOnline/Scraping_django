from django.db import models


class Zvk(models.Model):
    number = models.PositiveIntegerField()
    category = models.CharField(max_length=5)
    type = models.CharField(max_length=5)
    item = models.CharField(max_length=225)
    status = models.CharField(max_length=20)
    start = models.CharField(max_length=40)
    end = models.CharField(max_length=40)
    ready = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.number} - {self.item}'

