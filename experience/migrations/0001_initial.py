# Generated by Django 4.0.4 on 2022-04-13 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='School Name')),
                ('level', models.CharField(blank=True, max_length=255, verbose_name='Level')),
                ('time_period', models.CharField(blank=True, max_length=255, verbose_name='Time Period')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('town', models.CharField(blank=True, max_length=255, verbose_name='City/Town')),
                ('url', models.URLField(blank=True, max_length=255, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Company Name')),
                ('position', models.CharField(blank=True, max_length=255, verbose_name='Position')),
                ('time_period', models.CharField(blank=True, max_length=255, verbose_name='Time Period')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('town', models.CharField(blank=True, max_length=255, verbose_name='City/Town')),
                ('url', models.URLField(blank=True, max_length=255, verbose_name='URL')),
            ],
        ),
    ]
