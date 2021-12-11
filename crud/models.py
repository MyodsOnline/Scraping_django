from django.db import models


class Posts(models.Model):
    post_title = models.CharField(max_length=300, unique=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.post_title
