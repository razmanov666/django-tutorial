from django.urls import path

from .views import add_news
from .views import get_category
from .views import HomeNews
from .views import view_news

# from .views import index

urlpatterns = [
    # path("", index, name="home"),
    path("", HomeNews.as_view(), name="home"),
    path("category/<int:category_id>/", get_category, name="category"),
    path("news/<int:news_id>/", view_news, name="view_news"),
    path("news/add-news/", add_news, name="add_news"),
]
