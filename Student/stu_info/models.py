from django.db import models

# Create your models here.
class Students(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    address = models.TextField()
    dob = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    eligible = models.BooleanField()