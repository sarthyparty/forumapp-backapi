from django.db import models
from django.utils import timezone


class Question(models.Model):
    content = models.CharField(max_length=10000)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
