from django import forms


class PostFilterForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Buscar...", "class": "w-full p-2"}
        ),
    )
    order_by = forms.ChoiceField(
        required=False,
        choices=(
            ("-created_at", "Más recientes"),
            ("created_at", "Más antiguos"),
            ("-comments_count", "Más comentados"),
        ),
        widget=forms.Select(attrs={"class": "w-full p-2"}),
    )
