from django.contrib.auth.models import User
from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id', ]
