from django.urls import path
from apps.post.views import *

app_name = "post"

urlpatterns = [
    path("post/", PostListView.as_view(), name="post_list"),
    path("post/<slug:slug>", PostDetailView.as_view(), name="post_detail"),
    path("post/mis-publicaciones/", MyPostView.as_view(), name="my_post"),
    path("post/nuevo/", PostCreateView.as_view(), name="post_create"),
]
