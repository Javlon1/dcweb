# Generated by Django 4.0.4 on 2022-06-06 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_raqamlashtirishxizmalari_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raqamlashtirishxizmalari',
            name='category',
        ),
        migrations.RemoveField(
            model_name='raqamlashtirishxizmalari',
            name='category_en',
        ),
        migrations.RemoveField(
            model_name='raqamlashtirishxizmalari',
            name='category_ru',
        ),
    ]