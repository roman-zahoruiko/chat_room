# Generated by Django 3.2.8 on 2021-10-27 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='author',
            new_name='author_username',
        ),
    ]
