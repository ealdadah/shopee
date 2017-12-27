from django.shortcuts import render

from django.views.generic import ListView

from shop.models import Product, Category


def index_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, "index.html", context)
