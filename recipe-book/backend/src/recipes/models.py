from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save


class Recipe(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def recipe_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(recipe_pre_save_receiver, sender=Recipe)

