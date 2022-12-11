from django.db import models
from projects.models import Project
from core.models import TimeStampedModel


class Board(TimeStampedModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="board"
    )
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=10)


    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self):
        return f"Board: {self.name}"
