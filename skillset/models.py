from django.db import models


class Skill(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Skill Name",
        blank=True
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="Rating",
        default=0
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-rating',)


class Software(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Software Name",
        blank=True
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="Rating",
        default=0
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-rating',)
