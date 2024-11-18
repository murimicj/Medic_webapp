from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password=models.CharField(max_length=50)
    age = models.IntegerField()
    yob = models.DateField()
    def __str__(self):
        return self.fullname

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    quantity = models.IntegerField()
    def __str__(self):
        return self.name
