# Generated by Django 3.2.20 on 2023-08-27 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_categary_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categary',
            new_name='category',
        ),
    ]
