from django.db import models
from apps.categories.models import Category

class ConfirmContact(models.Model):
    confirmed = models.BooleanField(default=False)

    class Meta:
        abstract = True
