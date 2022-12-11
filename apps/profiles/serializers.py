from rest_framework import serializers
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'date_joined',
        )
        read_only_fields = ('id',)


class ProfileHeavySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'date_joined',
        )
        read_only_fields = ('id',)
