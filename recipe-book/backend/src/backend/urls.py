"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include, re_path 
from django.urls import path
from main_pages.views import FrontendRenderView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recipes.api.urls')),
]
urlpatterns += [
    # integration path that catches every url possible whereby django will no longer handle 404 errors; frontend will
    re_path(r'(?P<path>.*)', FrontendRenderView.as_view()),
]