from django import forms
from django.forms import models

from retake.common.models import ProfileModel, EventModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password', 'profile_picture']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        exclude = ['first_name', 'last_name', 'email', 'password', 'profile_picture']

        def __init__(self):
            self.instance = None

        def save(self, commit=True):
            if commit:
                ProfileModel.objects.all().delete()
            return self.instance


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['event_name', 'category', 'description', 'date', 'event_image']


class EventCreateForm(EventBaseForm):
    pass



class EventEditForm(EventBaseForm):
    pass



class EventDeleteForm(EventBaseForm):
    class Meta:
        model = EventModel
        fields = ['event_name', 'category', 'description', 'date', 'event_image']

