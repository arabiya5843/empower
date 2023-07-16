from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices, CharField, URLField, TextField, ImageField, Model, DateTimeField, ForeignKey, \
    CASCADE, ManyToManyField
from phonenumber_field.formfields import PhoneNumberField


class Ability(Model):

    title = CharField(max_length=50, default='')
    description = TextField(max_length=1000, default='')

    def __str__(self):
        return f"{self.title}"


class User(AbstractUser):

    profile_image = ImageField(upload_to='apps/users/user_images/')
    job = CharField(max_length=50, default='')
    instagram_profile = URLField(max_length=100, default='')
    facebook_profile = URLField(max_length=100, default='')
    twitter_profile = URLField(max_length=100, default='')
    about_me = TextField(max_length=2000, default='Men Haqimda')
    phone_number = PhoneNumberField()
    location = CharField(max_length=50, default='Toshkent')
    abilities = ManyToManyField(Ability, related_name='users')

    class Type(TextChoices):
        EMPLOYEE = 'employee', 'Ishchi'
        EMPLOYER = 'employer', 'Ish beruvchi'

    type = CharField(max_length=25, choices=Type.choices, default=Type.EMPLOYEE)

    GENDER_CHOICES = [
        (1, 'Erkak'),
        (2, 'Ayol')
    ]

    gender = CharField(max_length=1, choices=GENDER_CHOICES, default=1)


class Experience(Model):

    profession = CharField(max_length=50, default='')
    company = CharField(max_length=50, default='')
    date = DateTimeField(auto_now_add=True)
    description = TextField(max_length=1000)
    user = ForeignKey('User', CASCADE)

    def __str__(self):
        return f"{self.profession}, {self.company}, {self.date}, {self.user.first_name}, {self.user.last_name}"
