from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db.models import Model, DateTimeField, CharField


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StringArrayField(ArrayField):
    def __init__(self, base_field=None, **kwargs):
        base_field = base_field or CharField(max_length=255)
        super().__init__(base_field=base_field, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        for item in value:
            if not isinstance(item, str):
                raise ValidationError("The array must only contain strings")
