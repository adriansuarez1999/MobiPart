from django.views.generic import TemplateView, CreateView
from apps.user.forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.models import Group


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
