from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    studentID = models.CharField(max_length=6)
    age = models.IntegerField()