# Generated by Django 4.2.3 on 2023-07-19 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_remove_category_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='category',
        ),
    ]
