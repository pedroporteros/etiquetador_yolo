# Generated by Django 4.2.17 on 2024-12-20 10:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('etiquetador_app', '0002_annotationclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationclass',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
