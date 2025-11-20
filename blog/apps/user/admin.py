# apps/user/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
from django.utils.html import format_html


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "name",
        "last_name",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "date_joined")
    search_fields = ("username", "email", "name", "last_name", "phone")
    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        ("Credenciales", {"fields": ("username", "password")}),
        (
            "Información personal",
            {
                "fields": (
                    "name",
                    "last_name",
                    "email",
                    "alias",
                    "avatar",
                    "bio",
                    "age",
                    "DNI",
                    "phone",
                )
            },
        ),
        (
            "Permisos",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Fechas", {"fields": ("last_login", "date_joined"), "classes": ("collapse",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    def avatar_preview(self, obj):
        if obj.avatar and hasattr(obj.avatar, "url"):
            return format_html(
                '<img src="{}" width="80" style="border-radius:50%;">', obj.avatar.url
            )
        return "Sin avatar"

    avatar_preview.short_description = "Avatar"
