from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth.models import User

import uuid

class Project(TimeStampedModel):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    slug = models.SlugField(
        blank=True,
        max_length=40
    )
    private = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    user = models.ForeignKey(
        User,
        related_name="projects",
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
