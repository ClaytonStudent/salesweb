from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from .forms import ProductAddForm
from .Entities import product
from django.contrib import messages

def index(request):
    return render(request, 'mysalesweb/index.html')

def dashboard(request):
    return render(request, 'mysalesweb/dashboard.html')

def product(request):
    products = product.Product.objects.all()
    return render(request, 'mysalesweb/product.html', {'products': products})

def productAdd(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            messages.error(request, 'Form is invalid')
    else:     
        form = ProductAddForm()
    return render(request, 'mysalesweb/productAdd.html', {'form': form})


def productEdit(request):
    return render(request, 'mysalesweb/productEdit.html')

def purchase(request):
    return render(request, 'mysalesweb/purchase.html')

def purchaseAdd(request):
    return render(request, 'mysalesweb/purchaseAdd.html')

def customer(request):
    return render(request, 'mysalesweb/customer.html')

def searchAddSelect(request):
    return render(request, 'mysalesweb/searchAddSelect.html')