from django.contrib import admin
from .Entities import product
from .Entities import address
from .Entities import customer
from .Entities import productInfo
from .Entities import provider

# Register your models here.
admin.site.register(product.Product)
admin.site.register(address.Address)
admin.site.register(customer.Customer)
admin.site.register(productInfo.ProductInfo)
admin.site.register(provider.Provider)