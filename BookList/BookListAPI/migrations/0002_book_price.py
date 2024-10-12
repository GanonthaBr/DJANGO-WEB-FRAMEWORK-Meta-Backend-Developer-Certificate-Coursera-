# Generated by Django 5.1.2 on 2024-10-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]