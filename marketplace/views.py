from django.shortcuts import render
from django.http import Http404
from .models import Product


def main(request):

    all_products = Product.objects.all()
    data = {"all_products": all_products}

    return render(request, "marketplace/main.html", data)

def product_detail(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        raise Http404('Товар не найден')

    return render(request, "marketplace/product.html", {"product": product})
