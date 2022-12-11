from django.contrib import admin
from tasks.models import TaskType, Task


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
