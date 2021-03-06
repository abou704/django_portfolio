# Generated by Django 4.0.4 on 2022-04-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Interest Name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/images/about/interest')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/images/about/profile')),
                ('town', models.CharField(blank=True, max_length=255, verbose_name='Town')),
                ('nationality', models.CharField(blank=True, max_length=255, verbose_name='Nationality')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone Number')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                ('website', models.URLField(blank=True, max_length=255, verbose_name='Website')),
                ('facebook', models.URLField(blank=True, max_length=255, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, max_length=255, verbose_name='Instagram')),
                ('twitter', models.URLField(blank=True, max_length=255, verbose_name='Twitter')),
                ('skype', models.CharField(blank=True, max_length=255, verbose_name='Skype')),
                ('linkedin', models.URLField(blank=True, max_length=255, verbose_name='LinkedIn')),
                ('spoken_lang', models.CharField(blank=True, max_length=255, verbose_name='Spoken Language')),
                ('years_exp', models.PositiveSmallIntegerField(blank=True, verbose_name='Years Experience')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
