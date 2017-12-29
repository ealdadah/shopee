import datetime
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from django.views.generic import ListView

from shop.models import Product, Category, Order


def index_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, "index.html", context)


def product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user = request.user
    order = Order()
    context = {
        'product': product,
    }
    if request.method == 'POST':

        order.product = product
        order.user = user
        order.total_cost = product.cost
        order.delivery_date = datetime.datetime.now() + datetime.timedelta(days=5)
        order.save()
    return render(request, 'product.html', context)


#
#
#
# def function_based_view(request):
#     """
#     Function based views take a request and are very explicit in the actions.
#     They have more code in some regards, but they go step by step in execution.
#     """
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('function')
#         else:
#             return HttpResponse('Error!')
#
#     context = {'form': form}
#
#     return render(request, 'my_template.html', context)
