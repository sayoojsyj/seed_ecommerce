# Generated by Django 4.2.6 on 2023-10-31 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_banner_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner_images',
            old_name='images1',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='banner_images',
            name='images2',
        ),
    ]