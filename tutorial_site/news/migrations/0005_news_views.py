# Generated by Django 4.0.6 on 2022-08-03 12:20
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_alter_news_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="views",
            field=models.IntegerField(default=0),
        ),
    ]