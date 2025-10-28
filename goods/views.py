from django.shortcuts import render
from goods.models import Products


# Create your views here.
def catalog(request):
    """Страница каталога товаров"""
    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    """Страница товара"""
    return render(request, "goods/product.html")
