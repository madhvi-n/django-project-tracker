from django.contrib import admin
from projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'name',
        'slug',
        'user'
    )
    raw_id_fields = (
        'user',
    )
    readonly_fields = ('slug',)
