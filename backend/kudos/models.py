from django.db import models

from models.basemodel import BaseModel

class Organization(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_by = models.UUIDField(null=True, blank=True)

class User(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def kudos_left_this_week(self):
        from .models import Kudo
        from django.utils import timezone
        from datetime import timedelta

        start_of_week = timezone.now().date() - timedelta(days=timezone.now().weekday())
        return 3 - Kudo.objects.filter(from_user=self, created_at__date__gte=start_of_week).count()

class Kudo(BaseModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_kudos')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_kudos')
    message = models.TextField()

