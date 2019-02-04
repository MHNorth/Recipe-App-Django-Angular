from django.db import models
from django.contrib.auth.models import User



# ==== Recipe Model ==== #

class Recipes(models.Model):
    name = models.CharField(max_length=255)
    # recipe_type categories go here
    description = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="creator")
    recipeBuddy = models.ManyToManyField(User, related_name = "joiners", blank=True)
    image = models.ImageField(width_field=None, height_field=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return " %s | %s..." % (self.destination, self.description[0:40])