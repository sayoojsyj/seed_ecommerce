# Generated by Django 4.2.6 on 2023-10-18 15:18

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.get_file_path),
        ),
    ]
