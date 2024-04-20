from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'mysalesweb/index.html')

def dashboard(request):
    return render(request, 'mysalesweb/dashboard.html')

def product(request):
    return render(request, 'mysalesweb/product.html')

def productAdd(request):
    return render(request, 'mysalesweb/productAdd.html')

def productEdit(request):
    return render(request, 'mysalesweb/productEdit.html')

def purchase(request):
    return render(request, 'mysalesweb/purchase.html')

def purchaseAdd(request):
    return render(request, 'mysalesweb/purchaseAdd.html')

def customer(request):
    return render(request, 'mysalesweb/customer.html')