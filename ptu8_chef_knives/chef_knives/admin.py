from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description')
    llist_filter = ('name', 'price', 'stock')
    search_fields = ('name',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'data_ordered', 'status')
    list_filter = ('status',)
    search_fields = ('customer__username',)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'date_added')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'order']
    list_filter = ['order__customer']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)