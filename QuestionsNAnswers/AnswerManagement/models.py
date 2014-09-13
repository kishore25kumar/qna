from django.db import models

# Create your models here.
from QuestionsManagement.models import Question


class Result(models.Model):
    userName = models.EmailField()
    answer = models.TextField()
    questionForeignKey = models.ForeignKey(Question)
    status = models.BooleanField()
