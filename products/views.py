from django.shortcuts import render, get_object_or_404
from sweets.models import Product
from products.forms import ProductForm
from django.shortcuts import redirect

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('ProductDetails', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'ProductCreateUpdate.html', {'form': form, 'is_edit': False})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ProductDetails.html', {'product': product})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'ProductList.html', {'products': products})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('ProductDetail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'ProductCreateUpdate.html', {'form': form, 'is_edit': True})
