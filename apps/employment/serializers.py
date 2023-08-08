from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.employment.models import JobVacancy, Experience


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

        work_hours_start = attrs.get('work_hours_start')
        work_hours_end = attrs.get('work_hours_end')

        if work_hours_start and work_hours_end:
            if work_hours_start >= work_hours_end:
                raise ValidationError("work_hours_start must be earlier than work_hours_end.")
        elif work_hours_start and not work_hours_end or work_hours_end and not work_hours_start:
            raise ValidationError(
                "If 1 of the fields about the beginning and end of the working time is filled, then the second of "
                "them must also be filled!")
        return super().validate(attrs)

    class Meta:
        # Use the JobVacancy model and include all fields in the serialization
        model = JobVacancy
        fields = '__all__'


class JobVacancyModelSerializer(ModelSerializer):
    class Meta:
        model = JobVacancy
        fields = '__all__'


class ExperienceSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Experience
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user

        if not user.has_subscription and Experience.objects.filter(user=user).count() >= 20:
            raise ValidationError("You have reached the maximum limit of experiences.")

        return data
