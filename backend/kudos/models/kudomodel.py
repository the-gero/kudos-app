from django.db import models

from .basemodel import BaseModel
from .usermodel import User



class Kudo(BaseModel):
    from_user = models.ForeignKey( User, on_delete=models.CASCADE, related_name='sent_kudos')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_kudos')
    message = models.TextField()

