from django.db import models
from django.core.mail import *
from educom.password import *
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150, unique=True)
    username = models.CharField(max_length=50, unique=True)
    pasw = models.TextField()
    phone = models.CharField(max_length=50, unique=True)
    SecKey = models.TextField()

    def save(self, *args, **kwargs):
        secKey = genSecKey(20)
        self.SecKey = secKey
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class UserRole(models.Model):

    ROLL = (
        ('stu_12', 'Student - 12'),
        ('stu_11', 'Student - 11'),
        ('stu_8_10', 'Student - 8 to 10'),
    )

    username = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=20, choices=ROLL)

    def __str__(self):
        return self.username
