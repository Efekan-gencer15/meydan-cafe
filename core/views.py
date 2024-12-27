from django.shortcuts import render
from menu.models import MenuItem, Category

def home(request):
    featured_items = MenuItem.objects.filter(is_available=True)[:6]
    return render(request, 'core/home.html', {
        'featured_items': featured_items
    })

def about(request):
    return render(request, 'core/about.html')
