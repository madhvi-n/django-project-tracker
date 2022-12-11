from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.views import BaseViewSet
from profiles.serializers import ProfileSerializer


class ProfileViewSet(BaseViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = ProfileSerializer

    def list(self, request):
        queryset = self.get_queryset()
        return self.paginated_response(queryset, context={'request': request})

    def retrieve(self, request, username=None):
        user = self.get_object()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def auth(self, request):
        if request.user.is_authenticated:
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        user = self.get_object()
        if user == request.user:
            user.is_active = False
            user.save()
        return Response({"message": "Account Deactivated"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = self.get_object()
        if user == request.user:
            user.is_requesting_delete = True
            user.save()
            return Response({'success': True, 'message': "You request for account deletion has been sent. Your account will be deleted in 15 days"}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': "You are not authorized to delete this account."}, status=status.HTTP_401_UNAUTHORIZED)
