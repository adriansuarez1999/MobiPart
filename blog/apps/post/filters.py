import django_filters
from apps.post.models import Post


class PostFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr="inicontains")

    class Meta:
        model = Post
        fields = ["title", "author", "create_at", "category"]
