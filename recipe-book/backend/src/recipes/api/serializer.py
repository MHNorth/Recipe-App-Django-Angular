from recipes.models import Recipe
from django.contrib.auth.models import User
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Recipe
        fields = ['name', 'slug', 'description', 'image']

    def get_image(self, obj):
        return "/static/ang/assets/images/recipes/applecrisp.jpg"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True, 'required': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user