from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CustomAuthToken

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Include login URLs for browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/', CustomAuthToken.as_view()),
]