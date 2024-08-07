from django.db import models


class UIDMapping(models.Model):
    uid = models.CharField(max_length=100, unique=True, verbose_name='uid параметра в модели СК-11')
    title = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.uid} - {self.title}'


class DatetimeValues(models.Model):
    uid = models.ForeignKey(UIDMapping, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField()
    timeStamp2 = models.DateTimeField()
    qCode = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return f'{self.uid} - {self.timeStamp} - {self.value}'
