from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'blade_length')


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.Cart)
admin.site.register(models.Category)