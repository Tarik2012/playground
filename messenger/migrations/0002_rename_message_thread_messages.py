# Generated by Django 5.1.1 on 2024-10-22 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='message',
            new_name='messages',
        ),
    ]
