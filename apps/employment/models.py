from django.db.models import CharField, TextField, DecimalField, TextChoices, ForeignKey, CASCADE, TimeField, Model, \
    DateField

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

    # Enum choices for GenderRequirement
    class GenderRequirement(TextChoices):
        male = 'male', 'Male'
        female = 'female', 'Female'
        any_gender = 'any_gender', 'Any Gender'

    # JobVacancy fields
    title = CharField(max_length=100)
    description = TextField()
    job_type = CharField(max_length=20, choices=JobTypes.choices)

    # Use ArrayField instead of StringArrayField for requirements and responsibilities fields
    # if using Postgres SQL. Otherwise, keep using StringArrayField.
    requirements = StringArrayField(CharField(max_length=100))
    desired_skills = StringArrayField(CharField(max_length=100))
    benefits = StringArrayField(CharField(max_length=100))
    salary = DecimalField(max_digits=10, decimal_places=2)
    location = CharField(max_length=100)
    user = ForeignKey('users.User', CASCADE)
    work_hours_start = TimeField(null=True, blank=True)
    work_hours_end = TimeField(null=True, blank=True)
    gender_requirement = CharField(max_length=20, choices=GenderRequirement.choices,
                                   default=GenderRequirement.any_gender)

    class Meta:
        db_table = 'job_vacancy'
        # Use '-created_at' for descending order. Change to 'created_at' for ascending order.
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Experience(Model):
    profession = CharField(max_length=50)
    company = CharField(max_length=50)
    start_date = DateField()
    end_date = DateField()
    description = TextField(max_length=1000)
    user = ForeignKey('users.User', CASCADE)

    def __str__(self):
        return f"{self.profession}, {self.company}, {self.start_date}, {self.user.first_name}, {self.user.last_name}"

    class Meta:
        db_table = 'experience'
