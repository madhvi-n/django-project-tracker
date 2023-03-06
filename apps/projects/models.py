from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth.models import User
from django.utils.text import slugify
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
        ordering = ['created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        count = Project.objects.filter(slug__startswith=self.slug).count()
        if count > 0:
            self.slug = f"{self.slug}-{count + 1}"
        super().save(*args, **kwargs)
