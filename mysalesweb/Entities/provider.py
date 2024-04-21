from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    tax_number = models.CharField(max_length=200)
