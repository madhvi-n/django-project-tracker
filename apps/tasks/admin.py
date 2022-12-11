from django.contrib import admin
from tasks.models import TaskType, Task


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'project'
    )
    raw_id_fields = ('project',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'reporter',
        'board_section'
    )
    raw_id_fields = (
        'board_section',
        'reporter',
        'assignee',
    )
