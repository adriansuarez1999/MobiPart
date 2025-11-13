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


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        fields = ["title", "content", "price", "category", "image"]
        model = Post
