from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
import uuid
import os


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    content = models.TextField(max_length=10000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="post"
    )
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1

        return unique_slug

    def save(self, *args, **kwargs):
        creating = self._state.adding
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

        if creating and not self.images.exists():
            PostImage.objects.create(post=self, image="post/default/post_default.png")


def get_image_path(instance, filename):
    post_id = instance.post.id
    images_count = instance.post.images.count()
    _, file_extension = os.path.splitext(filename)
    new_filename = f"post_{post_id}_image_{images_count + 1}{file_extension}"

    return os.path.join("post/cover/", new_filename)


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path)
    active = models.BooleanField(default=True)
    creted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"PostImage {self.id}"

    def save(self, *args, **kwargs):
        if not self.active:
            self.active = True

        super().save(*args, **kwargs)
