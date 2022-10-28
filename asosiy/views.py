from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from asosiy.models import *
from django.contrib.auth.models import User

class BoshView(View):
    def get(self, request):
        return render(request, 'bosh.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))

        if user is None:
            return redirect('/login/')
        login(request, user)
        return redirect('/blog/')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        user=User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        Muallif.objects.create(
            ism=request.POST.get('ism'),
            yosh=request.POST.get('yosh'),
            kasb=request.POST.get('kasb'),
            user=user
        )
        return redirect('/login/')

class BlogView(View):
    def get(self, request,):
        if request.user.is_authenticated:
            M= Maqola.objects.filter(muallif__user=request.user)
            data={
                'maqolalar': M
            }
            return render(request, 'blog.html', data)
        return redirect('/')
    def post(self, request):
        m=Muallif.objects.get(user=request.user)
        Maqola.objects.create(
            sarlavha=request.POST.get('sarlavha'),
            sana=request.POST.get('sana'),
            mavzu=request.POST.get('mavzu'),
            matn=request.POST.get('matn'),
            muallif=m
        )
        return redirect('/blog/')

class TanlanganMaqolaView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            data={
                'maqola': Maqola.objects.get(id=son)
            }
            return render(request, 'tanlangan.html', data)
        return redirect('/')





