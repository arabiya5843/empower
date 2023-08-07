from rest_framework import serializers
from apps.ai_supportive.models import ChatMessage


class AISupportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ('question', 'user_id')





