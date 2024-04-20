from django.urls import path

from . import views
#app_name = "salesweb"
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("product/",view=views.product,name="product"),
    path("productAdd/",view=views.productAdd,name="productAdd"),
    path("productEdit/",view=views.productEdit,name="productEdit"),
    path("purchase/",view=views.purchase,name="purchase"),
    path("purchaseAdd/",view=views.purchaseAdd,name="purchaseAdd"),
    path("customer/",view=views.customer,name="customer"),
]