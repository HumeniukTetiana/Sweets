from django.shortcuts import render
from sweets.models.ProductModel import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'ProductList.html', {'products': products})

