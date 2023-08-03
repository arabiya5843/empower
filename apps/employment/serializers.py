from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.employment.models import JobVacancy


class MyJobVacancyModelSerializer(ModelSerializer):
    # Use HiddenField with CurrentUserDefault to automatically set the user field to the current user
    user = HiddenField(default=CurrentUserDefault())

    @staticmethod
    def validate_requirements(value):
        # Validate that each item in the requirements array is a string
        for item in value:
            if not isinstance(item, str):
                raise ValidationError(
                    "The requirements array must only contain strings")
        return value

    @staticmethod
    def validate_responsibilities(value):
        # Validate that each item in the responsibilities array is a string
        for item in value:
            if not isinstance(item, str):
                raise ValidationError(
                    "The responsibilities array must only contain strings")
        return value

    def validate(self, attrs):
        # Get the current user from the request context
        user = self.context['request'].user

        # Check if the user has a subscription and the number of vacancies created by the user
        if not user.has_subscription and JobVacancy.objects.filter(user=user).count() > 2:
            raise ValidationError(
                "You have reached the limit of vacancies without a subscription.")
        return super().validate(attrs)

    class Meta:
        # Use the JobVacancy model and include all fields in the serialization
        model = JobVacancy
        fields = '__all__'


class JobVacancyModelSerializer(ModelSerializer):
    class Meta:
        model = JobVacancy
        fields = '__all__'
