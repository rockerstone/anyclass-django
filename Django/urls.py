"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView)
from django.views.generic.base import TemplateView, RedirectView
from django.views.static import serve
from Django.settings import STATIC_ROOT

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/', include('anyclass.urls')),
    path('favicon.ico', RedirectView.as_view(url=r'static/favicon.ico')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    re_path(r'.*', TemplateView.as_view(template_name='index.html'))
]
