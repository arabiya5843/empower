from django.contrib.auth.models import AbstractUser
from django.db.models import TextField, CharField, Model, DateTimeField, ForeignKey, CASCADE, TextChoices, \
    BooleanField, ManyToManyField, URLField, ImageField
from phonenumber_field.modelfields import PhoneNumberField


class Ability(Model):
    title = CharField(max_length=50)
    description = TextField(max_length=1000)

    def __str__(self):
        return self.title


class User(AbstractUser):
    GENDER_CHOICES = [
        ('1', 'Erkak'),
        ('2', 'Ayol')
    ]

    GENDER_MALE = '1'
    GENDER_FEMALE = '2'

    profile_image = ImageField(upload_to='apps/users/user_images/')
    job = CharField(max_length=50)
    instagram_profile = URLField(max_length=100)
    facebook_profile = URLField(max_length=100)
    twitter_profile = URLField(max_length=100)
    about_me = TextField(max_length=2000, default='Men Haqimda')
    phone_number = PhoneNumberField()
    location = CharField(max_length=50, default='Toshkent')
    abilities = ManyToManyField(Ability, related_name='users')
    has_subscription = BooleanField(default=False)
    gender = CharField(max_length=1, choices=GENDER_CHOICES,
                       default=GENDER_MALE)

    class Type(TextChoices):
        EMPLOYEE = 'employee', 'Ishchi'
        EMPLOYER = 'employer', 'Ish beruvchi'

    user_type = CharField(
        max_length=25, choices=Type.choices, default=Type.EMPLOYEE)

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.username


class Experience(Model):
    profession = CharField(max_length=50)
    company = CharField(max_length=50)
    date = DateTimeField(auto_now_add=True)
    description = TextField(max_length=1000)
    user = ForeignKey('users.User', CASCADE)

    def __str__(self):
        return f"{self.profession}, {self.company}, {self.date}, {self.user.first_name}, {self.user.last_name}"
