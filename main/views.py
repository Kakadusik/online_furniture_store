from django.shortcuts import render

from goods.models import Categories


# Create your views here.
def index(request):
    """Главная страница"""

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
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
