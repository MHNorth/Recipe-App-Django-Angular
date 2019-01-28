from .views import RecipeAPIList, UserViewSet
from django.urls import path
from django.conf.urls import url, include
from recipes.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('recipes/', RecipeAPIList.as_view(), name='api'),
]
