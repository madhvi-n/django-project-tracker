from rest_framework import serializers

from boards.models import BoardSection


class BoardSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardSection
        fields = ('id', 'title', 'board', 'max_issues_limit')

    def create(self, validated_data):
        return BoardSection.objects.create(**validated_data)
