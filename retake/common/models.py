from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator, ValidationError

from retake.common.validators import profile_name_must_start_with_a_letter, password_must_contain_at_least_one_digit


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=20,
                                  validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(4)])
    email = models.EmailField(max_length=45)
    profile_picture = models.URLField(null=True, blank=True)
    password = models.CharField(max_length=20,
                                validators=[MinLengthValidator(5)])

    def clean(self):
        if not self.first_name.isalpha():
            raise ValidationError("The name should contain only letters!")

        if not any(char.isdigit() for char in self.password):
            raise ValidationError("The password must contain at least 1 digit!")

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"


class EventModel(models.Model):
    EVENT_CATEGORIES = [
        ('Sports', 'Sports'),
        ('Festivals', 'Festivals'),
        ('Conferences', 'Conferences'),
        ('Performing Art', 'Performing Art'),
        ('Concerts', 'Concerts'),
        ('Theme Party', 'Theme Party'),
        ('Other', 'Other'),
    ]

    event_name = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=EVENT_CATEGORIES)
    description = models.TextField(blank=True)
    date = models.DateField()
    event_image = models.URLField()

    def clean(self):
        from datetime import date

        if self.date < date.today():
            raise ValidationError("The date cannot be in the past!")

    def __str__(self):
        return self.event_name
