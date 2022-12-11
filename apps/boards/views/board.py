from core.views import BaseReadOnlyViewSet, BaseViewSet

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from boards.models import Board
from boards.serializers import BoardSerializer
from projects.models import Project


class BoardPagination(PageNumberPagination):
    page_size = 24


class BoardViewSet(BaseViewSet):
    queryset = Board.objects.all()
    pagination_class = BoardPagination
    serializer_class = BoardSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs != {}:
            if 'project_uuid' in self.kwargs:
                queryset = queryset.filter(project__uuid=self.kwargs['project_uuid'])
        return queryset

    def create(self, request, project_uuid=None):
        data = request.data
        try:
            project = Project.objects.get(uuid=project_uuid)
            data['project'] = project.id
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=data)
        if (serializer.is_valid(raise_exception=False)):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, project_uuid=None, pk=None):
        data = request.data
        try:
            project = Project.objects.get(uuid=project_uuid)
            data['project'] = project.id
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=data)
        if (serializer.is_valid(raise_exception=False)):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, project_uuid=None, pk=None):
        board = self.get_object()
        project = Project.objects.get(uuid=project_uuid)

        if project.user != request.user:
            return Response(
                {'error': 'User not authorized'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        board.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
