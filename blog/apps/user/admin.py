from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
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
        return obj.groups.filter(name="Collaborators").exists()

    is_collaborator.short_description = "Es usuario colaborador"
    is_collaborator.boolean = True

    def is_admin(self, obj):
        return obj.groups.filter(name="admins").exists()

    is_admin.short_description = "Es usuario administrador"
    is_admin.boolean = True


    def add_to_registered(self, request, queryset):
        registered_group = Group.objects.get(name="Registered")
        for user in queryset:
            user.groups.add(registered_group)

    add_to_registered.short_description = (
        'Agregar usuario seleccionado al grupo "Registrado"'
    )

    def add_to_collaborators(self, request, queryset):
        collaborators_group = Group.objects.get(name="Collaborators")
        for user in queryset:
            user.groups.add(collaborators_group)

    add_to_collaborators.short_description = (
        'Agregar usuario seleccionado al grupo "Colaborador"'
    )

    def add_to_admins(self, request, queryset):
        admins_group = Group.objects.get(name="admins")
        for user in queryset:
            user.groups.add(admins_group)

    add_to_admins.short_description = (
        'Agregar usuario seleccionado al grupo "Administrador"'
    )

    def remove_from_registered(self, request, queryset):
        registered_group = Group.objects.get(name="Registered")
        for user in queryset:
            user.groups.remove(registered_group)

    remove_from_registered.short_description = (
        'Eliminar usuario seleccionado del grupo "Registrado"'
    )

    def remove_from_collaborators(self, request, queryset):
        collaborators_group = Group.objects.get(name="Collaborators")
        for user in queryset:
            user.groups.remove(collaborators_group)

    remove_from_collaborators.short_description = (
        'Eliminar usuario seleccionado del grupo "Colaborador"'
    )

    def remove_from_admins(self, request, queryset):
        admins_group = Group.objects.get(name="admins")
        for user in queryset:
            user.groups.remove(admins_group)

    remove_from_admins.short_description = (
        'Eliminar usuario seleccionado del grupo "Administrador"'
    )

    list_display = (
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_registered",
        "is_collaborator",
        "is_admin",
    )

    actions = [
        add_to_registered,
        add_to_collaborators,
        add_to_admins,
        remove_from_registered,
        remove_from_collaborators,
        remove_from_admins,
    ]


admin.site.register(User, CustomUserAdmin)
