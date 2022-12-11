from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth.models import User


class ProfileInfo(TimeStampedModel):
    user = models.OneToOneField(User, related_name="info", on_delete=models.CASCADE)
    username_changed = models.BooleanField(default=False)
    date_of_birth = models.DateField(auto_now=False, auto_add_now=False)
    bio = models.CharField(max_length=200)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Profile Info'
        verbose_name_plural = 'Profile Info'

    class __str__(self):
        return f"Profile Info: {self.user.username}"
