from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os


def get_avatar_filename(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f"user_{instance.id}_avatar{file_extension}"
    return os.path.join("user/avatar/", new_filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=15,
        unique=True,
        error_messages={"unique": "Ya existe un usuario con ese nombre."},
    )
    alias = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(
        upload_to=get_avatar_filename, default="user/default/default.jpg"
    )
    bio = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=30, blank=True, null=False)
    last_name = models.CharField(max_length=30, blank=True, null=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    DNI = models.CharField(max_length=20, blank=True, null=False)
    phone = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return self.username

    @property
    def is_registered(self):
        return self.groups.filter(name="registered").exists()

    @property
    def is_collaborator(self):
        return self.groups.filter(name="collaborators").exists()

    @property
    def is_admin(self):
        return self.groups.filter(name="admin").exists()

    # def is_collaborator(self):
    #     return self.groups.filter(name="Colaborators").exists()
