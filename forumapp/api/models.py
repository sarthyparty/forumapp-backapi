from django.db import models
from django.utils import timezone


class Question(models.Model):
    content = models.CharField(max_length=10000)
    time_asked = models.DateTimeField(default=timezone.now)
    email = models.EmailField(default="person@example.com")
    has_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class Answer(models.Model):
    content = models.CharField(max_length=10000)
    time_asked = models.DateTimeField(default=timezone.now)
    email = models.EmailField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return self.content