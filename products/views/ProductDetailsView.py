from django.shortcuts import render
from sweets.models.ProductModel import Product
from django.shortcuts import render, get_object_or_404

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ProductDetails.html', {'product': product})
