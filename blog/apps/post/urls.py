from django.urls import path
from apps.post import views as views

app_name = "post"

urlpatterns = [
    path("post/", views.PostListView.as_view(), name="post_list"),
    path("post/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),
]
