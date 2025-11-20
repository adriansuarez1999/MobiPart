from django import forms
from .models import Post


class PostFilterForm(forms.Form):
    search_query = forms.CharField(
        required=False,
    )
    order_by = forms.ChoiceField(
        required=False,
        choices=(
            ("-create_at", "Más recientes"),
            ("create_at", "Más antiguos"),
        ),
    )


# forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "brand",
            "model",
            "price",
            "category",
            "content",
            "Storage",
            "RAM",
            "screen_size",
            "camera_specs",
            "battery_capacity",
            "color",
            "phone",  # ← NUEVO
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Describí el estado, accesorios, si tiene caja, garantía, etc...",
                }
            ),
            "category": forms.Select(attrs={"class": "select-input"}),
            "price": forms.NumberInput(attrs={"placeholder": "Ej: 450000"}),
            "brand": forms.TextInput(
                attrs={"placeholder": "Samsung, Apple, Xiaomi..."}
            ),
            "model": forms.TextInput(attrs={"placeholder": "Galaxy S23, iPhone 15..."}),
            "phone": forms.TextInput(
                attrs={  # ← nuevo campo
                    "placeholder": "+54 9 11 1234-5678 (WhatsApp preferido)",
                    "maxlength": "20",
                }
            ),
        }
        labels = {"phone": "Teléfono de contacto (WhatsApp)"}
