from rest_framework.viewsets import ModelViewSet
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer


class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
