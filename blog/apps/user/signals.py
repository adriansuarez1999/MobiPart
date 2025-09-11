from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from apps.user.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_groups_and_permissions(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        try:
            # Definir los permisos de publicaciones y comentarios

            # Crear grupos de usuarios registrados
            registered_group, created = Group.objects.get_or_create(name="Registered")
            registered_group.permissions.add(
                # permiso para ver publicaciones
                # pemiso para publicar
                # permiso para editar su publicación
                # permiso para borrar su publicación
                # permiso para ver comentarios
                # permiso para comentar
                # permiso para editar su comentario
                # permiso para borrar su comentario
            )
            # Crear grupos de usuarios colaboradores
            registered_group, created = Group.objects.get_or_create(
                name="Collaborators"
            )
            registered_group.permissions.add(
                # permiso para ver publicaciones
                # pemiso para publicar
                # permiso para editar su publicación
                # permiso para borrar su publicación y de otros usuarios
                # permiso para ver comentarios
                # permiso para comentar
                # permiso para editar su comentario
                # permiso para borrar su comentario y de otros usuarios
            )
            # Crear grupos de uduarios administradores
            registered_group, created = Group.objects.get_or_create(name="admins")
            registered_group.permissions.add(
                # permiso para ver publicaciones
                # pemiso para publicar
                # permiso para editar su publicación y de otros usuarios
                # permiso para borrar su publicación y de otros usuarios
                # permiso para ver comentarios
                # permiso para comentar
                # permiso para editar su comentario
                # permiso para borrar su comentario y de otros usuarios
            )

            print("Grupos y permisos creados exitosamente.")
        except ContentType.DoesNotExist:
            print("El tipo de permiso aún no se encuentra disponible.")
        except Permission.DoesNotExist:
            print("Uno o más permisos no se encuentran disponibles.")
