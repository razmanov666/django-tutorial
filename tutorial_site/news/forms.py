import re

from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import News


class ContactForm(forms.Form):
    adress = subject = forms.EmailField(
        label="Adress",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    content = forms.CharField(
        label="Text",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
    )
    capthca = CaptchaField()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text="Вводи норм юзернейм",
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class NewsForm(forms.ModelForm):
    class Meta:
        model = News

        # Auto creating all fields
        # fields = '__all__'

        fields = ["title", "content", "category", "is_published"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(
                attrs={"class": "form-control", "row": 5}
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r"\d", title):
            raise ValidationError("Название не должно начинаться с цифры.")
        return title
