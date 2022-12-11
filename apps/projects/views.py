from core.views import BaseReadOnlyViewSet, BaseViewSet

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 100


class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    lookup_field = 'uuid'
    pagination_class = ProjectPagination
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset

    def create(self, request):
        pass

    def update(self, request, project_uuid=None):
        pass

    def destroy(self, request, project_uuid=None):
        pass
