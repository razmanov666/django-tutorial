# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Category
from .models import News


def index(request):
    news = News.objects.all()
    context = {
        "news": news,
        "title": "Список новостей",
    }
    return render(request, "news/index.html", context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(
        request,
        "news/category.html",
        {"news": news, "category": category},
    )


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, "news/view_news.html", {"news_item": news_item})
