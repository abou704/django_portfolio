# Generated by Django 4.0.4 on 2022-04-13 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Skill Name')),
                ('rating', models.PositiveSmallIntegerField(default=0, verbose_name='Rating')),
            ],
            options={
                'ordering': ('-rating',),
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Software Name')),
                ('rating', models.PositiveSmallIntegerField(default=0, verbose_name='Rating')),
            ],
            options={
                'ordering': ('-rating',),
            },
        ),
    ]
