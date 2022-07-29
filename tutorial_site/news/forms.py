from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        label="Заголовок",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    content = forms.CharField(
        label="Содержимое",
        required=False,
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Категория",
        empty_label="Выберите категорию",
        widget=forms.Select(attrs={"class": "form-control", "row": 5}),
    )
    is_published = forms.BooleanField(label="Опубликовать?", initial=True)
