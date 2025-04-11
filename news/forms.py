from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "anons", "full_text", "date", "time"]

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название статьи"
            }),
            "anons": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Aнонс статьи"
            }),
            "date": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Дата публикации",
                "type": "date"
            }),
            "time": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Дата публикации",
                "type": "time"
            }),
            "full_text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Текст статьи"
            }),

        }