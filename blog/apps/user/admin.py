from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.user.models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("alias", "avatar")}),)

    add_fieldsets = (
        (None, {"fields": ("username", "email", "avatar", "password1", "password2")}),
    )

    def is_registered(self, obj):
        return obj.groups.filter(name="Registered").exists()

    is_registered.short_description = "Es usuario registrado"
    is_registered.boolean = True

    def is_collaborator(self, obj):
        return obj.groups.filter(name="Collaborator").exists()

    is_collaborator.short_description = "Es usuario colaborador"
    is_collaborator.boolean = True

    def is_admin(self, obj):
        return obj.groups.filter(name="Admin").exists()

    is_admin.short_description = "Es usuario administrador"
    is_admin.boolean = True


admin.site.register(User, CustomUserAdmin)
