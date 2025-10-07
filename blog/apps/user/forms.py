from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from apps.user.models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "alias", "avatar"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "paceholder": "Usuario"}
        ),
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "paceholder": "Contraseña"}
        ),
    )

