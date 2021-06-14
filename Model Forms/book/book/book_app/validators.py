from django.core.exceptions import ValidationError


def page_validator(value):
    if value <= 0:
        raise ValidationError('Page count must be bigger than zero')
