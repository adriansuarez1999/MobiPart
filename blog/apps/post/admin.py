# apps/post/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Post, PostImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover; border-radius:8px;" />',
                obj.image.url,
            )
        return "Sin imagen"

    image_preview.short_description = "Vista previa"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "brand",
        "model",
        "author",
        "price",
        "category",
        "create_at",
        "phone_link",
    )
    list_filter = ("category", "create_at", "author")
    search_fields = ("brand", "model", "content", "author__username", "author__email")
    readonly_fields = ("create_at", "update_at", "slug")
    prepopulated_fields = {"slug": ("brand", "model")}
    inlines = [PostImageInline]
    date_hierarchy = "create_at"
    ordering = ("-create_at",)

    fieldsets = (
        (
            "Información principal",
            {"fields": ("brand", "model", "category", "price", "phone", "content")},
        ),
        (
            "Especificaciones",
            {
                "fields": (
                    "Storage",
                    "RAM",
                    "screen_size",
                    "camera_specs",
                    "battery_capacity",
                    "color",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Autor y fechas",
            {
                "fields": ("author", "create_at", "update_at", "slug"),
                "classes": ("collapse",),
            },
        ),
    )

    def phone_link(self, obj):
        if obj.phone:
            phone_clean = obj.phone.replace(" ", "").replace("-", "")
            return format_html(
                '<a href="https://wa.me/54{}" target="_blank">{} <i class="fab fa-whatsapp" style="color:green;"></i></a>',
                phone_clean,
                obj.phone,
            )
        return "Sin teléfono"

    phone_link.short_description = "Contacto"
