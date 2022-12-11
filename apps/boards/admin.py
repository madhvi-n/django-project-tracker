from django.contrib import admin
from boards.models import Board, BoardSection


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'key',
        'project'
    )
    raw_id_fields = ('project',)



@admin.register(BoardSection)
class BoardSectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'board',
        'max_issues_limit'
    )
    raw_id_fields = ('board',)
