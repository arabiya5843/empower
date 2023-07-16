from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views import UserViewSet, EmployeeModelViewSet, EmployerModelViewSet

router = DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('employee', EmployeeModelViewSet, 'employee')
router.register('employer', EmployerModelViewSet, 'employer')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('apps.users.urls')),
]
