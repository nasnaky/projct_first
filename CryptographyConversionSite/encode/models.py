from django.db import models


class ChangeEncode(models.Model):
    origen = models.TextField()
    change = models.TextField(null=True, blank=True)


