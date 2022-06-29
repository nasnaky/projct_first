from django.db import models


class ChangeDecode(models.Model):
    origen = models.TextField()
    change = models.TextField(null=True, blank=True)
