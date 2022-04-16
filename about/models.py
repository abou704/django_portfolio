from django.db import models
from aboubakiri.aboubakiri_model import AboubakiriModelManager, AboubakiriModel
from django.utils import timezone


class Profile(AboubakiriModel):
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        blank=True
    )
    photo = models.ImageField(
        upload_to='static/images/about/profile',
        blank=True,
        null=True
    )
    town = models.CharField(
        max_length=255,
        verbose_name="Town",
        blank=True
    )
    nationality = models.CharField(
        max_length=255,
        verbose_name="Nationality",
        blank=True
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Phone Number",
        blank=True,
        null=True
    )
    latitude = models.FloatField(
        max_length=None,
        verbose_name="Latitude",
        blank=True,
        null=True
    )
    longitude = models.FloatField(
        max_length=None,
        verbose_name="Longitude",
        blank=True,
        null=True
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Email",
        blank=True
    )
    website = models.URLField(
        max_length=255,
        verbose_name="Website",
        blank=True
    )
    facebook = models.URLField(
        max_length=255,
        verbose_name="Facebook",
        blank=True
    )
    instagram = models.URLField(
        max_length=255,
        verbose_name="Instagram",
        blank=True
    )
    twitter = models.URLField(
        max_length=255,
        verbose_name="Twitter",
        blank=True
    )
    skype = models.CharField(
        max_length=255,
        verbose_name="Skype",
        blank=True
    )
    linkedin = models.URLField(
        max_length=255,
        verbose_name="LinkedIn",
        blank=True
    )
    spoken_lang = models.CharField(
        max_length=255,
        verbose_name="Spoken Language",
        blank=True
    )
    years_exp = models.PositiveSmallIntegerField(
        verbose_name="Years Experience",
        blank=True
    )

    objects = AboubakiriModelManager()


    def __str__(self):
        return self.name


class Interest(AboubakiriModel):
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(
        max_length=255,
        verbose_name="Interest Name",
        blank=True
    )
    photo = models.ImageField(
        upload_to='static/images/about/interest',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True
    )

    objects = AboubakiriModelManager()

    def __str__(self):
        return self.name
