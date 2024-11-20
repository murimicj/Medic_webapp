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

class Patients(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    SHA_NO=models.IntegerField()
    age=models.IntegerField()
    yob=models.DateField()
    def __str__(self):
        return self.firstname

class Appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    date=models.DateTimeField()
    department=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name