from django.db import models
from core.models import TimeStampedModel
from projects.models import Project
from boards.models import BoardSection
from django.contrib.auth.models import User


class TaskType(TimeStampedModel):
    title = models.CharField(max_length=30)
    project = models.ForeignKey(
        Project,
        related_name="task_types",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['title']
        verbose_name = "Task Type"
        verbose_name_plural = "Task Types"

    def __str__(self):
        return f"{self.title}"


class Task(TimeStampedModel):
    board_section = models.ForeignKey(
        BoardSection,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    summary = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    assignee = models.ForeignKey(
        User,
        related_name="assigned_tasks",
        on_delete=models.CASCADE
    )
    reporter = models.ForeignKey(
        User,
        related_name="reported_tasks",
        on_delete=models.CASCADE
    )
