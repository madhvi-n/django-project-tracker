from core.views import BaseReadOnlyViewSet, BaseViewSet

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from boards.models import BoardSection, Board
from boards.serializers import BoardSectionSerializer
from projects.models import Project


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
                queryset = queryset.filter(board__pk=self.kwargs['board_pk'])
        return queryset

    def create(self, request, project_uuid=None, board_pk=None):
        data = request.data
        try:
            project = Project.objects.get(uuid=project_uuid)
            board = Board.objects.get(pk=board_pk)
            new_data = data.copy()
            new_data['project'] = project.id
            new_data['board'] = board.id
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Board.DoesNotExist:
            return Response(
                {'error': 'Board does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, project_uuid=None, board_pk=None, pk=None):
        data = request.data
        try:
            project = Project.objects.get(uuid=project_uuid)
            board = Board.objects.get(pk=board_pk)
            new_data = data.copy()
            new_data['project'] = project.id
            new_data['board'] = board.id
        except Project.DoesNotExist:
            return Response(
                {'error': 'Project does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Board.DoesNotExist:
            return Response(
                {'error': 'Board does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=new_data)
        if (serializer.is_valid(raise_exception=False)):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, project_uuid=None, board_pk=None, pk=None):
        section = self.get_object()
        project = Project.objects.get(uuid=project_uuid)

        if project.user != request.user:
            return Response(
                {'error': 'User not authorized'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        section.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
