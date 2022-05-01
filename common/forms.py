from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    google_email = forms.EmailField(label="구글이메일")
    wv_email = forms.EmailField(label="월드비전이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "google_email", "wv_email")