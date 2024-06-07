# shortener/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)

class URL(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_url} - {self.original_url}"
