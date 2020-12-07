from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request):
    products = Product.objects.filter(available= True)
    pizza_category = get_object_or_404(Category, slug= 'pizza')
    pizza_products = products.filter(category = pizza_category)
    sushi_category = get_object_or_404(Category, slug= 'sushi')
    sushi_products = products.filter(category = sushi_category)  
    dessert_category = get_object_or_404(Category, slug= 'dessert')
    dessert_products = products.filter(category = dessert_category)  
    new_products = products.filter(new = True)    
    context ={
        'pizza': pizza_products,
        'sushi': sushi_products,      
        'dessert': dessert_products, 
        'new': new_products,           
    }    
    return render(request, 'pages/index.html',context)


def about(request):
    return render(request, 'pages/about.html')


def menu(request):
    products = Product.objects.filter(available= True)
    pizza_category = get_object_or_404(Category, slug= 'pizza')
    pizza_products = products.filter(category = pizza_category)
    sushi_category = get_object_or_404(Category, slug= 'sushi')
    sushi_products = products.filter(category = sushi_category)  
    dessert_category = get_object_or_404(Category, slug= 'dessert')
    dessert_products = products.filter(category = dessert_category) 
    cart_product_form = CartAddProductForm()
    context ={
        'pizza': pizza_products,
        'sushi': sushi_products,      
        'dessert': dessert_products,
        'cart_product_form': cart_product_form,       
    } 
    return render(request, 'pages/menu.html', context)


def blog(request):
    return render(request, 'pages/blog.html')


def contact(request):
    return render(request, 'pages/contact.html')


def elements(request):
    return render(request, 'pages/elements.html')
