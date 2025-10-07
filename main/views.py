from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """Главная страница"""
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)

def about(request):
    """Страница 'О нас' """
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'lorem ipsum'
    }
    return render(request, 'main/about.html', context)
