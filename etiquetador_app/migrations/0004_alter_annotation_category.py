# Generated by Django 4.2.17 on 2025-01-13 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etiquetador_app', '0003_annotationclass_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etiquetador_app.annotationclass'),
        ),
    ]
