"""
URL configuration for webgaleria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('adicionar/', views.Adiciona, name="adicionar"),
    path('login/', views.recebe_login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('logout/', views.realiza_logout, name="logout"),
    path('colecoes/', views.collections, name="colecoes"),
]
