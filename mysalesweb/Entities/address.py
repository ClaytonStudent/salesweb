from django.db import models

from mysalesweb.Entities.customer import Customer
from mysalesweb.Entities.provider import Provider


class Address(models.Model):
    street = models.CharField(max_length=200)
    house_nr = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)

    providers = models.ForeignKey(
        Provider,
        related_name='providers',
        on_delete=models.CASCADE
    )

    customers = models.ForeignKey(
        Customer,
        related_name='customers',
        on_delete=models.CASCADE
    )
