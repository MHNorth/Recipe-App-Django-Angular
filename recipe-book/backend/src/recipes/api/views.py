from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import UserSerializer

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from recipes.models import Recipe
from .serializer import RecipeSerializer


class RecipeAPIList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = []
    authentication_classes = []

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer