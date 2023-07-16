from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt import views

from apps.users.models import User, Experience, Ability
from apps.users.permissions import IsAdminUser
from apps.users.serializers import UserSerializer, EmployerModelSerializer, EmployeeModelSerializer, LoginSerializer, \
    RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer, ExperienceModelSerializer, AbilityModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class LoginView(views.TokenObtainPairView):
    permission_classes = [AllowAny,]
    serializer_class = LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated,]


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated,]


class EmployeeModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.EMPLOYEE)
    serializer_class = EmployeeModelSerializer


class EmployerModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.EMPLOYER)
    serializer_class = EmployerModelSerializer


class ExperienceModelViewSet(ModelViewSet):
    queryset = Experience.objects
    serializer_class = ExperienceModelSerializer


class AbilityModelViewSet(ModelViewSet):
    queryset = Ability.objects
    serializer_class = AbilityModelSerializer
