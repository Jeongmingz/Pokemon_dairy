from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import User

# Create your views here.

def login_action(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password, backend='django.contrib.auth.backends.ModelBackend')

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            try:
                # 사용자 이름에 해당하는 사용자가 존재하는지 확인
                user = User.objects.get(email=email)
                # 사용자 이름은 존재하지만 비밀번호가 올바르지 않음
                msg = "비밀번호가 올바르지 않습니다."
            except User.DoesNotExist:
                # 맞는 계정이 존재하지 않음
                msg = "존재하지 않는 계정입니다. 회원가입을 해주세요."
            messages.add_message(request, messages.ERROR, msg)
            return redirect('index')
    else:
        return redirect('index')
    



# views.py
def signup_action(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password_check']
        
        if password1 == password2:
            # 비밀번호 일치
            try:
                user = User.objects.create_user(email=email, password=password1)
            except Exception as e:
                msg = f"회원가입 오류. {e}"
                messages.add_message(request, messages.ERROR, msg)
                return redirect('index')
            login(request, user)
            return redirect('main')  # 회원가입 성공 시 리다이렉션할 페이지
        else:
            # 비밀번호 불일치
            msg = "비밀번호 검증 오류, 회원가입을 다시 시도해주세요."
            messages.add_message(request, messages.ERROR, msg)
            return redirect('index')
    else:
        return render(request, 'registration/signup.html')


def user_logout(request):
    logout(request)
    msg = "로그아웃 완료 !"
    messages.add_message(request, messages.SUCCESS, msg)
    return redirect('index')

