from rest_framework import serializers

from boards.models import BoardSection


class BoardSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardSection
        fields = '__all__'
