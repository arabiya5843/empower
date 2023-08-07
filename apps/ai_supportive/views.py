from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from apps.ai_supportive.models import ChatMessage
from apps.ai_supportive.serializers import AISupportModelSerializer
from shared.django import os_environ_get
import openai

openai.api_key = os_environ_get("API_KEY")


class AISupportiveReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = AISupportModelSerializer


class AISupportiveCreateView(GenericAPIView, CreateModelMixin):
    queryset = ChatMessage.objects.all()
    serializer_class = AISupportModelSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.validated_data.get("question")

        messages = []
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})

        serializer.save(user=request.user)
        serializer.save(answer=reply)

        serializer_data = serializer.data
        serializer_data["answer"] = reply

        return Response(serializer_data, status=status.HTTP_201_CREATED)
