from django.db import models
from .basemodel import BaseModel
from django.contrib.auth.hashers import make_password, check_password
class User(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def kudos_left_this_week(self):
        from .kudomodel import Kudo
        from django.utils import timezone
        from datetime import timedelta

        start_of_week = timezone.now().date() - timedelta(days=timezone.now().weekday())
        return 3 - Kudo.objects.filter(from_user=self, created_at__date__gte=start_of_week).count()
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)