from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=255, default="",blank=True, null=True)
    barcodes = models.CharField(max_length=255, default="",blank=True, null=True)
    sku = models.CharField(max_length=255,default="",blank=True, null=True)
    location = models.CharField(max_length=255,default="",blank=True, null=True)
    quantity = models.IntegerField(default=0)
    isactive = models.BooleanField(default=True)
    unit = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)     
    note = models.TextField(default="",blank=True, null=True)    
    #lower_threshold = models.IntegerField(default=0,blank=True, null=True)
    #date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    #def barcode_list(self):
        # This method can be used to parse the comma-separated barcodes or handle JSON parsing
    #    return self.barcodes.split(',') if self.barcodes else []