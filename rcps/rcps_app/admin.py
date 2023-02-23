from django.contrib import admin
from .models import Recipe, Categories

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created']
    search_fields = ['category', 'name']
    readonly_field = ['created']



admin.site.register(Categories)
