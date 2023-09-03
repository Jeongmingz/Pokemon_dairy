from django.urls import path
from .views import *
# from users.views import userinfo

urlpatterns = [
    path('', main_page, name='main'),

]
