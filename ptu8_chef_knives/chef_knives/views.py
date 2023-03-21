from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Customer, Order, Cart, Category


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'home.html', context)

def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

def cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = []
    context = {
        'cart_items': cart_items
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        new_cart_item = Cart(user=request.user, product=product)
        new_cart_item.save()
    return redirect('cart')

def remove_from_cart(request, pk):
    cart_item = Cart.objects.get(id=pk)
    cart_item.delete()
    return redirect('cart')

def checkout(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        cart_items = Cart.objects.filter(user=request.user)
        order = Order.objects.create(customer=customer, status='P')
        for item in cart_items:
            order_item = OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
            item.delete()
        context = {
            'order': order
        }
        return render(request, 'checkout.html', context)
    else:
        return redirect('login')
