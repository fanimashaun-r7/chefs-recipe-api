# Generated by Django 3.0.8 on 2020-07-21 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ingredients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
    ]
