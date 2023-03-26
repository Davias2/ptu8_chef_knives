from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chef_knives/', views.index, name='index'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    #path('categories/', views.categories, name='categories'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
