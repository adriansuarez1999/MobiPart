from django.urls import path
from apps.post.views import PostListView, PostDetailView, MyPostView

app_name = "post"

urlpatterns = [
    path("post/", PostListView.as_view(), name="post_list"),
    path("post/<slug:slug>", PostDetailView.as_view(), name="post_detail"),
    path("post/mis-publicaciones/", MyPostView.as_view(), name= "my_post"),
]
