from django.urls import path
from apps.user.views import *
from apps.user.views import ProfileView
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path("user/profile", UserProfileView.as_view(), name="user_profile"),
    path("perfil/", ProfileUpdateView.as_view(), name="user_profile"),
    path("auth/register", RegisterView.as_view(), name="auth_register"),
    path("auth/login", LoginView.as_view(), name="auth_login"),
    path("auth/logout", LogoutView.as_view(), name="auth_logout"),
    path(
        "password/change/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/password_change_form.html",
            success_url=reverse_lazy("user:user_profile"),
        ),
        name="password_change",
    ),
    path("perfil/<str:username>/", ProfileView.as_view(), name="profile"),
]
