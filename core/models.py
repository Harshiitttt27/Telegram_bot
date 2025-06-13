from django.db import models

# Create your models here.
from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
