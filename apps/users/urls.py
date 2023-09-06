from django.urls import path
from rest_framework.generics import RetrieveAPIView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import (
    UserCreateView,
    UserLoginView,
    UserChangePasswordView,
    UserChangeAccountView, UserRetrieveAPIView,  # UserForgotPasswordView,
)

router = DefaultRouter()

urlpatterns = [
                  path('register/', UserCreateView.as_view(), name='register'),
                  path('login/', UserLoginView.as_view(), name='login'),
                  path('change-password/', UserChangePasswordView.as_view(),
                       name='change-password'),
                  path('update-account/', UserChangeAccountView.as_view(), name='change-account'),
                  # path('forgot-password/', UserForgotPasswordView.as_view(), name='forgot-password'),
                  path('token/refresh/', TokenRefreshView.as_view(),
                       name='token-refresh'),
                  path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='users')
              ] + router.urls
