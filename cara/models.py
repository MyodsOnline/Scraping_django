from django.db import models


class BranchData(models.Model):
    ip = models.IntegerField()
    iq = models.IntegerField()
    np = models.IntegerField()
    name = models.CharField(max_length=500)
    id_sk11 = models.TextField()
    svg_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
