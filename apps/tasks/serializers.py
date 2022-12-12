from rest_framework import serializers

from tasks.models import TaskType, Task


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = ('id', 'title', 'project')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'type', 'board_section', 'summary', 'description', 'assignee', 'reporter',
        )
        read_only_fields = ('id',)
        extra_kwargs = {
            'board_section': {'write_only': True},
            'assignee': {'write_only': True},
        }

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
