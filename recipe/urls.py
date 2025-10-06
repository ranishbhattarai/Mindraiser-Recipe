from django.urls import path
from . import views
urlpatterns = [
    path('recipe/', views.recipe_list, name='recipe_list'),
    path('recipe/create/', views.recipe_create, name='recipe_create'),
    path('recipe/edit/<int:recipe_id>/', views.recipe_edit, name='edit_recipe'),
    path('recipe/delete/<int:recipe_id>/', views.recipe_delete, name='delete_recipe'),
]