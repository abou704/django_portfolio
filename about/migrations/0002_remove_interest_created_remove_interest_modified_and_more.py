# Generated by Django 4.0.4 on 2022-04-13 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='created',
        ),
        migrations.RemoveField(
            model_name='interest',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='modified',
        ),
    ]
