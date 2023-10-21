from django.db import models
from django.contrib.postgres.fields import ArrayField


class Directory(models.Model):

    name = models.CharField(max_length=500, null=False)

    emails = ArrayField(models.EmailField(), null=False)
