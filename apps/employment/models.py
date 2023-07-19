from django.db.models import CharField, TextField, DecimalField, TextChoices, ForeignKey, CASCADE

# Importing custom field StringArrayField from shared.django.models
from shared.django.models import TimeBaseModel, StringArrayField


class JobVacancy(TimeBaseModel):
    # Enum choices for JobTypes
    class JobTypes(TextChoices):
        full_time = 'full_time', 'Full Time'
        part_time = 'part_time', 'Part Time'
        contract = 'contract', 'Contract'
        temporary = 'temporary', 'Temporary'
        internship = 'internship', 'Internship'

    # JobVacancy fields
    title = CharField(max_length=100)
    description = TextField()
    job_type = CharField(max_length=20, choices=JobTypes.choices)

    # Use ArrayField instead of StringArrayField for requirements and responsibilities fields
    # if using Postgres SQL. Otherwise, keep using StringArrayField.
    requirements = StringArrayField(CharField(max_length=100))
    responsibilities = StringArrayField(CharField(max_length=100))

    salary = DecimalField(max_digits=10, decimal_places=2)
    location = CharField(max_length=100)

    # Use Django's built-in on_delete=models.CASCADE for ForeignKey
    user = ForeignKey('users.User', CASCADE)

    class Meta:
        # Use '-created_at' for descending order. Change to 'created_at' for ascending order.
        ordering = ['-created_at']

    def __str__(self):
        return self.title
