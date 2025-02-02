# Generated by Django 2.2.2 on 2019-06-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsBlog', '0002_auto_20190612_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug_field',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug_field',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
