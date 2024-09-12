# Generated by Django 5.1 on 2024-09-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articlesapp', '0002_alter_articles_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
    ]
