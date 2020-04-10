from django.db import models
from django.core import validators
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, validators=[validators.MinLengthValidator(3)])
    page = models.IntegerField()
    price = models.FloatField()


class User2(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)