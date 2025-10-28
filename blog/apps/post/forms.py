from django import forms


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
