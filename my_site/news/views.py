from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'title': 'Новости',
        'news': news,
        'categories': categories
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id).order_by('-created_at')
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
        'categories': categories,
    }
    return render(request, 'news/get_category.html', context)
