from django.urls import path  
from apps.post import views as views 

app_name = 'post'

urlpatterns = [
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
]