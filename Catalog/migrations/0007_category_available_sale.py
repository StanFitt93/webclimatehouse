# Generated by Django 2.2.2 on 2019-06-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0006_auto_20190612_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='available_sale',
            field=models.BooleanField(default=False),
        ),
    ]
