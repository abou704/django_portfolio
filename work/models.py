from django.db import models
from skillset.models import Skill, Software
# from multiselectfield import MultiSelectField


class Client(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Client Name"
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    status = models.BooleanField(
        default=True
    )
    completed = models.BooleanField(
        default=True
    )
    client_name = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name="Client Name",
        related_name="clients_name"
    )
    TYPES = (
        ('Website', 'Website'),
        ('Logo', 'Logo'),
        ('App', 'App'),
        ('Flyer', 'Flyer'),
        ('Business Card', 'Business Card'),
        ('Banner', 'Banner'),
        ('Brochure', 'Brochure'),
    )
    type = models.CharField(
        max_length=13,
        choices=TYPES,
        default=None,
        verbose_name="Project Type"
    )
    date = models.CharField(
        max_length=255,
        verbose_name="Date",
        blank=True
    )
    skills = models.ManyToManyField(
        Skill,
        verbose_name="Technologies Used",
        blank=True
    )
    software = models.ManyToManyField(
        Software,
        verbose_name="Software Used",
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True
    )
    url = models.URLField(
        max_length=255,
        verbose_name="URL",
        blank=True
    )
    photo = models.ImageField(
        upload_to='static/images/projects',
        blank=True,
        null=True
    )

    # project_name = Client.objects.get()

    # def __str__(self):
    #    return self.project_name

    # def __unicode__(self):
    #    return unicode(self.id)

    class Meta:
        ordering = ['-date']
