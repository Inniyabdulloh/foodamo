from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'base.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'login-register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username, email)
            user.set_password(password)
            user.save()
            return render(request, 'login-register.html')
        except:
            msgs = messages.error(request, 'Username already taken')
            return render(request, 'login-register.html', {'msgs': msgs})




class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            print(f"{user} logged in")
            return render(request, 'base.html')
        print(f"{user} failed to login")
        return redirect('main:register')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main:login')