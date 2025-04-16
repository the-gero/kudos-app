from django.db import models

from models.basemodel import BaseModel




class Kudo(BaseModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_kudos')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_kudos')
    message = models.TextField()

