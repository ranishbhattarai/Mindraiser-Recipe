from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipe_lists.html', context)

def recipe_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        instructions = request.POST.get('instructions')
        ingredients = request.POST.get('ingredients')
        prep_time = request.POST.get('prep_time')

        Recipe.objects.create(
            name=name,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time,
        )

        return redirect('recipe_list')

    return render(request, 'recipe_create.html')

def recipe_edit(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == 'POST':
        recipe.name = request.POST.get('name')
        recipe.instructions = request.POST.get('instructions')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.prep_time = request.POST.get('prep_time')
        recipe.save()
        return redirect('recipe_list')

    context = {
        'recipe': recipe,
    }
    return render(request, 'recipe_edit.html', context)

def recipe_delete(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipe_delete.html', context)