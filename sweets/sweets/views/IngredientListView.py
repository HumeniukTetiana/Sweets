from django.shortcuts import render, redirect
from sweets.NetworkHelper import NetworkHelper

def ingredient_list(request):
    if request.method == 'POST':
        ingredient_id = request.POST.get('ingredient_id')
        if ingredient_id:
            NetworkHelper.delete_ingredient(ingredient_id)
        return redirect('ingredient_list')

    ingredients = NetworkHelper.get_ingredients()
    return render(request, 'ingredient_list.html', {'ingredients': ingredients})
