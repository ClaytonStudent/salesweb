from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    tax_number = models.CharField(max_length=200)
