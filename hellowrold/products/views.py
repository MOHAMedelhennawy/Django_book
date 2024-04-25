from django.shortcuts import render
from .models import Car
# Create your views here.
def productsPageView(request):
    return render(request, 'products/products.html')

def productPageView(request):
    return render(request, 'products/product.html', {'cars': Car.objects.all()})