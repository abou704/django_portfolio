from django.db import models


class Employment(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Company Name",
        blank=True
    )
    position = models.CharField(
        max_length=255,
        verbose_name="Position",
        blank=True
    )
    time_period = models.CharField(
        max_length=255,
        verbose_name="Time Period",
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True
    )
    town = models.CharField(
        max_length=255,
        verbose_name="City/Town",
        blank=True
    )
    url = models.URLField(
        max_length=255,
        verbose_name="URL",
        blank=True
    )

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="School Name",
        blank=True
    )
    level = models.CharField(
        max_length=255,
        verbose_name="Level",
        blank=True
    )
    time_period = models.CharField(
        max_length=255,
        verbose_name="Time Period",
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True
    )
    town = models.CharField(
        max_length=255,
        verbose_name="City/Town",
        blank=True
    )
    url = models.URLField(
        max_length=255,
        verbose_name="URL",
        blank=True
    )

    def __str__(self):
        return self.name
