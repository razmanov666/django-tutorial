# from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import NewsForm
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


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, "news/add_news.html", {"form": form})
