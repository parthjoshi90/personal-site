from django.db import models
from typing import Any, Optional
from django.db import models
from django.db.models import(
    DateTimeField
)

# Create your models here.

class TimestampedModel(models.Model):
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
