from django.shortcuts import render
from sweets.models.ProductModel import Product
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
