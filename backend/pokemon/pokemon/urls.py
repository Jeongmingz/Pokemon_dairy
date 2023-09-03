"""
URL configuration for pokemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main.views import *
from django.urls import path, include
from main.views import pokemon_index, login_action, signup_action

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', pokemon_index, name='index'),
    path('main/',include('main.urls'), name='main'),

    path('login', login_action, name='login'),
    path('signup', signup_action, name='signup'),

]
