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
        msg = f'''<div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
            <div style="margin:50px auto;width:70%;padding:20px 0">
              <div style="border-bottom:1px solid #eee">
                <a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">EduCom</a>
              </div>
              <p style="font-size:1.1em">Hi,</p>
              <p><b>{self.name}</b>&nbsp;&nbsp;Your username is</p>
              <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">{self.username}</h2><br>
              <h2>Create Password <a href="http://127.0.0.1:8000/forgot-pass/{self.username}/{secKey}">click here</a></h2><br>
              <p style="font-size:0.9em;">Regards,<br />EduCom</p>
              <hr style="border:none;border-top:1px solid #eee" />
              <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
                <p>EduCom</p>
                <p>Teacher - Samir Das.</p>
                <p>Location - Purnanagar</p>
              </div>
            </div>
          </div>'''
        mail = EmailMultiAlternatives(
            'Account Confirmation', msg, 'educom0075@gmail.com', ['shovanm50@gmail.com', f'{self.email}'],)
        mail.content_subtype = "html"
        mail.send()
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
