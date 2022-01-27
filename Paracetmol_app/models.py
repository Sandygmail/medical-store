from django.db import models
from datetime import datetime

# Create your models here.


class Medical(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.login


class Registation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.mail
