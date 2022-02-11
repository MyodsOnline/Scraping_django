from django.db import models


class Posts(models.Model):
    AVAILABLE_EQUIPMENT_MODES = [
        ('AP', 'аварийный ремонт'),
        ('TP', 'текущий ремонт'),
        ('XP', 'холодный резерв'),
        ('on', 'в работе'),
    ]

    post_title = models.CharField(max_length=300, unique=True)
    time = models.DateTimeField(auto_now_add=True)
    is_posted = models.BooleanField(default=False)
    equipment_mode = models.CharField(max_length=3, choices=AVAILABLE_EQUIPMENT_MODES, default='on')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.post_title
