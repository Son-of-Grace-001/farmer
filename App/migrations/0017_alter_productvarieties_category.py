# Generated by Django 4.2.3 on 2023-07-22 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_alter_cropvarieties_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvarieties',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.productcategory'),
        ),
    ]
