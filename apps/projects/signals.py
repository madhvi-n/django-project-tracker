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


@receiver(post_save, sender=Project)
def create_default_board(sender, instance, created, **kwargs):
    if created:
        board_name = f"{instance.name}'s board"
        board = Board.objects.create(name=board_name, project=instance, key=board_name.upper()[:4])


@receiver(post_save, sender=Board)
def create_default_board_sections(sender, instance, created, **kwargs):
    print("Signal was called")
    if created:
        section_names = ['To Do', 'In Progress', 'Done']
        for name in section_names:
            BoardSection.objects.create(title=name, board=instance)
