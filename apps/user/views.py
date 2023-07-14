from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt import views

from apps.user import models, serializers
from apps.user.models import User
from apps.user.permissions import IsAdminUser, IsAdminUserOrEmployerReadOnly
from apps.user.serializers import UserSerializer, EmployerModelSerializer, EmployeeModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class LoginView(views.TokenObtainPairView):
    permission_classes = [AllowAny,]
    serializer_class = serializers.LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.RegisterSerializer
    permission_classes = [AllowAny,]


class ChangePasswordView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticated,]


class UpdateProfileView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UpdateUserSerializer
    permission_classes = [IsAuthenticated,]


class EmployeeModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.EMPLOYEE)
    serializer_class = EmployeeModelSerializer
    permission_classes = [IsAdminUserOrEmployerReadOnly, IsAuthenticated]


class EmployerModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.EMPLOYER)
    serializer_class = EmployerModelSerializer
    permission_classes = [IsAdminUserOrEmployerReadOnly, IsAuthenticated]
