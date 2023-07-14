from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices, CharField


class User(AbstractUser):

    class Type(TextChoices):
        EMPLOYEE = 'employee', 'Ishchi'
        EMPLOYER = 'employer', 'Ish beruvchi'

    type = CharField(max_length=25, choices=Type.choices, default=Type.EMPLOYEE)
