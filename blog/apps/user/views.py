from django.views.generic import TemplateView, CreateView
from apps.user.forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView as LoginViewDjango
from django.shortcuts import redirect
from django.views import View


class UserProfileView(TemplateView):
    template_name = "user/user_profile.html"


class RegisterView(CreateView):
    template_name = "auth/auth_register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)

        registered_group = Group.objects.get(name="Registered")

        self.object.groups.add(registered_group)

        return response


class LoginView(LoginViewDjango):
    template_name = "auth/auth_login.html"
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy("home")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        next_url = request.META.get("HTTP_REFERER", "/")
        return redirect(next_url)
