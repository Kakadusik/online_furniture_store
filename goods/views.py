from django.shortcuts import render


# Create your views here.
def catalog(request):
    """ Страница каталога товаров"""
    return render(request, 'goods/catalog.html')

def product(request):
    """ Страница товара """
    return render(request, 'goods/product.html')
