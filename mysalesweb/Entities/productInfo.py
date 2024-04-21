from django.db import models

from mysalesweb.Entities.product import Product


class ProductInfo(models.Model):
    store_location = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=100, blank=True, null=True)
    discount = models.DecimalField(decimal_places=5, max_digits=8)
    tax = models.DecimalField(decimal_places=5, max_digits=8)
    commission_rate = models.DecimalField(decimal_places=5, max_digits=8)
    price = models.DecimalField(decimal_places=5, max_digits=8, default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    note = models.TextField(default="", blank=True, null=True)
    description = models.TextField(default="", blank=True, null=True)
    data_created = models.DateTimeField(auto_now_add=True)
    product_infos = models.ForeignKey(
        Product,
        related_name='product_infos',
        on_delete=models.CASCADE
    )



