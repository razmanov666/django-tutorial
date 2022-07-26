from django.urls import path

from .views import get_category
from .views import index

urlpatterns = [
    path("", index, name="home"),
    path("category/<int:category_id>/", get_category, name="category"),
]
