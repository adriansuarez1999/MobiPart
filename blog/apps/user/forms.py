from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from apps.user.models import User
from django.contrib.auth.models import Group


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuario",
                "maxlength": "15",
                "autocomplete": "username",
            }
        ),
        label="Usuario",
        help_text="Máximo 15 caracteres.",
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "tu@email.com",
                "maxlength": "100",
                "autocomplete": "email",
            }
        ),
        label="Email",
        help_text="Usaremos tu email solo para recuperación de cuenta.",
    )

    alias = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Cómo te verán los demás (opcional)",
                "maxlength": "20",
            }
        ),
        label="Nombre visible (alias)",
        help_text="Máximo 20 caracteres.",
    )

    avatar = forms.ImageField(
        required=False,
        label="Foto de perfil",
        widget=forms.FileInput(attrs={"accept": "image/*"}),
    )

    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Tu nombre real",
                "maxlength": "30",
                "autocomplete": "given-name",
            }
        ),
        label="Nombre real",
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Tu apellido real",
                "maxlength": "30",
                "autocomplete": "family-name",
            }
        ),
        label="Apellido real",
    )

    age = forms.IntegerField(
        required=False,
        min_value=13,
        max_value=120,
        widget=forms.NumberInput(
            attrs={"placeholder": "Edad (opcional)", "min": "13", "max": "120"}
        ),
        label="Edad",
    )

    DNI = forms.CharField(
        max_length=10,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Solo números (opcional)",
                "maxlength": "10",
                "pattern": "[0-9]+",
                "inputmode": "numeric",
            }
        ),
        label="DNI / Documento",
    )

    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "+54 9 11 1234-5678 (opcional)",
                "maxlength": "20",
                "autocomplete": "tel",
            }
        ),
        label="Teléfono / WhatsApp",
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "alias",
            "avatar",
            "name",
            "last_name",
            "age",
            "DNI",
            "phone",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update(
            {"placeholder": "Crear contraseña", "autocomplete": "new-password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"placeholder": "Repetir contraseña", "autocomplete": "new-password"}
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        user.alias = self.cleaned_data.get("alias", "")
        user.name = self.cleaned_data["name"]
        user.last_name = self.cleaned_data["last_name"]
        user.age = self.cleaned_data.get("age")
        user.DNI = self.cleaned_data.get("DNI", "")
        user.phone = self.cleaned_data.get("phone", "")

        if self.cleaned_data.get("avatar"):
            user.avatar = self.cleaned_data["avatar"]

        if commit:
            user.save()
            registered_group = Group.objects.get(name="Registered")
            user.groups.add(registered_group)

        return user


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
