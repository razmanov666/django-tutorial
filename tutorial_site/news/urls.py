from django.urls import path
from django.views.decorators.cache import cache_page

from .views import CreateNews
from .views import HomeNews
from .views import mail
from .views import NewsByCategory
from .views import register
from .views import user_login
from .views import user_logout
from .views import ViewNews

# from .views import view_news

# from .views import get_category

# from .views import index

urlpatterns = [
    path("mail/", mail, name="mail"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
    path("", cache_page(60)(HomeNews.as_view()), name="home"),
    path(
        "category/<int:category_id>/",
        NewsByCategory.as_view(),
        name="category",
    ),
    path("news/<int:pk>/", ViewNews.as_view(), name="view_news"),
    path("news/add-news/", CreateNews.as_view(), name="add_news"),
    # path("", index, name="home"),
    # path("", cache_page(60)(HomeNews.as_view()), name="home"),
    # path("category/<int:category_id>/", get_category, name="category"),
    # path("news/<int:news_id>/", view_news, name="view_news"),
    # path("news/add-news/", add_news, name="add_news"),
]
