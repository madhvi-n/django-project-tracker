from core.views import BaseReadOnlyViewSet, BaseViewSet

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from boards.models import BoardSection
from boards.serializers import BoardSectionSerializer


class BoardSectionPagination(PageNumberPagination):
    page_size = 24


class BoardSectionViewSet(BaseViewSet):
    queryset = BoardSection.objects.all()
    pagination_class = BoardSectionPagination
    serializer_class = BoardSectionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs != {}:
            if 'board_pk' in self.kwargs:
                return self.queryset.filter(board__pk=self.kwargs['board_pk'])
        return queryset

    def create(self, request, project_uuid=None, board_pk=None):
        pass

    def update(self, request, project_uuid=None, board_pk=None, section_pk=None):
        pass

    def destroy(self, request, project_uuid=None, board_pk=None, section_pk=None):
        pass
