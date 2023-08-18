from django.core.exceptions import ValidationError


def profile_name_must_start_with_a_letter(value):
    if not value.isalpha():
        raise ValidationError("The name should contain only letters!")


def password_must_contain_at_least_one_digit(self):
    if not any(char.isdigit() for char in self.password):
        raise ValidationError("The password must contain at least 1 digit!")