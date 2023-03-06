from rest_framework import serializers

from projects.models import Project
from boards.models import Board, BoardSection


class ProjectSerializer(serializers.ModelSerializer):
    boards = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            'uuid', 'name', 'desc', 'user',
            'created_at', 'boards',
        )

    def get_boards(self, obj):
        if hasattr(obj, 'board'):
            return obj.board.count()
        return 0


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('uuid', 'name', 'desc', 'user',)
        read_only_fields = ('uuid',)

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        return project

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.save()
        return instance
