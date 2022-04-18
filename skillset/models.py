from django.db import models
from django.utils import timezone
from aboubakiri.aboubakiri_model import AboubakiriModelManager, AboubakiriModel



class Skill(AboubakiriModel):
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(
        max_length=255,
        verbose_name="Skill Name",
        blank=True
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="Rating",
        default=0
    )
    objects = AboubakiriModelManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-rating',)


class Software(AboubakiriModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Software Name",
        blank=True
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="Rating",
        default=0
    )

    objects = AboubakiriModelManager()
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-rating',)
