from django.db import models


class Bird(models.Model):
    name = models.CharField("Name", max_length=50)

    class Meta:
        verbose_name = "Bird"
