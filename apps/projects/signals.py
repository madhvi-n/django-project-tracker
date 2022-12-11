from django.db.models.signals import post_save
from django.dispatch import receiver
from boards.models import Board


@receiver(post_save, sender=Board)
def create_board_sections_signal(sender, instance, created, **kwargs):
    if instance:
        pass
