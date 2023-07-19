from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.orders.models import UserCard


# Serializer for the UserCard model
class UserCardSerializer(ModelSerializer):
    class Meta:
        model = UserCard
        fields = ('card_number', 'expiration_date')

    # Custom validation method for the serializer
    def validate(self, attrs):
        # Get the requesting user from the context
        user = self.context['request'].user

        # Check if the user has a subscription and the number of cards they already have
        if not user.has_subscription and UserCard.objects.filter(user=user).count() >= 3:
            raise ValidationError("You have reached the limit of cards without a subscription.")

        # Call the parent class's validate method to perform default validation
        return super().validate(attrs)

    # Custom validation method for the 'card_number' field
    @staticmethod
    def validate_card_number(value):
        # Check if the card number contains only numbers
        if not value.isdigit():
            raise ValidationError("Card number must contain only numbers.")

        len_value = len(value)

        # Check if the card number has a length of 16 characters
        if len_value != 16:
            raise ValidationError("Card numbers length must be 16 characters.")

        # Check if a card with this number already exists
        if UserCard.objects.filter(card_number=value).exists():
            raise ValidationError("Card with this number already exists.")

        return value

    # Custom validation method for the 'expiration_date' field
    @staticmethod
    def validate_expiration_date(value):
        # Check the format of the expiration date (MM/YY)
        if not value or len(value) != 5 or not value[:2].isdigit() or not value[3:].isdigit():
            raise ValidationError("Wrong card expiration date format. Use MM/YY format.")

        return value
