from django.urls import path
from views import login
from views import register

from .views import CreateNews
from .views import HomeNews
from .views import NewsByCategory
from .views import ViewNews

# from .views import view_news

# from .views import get_category

# from .views import index

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    # path("", index, name="home"),
    path("", HomeNews.as_view(), name="home"),
    # path("category/<int:category_id>/", get_category, name="category"),
    path(
        "category/<int:category_id>/",
        NewsByCategory.as_view(),
        name="category",
    ),
    # path("news/<int:news_id>/", view_news, name="view_news"),
    path("news/<int:pk>/", ViewNews.as_view(), name="view_news"),
    path("news/add-news/", CreateNews.as_view(), name="add_news"),
    # path("news/add-news/", add_news, name="add_news"),
]
