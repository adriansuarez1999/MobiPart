from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from apps.user.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "alias", "avatar"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Usuario"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Contraseña"}
        ),
    )


User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "alias", "avatar"]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "input-perfil", "id": "id_username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "input-perfil", "id": "id_email"}
            ),
            "alias": forms.TextInput(attrs={"class": "input-perfil", "id": "id_alias"}),
            "avatar": forms.ClearableFileInput(
                attrs={"class": "input-perfil", "id": "id_avatar", "accept": "image/*"}
            ),
        }
