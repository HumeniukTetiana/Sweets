from django.http import JsonResponse
from sweets.models import Product  # або ваш шлях до Product
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404

@require_GET
def get_products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id).values()
    return JsonResponse(list(products), safe=False)
