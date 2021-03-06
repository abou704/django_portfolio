# Generated by Django 4.0.4 on 2022-04-18 18:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('skillset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='skill',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='skill',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='software',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='software',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
