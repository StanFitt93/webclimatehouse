# Generated by Django 2.2.2 on 2019-06-13 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0009_auto_20190613_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfSaleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Тип продажи',
                'verbose_name_plural': 'Типы продаж',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='typeOfSale',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.DO_NOTHING, to='Catalog.TypeOfSaleProduct'),
            preserve_default=False,
        ),
    ]
