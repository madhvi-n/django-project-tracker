from django.contrib import admin
from boards.models import Board, BoardSection


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass



@admin.register(BoardSection)
class BoardSectionAdmin(admin.ModelAdmin):
    pass
