from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Category

def menu_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = MenuItem.objects.filter(is_available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)
    
    return render(request, 'menu/menu_list.html', {
        'category': category,
        'categories': categories,
        'items': items
    })

def menu_item_detail(request, id):
    item = get_object_or_404(MenuItem, id=id, is_available=True)
    return render(request, 'menu/menu_item_detail.html', {
        'item': item
    })
