from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150, unique=True)
    username = models.CharField(max_length=50, unique=True)
    pasw = models.CharField(max_length=150)
    phone = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username


class UserRole(models.Model):
    
    ROLL = (
        ('stu_12', 'Student - 12'),
        ('stu_11', 'Student - 11'),
        ('stu_8_10', 'Student - 8 to 10'),
    )

    username = models.CharField(max_length=50,unique=True)
    role = models.CharField(max_length=20,choices=ROLL)

    def __str__(self):
        return self.username
