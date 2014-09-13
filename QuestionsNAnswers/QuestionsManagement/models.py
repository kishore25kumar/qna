from django.db import models

# Create your models here.


class Exam(models.Model):
    title = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()


class Question(models.Model):
    examForeignKey = models.ForeignKey(Exam)
    questionText = models.TextField()
    optionA = models.TextField()
    optionB = models.TextField()
    optionC = models.TextField()
    optionD = models.TextField()

class Answer(models.Model):
    questionForeignKey = models.ForeignKey(Question)
    answer = models.TextField()


