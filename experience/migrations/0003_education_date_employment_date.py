# Generated by Django 4.0.4 on 2022-04-17 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_education_created_education_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='employment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]