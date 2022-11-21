from django.contrib import admin
from numpy import product
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name' ,'slug']
    prepopulated_fields={'slug': ('name',)}
###############
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['brand','part_number','name_part','code', 'quantity','price','in_stock','is_active','created','updated']
    list_filter= ['in_stock','is_active']
    list_editable= ['price','in_stock']
    prepopulated_fields={'slug': ('name_part',)}