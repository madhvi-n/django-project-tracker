from rest_framework import serializers

from boards.models import BoardSection


class BoardSectionSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = BoardSection
        fields = ('id', 'title', 'board', 'max_issues_limit', 'tasks')

    def create(self, validated_data):
        return BoardSection.objects.create(**validated_data)

    def get_tasks(self, obj):
        if hasattr(obj, 'tasks'):
            return obj.tasks.count()
        return 0
