from os import environ
from re import search

from rest_framework.exceptions import ValidationError


def os_environ_get(value):
    return environ.get(value)


def validate_name(name):
    pattern = r'^[a-zA-Z0-9_]{3,16}$'

    if search(pattern, name):
        return name
    raise ValidationError({
        "username": "Invalid username. Usernames must contain only letters, numbers, "
                    "and underscores (_), and be between 3 and 16 characters long."})
