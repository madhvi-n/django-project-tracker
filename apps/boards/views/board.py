from core.views import BaseReadOnlyViewSet, BaseViewSet

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from boards.models import Board
from boards.serializers import BoardSerializer


class BoardPagination(PageNumberPagination):
    page_size = 100


class BoardViewSet(BaseViewSet):
    queryset = Board.objects.all()
    pagination_class = BoardPagination
    serializer_class = BoardSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs != {}:
            if 'project_uuid' in self.kwargs:
                return self.queryset.filter(project__uuid=self.kwargs['project_uuid'])
        return queryset

    def create(self, request, project_uuid=None):
        pass

    def update(self, request, project_uuid=None, board_pk=None):
        pass

    def destroy(self, request, project_uuid=None, board_pk=None):
        pass
