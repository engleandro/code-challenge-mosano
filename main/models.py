from django.db import models
from django.utils.translation import gettext


class Registry(models.Model):
    class Meta:
        abstract = True

    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now=True)
    is_active = models.fields.BooleanField(default=True)
