# Generated by Django 4.0.4 on 2022-07-31 12:52
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        (
            "news",
            "0002_category_alter_news_options_alter_news_content_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="content",
            field=models.TextField(blank=True, verbose_name="Содержимое"),
        ),
    ]