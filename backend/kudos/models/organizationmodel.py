from django.db import models
from .basemodel import BaseModel
import uuid
class Organization(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_by = models.UUIDField(null=True, blank=True)