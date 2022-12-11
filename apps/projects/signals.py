from django.db.models.signals import post_save
from django.dispatch import receiver
from boards.models import Board, BoardSection
from projects.models import Project
from tasks.models import TaskType


@receiver(post_save, sender=Project)
def create_task_types_project_hook(sender, instance, created, **kwargs):
    if instance:
        for type in ["Task", "Bug", "Story"]:
            TaskType.objects.get_or_create(project=instance, title=type)
