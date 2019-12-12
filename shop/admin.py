from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
