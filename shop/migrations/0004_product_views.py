# Generated by Django 5.2.4 on 2025-07-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_product_category_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="views",
            field=models.BigIntegerField(default=0, verbose_name="بازدید ها"),
        ),
    ]
