# Generated by Django 4.0.2 on 2022-02-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
