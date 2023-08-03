from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User
from shared.django.functions import validate_name


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        username = attrs.get('username')
        try:
            User.objects.get(username=username, is_active=True)
        except User.DoesNotExist:
            raise ValidationError(
                {"Not Found": "User with this credentials not found or account is not active!"})
        return super().validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    password2 = CharField(write_only=True, required=True)
    username = CharField(validators=[validate_name], required=True)
    first_name = CharField(validators=[validate_name], required=True)
    last_name = CharField(validators=[validate_name], required=True)

    class Meta:
        model = User
        fields = (
            'username', 'phone_number', 'password', 'password2', 'location', 'first_name', 'last_name', 'user_type')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    @staticmethod
    def validate_username(username):
        try:
            User.objects.get(username=username)
            raise ValidationError(
                {"username": "User with this username already exists."})
        except User.DoesNotExist:
            return username

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            location=validated_data['location'],
            user_type=validated_data['user_type'],
            password=validated_data['password']
        )

        return user


class ChangePasswordSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    password2 = CharField(write_only=True, required=True)
    old_password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class ChangeAccountSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'profile_image', 'job',
                  'instagram_profile', 'facebook_profile', 'twitter_profile', 'about_me', 'location', 'gender',
                  'user_type')


class ForgotPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phone_number']


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ()
