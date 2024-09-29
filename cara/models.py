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


class SwitchStatus(models.IntegerChoices):
    ON = 0, "ON"
    OFF = 1, "OFF"


class VetvType(models.IntegerChoices):
    LINE = 0, "Line"
    TRANS = 1, "Transformator"
    SWITCH = 2, "Switch"


class Vetv(models.Model):
    name = models.CharField(max_length=500)
    type = models.IntegerField(choices=VetvType.choices)
    status = models.IntegerField(choices=SwitchStatus.choices)
    start = models.IntegerField()
    end = models.IntegerField()
    parallel = models.IntegerField(default=0)
    P_start = models.FloatField()
    Q_start = models.FloatField()
    P_end = models.FloatField()
    Q_end = models.FloatField()
    I_start = models.FloatField()
    I_end = models.FloatField()
    rastr_index = models.IntegerField()

    def __str__(self):
        return f"Ветвь {self.start, self.end, self.parallel}: {self.name}"


class Node(models.Model):
    name = models.CharField(max_length=500)
    status = models.IntegerField(choices=SwitchStatus.choices, default=SwitchStatus.ON)
    number = models.IntegerField()
    U_calc = models.FloatField()
    P_gen = models.FloatField()
    P_load = models.FloatField()
    rastr_index = models.IntegerField()

    def __str__(self):
        return f"Узел №{self.number}: {self.name}"