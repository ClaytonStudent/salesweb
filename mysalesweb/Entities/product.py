from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    main_category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    uuId = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default="active")
    barcodes = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return self.product_name
