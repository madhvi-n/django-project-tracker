from core.views import BaseReadOnlyViewSet, BaseViewSet

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from projects.models import Project
from projects.serializers import ProjectSerializer, ProjectCreateSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 24


class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    lookup_field = 'uuid'
    pagination_class = ProjectPagination
    serializer_class = ProjectSerializer
    serializer_action_classes = {
        'create' : ProjectCreateSerializer,
        'update' : ProjectCreateSerializer,
    }

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset

    def create(self, request):
        data = request.data
        user = request.user

        if not user.is_authenticated:
            return Response({'error':'The user is anonymous'}, status=status.HTTP_401_UNAUTHORIZED)

        if data['user'] != user.pk:
            return Response({'error': 'Spoofing detected'}, status=status.HTTP_403_FORBIDDEN)

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, uuid=None):
        project = self.get_object()
        data = request.data
        user = request.user

        if not user.is_authenticated:
            return Response({"error": "User not authorized"}, status=status.HTTP_401_UNAUTHORIZED)

        if project.user != user:
            return Response({"error": "Spoofing detected"}, status=status.HTTP_403_FORBIDDEN)

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=data, instance=project)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, uuid=None):
        project = self.get_object()
        user = request.user
        if project.user != user:
            return Response (
                {'error' : 'User not authorized'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        project.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
