from django.contrib import admin
from apps.post.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "category",
        "create_at",
        "update_at",
        "allow_comments",
    )
    search_fields = ("id", "title", "content", "author__username")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("category", "author", "create_at", "allow_comments")
    ordering = ("-create_at",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post", "creted_at")
    search_fields = ("id", "author__username", "post__title")
    list_filter = ("creted_at", "author")
    ordering = ("-creted_at",)


def activate_images(modeladmin, request, queryset):
    updated = queryset.update(active=True)
    modeladmin.message_user(
        request, f"{updated} imagenes fueron activadas correctamente."
    )


activate_images.short_description = "Activar imagenes seleccionadas"


def deactivate_images(modeladmin, request, queryset):
    updated = queryset.update(active=False)
    modeladmin.message_user(
        request, f"{updated} imagenes fueron desactivadas correctamente."
    )


deactivate_images.short_description = "Desactivar imagenes seleccionadas"


class PostImageAdmin(admin.ModelAdmin):
    list_display = ("post", "image", "active", "creted_at")
    search_fields = (
        "post__id",
        "post__title",
        "image",
    )
    list_filter = ("active",)

    actions = [activate_images, deactivate_images]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)