from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import User

# Create your views here.

def pokemon_index(request):
    content = {}
    
    if request.user.is_authenticated:
        return redirect('main')
    
    content['title'] = 'POKEMON_Dairy'
    return render(request, 'index.html', content)


def main_page(request):
    content = {}

    content['title'] = 'Main | POKEMON-Dairy'

    if request.user.is_authenticated:
        if request.user.nickname == None:
            return render(request, 'getnickname.html', content)
        else:
            return render(request, 'main.html', content)


