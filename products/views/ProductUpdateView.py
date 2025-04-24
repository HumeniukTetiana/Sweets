from products.forms import ProductForm
from django.shortcuts import render
from sweets.models.ProductModel import Product
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

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
