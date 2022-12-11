from django.db.models.signals import post_save
from django.dispatch import receiver
from boards.models import Board, BoardSection
from projects.models import Project
from tasks.models import TaskType


@receiver(post_save, sender=Project)
def project_created_hook(sender, instance, created, **kwargs):
    if instance:
        project = instance
        board_name = f"{project.name}'s board"
        board = Board.objects.get_or_create(
            project=project, name=board_name,
            key=project.name[:4].upper()
        )


@receiver(post_save, sender=Project)
def create_task_types_project_hook(sender, instance, created, **kwargs):
    if instance:
        for type in ["Task", "Bug", "Story"]:
            TaskType.objects.get_or_create(project=instance, title=type)
