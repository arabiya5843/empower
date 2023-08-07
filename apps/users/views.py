from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import User
from apps.users.serializers import LoginSerializer, RegisterSerializer, ChangePasswordSerializer, \
    ChangeAccountSerializer, UserModelSerializer, ForgotPasswordSerializer
from shared.django.permissions import IsUserOwner


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class UserLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class UserChangePasswordView(GenericAPIView, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated, IsUserOwner)

    def put(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        new_password = serializer.validated_data.get('password')
        instance.set_password(new_password)
        instance.save()

        return Response({"Successfully": "Password was updated successfully!"})


class UserChangeAccountView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangeAccountSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class UserForgotPasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ForgotPasswordSerializer
    permission_classes = (AllowAny,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Check if the provided email exists in the database
        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User with provided email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Generate and send the password reset link or token
        # You can use your preferred method here, such as sending an email with a reset link
        # or generating a token and returning it in the API response
        user.send_password_reset_email()

        serializer.save()

        return Response(serializer.data)


class UserReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsAuthenticated,)
