# Generated by Django 4.2.3 on 2023-07-20 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_alter_symptoms_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='varieties',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dis', to='App.varieties'),
        ),
        migrations.AlterField(
            model_name='symptoms',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.disease'),
        ),
    ]
