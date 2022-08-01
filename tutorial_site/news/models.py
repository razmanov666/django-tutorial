from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Содержимое")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано"
    )
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("view_news", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at", "title"]


class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name="Наименование категории"
    )

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"
        ordering = ["title"]
