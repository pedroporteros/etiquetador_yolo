# Generated by Django 4.2.17 on 2024-12-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etiquetador_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=7)),
            ],
        ),
    ]
