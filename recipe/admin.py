from django.contrib import admin
from .models import Recipe

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'created_at']  # Fields to show in list
    search_fields = ['name', 'ingredients']  # Enable search in admin
    list_filter = ['created_at', 'prep_time']  # Filters in sidebar
    fields = ['name', 'ingredients', 'instructions', 'prep_time']  # Order fields in form