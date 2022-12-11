from core.views import BaseReadOnlyViewSet, BaseViewSet

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from tasks.models import TaskType, Task
from tasks.serializers import TaskTypeSerializer, TaskSerializer


class TaskTypeViewSet(BaseViewSet):
    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer

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


class TaskViewSet(BaseViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs != {}:
            if 'section_pk' in self.kwargs:
                return self.queryset.filter(section__pk=self.kwargs['section_pk'])
        return queryset

    def create(self, request, project_uuid=None, board_pk=None, section_pk=None):
        pass

    def update(self, request, project_uuid=None, board_pk=None, section_pk=None, pk=None):
        pass

    def destroy(self, request, project_uuid=None, board_pk=None, section_pk=None, pk=None):
        pass

    @action(detail=True, methods=['put'])
    def change_task_type(self, request, project_uuid=None, board_pk=None, section_pk=None, pk=None):
        task = self.get_object()
        pass
