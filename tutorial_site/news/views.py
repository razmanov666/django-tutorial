from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from .forms import NewsForm
from .forms import UserLoginForm
from .forms import UserRegisterForm
from .models import Category
from .models import News
from .utils import MyMixin

# from django.core.paginator import Paginator


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print()
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Succesfully registrated " + form.data.get("username")
            )
            return redirect("home")
        else:
            messages.error(request, "Error")
    else:
        form = UserRegisterForm()
    return render(request, "news/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "news/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


class HomeNews(MyMixin, ListView):
    model = News
    template_name: str = "news/home_news_list.html"
    context_object_name: str = "news"
    # extra_context = {'title': 'Главная'}
    paginate_by: int = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_upper("Главная страница")
        context["mixin_prop"] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related(
            "category"
        )


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name: str = "news/home_news_list.html"
    context_object_name = "news"
    allow_empty: bool = False
    paginate_by: int = 2

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs["category_id"], is_published=True
        ).select_related("category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_upper(
            Category.objects.get(pk=self.kwargs["category_id"])
        )
        return context


class ViewNews(DetailView):
    model = News
    context_object_name = "news_item"
    # template_name: str = 'news/news_detail.html'
    # pk_url_kwarg: str = 'news_id'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name: str = "news/add_news.html"
    login_url = "/admin/"
    # success_url = reverse_lazy('home')
