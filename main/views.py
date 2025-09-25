from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """Главная страница"""
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME'
    }
    return render(request, 'main/index.html', context)

def about(request):
    """Страница 'О нас' """
    return HttpResponse("About")
