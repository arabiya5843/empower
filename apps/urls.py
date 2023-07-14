from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user.views import UserViewSet, EmployeeModelViewSet, EmployerModelViewSet

router = DefaultRouter()
router.register('user', UserViewSet, 'user')
router.register('employee', EmployeeModelViewSet, 'employee')
router.register('employer', EmployerModelViewSet, 'employer')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('apps.user.urls')),
]
