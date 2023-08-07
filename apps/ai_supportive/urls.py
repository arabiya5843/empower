from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.ai_supportive.views import AISupportiveCreateView, AISupportiveReadOnlyModelViewSet


router = DefaultRouter()
router.register('chats', AISupportiveReadOnlyModelViewSet, 'chats')


urlpatterns = [
    path('sending-question/', AISupportiveCreateView.as_view(), name='sending-questions'),

] + router.urls
