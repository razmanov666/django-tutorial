import re

from django import forms
from django.core.exceptions import ValidationError

from .models import News


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
